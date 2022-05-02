import time
from omdblib import OMDB
from nfrtitles import  get_nfr_title_list

movie_titles = get_nfr_title_list()

omdb = OMDB("b87452b6")

start_time = time.time()

ratings = []
for title in movie_titles:
    movie = omdb.title_search(title)
    ratings.append(movie.rotten_tomatoes_score)

total_time = time.time() - start_time

print(ratings, '\n')
print(f"length: {len(ratings)} total time: {total_time}")



