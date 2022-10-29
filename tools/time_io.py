import re
import time
import datetime


def string2timestamp(ts_str, ts_format):
#     "%Y-%m-%d %H:%M:%S.%f"
    d = datetime.datetime.strptime(ts_str, ts_format)
    t = d.timetuple()
    timeStamp = int(time.mktime(t))
    return timeStamp


def twentyfour_converter(t):
    # e.g. 09:43am in string format
    time_str = str(t)
    if 'Closed' in time_str:
        return time_str
    if 'am' in time_str:
        return time_str.replace('am', '')
    elif 'pm' in time_str:
        parts = time_str.split(':')
        if len(parts) != 2:
            return time_str.replace('pm', '')
        hour = int(parts[0])
        if hour < 12:
            hour = hour + 12
        else:
            hour = hour - 12
        hour = str(hour)
        if len(hour) <= 1:
            hour = '0' + hour
        time_str = hour + ':' + parts[1]
        return(time_str.replace('pm', ''))
    else:
        return '00:00'


def duration(slots):
    pattern = re.compile(r'(\d.+?):(\d.+?)')
    total_prd = 0
    for period in slots:
        if len(period) != 2:
            continue
        start_hm = re.findall(pattern, period[0])
        if len(start_hm) < 1:
            continue
        if len(start_hm[0]) != 2:
            continue
        start_h = int(start_hm[0][0])
        start_m = int(start_hm[0][1])
        start = start_h * 60 + start_m
        end_hm = re.findall(pattern, period[1])
        if len(end_hm) < 1:
            continue
        if len(end_hm[0]) != 2:
            continue
        end_h = int(end_hm[0][0])
        end_m = int(end_hm[0][1])
        end = end_h * 60 + end_m
        prd = end - start
        if prd < 0:
            prd = 60 * 24 - start + end
        total_prd += prd
    return float(total_prd) / 60.0


def timestr_to_timestamp(tm_format, tm_str):
    # '%Y-%m-%d %H:%M:%S.%f'
    return time.mktime(datetime.datetime.strptime(tm_str, tm_format).timetuple())


def digit_len(num: int):
    a = num
    b = len(str(a))
    return b


def timestamp_to_timestr(tm_format, tm=-1, local=False):
    # '%Y-%m-%d %H:%M:%S.%f'
    if tm == -1:
        tm = current_timestamp()
    if digit_len(tm) == 13:
        tm = tm / 1000
    # tm = time.time()
    if local:
        tm = time.localtime(tm)
    if len(tm_format) == 0:
        tm_format = '%Y%m%d_%H%M'
    format_time  = time.strftime(tm_format, tm)
    return format_time


def current_timestamp(milli_second=False):
    t = time.time()
    if milli_second:
        return t * 1000
    else:
        return int(t)


def current_date(format, in_str_format=True):
    today = datetime.date.today()
    if in_str_format:
        if len(format) < 1:
            format = "%b-%d-%Y"
        dday = today.strftime(format)
        return dday
    else:
        format = "%Y%m%d"
        dday = today.strftime(format)
        dday_in_int = int(dday)
        return dday_in_int