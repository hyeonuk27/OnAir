import pandas as pd
from pandas.io.parsers import read_csv

import random, string

def make_random_id():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(13))

df = read_csv('./arrival_data.csv')
id = [ make_random_id() for _ in range(120) ]
df.insert(1, 'id', id)
df.to_csv('./arrival_cities.csv')