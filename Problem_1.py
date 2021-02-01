import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from CleanData import clean_eng_text


def get_all_msg():
    posts_data = pd.read_csv('FBPosts.csv', encoding='utf-8')
    message = posts_data['message_and_description']
    return message


def get_one_movie_msg(imdb_id):
    posts_data = pd.read_csv('FBPosts.csv', encoding='utf-8')
    message = posts_data[posts_data['imdb_id'] == imdb_id]['message_and_description']
    message = message.reset_index().iloc[:, -1]
    return message


def merge_msg(msg_series):
    message = ' '.join(msg_series)
    return message


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


def plot_rank_freq(words_df):
    words_df = words_df.iloc[0:1000, :]
    plt.figure(figsize=(7, 5))
    plt.scatter(words_df.iloc[:, 0], words_df.iloc[:, 2], marker='o')
    plt.grid(True)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title('Scatter Plot')
    plt.show()


if __name__ == '__main__':
    msgSeries = get_all_msg()
    fullMsg = merge_msg(msgSeries)
    msg_noStopWords = clean_eng_text(fullMsg)
    msg_withStopWords = clean_eng_text(fullMsg, rm_stpwds=False)
    wordsCnt_noStop = words_count(msg_noStopWords)
    plot_rank_freq(wordsCnt_noStop)
    wordsCnt_withStop = words_count(msg_withStopWords)
    plot_rank_freq(wordsCnt_withStop)
