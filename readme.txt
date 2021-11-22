# Source used to express total travel time in hour:min:sec
# https://www.kite.com/python/answers/how-to-convert-seconds-to-hours,-minutes,-and-seconds-in-python
    conversion = datetime.timedelta(seconds=tot_trav_time)
    tot_trav_time_convert = str(conversion)
# Source used as guidance to get weekday_name
# https://docs.python.org/3/library/datetime.html#datetime.date.day