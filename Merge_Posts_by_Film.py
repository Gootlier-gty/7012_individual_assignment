from Function_Bags import *


def posts_by_film():
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
        print(i)
        lemma_posts.append(lemmatization(postSeries[i]))
    msg_dataframe['lemma'] = lemma_posts
    msg_dataframe.to_csv('MergedPosts.csv')
    print(msg_dataframe)


if __name__ == '__main__':
    posts_by_film()
