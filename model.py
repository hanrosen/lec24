#model.py
import csv

BB_FILE_NAME = 'umbball.csv'


def init_bball(csv_file_name=BB_FILE_NAME):
    with open('umbball.csv') as f:
        reader = csv.reader(f)
        next(reader)
        next(reader)
        global bb_seasons
        bb_seasons = []
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            bb_seasons.append(r)


def get_bball_seasons(sortby='year', sortorder='desc'):
    global bb_seasons

    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list

    return bb_seasons
