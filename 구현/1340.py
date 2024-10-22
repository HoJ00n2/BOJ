# # 51분 시작 (구현, 문자열, 파싱)

def convert_month_str_to_num(month_str):
    month_dict = {
        "January": 1, "February": 2, "March":3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    
    return month_dict[month_str]    


def check_leap_year_or_not(year):
    is_leap_year = False
    
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        is_leap_year = True
        
    return is_leap_year


def get_total_day_count(year, month=0, day=0):
    month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total_day = sum(month_day_list)
    
    if month != 0 and day != 0:
        total_day = total_day - sum(month_day_list[month-1:]) + day - 1
    
    if check_leap_year_or_not(year=year) and (month > 2 or month == 0):
        total_day += 1
        
    return total_day


def get_total_minute_from_day(total_day, hour, minute):
    return total_day * 24 * 60 + hour * 60 + minute


def year_progress_bar(year_time):
    month, dd, year, hh_mm = year_time.split()
    year, day = int(year), int(dd[:-1])
    hour, minute = list(map(int, hh_mm.split(":")))
    
    month = convert_month_str_to_num(month_str=month)
    
    total_year_day = get_total_day_count(year=year)
    
    total_day = get_total_day_count(year=year, month=month, day=day)
    
    total_year_minute = get_total_minute_from_day(
        total_day=total_year_day, hour=0, minute=0
    )
    
    total_minute = get_total_minute_from_day(
        total_day=total_day, hour=hour, minute=minute
    )
    
    return (total_minute / total_year_minute) * 100


if __name__ == "__main__":
    year_time = input()
    print(year_progress_bar(year_time=year_time))

# current = input()

# callender = {"January":31, "Feburary":28, "March":31, "April":30, "May":31, "June":30, 
#              "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
# month, dd, year, hour = current.split()
# year = int(year)
# dd = int(dd[:-1])
# hh, mm = hour.split(':')
# hh, mm = int(hh), int(mm)

# optional = False
# # 윤년
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     optional = True
    
# # 총 시간 (분 단위로 표현)
# if optional:
#     total_time = 366 * 24 * 60
#     callender["Feburary"] = 29
# else:
#     total_time = 365 * 24 * 60

# # 현재까지 누적된 시간
# current_day = 0
# for i in callender:
#     if i == month:
#         current_day += dd
#         break
#     current_day += callender[i]


# current_time = (current_day-1) * 24 * 60 + (hh * 60) + mm

# print((current_time/total_time)*100)