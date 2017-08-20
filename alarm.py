import time
import os

def GetTime():
    time_list = list(time.localtime())
    return time_list

total_times = 0
time_for_once = 1

time_last = GetTime()
hour_last = time_last[3]
mins_last = time_last[4]    
hour_now = hour_last
mins_now = mins_last
print('open success')

while True:
    mins_last = mins_now
    hour_last = hour_now
    print('begin counting')
    while ((mins_now - mins_last) != time_for_once):
        time_now = GetTime()
        hour_now = time_now[3]
        mins_now = time_now[4]  
    total_times += 1  
    print('{} mins already'.format(total_times))
    os.system('notepad e:\\code\\py\\alarm\\alarm.txt')
