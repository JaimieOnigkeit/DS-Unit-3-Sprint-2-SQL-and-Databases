import pandas as pd
import os
import sqlite3

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")

df = pd.read_csv(CSV_FILEPATH)

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

df.to_sql(name='review', con=connection, if_exists='replace')

#(Stretch) What are the average number of reviews for each category?

queries = [
    '''SELECT COUNT ("User Id")
    FROM review;''',
    '''SELECT COUNT ("User ID")
    FROM(	
        SELECT *
        FROM review
        WHERE Nature >= 100
    )
    WHERE Shopping >= 100;''',
    '''SELECT AVG (Sports) as Sports
        ,AVG (Religious) as Religious
        ,AVG (Nature) as Nature
        ,AVG (Theatre) as Theatre
        ,AVG (Shopping) as Shopping
        ,AVG (Picnic) as Picnic
    FROM review;'''
]

for query in queries:
    print("--------------")
    print(f"QUERY: '{query}'")
    results = cursor.execute(query).fetchall()
    print("RESULTS:")
    print(results)