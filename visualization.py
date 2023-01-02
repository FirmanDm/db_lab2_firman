import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt


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
    plt.plot(years, revenue)
    plt.ticklabel_format(style='plain')
    plt.xticks(years)
    plt.xlabel('Year')
    plt.ylabel('Revenue, $')
    plt.title('Revenue of best film per year')
    plt.show()


def genre_by_market_share(cur):
    cur.execute('select genre_name, genre_market_share from genre;')

    genres = []
    genre_ms = []
    genre_label = []
    for result in cur.fetchall():
        genres.append(result['genre_name'])
        genre_ms.append(float(result['genre_market_share']))
        genre_label.append(str(float(result['genre_market_share']))+'%')

    print(
        f"genre_by_market_share:"
        f"\n\tgenre={genres}"
        f"\n\tmarket_share={genre_ms}"
    )
    patches, texts = plt.pie(genre_ms, startangle=90)
    plt.pie(genre_ms, startangle=90, labels=genre_label, rotatelabels=True, labeldistance=0.77,
            textprops=dict(rotation_mode='anchor', va='center', ha='left'))
    plt.legend(patches, genres, loc="best")
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.title('Market share by genres')
    plt.tight_layout()
    plt.show()


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
    plt.bar(dist, dist_movies_count)
    plt.xticks(dist)
    plt.xlabel('Distributor id')
    plt.ylabel('# of movies')
    plt.title('Amount of movies from each distributor')
    plt.show()


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
