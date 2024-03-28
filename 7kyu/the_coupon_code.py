"""Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False"""


import calendar
from datetime import date

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if str(entered_code) != str(correct_code) or type(entered_code) == int and type(correct_code) == str:
        return False
    months = list(calendar.month_name)
    current_date_parts = current_date.split()
    expiration_date_parts = expiration_date.split()
    current_day = int(current_date_parts[1].replace(',', ''))
    expiration_day = int(expiration_date_parts[1].replace(',', ''))
    current_date = date(int(current_date_parts[2]), months.index(current_date_parts[0]), current_day)
    expiration_date = date(int(expiration_date_parts[2]), months.index(expiration_date_parts[0]), expiration_day)
    return current_date <= expiration_date

