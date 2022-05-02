import time
import asyncio
import aiohttp
from omdblib import OMDBasync
from nfrtitles import  get_nfr_title_list

movie_titles = get_nfr_title_list()

start_time = time.time()

async def get_rt_rating(title, session, omdb):
    movie = await omdb.title_search(title, session=session)
    return movie.rotten_tomatoes_score


async def main():
    async with aiohttp.ClientSession() as session:
        omdb = OMDBasync("b87452b6")
        tasks = []
        for title in movie_titles:
            tasks.append(asyncio.ensure_future(get_rt_rating(title, session, omdb)))

        ratings = await asyncio.gather(*tasks)
        return ratings



ratings = asyncio.run(main())

total_time = time.time() - start_time

print(ratings, '\n')
print(f"length: {len(ratings)} total time: {total_time}")
