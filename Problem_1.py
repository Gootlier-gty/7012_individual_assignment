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
    posts_data = pd.read_csv('FBPosts.csv', encoding='utf-8')
    msgSeries = get_all_msg(posts_data)
    fullMsg = merge_msg(msgSeries)
    msg_noStopWords = clean_eng_text(fullMsg)
    msg_withStopWords = clean_eng_text(fullMsg, rm_stpwds=False)
    wordsCnt_noStop = words_count(msg_noStopWords)
    wordsCnt_withStop = words_count(msg_withStopWords)
    plot_rank_freq(wordsCnt_noStop, 'No Stop Words')
    plot_rank_freq(wordsCnt_withStop, 'With Stop Words')
