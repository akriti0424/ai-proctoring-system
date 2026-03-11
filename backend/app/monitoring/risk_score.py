def calculate_risk(events):
    score = 0
    for event in events:
        if event == "multiple_faces":
            score += 3
        elif event == "tab_switch":
            score += 2
    return score