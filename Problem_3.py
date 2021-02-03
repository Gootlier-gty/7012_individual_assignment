from Function_Bags import *
from sklearn.feature_extraction.text import TfidfVectorizer


def get_film_posts(filename):
    words_series= pd.read_csv(filename)
    return words_series  # df


def film_bv_tf_idf():
    post_df = get_film_posts('MergedPosts_nostp.csv')
    post_series = post_df['lemma']
    bv = TfidfVectorizer(ngram_range=(2, 2))
    bv_matrix = bv.fit_transform(post_series)
    names = bv.get_feature_names()
    bv_matrix = bv_matrix.toarray()
    matrix = pd.DataFrame(bv_matrix)
    matrix.columns = names
    matrix['imdb_id'] = post_df['imdb_id']
    return matrix


def get_15words(imdb_id):
    matrix = film_bv_tf_idf()
    words_tfidf = matrix[matrix['imdb_id'] == imdb_id].iloc[0, :-1]
    sortWords = words_tfidf.sort_values(ascending=False)
    print(sortWords[:15])
    word_str = ' '.join(sortWords.index[:15])
    return word_str


if __name__ == '__main__':
    film_names = ['Avengers', 'The Dark Knight Rises', 'The Hunger Games', 'The Twilight Saga']
    film_id = ['tt0848228', 'tt1345836', 'tt1392170', 'tt1673434']
    for i in range(0, len(film_id)):
        print('Film Name: ' + film_names[i])
        get_15words(film_id[i])
