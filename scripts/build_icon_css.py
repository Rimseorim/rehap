"""화면 코드가 쓰는 tabler 아이콘만 골라 index.html 안의 작은 스타일로 넣는다 (아이콘 글꼴 761KB 대체).

index.html 에서 `ti-이름` 을 찾아, 같은 이름의 SVG 를 받아 CSS mask 로 그리는 한 줄짜리 <style id="ti-icons"> 를 만든다.
마크업(<i class="ti ti-run">)은 그대로 쓴다. 크기는 font-size, 색은 color 를 따른다.

사용: python scripts/build_icon_css.py          (새 아이콘을 코드에 쓴 뒤 다시 실행. 인터넷 필요)
"""
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rehab_data import INDEX, MARK  # noqa: E402

VERSION = '2.47.0'  # 바꾸기 전 아이콘 글꼴과 같은 판
SVG_URL = 'https://cdn.jsdelivr.net/npm/@tabler/icons@{v}/icons/{name}.svg'
BASE = ('.ti{display:inline-block;width:1em;height:1em;flex:none;vertical-align:-.125em;background-color:currentColor;'
        '-webkit-mask:var(--ti) center/contain no-repeat;mask:var(--ti) center/contain no-repeat}')
STYLE_RE = re.compile(r'^.*<style id="ti-icons">.*</style>.*$|^.*<link[^>]*tabler[^>]*>.*$', re.M)


def used_icons(html):
    """데이터(BUNDLED) 밖의 화면 코드에서 쓰는 아이콘 이름."""
    start = html.index(MARK)
    end = html.index('</script>', start)
    code = html[:start] + html[end:]
    code = STYLE_RE.sub('', code)
    return sorted(set(re.findall(r'\bti-([a-z0-9]+(?:-[a-z0-9]+)*)', code)))


def defined_icons(html):
    m = re.search(r'<style id="ti-icons">(.*?)</style>', html)
    return sorted(set(re.findall(r'\.ti-([a-z0-9-]+)\{', m.group(1)))) if m else []


def data_uri(svg):
    body = re.sub(r'<path stroke="none" d="M0 0h24v24H0z" fill="none"\s*/>', '', svg)
    body = re.sub(r'\s+', ' ', body).replace('> <', '><').strip()
    body = re.sub(r' class="[^"]*"', '', body).replace('stroke="currentColor"', 'stroke="#000"')
    body = body.replace('"', "'").replace('%', '%25').replace('#', '%23').replace('<', '%3C').replace('>', '%3E')
    return 'url("data:image/svg+xml,' + body + '")'


def build(names):
    rules = [BASE]
    for name in names:
        req = urllib.request.Request(SVG_URL.format(v=VERSION, name=name), headers={'User-Agent': 'Mozilla/5.0'})
        svg = urllib.request.urlopen(req, timeout=20).read().decode('utf-8')
        rules.append('.ti-%s{--ti:%s}' % (name, data_uri(svg)))
    return '  <style id="ti-icons">' + ''.join(rules) + '</style>'


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    html = open(INDEX, encoding='utf-8').read()
    names = used_icons(html)
    line = build(names)
    new, n = STYLE_RE.subn(lambda m: line, html, count=1)
    if n != 1:
        sys.exit('index.html 에서 아이콘 스타일(또는 tabler 링크) 줄을 찾지 못했습니다')
    open(INDEX, 'w', encoding='utf-8').write(new)
    print(f'아이콘 {len(names)}개: {", ".join(names)} / 스타일 {len(line)}자')
