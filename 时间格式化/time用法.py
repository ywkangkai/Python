import datetime
import time
times = datetime.datetime.now()
time_now = times.strftime('%Y-%m-%d %H:%M:%S')
print("time_now", time_now)

endtimenow = time.mktime(time.strptime(time_now, '%Y-%m-%d %H:%M:%S'))
print("endtimenow", endtimenow)

endtime = str(endtimenow).split(".")[0] + "000"
print("endtime", endtime)

hoursago = (times - datetime.timedelta(hours=1)
            ).strftime("%Y-%m-%d %H:%M:%S")
print("hoursago", hoursago)

starttimeago = time.mktime(
    time.strptime(
        hoursago,
        '%Y-%m-%d %H:%M:%S'))
print("starttimeago", starttimeago)

starttime = str(starttimeago).split(".")[0] + "000"
print("starttime",starttime)
