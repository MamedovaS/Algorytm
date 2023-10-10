def simplify_calendar(calendar):
    if not calendar:
        return []

    calendar.sort()

    simplified_calendar = [calendar[0]]

    for i in range(1, len(calendar)):
        interval = calendar[i]
        if interval[0] <= simplified_calendar[-1][1]:
            if interval[0] <= simplified_calendar[-1][1]:
                current_interval = simplified_calendar[-1]
                start = current_interval[0]
                end = max(current_interval[1], interval[1])
                simplified_calendar[-1] = (start, end)
        else:
            simplified_calendar.append(interval)

    return simplified_calendar

