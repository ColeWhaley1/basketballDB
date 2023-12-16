import sqlite3

# Connect to the SQLite database 
conn = sqlite3.connect('SQLite DB/Hoops.db')
cursor = conn.cursor()

# store array of all teams and their respective conference
cursor.execute(
    '''
        SELECT *
            FROM teams
    ''')

all_teams = cursor.fetchall()
