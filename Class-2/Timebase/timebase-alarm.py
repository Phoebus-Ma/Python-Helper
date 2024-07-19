###
# Python alarm clock example.
#
# License - MIT.
###

from time import sleep
from datetime import datetime


# Alarm function.
def wait_alarm(hour, min, sec) -> int:
# {
    # Calibration factor.
    if 55 < sec:
        min = min + 1
        sec = 0

    while True:
        alm_time = datetime.now()

        if alm_time.hour == hour:
            if alm_time.minute == min:
                if alm_time.second >= sec:
                    print(alm_time.ctime())
                    print('Alarm, Di di di di~')
                    break

        sleep(2)

    return 0
# }


# Verify date time.
def verify_time(hour, min, sec) -> bool:
# {
    if 24 < hour:
        return False
    
    if 59 < min:
        return False

    if 59 < sec:
        return False

    return True
# }


# Main function.
def main() -> int:
# {
    # Such as: 09:30:00, 17:59:59
    alarm_time = input("Input alarm time(HH:MM:SS):")

    if len('HH:MM:SS') != len(alarm_time):
        print('Error for input time format.')
        return -1

    alarm_hour = int(alarm_time[0:2])
    alarm_min  = int(alarm_time[3:5])
    alarm_sec  = int(alarm_time[6:8])

    if not verify_time(alarm_hour, alarm_min, alarm_sec):
        print('Error for overflow time.')
        return -1

    wait_alarm(alarm_hour, alarm_min, alarm_sec)

    return 0
# }


# Program entry.
if '__main__' == __name__:
# {
    main()
# }
