import os
import time

# Function to get system uptime
def get_uptime():
    uptime_seconds = os.popen('awk \"/proc/uptime/{print $1}\"').read()
    uptime_hours = int(float(uptime_seconds)) // 3600
    uptime_minutes = (int(float(uptime_seconds)) % 3600) // 60
    return f'Uptime: {uptime_hours} hours, {uptime_minutes} minutes'

if __name__ == '__main__':
    print(get_uptime())