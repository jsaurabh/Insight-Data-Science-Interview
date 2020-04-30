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

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return math.nan

def get_list(x, n = 5):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        if len(names) > n:
            names = names[:n]
        return names

    return []

def clean_list(x):
    if isinstance(x, list):
        return [str.lower(idx.replace(" ", "")) for idx in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ""
        
def create_feature(x):
    keywords = ' '.join(x['keywords'])
    cast = ' '.join(x['cast'])
    genre = ' '.join(x['genres'])
    return keywords + ' ' + cast + ' ' + genre + ' ' + str(x['director'])