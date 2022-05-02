import time
from multiprocessing import Pool
from omdblib import OMDB
from nfrtitles import  get_nfr_title_list

movie_titles = get_nfr_title_list()


def get_rt_score(title):
    movie = omdb.title_search(title)
    return movie.rotten_tomatoes_score

if __name__ == '__main__':
    omdb = OMDB("b87452b6")
    process_pool = Pool(processes=128)

    start_time = time.time()

    ratings = process_pool.map(get_rt_score, movie_titles)

    total_time = time.time() - start_time

    print(ratings, '\n')
    print(f"length: {len(ratings)} total time: {total_time}")



