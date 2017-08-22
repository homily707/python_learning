import time
import os

def GetTime():
    time_list = list(time.localtime())
    return time_list

def CheckTime(time_remain,h1,m1,h2,m2):
    hour_remain = time_remain // 60
    mins_remain = time_remain % 60
    if (mins_remain + m1) >= 60 :
        if ((mins_remain + m1) == (60 + m2)) and ((hour_remain + h1) == (1+h2)) :
            return True
        else:
            return False
    else:
        if ((mins_remain + m1) == m2) and ((hour_remain + h1) == h2) :
            return True
        else:
            return False          

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
    print('now is {}:{}'.format(hour_now,mins_now))
    print('begin counting')
    while not CheckTime(time_for_once,hour_last,mins_last,hour_now,mins_now):
        time_now = GetTime()
        hour_now = time_now[3]
        mins_now = time_now[4]  
    total_times += 1  
    print('{} mins already'.format(total_times))
    os.system('notepad e:\\code\\py\\alarm\\alarm.txt')
