# file = sys.argv
# for filename in file:
#     print(filename)
# i = 0
# while True:
#     i = i + 1
import time

# 将获取到的年月日转换为 - 连接
split_time = time.strptime("2017年1月9日", "%Y年%m月%d日")
print(split_time)
time = "{}-{:0>2d}-{:0>2d}".format(split_time.tm_year, split_time.tm_mon, split_time.tm_mday)
print(time)
