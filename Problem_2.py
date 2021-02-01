import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# firstly run the
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


if __name__ == '__main__':
    print('Film Name: Avengers')
    get_15words('tt0848228')
    print('\n')

    print('Film Name: The Dark Knight Rises')
    get_15words('tt1345836')
    print('\n')

    print('Film Name: The Hunger Games')
    get_15words('tt1392170')
    print('\n')

    print('Film Name: The Twilight Saga')
    get_15words('tt1673434')
