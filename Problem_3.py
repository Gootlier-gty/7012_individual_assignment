from Function_Bags import *
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':
    words_series_nostp = pd.read_csv('MergedPosts_nostp.csv')['lemma']
    words_list_nostp = merge_msg(words_series_nostp).split(sep=' ')

