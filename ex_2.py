def time_display(time1, time2):
    list_time1 = time1.split(":")
    list_time2 = time2.split(":")

    seconds = int(list_time1[2]) + int(list_time2[2])
    minute = int(list_time1[1]) + int(list_time2[1])
    hours = int(list_time1[0]) + int(list_time2[0])
    if seconds > 60:
        minute += 1
        seconds -= 60
    if minute > 60:
        hours += 1
        minute -= 60

    return f'Time is {hours} hour(s) and {minute} minute(s) and {seconds} second(s)'

print(time_display('19:50:15', '01:31:00'))