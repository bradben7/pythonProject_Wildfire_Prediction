import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
pd.set_option('display.max_rows', None)
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv')
print(df.head(30))
from collections import Counter as ct
from functools import reduce




wind = df['wind']
RH = df['RH']
FFMC = df['FFMC']
DMC = df['DMC']
DC = df['DC']
ISI = df['ISI']
temp = df['temp']
rain = df['rain']
area = df['area']
X = df['X']


def area_vs_FFMC(area, FFMC):
    x = area
    y = FFMC
    plt.scatter(x, y, marker='o')
    plt.show()
    return
def area_vs_wind(area, wind):
    x = area
    y = wind
    plt.scatter(x, y, marker='o')
    plt.show()
    return
def area_vs_RH(area, RH):
    x = area
    y = RH
    plt.scatter(x, y, marker='o')
    plt.show()
    return
def area_vs_temp(area,temp):
    x = area
    y = temp
    plt.scatter(x, y, marker='o')
    plt.show()
    return
def area_vs_DMC (area,temp):
    x = area
    y = DMC
    plt.scatter(x, y, marker='o')
    plt.show()
    return
def area_vs_DC(area,DC):
    x = area
    y = DC
    plt.scatter(x, y, marker='o')
    plt.show()
    return
def area_vs_rain(area, rain):
    x = area
    y = rain
    plt.scatter(x, y, marker='o')
    plt.show()
    return
def area_vs_ISI(area, ISI):
    x = area
    y = ISI
    plt.scatter(x, y, marker='o')
    plt.show()
    return


def mean(numbers):
    total_num = reduce(lambda x, y: x + y, numbers)
    mean_num = total_num / len(numbers)
    return mean_num


def median(wind):
    wind_sorted = sorted(wind)
    length = len(wind_sorted)
    if length % 2 == 0:
        mid_num = wind_sorted[int(length / 2)]
        median_num = (mid_num + wind_sorted[(length / 2) - 1]) / 2

    if length % 2 != 0:
        median_num = wind_sorted[int(length // 2)]
    return median_num


def mode(n_num):
    n = len(n_num)

    data = ct(n_num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = ', '.join(map(str, mode))

    return get_mode


print('mean of the wind speed is :', mean(wind))
print('median of the wind speed is :', median(wind))
print('mean of the RH is :', mean(RH))
print('median of the RH is :', median(RH))
print('mean of the X is :', mean(X))
print('median of the X is :', median(X))
print('mode of the X is :', mode(X))

area_vs_FFMC(area,FFMC)
area_vs_wind(area, wind)
area_vs_RH(area,RH)
area_vs_temp(area,temp)
area_vs_DMC(area, DMC)
area_vs_DC(area,DC)
area_vs_rain(area,rain)
area_vs_ISI(area,ISI)
#from the graph, we can see that the area of the fire is directly related to FFMC, 