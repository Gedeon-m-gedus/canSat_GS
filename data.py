import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
from datetime import date, time, datetime
import os

data = {
    'name': ['temp','hum','press','alt','temp','hum','press','alt','temp','hum','press','alt','temp','hum','press','alt'],
    #'group':['HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD','HKD'],
    'group': ['Celcius','Percent_%','Bar','Meters','Celcius','Percent_%','Bar','Meters','Celcius','Percent_%','Bar','Meters','Celcius','Percent_%','Bar','Meters'],
    'year': [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3],
    'value':[27,62,847,1478, 25.2,68.07,853,1462, 29.6,69.4,867,1438, 27,65,842,1458]
}

df = pd.DataFrame.from_dict(data)

colors = dict(zip(['temp','hum','press','alt'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381']))
group_lk = df.set_index('name')['group'].to_dict()


fig, ax = plt.subplots(figsize=(15, 8))
def draw_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'],color=['#adb0ff', '#ffb3ff', '#90d595', '#e48381'])
    dx = dff['value'].max() / 20
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
        
    # ... polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Magnitude', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0.5, 1.12, 'CanSat Data Visiulization',
            transform=ax.transAxes, size=24, weight=600, ha='center')
    plt.box(False)
    

def view_hdk():
    animator = animation.FuncAnimation(fig, draw_barchart, frames=range(0, 4))
    HTML(animator.to_jshtml()) 
    # or use animator.to_html5_video() or animator.save()
    plt.show()
    
def handle_dirs(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def exp_name(model = 'data'):
    now = datetime.now()
    today = date.today()
    tim = str(now.hour)+'-'+str(now.minute)
    dat = str(today)
    model = model + '___' +dat + '___' + tim +'.csv'
    return model

def exportHKD():
    dirpath = './files/data/'
    handle_dirs(dirpath)
    filepath = dirpath + exp_name()
    df.to_csv(filepath,index=False)
    return True
