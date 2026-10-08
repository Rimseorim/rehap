"""첫 화면 로딩을 정해진 조건(휴대폰·느린 4G·캐시 없음)으로 잰다.

사용: python scripts/measure_load.py [URL] [--runs N]
      URL 기본값 = 배포본 https://rimseorim.github.io/rehap/  (로컬 파일은 file:///.../index.html)
필요: pip install playwright && python -m playwright install chromium

조건 (바꾸면 예전 측정과 비교할 수 없다)
- 기기: Galaxy S9+ 화면, CPU 4배 감속, 브라우저 캐시 끔
- 네트워크 2종: Lighthouse 느린 4G(지연 150ms·1.6Mbps) / DevTools 느린 4G(지연 562.5ms·1.44Mbps)
- 다운로드 양(종류별 KB)은 네트워크 조건과 무관하므로 측정끼리 그대로 비교할 수 있다

기준값 (2026-10-08, 커밋 2286078 배포본, 아이콘 글꼴 교체 후)
- 받은 양 509~512KB = 문서 377 · 글꼴 111~114 · 스타일 21
- Lighthouse 느린 4G: 첫 화면 2.3~2.7초 · 로딩 완료 2.9~3.4초
- DevTools 느린 4G:   첫 화면 3.0~3.1초 · 로딩 완료 4.2~4.3초
"""
import argparse
import time

from playwright.sync_api import sync_playwright

DEFAULT_URL = 'https://rimseorim.github.io/rehap/'
DEVICE = 'Galaxy S9+'
CPU_SLOWDOWN = 4
NETWORKS = {
    'Lighthouse 느린 4G': {'latency': 150, 'downloadThroughput': 1.6 * 1024 * 1024 / 8, 'uploadThroughput': 750 * 1024 / 8},
    'DevTools 느린 4G': {'latency': 562.5, 'downloadThroughput': 1.44 * 1000 * 1000 / 8, 'uploadThroughput': 675 * 1000 / 8},
}
TIMING_JS = """() => {
  const n = performance.getEntriesByType('navigation')[0];
  const f = performance.getEntriesByName('first-contentful-paint')[0];
  return {fcp: f ? f.startTime : null, load: n.loadEventEnd};
}"""


def measure(p, url, net):
    browser = p.chromium.launch()
    ctx = browser.new_context(**p.devices[DEVICE])
    page = ctx.new_page()
    cdp = ctx.new_cdp_session(page)
    cdp.send('Network.enable')
    cdp.send('Network.setCacheDisabled', {'cacheDisabled': True})
    cdp.send('Network.emulateNetworkConditions', {'offline': False, **net})
    cdp.send('Emulation.setCPUThrottlingRate', {'rate': CPU_SLOWDOWN})
    kinds, sizes = {}, {}
    cdp.on('Network.responseReceived', lambda e: kinds.__setitem__(e['requestId'], e['type']))
    cdp.on('Network.loadingFinished', lambda e: sizes.__setitem__(e['requestId'], e['encodedDataLength']))
    page.goto(url, wait_until='load', timeout=120000)
    page.evaluate('document.fonts.ready')
    timing = page.evaluate(TIMING_JS)
    browser.close()
    by_kind = {}
    for rid, n in sizes.items():
        k = kinds.get(rid, 'Other')
        by_kind[k] = by_kind.get(k, 0) + n
    return timing, by_kind


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('url', nargs='?', default=DEFAULT_URL)
    ap.add_argument('--runs', type=int, default=3)
    args = ap.parse_args()
    sep = '&' if '?' in args.url else '?'
    with sync_playwright() as p:
        for name, net in NETWORKS.items():
            print(f'[{name}]')
            for i in range(args.runs):
                url = args.url if args.url.startswith('file:') else f'{args.url}{sep}m={time.time_ns()}'
                timing, by_kind = measure(p, url, net)
                kb = {k: round(v / 1024) for k, v in sorted(by_kind.items(), key=lambda x: -x[1]) if v}
                print(f"  {i + 1}회: 첫 화면 {timing['fcp'] / 1000:.1f}초 · 로딩 완료 {timing['load'] / 1000:.1f}초"
                      f" · 받은 양 {sum(kb.values())}KB {kb}")


if __name__ == '__main__':
    main()
