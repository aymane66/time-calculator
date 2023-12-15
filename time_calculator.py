def add_time(start, duration, starting_day=None):
    
  # Splitting Start time into hours and minutes
    start_hour, start_min_mer = start.split(":")
    start_min, meridiem = start_min_mer.split(" ")

    start_hour = int(start_hour)
    start_min = int(start_min)
    meridiem = str(meridiem)

  # Splitting the duration into hours and minutes
    duration_hour, duration_min = duration.split(":")
    
    duration_hour = int(duration_hour)
    duration_min = int(duration_min)

  # Calculating total minutes of start time and duration
    total_start_min = start_hour * 60 + start_min
    total_duration_min = duration_hour * 60 + duration_min

    new_time = total_start_min + total_duration_min

  # Calculating new hour and minute
    new_hour = new_time // 60
    new_min = new_time % 60

  # Adjusting new hour
    if meridiem == "PM":
        new_hour += 12

  # Calculating number of days later
    days_later = new_hour // 24
    new_hour = new_hour % 24
    
  # Adjusting new meridiem and hour format
    if new_hour == 0:
        new_hour = 12
        new_meridiem = "AM"
    elif new_hour >= 12:
        new_meridiem = "PM"
        if new_hour > 12:
            new_hour -= 12
    else:
        new_meridiem = "AM"

  # Constructing new full time string
    new_time_str = f"{new_hour:02d}:{new_min:02d} {new_meridiem}"

  # Adding the starting day if given
    if starting_day:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        starting_day_index = days.index(starting_day.lower().capitalize())
        days_later %= 7
        new_day_index = (starting_day_index + days_later) % 7
        new_day = days[new_day_index]
        new_time_str += f", {new_day}"

  ## Constructing days later
    days_later_str = ""
    if days_later == 1:
        days_later_str = " (next day)"
    elif days_later > 1:
        days_later_str = f" ({days_later} days later)"


    return new_time_str + days_later_str