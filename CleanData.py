import pandas as pd
import numpy as np
from Function_Bags import merge_msg, get_one_movie_msg


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


def posts_by_film():
    posts_data = pd.read_csv('FBPosts.csv', encoding='utf-8')
    file_id = list(set(posts_data['imdb_id']))
    msg_dataframe = pd.DataFrame()
    msg_dataframe['imdb_id'] = file_id
    msg_dataframe['posts'] = msg_dataframe.apply(lambda x: merge_msg(get_one_movie_msg(posts_data, [0])), axis=1)
    msg_dataframe['CleanedPosts'] = msg_dataframe.apply(lambda x: ' '.join(clean_eng_text(x[1])), axis=1)
    msg_dataframe.to_csv('MergedPosts.csv')
    print(msg_dataframe)


if __name__ == '__main__':
    pass
