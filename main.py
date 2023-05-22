import datetime

def determine_weekday(year, month, day):
    try:
        date = datetime.datetime(year, month, day)
        weekday = date.strftime('%A')
        return weekday
    except ValueError:
        return "Invalid date"

# 获取用户输入
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))

# 调用函数判断星期几
weekday = determine_weekday(year, month, day)
print("该日期是：", weekday)
