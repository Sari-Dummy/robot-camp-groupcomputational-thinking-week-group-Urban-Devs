from datetime import datetime
def solution_station_2(date_string):
    date = 0
    date = datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = 0
    day_in_japanese = ''
    day_of_week = date.weekday()
    if day_of_week == 0:
        day_in_japanese = '月曜日'
    if day_of_week == 1:
        day_in_japanese = '火曜日'
    if day_of_week == 2:
        day_in_japanese = '水曜日'
    if day_of_week == 3:
        day_in_japanese = '木曜日'
    if day_of_week == 4:
        day_in_japanese = '金曜日'
    if day_of_week == 5:
        day_in_japanese = '土曜日'
    if day_of_week == 6:
        day_in_japanese = '日曜日'
    return day_in_japanese
