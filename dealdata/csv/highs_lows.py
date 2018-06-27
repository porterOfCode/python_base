import csv
from matplotlib import pyplot as plt

from datetime import datetime

filename = "death_valley_2014.csv"
# filename = "sitka_weather_07-2014.csv"
# filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)   # next获取下一行数值
    # print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # 获取最高气温
    dates, highs, lows = [], [], []
    info_dict = {}
    for rows in reader:
        # if rows[1] != "":
        try:
            current_date = datetime.strptime(rows[0], "%Y-%m-%d")
            high = int(rows[1])
            low = int(rows[3])
        except ValueError:
            print(current_date, 'miss data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

            info_dict['pst'] = current_date
            info_dict['maxTemperatureF'] = (high)
            info_dict['minTemperatureF'] = (low)
            print(info_dict)
        finally:
            print("---------------我是分割线---------------")

print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
# 填充两个y值之间的空间 alpha为透明度
plt.fill_between(dates, highs, lows, facecolor='green', alpha=1)

# 设置图形的格式
plt.title("Daliy high and low temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)

# 设置刻度标记的大小
# axis为影响范围，both为x&y
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
