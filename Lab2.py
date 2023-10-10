def simplify_calendar(calendar):
    if not calendar:
        return []

    calendar.sort()

    simplified_calendar = [calendar[0]]


    for i in range(1, len(calendar)):
        interval = calendar[i]
        if interval[0] <= simplified_calendar[-1][1]:
            current_interval = simplified_calendar[-1]
            start = current_interval[0]
            end = max(current_interval[1], interval[1])
            simplified_calendar[-1] = (start, end)
        else:
            simplified_calendar.append(interval)

    return simplified_calendar

def print_intervals_as_hours(calendar):
    for interval in calendar:
        start_hour = interval[0] // 2 + 9
        start_minute = (interval[0] % 2) * 30
        end_hour = interval[1] // 2 + 9
        end_minute = (interval[1] % 2) * 30
        print(f"{start_hour:02}:{start_minute:02} - {end_hour:02}:{end_minute:02}")



if __name__ == "__main__":

    calendar=[(0,1),(1,2),(3,4),(10,11),(5,6)]
    print(simplify_calendar(calendar))
    print_intervals_as_hours(simplify_calendar(calendar))