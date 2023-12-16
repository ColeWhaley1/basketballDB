import sqlite3

# Connect to the SQLite database 
conn = sqlite3.connect('SQLite DB/Hoops.db')
cursor = conn.cursor()

# Assuming your document is read line by line
with open('database data/NCAA D1 teams.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables
current_conference = None

# Iterate through each line in the document
for line in lines:
    # Remove leading and trailing whitespaces
    line = line.strip()

    # If the line is not empty, either it's a conference or a school
    if line:
        if current_conference is None:
            # This is a new conference
            current_conference = line
        else:
            # This is a school
            cursor.execute('''INSERT INTO teams(team_name, conference)
                                        VALUES(?,?)
                           ''', (line, current_conference))

    else:
        # Line is empty, indicating the end of a conference
        current_conference = None


# Commit changes and close the connection
conn.commit()
conn.close()
