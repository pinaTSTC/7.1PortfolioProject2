import sqlite3 as sl

# create/connect to the database named my-test.db
con = sl.connect('movies.db')

# Once you have a Connection, you can create a Cursor object 
# and call its execute() method to perform SQL commands
c = con.cursor()

# get the count of tables with the name
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type = 'table' AND name = 'MOVIES' ''')

# if the count is 1, then table exists
if c.fetchone()[0] == 1 :
    print('Table exists')
else :
    # does not exist, create
    print('Table does not exist.')

    # create a table with a primary key, name field of text, and a age field of integer
    with con:
        con.execute("""
            CREATE TABLE MOVIES (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                name TEXT,
                genre TEXT,
                year INTEGER
            );
        """)

    # create sql to insert data into the table
    sql = 'INSERT INTO MOVIES (id, name, genre, year) values (?, ?, ?, ?)'
    data = [
        (1, 'Citizen Kane', 'Drama', 1941),
        (2, 'The Godfather', 'Drama', 1972),
        (3, 'The Wizard of Oz', 'Musical', 1939),
        (4, 'Singin'' the Rain', 'Musical', 1952), 
        (5, 'It''s a Wonderful Life', 'Drama', 1946),
        (6, 'No Country For Old Men', 'Thriller', 2007),
        (7, 'Joker', 'Drama', 2019),
        (8, 'Whiplash', 'Drama', 2014),
        (9, 'Lord of the Rings: The Fellowship of the Ring', 'Fantasy', 2001),
        (10, 'The Shooter', 'Action', 2007)
    ]

    # run sql query
    with con:
        con.executemany(sql, data)

# connect and read back data
with con:
    data = con.execute("SELECT * FROM MOVIES WHERE year >= 2000")
    for row in data:
        print(row)

# connect and read back data
with con:
    data = con.execute("SELECT * FROM MOVIES WHERE year < 2000")
    for row in data:
        print(row)