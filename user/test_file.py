from datetime import datetime, time
import datetime
from datetime import datetime, timedelta
import datetime
#
# time_str1 = datetime.datetime.now().time()
# time_str2 = datetime.datetime.now().time()


# #
# def time_diff(time_str1, time_str2):
#     t1 = datetime.datetime.strptime('time_str1', '%H:%M')
#     t2 = datetime.datetime.strptime('time_str2', '%H:%M')
#     dt = abs(t2 - t1)
#     print(time_str1)
#     time(dt.seconds // 3600, (dt.seconds // 60) % 60).strftime('%H:%M')
#
#
# time_diff(time_str1, time_str2)
#
#
#
from time import sleep

currentDate_in = datetime.date.today()
currentTime_in = datetime.datetime.now().time()

currentDate_out = datetime.date.today()
currentTime_out = datetime.datetime.now().time()

clock_in = datetime.datetime.now()
sleep(65)
clock_out = datetime.datetime.now()
duration = clock_out - clock_in

print(currentDate_in)
print(currentTime_in)
print(currentDate_out)
print(currentTime_out)

print(duration)

#
# log_in_time = datetime.now()
# log_out_time = datetime.now()
#
# # time formatting
# '{:%H:%M:%S}'.format(log_in_time, log_out_time)
#
# updated_time = log_in_time + timedelta('log_out_time')
# print(updated_time)
#
# from timer import Timer
#
# t = Timer()
# t.start()
#
# t.stop()

# formatt = '{:%H:%M:%S}'.format(time_str1, time_str2)
# t1 = datetime.datetime.strptime('time_str1', 'formatt')
# t2 = datetime.datetime.strptime('time_str2', 'formatt')
#
# dt = abs(t2 - t1)
#
# t = time(dt.seconds // 3600, (dt.seconds // 60) % 60)
#
# t.strftime('%H:%M')

# from timer import Timer
# from reader import feed
#
# def main():
#     """Print the latest tutorial from Real Python"""
#     t = Timer()
#     t.start()
#     tutorial = feed.get_article(0)
#     t.stop()
#
#     print(tutorial)
#
# if __name__ == "__main__":
#     main()