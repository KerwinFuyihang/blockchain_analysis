#this script is to transform the unix time to YYYY-MM-DD H:M:S time


import time

timestamp = 1438214400000 / 1000

time_tuple = time.localtime(timestamp)

formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)

print(formatted_time)