# Task 19 - Python
# Counting Sundays

import time
import calendar

def date_checker():
    number_sundays = 0
    calendar.setfirstweekday(6)

    for year in range(1901, 2001, 1):
        for month in range(1, 13, 1):
            if calendar.weekday(year, month, 1) == calendar.SUNDAY:
                number_sundays += 1
    return number_sundays

def main():
    time_start = time.time()
    counting_sundays = date_checker()

    print("Answer: {0} => Calculated in: {1}".format(counting_sundays, (time.time() - time_start)))

if __name__ == '__main__':
    main()