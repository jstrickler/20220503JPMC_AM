import time
from multiprocessing.dummy import Pool
from omdblib import OMDB
from nfrtitles import  get_nfr_title_list

movie_titles = get_nfr_title_list()

omdb = OMDB("b87452b6")

start_time = time.time()

thread_pool = Pool(16)

def get_rt_score(title):
    movie = omdb.title_search(title)
    return movie.rotten_tomatoes_score

ratings = thread_pool.map(get_rt_score, movie_titles)

total_time = time.time() - start_time

print(ratings, '\n')
print(f"length: {len(ratings)} total time: {total_time}")



