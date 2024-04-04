"""Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either a.m. or p.m.) as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.

Notes
By convention, noon is 12:00 pm, and midnight is 12:00 am.
On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015."""


hours_dict = {}
for i in range(1, 13):
    if i == 12:
        hours_dict[i] = "12"
    else:
        hours_dict[i] = str(12 + i)

def to24hourtime(hour, minute, period):
    if period == "pm":
        return f"{hours_dict.get(hour)}{str(minute).zfill(2)}"
    else:
        if hour == 12:
            hour = "00"
        return f"{str(hour).zfill(2)}{str(minute).zfill(2)}"

print(to24hourtime( 12, 5, 'pm'))
