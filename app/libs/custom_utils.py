from datetime import datetime as dt

DOB_FORMAT = {
    'DOB': '%Y-%m-%d',
}
def check_ten_digit_number(number):
    if int(len(number)) != 10:
        return False
    else:return number

def parse_datetime_str(datetime_str):
    """
    parse date string in format C.DATETIME_FORMAT['DATE']
    """
    return dt.strptime(datetime_str, DOB_FORMAT['DOB'])