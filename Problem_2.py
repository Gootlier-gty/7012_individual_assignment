import pandas as pd
from Function_Bags import *
from sklearn.feature_extraction.text import TfidfVectorizer
import wordcloud


def get_film_posts():
    msg = pd.read_csv('MergedPosts.csv')
    msg = msg.iloc[:, [1, -1]]
    return msg  # dataframe


def film_tf_idf_matrix():
    post_df = get_film_posts()
    docs_list = []
    for i in post_df['CleanedPosts']:
        docs_list.append(i)
    tfidf_vec = TfidfVectorizer()
    tfidf_matrix = tfidf_vec.fit_transform(docs_list)
    matrix = tfidf_matrix.toarray()
    matrix = pd.DataFrame(matrix)
    names = tfidf_vec.get_feature_names()
    matrix.columns = names
    matrix['imdb_id'] = post_df['imdb_id']
    return matrix


def get_15words(imdb_id):
    matrix = film_tf_idf_matrix()
    words_tfidf = matrix[matrix['imdb_id'] == imdb_id].iloc[0, :-1]
    sortWords = words_tfidf.sort_values(ascending=False)
    print(sortWords[:15])
    word_str = ' '.join(sortWords.index[:15])
    return word_str


def posts_by_film():
    stop_words = pd.read_csv('stop_words.txt', header=None)[0].tolist()
    posts_data = pd.read_csv('FBPosts.csv', encoding='utf-8')
    file_id = list(set(posts_data['imdb_id']))
    msg_dataframe = pd.DataFrame()
    msg_dataframe['imdb_id'] = file_id
    msg_dataframe['posts'] = msg_dataframe.apply(lambda x: merge_msg(get_one_movie_msg(posts_data, x[0])), axis=1)
    msg_dataframe['CleanedPosts'] = msg_dataframe.apply(lambda x: ' '.join(clean_eng_text(x[1], stop_words=stop_words)),
                                                        axis=1)
    # print('finish step 1')
    # # python -m spacy download en_core_web_sm 下载数据模型
    # nlp = spacy.load("en_core_web_sm")
    # msg_dataframe['lemma'] = msg_dataframe.apply(lambda x: lemmatization(x[2],nlp),axis=1)
    msg_dataframe.to_csv('test.csv')
    print(msg_dataframe)


def merge_or_not():
    print('Merge the posts by film id? Enter y/n: ')
    switch = input()  # input N or Y
    if switch == 'y':
        posts_by_film()
    elif switch == 'n':
        pass
    else:
        print('wrong input, enter y/n')
        merge_or_not()


def word_cloud(word_str, film_name):
    w = wordcloud.WordCloud(background_color='white', width=1000, height=500, margin=0, max_font_size=100, scale=20)
    w.generate(word_str)
    w.to_file('./p2_figures/' + film_name + '.png')


if __name__ == '__main__':
    merge_or_not()
    film_names = ['Avengers', 'The Dark Knight Rises', 'The Hunger Games', 'The Twilight Saga']
    film_id = ['tt0848228', 'tt1345836', 'tt1392170', 'tt1673434']
    for i in range(0, len(film_id)):
        print('Film Name: ' + film_names[i])
        words = get_15words(film_id[i])
        word_cloud(words, film_names[i])

