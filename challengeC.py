import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter.messagebox import showinfo

# C#1
# Data cleaning for Sheet 1
df = pd.read_excel(r'SocMed_Geographic.xlsx', 'Sheet1')
df = df.dropna(how='all')
df = df.rename(columns={'Number of users ': 'United States', 'Unnamed: 2': 'Indonesia', 'Unnamed: 3': 'Singapore',
                        'Unnamed: 4': 'China', 'Unnamed: 5': 'India', 'Unnamed: 6': 'Vietnam', 'Unnamed: 7': 'Philippines', 'Unnamed: 8': 'Bangladesh'})
df = df.drop(df.index[0])

# C#1 optional
population_data = [{'United States': 331449281, 'Indonesia': 270200000, 'Singapore': 5453600,
                    'China': 1443497378, 'India': 1380000000, 'Vietnam': 96208984, 'Philippines': 109035343, 'Bangladesh': 164689383}]
population_df = pd.DataFrame(population_data)


for col in df.columns:
    if col == 'Social Media Platform':
        continue
    # Remove substrings that are not numbers
    df[col] = df[col].str.replace(r" \(.*\)", "", regex=True)
    df[col] = df[col].str.replace(" ", "", regex=True)
    df[col] = df[col].str.replace(",", "", regex=True)
    df[col] = df[col].str.replace("\u202c", "", regex=True)
    df[col] = df[col].fillna(0)
    df[col] = df[col].astype(int)
    # Divide num of users with the population
    df[col] = (df[col]/population_df[col].values[0])


df = df.T
df = df.rename(columns={1: 'Bilibili', 2: 'Facebook', 3: 'Instagram', 4: 'Linkedln',
                        5: 'Tencent QQ', 6: 'Tik Tok', 7: 'Twitter', 8: 'WeChat', 9: 'Weibo', 10: 'Youtube'})
df = df.drop(df.index[0])
df = df.apply(pd.to_numeric)


# C#1: Plot heatmap


def plot_heatmap(s):
    x_axis_labels = ['United States', 'Indonesia', 'Singapore',
                     'China', 'India', 'Vietnam', 'Philippines', 'Bangladesh']
    h = sns.heatmap(df[s].to_numpy().reshape(1, len(df.index)), cmap='coolwarm',
                    xticklabels=x_axis_labels, yticklabels=['Number of users / population'], annot=True, annot_kws={'rotation': 90})
    plt.xticks(rotation=35)
    plt.yticks(va='center')
    plt.title("Heatmap for " + s)
    plt.show()


# C#2
# Data cleaning for Sheet 2
df2 = pd.read_excel(r'SocMed_Geographic.xlsx', 'Sheet2')
df2 = df2.rename(columns={'Duration of time spent on platform per day': 'United States', 'Unnamed: 2': 'Indonesia', 'Unnamed: 3': 'Singapore',
                          'Unnamed: 4': 'China', 'Unnamed: 5': 'India', 'Unnamed: 6': 'Vietnam', 'Unnamed: 7': 'Philippines', 'Unnamed: 8': 'Bangladesh'})
df2 = df2.drop(df2.index[0])
for col in df2.columns:
    if col == 'Social Media ':
        continue
    df2[col] = df2[col].str.replace(r" \(.*\)", "", regex=True)
    df2[col] = df2[col].str.replace(" ", "", regex=True)
    df2[col] = df2[col].str.replace(",", "", regex=True)
    df2[col] = df2[col].str.replace("\u202c", "", regex=True)
    df2[col] = df2[col].fillna(0)

# Convert the units of all duration of time to minute, for those without units treat them as minute
for col in df2.columns:
    if col == 'Social Media ':
        continue
    for i in range(len(df.index)):
        if isinstance(df2[col].values[i-1], int) or isinstance(df2[col].values[i-1], float):
            continue
        elif any(j.isdigit() for j in df2[col].values[i-1]) == False:
            # Not sure how to convert 'fourhour' to 240 minutes, so I change it manually
            df2[col].values[i-1] = 240.0
        elif ('hour' and 'mins') in df2[col].values[i-1]:
            a, b = df2[col].values[i-1].split('hour')
            df2[col].values[i-1] = float(a)*60 + \
                float(b.translate({ord(j): None for j in 'mins'}))
        elif 'hours' in df2[col].values[i-1]:
            df2[col].values[i-1] = df2[col].values[i -
                                                   1].translate({ord(j): None for j in 'hours'})
            # Convert hour to minutes
            df2[col].values[i-1] = float(df2[col].values[i-1]) * 60
        elif 'minutes' in df2[col].values[i-1]:
            df2[col].values[i-1] = df2[col].values[i -
                                                   1].translate({ord(j): None for j in 'minutes'})
            df2[col].values[i-1] = float(df2[col].values[i-1])
        else:
            df2[col].values[i-1] = float(df2[col].values[i-1])

# C#2: Show social media usage ranking for each country


def show_rank(s):
    df2[s] = df2[s].astype(float)
    sorted_df2 = df2.sort_values(s, ascending=False)
    x_axis = sorted_df2['Social Media ']
    y_axis = sorted_df2[s]
    plt.bar(x_axis, y_axis)
    plt.xticks(rotation=35)
    plt.ylabel('Duration (mins)')
    plt.title("Social Media Usage Ranking in " + s)
    plt.show()


window = tk.Tk()

# Buttons for Challenge C #1
# For user to choose the heatmap of which social media to view
window.title('Challenge C')
c1 = tk.Label(window, text="#1 Heatmap for each social media network",
              width="45", height="1")
c1.pack()


def c1_button_event(s):
    plot_heatmap(s)


button1 = tk.Button(window, text='Bilibili',
                    command=lambda: c1_button_event('Bilibili'))
button1.pack()

button2 = tk.Button(window, text='Facebook',
                    command=lambda: c1_button_event('Facebook'))
button2.pack()

button3 = tk.Button(window, text='Instagram',
                    command=lambda: c1_button_event('Instagram'))
button3.pack()

button4 = tk.Button(window, text='Linkedln',
                    command=lambda: c1_button_event('Linkedln'))
button4.pack()

button5 = tk.Button(window, text='Tencent QQ',
                    command=lambda: c1_button_event('Tencent QQ'))
button5.pack()

button6 = tk.Button(window, text='Tik Tok',
                    command=lambda: c1_button_event('Tik Tok'))
button6.pack()

button7 = tk.Button(window, text='Twitter',
                    command=lambda: c1_button_event('Twitter'))
button7.pack()

button8 = tk.Button(window, text='WeChat',
                    command=lambda: c1_button_event('WeChat'))
button8.pack()

button9 = tk.Button(window, text='Weibo',
                    command=lambda: c1_button_event('Weibo'))
button9.pack()

button10 = tk.Button(window, text='Youtube',
                     command=lambda: c1_button_event('Youtube'))
button10.pack()

# Buttons for Challenge C #2
c2 = tk.Label(window, text="#2 Rank social network usage by platform for each country",
              width="50", height="1")
c2.pack()


def c2_button_event(s):
    show_rank(s)


c2_button1 = tk.Button(window, text='United States',
                       command=lambda: c2_button_event('United States'))
c2_button1.pack()

c2_button2 = tk.Button(window, text='Indonesia',
                       command=lambda: c2_button_event('Indonesia'))
c2_button2.pack()

c2_button3 = tk.Button(window, text='Singapore',
                       command=lambda: c2_button_event('Singapore'))
c2_button3.pack()

c2_button4 = tk.Button(window, text='China',
                       command=lambda: c2_button_event('China'))
c2_button4.pack()

c2_button5 = tk.Button(window, text='India',
                       command=lambda: c2_button_event('India'))
c2_button5.pack()

c2_button6 = tk.Button(window, text='Vietnam',
                       command=lambda: c2_button_event('Vietnam'))
c2_button6.pack()

c2_button7 = tk.Button(window, text='Philippines',
                       command=lambda: c2_button_event('Philippines'))
c2_button7.pack()

c2_button8 = tk.Button(window, text='Bangladesh',
                       command=lambda: c2_button_event('Bangladesh'))
c2_button8.pack()

window.mainloop()
