import math
class TimeTrack:
    TotalDay = 0
    Day = 0
    Week = 0
    Month = 0
    Year = 0
class MonthDays:
    @staticmethod
    def get_days(year):
        leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return [0, 31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
