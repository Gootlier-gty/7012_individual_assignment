from Function_Bags import *


def posts_by_film_nostp():
    stop_words = pd.read_csv('stop_words.txt', header=None)[0].tolist()
    posts_data = pd.read_csv('FBPosts.csv', encoding='utf-8')
    file_id = list(set(posts_data['imdb_id']))
    msg_dataframe = pd.DataFrame()
    msg_dataframe['imdb_id'] = file_id
    msg_dataframe['posts'] = msg_dataframe.apply(lambda x: merge_msg(get_one_movie_msg(posts_data, x[0])), axis=1)
    msg_dataframe['CleanedPosts'] = msg_dataframe.apply(lambda x: ' '.join(clean_eng_text(x[1], stop_words=stop_words)),
                                                        axis=1)
    print('finish step 1')
    # msg_dataframe['lemma'] = msg_dataframe.apply(lambda x: lemmatization(x[2]),axis=1)
    lemma_posts = []
    postSeries = msg_dataframe['CleanedPosts']
    for i in range(0, len(postSeries)):
        lemma_posts.append(lemmatization(postSeries[i]))
    msg_dataframe['lemma'] = lemma_posts
    msg_dataframe.to_csv('MergedPosts_nostp.csv')
    return msg_dataframe


def posts_by_film_withstp():
    stop_words = pd.read_csv('stop_words.txt', header=None)[0].tolist()
    posts_data = pd.read_csv('FBPosts.csv', encoding='utf-8')
    file_id = list(set(posts_data['imdb_id']))
    msg_dataframe = pd.DataFrame()
    msg_dataframe['imdb_id'] = file_id
    msg_dataframe['posts'] = msg_dataframe.apply(lambda x: merge_msg(get_one_movie_msg(posts_data, x[0])), axis=1)
    msg_dataframe['CleanedPosts'] = msg_dataframe.apply(lambda x: ' '.join(clean_eng_text(x[1], rm_stpwds=False)),
                                                        axis=1)
    print('finish step 1')
    # msg_dataframe['lemma'] = msg_dataframe.apply(lambda x: lemmatization(x[2]),axis=1)
    lemma_posts = []
    postSeries = msg_dataframe['CleanedPosts']
    for i in range(0, len(postSeries)):
        lemma_posts.append(lemmatization(postSeries[i]))
    msg_dataframe['lemma'] = lemma_posts
    msg_dataframe.to_csv('MergedPosts_withstp.csv')
    return msg_dataframe


def rm_words_s():
    posts_nostp = pd.read_csv('MergedPosts_nostp.csv')
    posts_withstp = pd.read_csv('MergedPosts_withstp.csv')
    posts_nostp['lemma'] = posts_nostp['lemma'].apply(lambda x: rm_s_longwords(x))
    posts_withstp['lemma'] = posts_withstp['lemma'].apply(lambda x: rm_s_longwords(x))
    posts_withstp = posts_withstp.loc[:,['imdb_id','lemma']]
    posts_nostp = posts_nostp.loc[:,['imdb_id','lemma']]
    posts_nostp.to_csv('MergedPosts_nostp.csv')
    posts_withstp.to_csv('MergedPosts_withstp.csv')


if __name__ == '__main__':
    posts_by_film_nostp()
    posts_by_film_withstp()
    rm_words_s()
