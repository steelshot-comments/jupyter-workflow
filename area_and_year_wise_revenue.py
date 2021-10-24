import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("netflix_revenue_2020.csv")

a = data['area']
y = data['years']
r = data['revenue']

#First year variables

USC_year1_data = []
EMEA_year1_data = []
AP_year1_data = []
LA_year1_data = []

USC_year1_total = 0
EMEA_year1_total = 0
AP_year1_total = 0
LA_year1_total = 0

i = 0
while i < 16:
    if a[i] == 'United States and Canada':
        USC_year1_data.append(r[i])
    elif a[i] == 'Europe,  Middle East and Africa':
        EMEA_year1_data.append(r[i])
    elif a[i] == 'Latin America':
        LA_year1_data.append(r[i])
    elif a[i] == 'Asia-Pacific':
        AP_year1_data.append(r[i])
    i += 1
    
#First year totals

for x in USC_year1_data:
    USC_year1_total += x
    
for x in EMEA_year1_data:
    EMEA_year1_total += x

for x in AP_year1_data:
    AP_year1_total += x
    
for x in LA_year1_data:
    LA_year1_total += x
    
top3_2018 = [USC_year1_total, EMEA_year1_total, AP_year1_total, LA_year1_total]
top3_2018.sort()
top3_2018.pop(0)

top3_2018

#top3_2018
fig, ax = plt.subplots(1, 1)

mylabels = ["LA", "EMEA", "USC"]

plt.pie(top3_2018, labels = mylabels, autopct='%1.0f%%')
plt.show()

#Country wise revenue
plt.bar(['USC', 'EMEA', 'AP', 'LA'], [USC_year1_total, EMEA_year1_total, AP_year1_total, LA_year1_total])
plt.show()

# Second year variables
USC_year2_data = []
EMEA_year2_data = []
AP_year2_data = []
LA_year2_data = []

USC_year2_total = 0
EMEA_year2_total = 0
AP_year2_total = 0
LA_year2_total = 0

i = 16
while i < 32:
    if a[i] == 'United States and Canada':
        USC_year2_data.append(r[i])
    elif a[i] == 'Europe,  Middle East and Africa':
        EMEA_year2_data.append(r[i])
    elif a[i] == 'Latin America':
        LA_year2_data.append(r[i])
    elif a[i] == 'Asia-Pacific':
        AP_year2_data.append(r[i])
    i += 1
    
#second year totals
for x in USC_year2_data:
    USC_year2_total += x

for x in EMEA_year2_data:
    EMEA_year2_total += x
    
for x in AP_year2_data:
    AP_year2_total += x
   
for x in LA_year2_data:
    LA_year2_total += x
   
top3_2019 = [USC_year2_total, EMEA_year2_total, AP_year2_total, LA_year2_total]
top3_2019.sort()
top3_2019.pop(0)

#top3 2019
fig, ax = plt.subplots(1, 1)

mylabels = ["LA", "EMEA", "USC"]

plt.pie(top3_2019, labels = mylabels, autopct='%1.0f%%')
plt.show()

# country wise revenue
plt.bar(['USC', 'EMEA', 'AP', 'LA'], [USC_year2_total, EMEA_year2_total, AP_year2_total, LA_year2_total])
plt.show()

#First year variables
USC_year3_data = []
EMEA_year3_data = []
AP_year3_data = []
LA_year3_data = []

USC_year3_total = 0
EMEA_year3_total = 0
AP_year3_total = 0
LA_year3_total = 0

i = 32
while i < 40:
    if a[i] == 'United States and Canada':
        USC_year3_data.append(r[i])
    elif a[i] == 'Europe,  Middle East and Africa':
        EMEA_year3_data.append(r[i])
    elif a[i] == 'Latin America':
        LA_year3_data.append(r[i])
    elif a[i] == 'Asia-Pacific':
        AP_year3_data.append(r[i])
    i += 1
    
for x in USC_year3_data:
    USC_year3_total += x
    
for x in EMEA_year3_data:
    EMEA_year3_total += x
    
for x in AP_year3_data:
    AP_year3_total += x
    
for x in LA_year3_data:
    LA_year3_total += x
    
top3_2020 = [USC_year3_total, EMEA_year3_total, AP_year3_total, LA_year3_total]
top3_2020.sort()
top3_2020.pop(0)

#top3 2020
fig, ax = plt.subplots(1, 1)

plt.pie(top3_2020, labels = mylabels, autopct='%1.0f%%')
plt.show()

#area wise revenue 2020
plt.bar(['USC', 'EMEA', 'AP', 'LA'], [USC_year3_total, EMEA_year3_total, AP_year3_total, LA_year3_total])
plt.show()

#year wise revenue USC
plt.bar([2018, 2019, 2020], [USC_year1_total, USC_year2_total, USC_year3_total])
plt.show()

#year wise revenue EMEA
plt.bar([2018, 2019, 2020], [EMEA_year1_total, EMEA_year2_total, EMEA_year3_total])
plt.show()

#year wise revenue AP
plt.bar([2018, 2019, 2020], [AP_year1_total, AP_year2_total, AP_year3_total])
plt.show()

#year wise revenue LA
plt.bar([2018, 2019, 2020], [LA_year1_total, LA_year2_total, LA_year3_total])
plt.show()
