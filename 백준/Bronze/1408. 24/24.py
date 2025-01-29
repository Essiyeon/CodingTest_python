now = input().split(':')
start = input().split(':')

now_h = int(now[0])*3600
now_m = int(now[1])*60
now_s = int(now[2])
now_total = now_h + now_m + now_s
# print(now_total)

start_h = int(start[0])*3600
start_m = int(start[1])*60
start_s = int(start[2])
start_total = start_h + start_m + start_s
# print(start_total)

use_time = now_total - start_total
if use_time < 0 :
  use_time = use_time + 24*3600

remain = 24*3600 - use_time
# print(remain)

remain_h = remain//3600
remain_m = (remain%3600)//60
remain_s = (remain%3600)%60

print(f'{remain_h:02}:{remain_m:02}:{remain_s:02}')

