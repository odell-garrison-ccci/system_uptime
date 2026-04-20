import os
import time

# Function to get the system uptime
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

# Print the system uptime
if __name__ == '__main__':
    uptime = get_uptime()
    print(f'System Uptime: {uptime // 3600} hours, {(uptime % 3600) // 60} minutes, {uptime % 60} seconds')