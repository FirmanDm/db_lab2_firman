import psycopg2
import psycopg2.extras

def years_best_revenue(cur):
    cur.execute('select movie_year, movie_revenue from movie;')

    years = []
    revenue = []
    for result in cur.fetchall():
        years.append(int(result['movie_year']))
        revenue.append(float(result['movie_revenue']))

    print(
        f"years_best_revenue:"
        f"\n\tyears={years}"
        f"\n\tbest_revenue={revenue}"
    )


def genre_by_market_share(cur):
    cur.execute('select genre_name, genre_market_share from genre;')

    genres = []
    genre_ms = []
    for result in cur.fetchall():
        genres.append(result['genre_name'])
        genre_ms.append(float(result['genre_market_share']))

    print(
        f"genre_by_market_share:"
        f"\n\tgenre={genres}"
        f"\n\tmarket_share={genre_ms}"
    )


def distributors_by_movies_num(cur):
    cur.execute('select dist_id, dist_movies_number from distributor;')

    dist = []
    dist_movies_count = []
    for result in cur.fetchall():
        dist.append(int(result['dist_id']))
        dist_movies_count.append(int(result['dist_movies_number']))

    print(
        f"distributors_by_movies_num:"
        f"\n\tdistributor={dist}"
        f"\n\tmovies count={dist_movies_count}"
    )


if __name__ == "__main__":
    conn = psycopg2.connect(
        dbname='lab2', user='firman',
        password='777', host='localhost'
    )
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        years_best_revenue(cursor)
        genre_by_market_share(cursor)
        distributors_by_movies_num(cursor)

    conn.close()
