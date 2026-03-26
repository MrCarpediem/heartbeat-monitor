def classify(data):
    urgent = []
    info = []
    seen = set()

    for item in data:
        msg = item.get("message")

        # Deduplication
        if msg in seen:
            continue
        seen.add(msg)

        if item.get("priority") == "high":
            urgent.append(item)
        else:
            info.append(item)

    return urgent, info