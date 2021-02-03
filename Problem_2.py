from Function_Bags import *
from sklearn.feature_extraction.text import TfidfVectorizer
import wordcloud


def get_film_posts():
    msg = pd.read_csv('MergedPosts_nostp.csv')
    return msg  # dataframe


def film_tf_idf_matrix():
    post_df = get_film_posts()
    docs_list = []
    for i in post_df['lemma']:
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


def word_cloud(word_str, film_name):
    w = wordcloud.WordCloud(background_color='white', width=1000, height=500, margin=0, max_font_size=100, scale=20, normalize_plurals=False)
    w.generate(word_str)
    w.to_file('./p2_figures/' + film_name + '.png')


if __name__ == '__main__':
    film_names = ['Avengers', 'The Dark Knight Rises', 'The Hunger Games', 'The Twilight Saga']
    film_id = ['tt0848228', 'tt1345836', 'tt1392170', 'tt1673434']
    for i in range(0, len(film_id)):
        print('Film Name: ' + film_names[i])
        words = get_15words(film_id[i])
        word_cloud(words, film_names[i])
