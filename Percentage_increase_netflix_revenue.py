import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("netflix_revenue_2020.csv")

a = data['area']
y = data['years']
r = data['revenue']

#revenue in 2018
i = 0
total_2018 = 0
while i < 16:
    total_2018 += r[i]
    i += 1

total_2018

#revenue in 2019
i = 16
total_2019 = 0
while i < 32:
    total_2019 += r[i]
    i += 1

total_2019

#percentage increase 2019
diff_2019 = total_2019 - total_2018

percent_2019 = diff_2019/total_2018

#revenue 2020
i = 32
total_2020 = 0
while i < 40:
    total_2020 += r[i]
    i += 1

total_2020

#percentage increase 2020
diff_2020 = total_2020 - total_2019

percent_2020 = diff_2020/total_2019

#bar graph
y = np.array([percent_2019, percent_2020])
mylabels = ["2019", "2020"]

plt.bar(mylabels, y)
plt.show()
