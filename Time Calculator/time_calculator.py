def add_time(start: str, duration: str, weekday=''):
    weekdays = ['monday', "tuesday", 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    start_time, time_format = [i for i in start.split()]
    start_hour, start_min = [i for i in start_time.split(sep=':')]
    duration_hour, duration_min = [i for i in duration.split(sep=':')]

    total_mins = int(start_min)+int(duration_min)
    if total_mins > 60:
        extra_hrs, total_min = divmod(total_mins, 60)
    else:
        extra_hrs, total_min = (0, total_mins)

    total_hrs = int(start_hour)+int(duration_hour)+extra_hrs

    num__halfdays, total_hr = divmod(total_hrs, 12)

    if total_hr == 0:
        total_hr = 12

    if num__halfdays % 2 == 0:
        num_days = num__halfdays//2
    elif num__halfdays % 2 == 1:
        num_days = num__halfdays//2
        if time_format == 'PM':
            num_days += 1
            time_format = 'AM'
        elif time_format == 'AM':
            time_format = 'PM'

    try:
        weekday = weekday.lower()
        weekday_index = weekdays.index(weekday)
        weekday = ", "+weekdays[(weekday_index+num_days) % 7].title()
    except (UnboundLocalError, ValueError):
        weekday = ''

    if num_days == 1:
        new_time = (str(total_hr)+':'+'%02d' %
                    total_min+' '+time_format+weekday+' (next day)')
    elif num_days > 1:
        new_time = (str(total_hr)+':'+'%02d' %
                    total_min+' '+time_format + weekday+f' ({num_days} days later)')
    else:
        new_time = (str(total_hr)+':'+'%02d' %
                    total_min+' '+time_format+weekday)

    return new_time


print(add_time("10:10 PM", "3:30"))


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
