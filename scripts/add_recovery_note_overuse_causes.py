import json

PATH = "data/phase-exercises.json"

RECOVERY_NOTE = "이 루틴은 회복이 목적입니다. 단계를 서두르다 오히려 다시 아플 수 있어요."

VOLUME_FULL_TEXT = "훈련 빈도를 평소의 절반으로 줄이고, 최소 주 1일은 완전 휴식일로 확보하세요."
VOLUME_APPEND_TEXT = " 이번 주는 훈련 빈도를 평소의 절반으로 줄이고, 최소 주 1일은 완전 휴식일로 확보하세요."
TENDON_APPEND_TEXT = " 통증 재현이 없으면 매일 진행 가능하지만, 다음날 뻐근함이 남으면 하루 쉬어주세요."

FREQUENCY_KEYWORDS = ("48시간", "간격", "빈도", "휴식")


def is_volume_type(cause):
    name = cause.get("name", "")
    return name == "과부하/과사용" or "볼륨·빈도" in name


def main():
    with open(PATH, encoding="utf-8") as f:
        data = json.load(f)

    added_recovery = []
    added_priority_full = []
    added_priority_append = []
    skipped_priority = []

    for mv in data["movements"]:
        for site in mv["pain_sites"]:
            for cause in site["causes"]:
                tag = cause.get("tag", "")
                if "과부하" not in tag and "과사용" not in tag:
                    continue

                stage1 = cause["route"]["stages"][0]
                path = (mv["id"], site["id"], cause["id"], cause["name"])

                if "recovery_note" not in stage1:
                    stage1["recovery_note"] = RECOVERY_NOTE
                    added_recovery.append(path)

                volume_type = is_volume_type(cause)
                current = cause.get("priority_note")

                if current and any(kw in current for kw in FREQUENCY_KEYWORDS):
                    skipped_priority.append(path)
                    continue

                if current is None:
                    cause["priority_note"] = VOLUME_FULL_TEXT if volume_type else (
                        "통증 재현이 없으면 매일 진행 가능하지만, 다음날 뻐근함이 남으면 하루 쉬어주세요."
                    )
                    added_priority_full.append(path)
                else:
                    cause["priority_note"] = current + (VOLUME_APPEND_TEXT if volume_type else TENDON_APPEND_TEXT)
                    added_priority_append.append(path)

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"recovery_note 추가: {len(added_recovery)}건")
    for p in added_recovery:
        print("  ", p)
    print(f"\npriority_note 신규 작성: {len(added_priority_full)}건")
    for p in added_priority_full:
        print("  ", p)
    print(f"\npriority_note 문장 추가: {len(added_priority_append)}건")
    for p in added_priority_append:
        print("  ", p)
    print(f"\npriority_note 건드리지 않음 (이미 빈도 정보 있음): {len(skipped_priority)}건")
    for p in skipped_priority:
        print("  ", p)


if __name__ == "__main__":
    main()
