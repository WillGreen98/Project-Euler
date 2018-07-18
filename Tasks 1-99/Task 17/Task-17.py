# Task 17 - Python
# Number letter counts

import time

num_ln = {ln: len(number) for (ln, number) in {
            "Units": {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"},
            "Tens": {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"},
            "Extra": {'and': "and", 100: "Hundred", 1000: "Thousand"}}.items()}

def count_letters():
    total = 0
    for i in range(1, 1000, 1):
        digit_units = (i % 10)
        digit_tens = (((i % 100) - digit_units) / 10)
        digit_hundreds = (((i % 1000) - (digit_tens * 10) - digit_units) / 100)

        if digit_hundreds != 0:
            total += num_ln['Units'][digit_hundreds] + num_ln['Extra'][1000]
            if digit_tens != 0 or digit_units != 0:
                total += num_ln['Extra']["and"]
        if digit_tens == 0 or digit_tens == 1:
            total += num_ln['Units'][(num_ln["Units"][digit_units] * 10) + digit_units]
        else: total += num_ln['Tens'][digit_tens] + num_ln["Units"][digit_tens]

    return total
def main():
    time_start = time.time()
    letters_count = count_letters()

    print("Answer: {0} => Calculated in: {1}".format(letters_count, (time.time() - time_start)))

if __name__ == '__main__':
    main()