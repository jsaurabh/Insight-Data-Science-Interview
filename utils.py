from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import math
import datetime

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def build_word_cloud(df, feature):
    wordcloud = WordCloud(stopwords = STOPWORDS, background_color = 'white', height = 2000, width= 1600).generate(''.join(df[feature]))
    plt.figure(figsize=(16,8))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

def clean_num(x):
    try:
        return float(x)
    except:
        return math.nan

def get_month(x):
    try:
        return months[int(str(x).split('-')[1]) - 1]
    except:
        return math.nan

def get_day(x):
    try:
        y,m,d = (int(i) for i in x.split('-'))    
        return days[datetime.date(year, month, day).weekday()]
    except:
        return math.nan

def clean(x):
    try:
        return float(x)
    except:
        return math.nan