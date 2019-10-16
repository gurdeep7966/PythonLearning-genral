import psutil

while True:

    cpu_utilization=psutil.cpu_percent(interval=1)
    print (cpu_utilization)