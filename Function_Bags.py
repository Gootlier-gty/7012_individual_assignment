import pandas as pd
from collections import Counter
import numpy as np


def get_all_msg(posts_data):
    message = posts_data['message_and_description']
    return message  # pd.series


def get_one_movie_msg(raw_data_df, imdb_id):
    message = raw_data_df[raw_data_df['imdb_id'] == imdb_id]['message_and_description']
    message = message.reset_index().iloc[:, -1]
    return message  # pd.series


def merge_msg(msg_series):
    message = ' '.join(msg_series)
    return message  # str


def clean_eng_text(text, rm_stpwds=True, rm_noEng=True):
    stop_words = pd.read_csv('stop_words.txt', header=None)[0].tolist()
    text = text.lower().split(sep=' ')
    text = pd.DataFrame(text)[0]
    if rm_stpwds:
        # remove stop words
        text = text[-text.isin(stop_words)].reset_index().iloc[:, -1]
    # remove urls
    text = text[-text.str.contains('www')]
    text = text[-text.str.contains('http')].reset_index().iloc[:, -1]
    if rm_noEng:
        # remove punctuations and nonEnglish words
        text = text.str.replace(r'[^a-zA-Z0\d]+', '')
    else:
        # only remove punctuation
        text = text.str.replace(r'[^\w]+', '')
    if rm_stpwds:
        # remove stop words again
        text = text[-text.isin(stop_words)].reset_index().iloc[:, -1]
    # remove empty value
    text = text[-text.isin([' ', '', None, np.nan])].reset_index().iloc[:, -1]
    return text.tolist()


def words_count(words_list):
    cnt = Counter()
    for word in words_list:
        cnt[word] += 1
    words = list(cnt.keys())
    num = list(cnt.values())
    words_count = pd.DataFrame({'words': words,
                                'num': num})
    words_count.sort_values(by='num', ascending=False, inplace=True)
    return words_count.reset_index().iloc[:, 1:].reset_index()
