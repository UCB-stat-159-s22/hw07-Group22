# import packages
import pandas as pd
import numpy as np
from collections import Counter
import re
import matplotlib.pyplot as plt
from IPython.display import display_html


def country_common_charac(chocolate_df, country_name):
    """
    Inputs:
        chocolate_df: dataframe containing chocolate bars info
        country_name: a country of bean origin
    Output:
        a dataframe containing all the characteristics for that country with their frequency and percentage of appearance
    """
    chocolate_country = chocolate_df[chocolate_df['Country of Bean Origin'] == country_name][["Most Memorable Characteristics"]]
    charac_lst = chocolate_country['Most Memorable Characteristics'].tolist()
    lst = []
    for i in np.arange(len(charac_lst)):
        charac_lst[i] = charac_lst[i].split(', ')

    for i in charac_lst:
        for j in i:
            lst.append(j)

    dic = Counter(lst)
    df = pd.DataFrame(dic.items(), columns=['characteristics', 'frequency']).sort_values(by=['frequency'], ascending=False)
    df['percentage'] = [i / sum(df['frequency'].tolist()) for i in df['frequency'].tolist()]
    return df


# Display_dfs helps to display multiple dataframes at once
def display_dfs(dfs, gap=50, justify='center'):
    html = ""
    for title, df in dfs.items():  
        df_html = df._repr_html_()
        cur_html = f'<div> <h3>{title}</h3> {df_html}</div>'
        html +=  cur_html
    html= f"""
    <div style="display:flex; gap:{gap}px; justify-content:{justify};">
        {html}
    </div>
    """
    display_html(html, raw=True)

def rangeScore(x):
    '''
    Set the bins for the score-range.
    input: dataframe with score value
    output: assigned score range
    '''
    value = ''
    if (x>= 0 and x < 1):
        value = '0-1'
    elif (x>= 1 and x < 2):
        value = '1-2'
    elif (x>= 2 and x < 3):
        value = '2-3'
    elif (x>= 3 and x < 4):
        value = '3-4'
    elif (x >= 4 and x  < 5):
        value = '4-5'
    return value