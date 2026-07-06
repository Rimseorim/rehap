import json

PATH = "data/phase-exercises.json"

with open(PATH, encoding="utf-8") as f:
    data = json.load(f)

renamed = []
deduped = []

for mv in data["movements"]:
    sites = mv["pain_sites"]
    ids = [s["id"] for s in sites]

    if "low_back" in ids and "lower-back" in ids:
        low = next(s for s in sites if s["id"] == "low_back")
        lower = next(s for s in sites if s["id"] == "lower-back")
        low_empty = all(not c.get("route", {}).get("stages", [{}])[0].get("phase_a") for c in low["causes"])
        if low_empty:
            sites.remove(low)
            deduped.append((mv["id"], "low_back (빈 스텁, phase_a 없음 - 제거, lower-back 유지)"))
        else:
            raise SystemExit(f"{mv['id']}: low_back에 실제 콘텐츠가 있어 자동 제거 불가 - 수동 확인 필요")
    elif "low_back" in ids:
        for s in sites:
            if s["id"] == "low_back":
                s["id"] = "lower-back"
                renamed.append((mv["id"], "low_back -> lower-back"))

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"이름 변경: {len(renamed)}건")
for r in renamed:
    print("  ", r)
print(f"\n중복 제거: {len(deduped)}건")
for r in deduped:
    print("  ", r)
