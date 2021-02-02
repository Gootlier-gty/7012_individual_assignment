from Function_Bags import get_all_msg, merge_msg, clean_eng_text, words_count
import matplotlib.pyplot as plt
import pandas as pd


def plot_rank_freq(words_df, title=None):
    words_df = words_df.iloc[0:1000, :]
    plt.figure(figsize=(7, 5))
    plt.scatter(words_df.iloc[:, 0], words_df.iloc[:, 2], marker='o')
    plt.grid(True)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.savefig('./p1_figures/'+title)
    plt.show()


if __name__ == '__main__':
    words_series_nostp = pd.read_csv('MergedPosts_nostp.csv')['lemma']
    words_list_nostp = merge_msg(words_series_nostp).split(sep=' ')
    words_series_withstp = pd.read_csv('MergedPosts_withstp.csv')['lemma']
    words_list_withstp = merge_msg(words_series_withstp).split(sep=' ')
    words_nostp_count = words_count(words_list_nostp)
    words_withstp_count = words_count(words_list_withstp)
    print(words_nostp_count.head(10))
    print(words_withstp_count.head(10))
    plot_rank_freq(words_withstp_count, 'with stop words')
    plot_rank_freq(words_nostp_count, 'no stop words')


