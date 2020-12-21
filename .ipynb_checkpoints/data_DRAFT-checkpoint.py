import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
REF = 'https://towardsdatascience.com/bar-chart-race-in-python-with-matplotlib-8e687a5c8a41'

df = pd.read_csv('https://gist.githubusercontent.com/johnburnmurdoch/4199dbe55095c3e13de8d5b2e5e5307a/raw/fa018b25c24b7b5f47fd0568937ff6c04e384786/city_populations', usecols=['name', 'group', 'year', 'value'])

#df.head(3)
current_year = 2018
dff = (df[df['year'].eq(current_year)].sort_values(by='value', ascending=True).head(10))
# dff

##########____CLASSICAL PLOT__________
# fig, ax = plt.subplots(figsize=(15, 8))
# ax.barh(dff['name'], dff['value'])

############_______improved with colors______________
colors = dict(zip(['India', 'Europe', 'Asia', 'Latin America',
     'Middle East', 'North America', 'Africa'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
     '#aafbff', '#f7bb5f', '#eafb50']))
group_lk = df.set_index('name')['group'].to_dict()


# fig, ax = plt.subplots(figsize=(15, 8))
# dff = dff[::-1]   # flip values from top to bottom
# # pass colors values to `color=`
# ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
# # iterate over the values to plot labels and values (Tokyo, Asia, 38194.2)
# for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
#     ax.text(value, i,     name,            ha='right')  # Tokyo: name
#     ax.text(value, i-.25, group_lk[name],  ha='right')  # Asia: group name
#     ax.text(value, i,     value,           ha='left')   # 38194.2: value
# # Add year right middle portion of canvas
# ax.text(1, 0.4, current_year, transform=ax.transAxes, size=46, ha='right')







fig, ax = plt.subplots(figsize=(15, 8))
def draw_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
    # ... polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, 'The most populous cities in the world from 1500 to 2018',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.text(1, 0, 'by @pratapvardhan; credit @jburnmurdoch', transform=ax.transAxes, ha='right',
            color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)
    
#draw_barchart(2018)

import matplotlib.animation as animation
from IPython.display import HTML
#fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1968, 2019))
HTML(animator.to_jshtml()) 
# or use animator.to_html5_video() or animator.save()

plt.show()








































# import numpy as np
# #import thingspeak
# import json
# import time
# import matplotlib.pyplot as plt



# def plot_my_data():
#     x=0
#     xx=0
    
#     temp_list = []
#     turb_list = []
#     x_cordinates = []
#     while x>=0 and xx==0:
#         print("good")
#         x_cordinates.append(x)
#         x = x + 1
#         ch = thingspeak.Channel(id=817351, api_key='H8QFEOWP3N5FFHC6',fmt='json')
#         data_from_thingspeak=ch.get({'results': 2})
#         data_list_from_thingspeak=data_from_thingspeak.split(",")

#         #print(data_from_thingspeak)
#         #print(data_list_from_thingspeak)

#         print("")
#         print("")
#         temperature=data_list_from_thingspeak[12]
#         temperature=temperature.split('"')
#         temperature = temperature[3]
#         print("Temperature = ",temperature)
#         temp_list.append(float(temperature))

#         print("")
#         print("")

#         #time.sleep(1)

#         turbidity=data_list_from_thingspeak[13]
#         turbidity=turbidity.split('"')
#         turbidity=turbidity[3]
#         turbidity=turbidity.split(" ")
#         turbidity = turbidity[0]
#         print("Pressure = ",turbidity)
#         turb_list.append(float(turbidity))

#         #time.sleep(1)

#         #Ploting data

#         #plt.scatter(x_cordinates,temp_list,color='r')
#         plt.plot(x_cordinates,temp_list,color='r')
#         plt.plot(x_cordinates,turb_list,color='b')
#         #labeling x and y axis
#         plt.xlabel('Data intries No')
#         plt.ylabel('Data values')

#         #titlle of my plot
#         plt.title('CanSat data')
#         #to show the graph
#         #plt.show()
#         plt.pause(0.0001)
#         #print("good_good")
#         time.sleep(5)

        
#         if x==10:
#             xx=5
#     print(x_cordinates)
#     print(temp_list)
#     print(turb_list)
# #plot_my_data()