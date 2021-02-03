from Function_Bags import *
import matplotlib.pyplot as plt


def sentiment_words_count():
    neg_words = pd.read_csv('negative-words.txt', encoding='gbk', header=None)[0]
    pos_words = pd.read_csv('positive-words.txt', encoding='gbk', header=None)[0]
    words_series_nostp = pd.read_csv('MergedPosts_nostp.csv')['lemma']
    words_list_nostp = merge_msg(words_series_nostp).split(sep=' ')
    words_nostp_count = words_count(words_list_nostp)
    neg_count = words_nostp_count[words_nostp_count['words'].isin(neg_words)].iloc[:, 1:].reset_index().iloc[:, 1:]
    pos_count = words_nostp_count[words_nostp_count['words'].isin(pos_words)].iloc[:, 1:].reset_index().iloc[:, 1:]
    return neg_count, pos_count


def draw_bar_chart(count_df, title):
    words_df = count_df.iloc[:20, :]
    plt.figure(figsize=(7, 5))
    plt.bar(words_df.iloc[:, 0], words_df.iloc[:, 1])
    plt.grid(True)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.savefig('./p4_figures/' + title)


if __name__ == '__main__':
    neg_count, pos_count = sentiment_words_count()
    draw_bar_chart(neg_count, 'Negative Words Frequency')
    draw_bar_chart(pos_count, 'positive Words Frequency')
