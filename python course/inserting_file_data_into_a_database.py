import sqlite3
connection = sqlite3.connect(':memory:')
connection.row_factory = sqlite3.Row

# Create the cursor.
cursor = connection.cursor()
create = """CREATE TABLE states (
                'state' text,
                'pop2020' integer,
                'pop2000' integer
            )"""

# Execute the create statement.
cursor.execute(create)
insert = 'INSERT INTO states VALUES (?, ?, ?)'

# Create a list of tuples from the data in '../data/states.txt'.
data = []
with open('Exercises\states.txt') as f:
    for line in f.readlines():
        state_data = line.split('\t')
        tpl_state_data = (state_data[0],
                          int(state_data[1].replace(',','')),
                          int(state_data[2].replace(',','')))
        data.append(tpl_state_data)

# Insert the data into the database.
cursor.executemany(insert, data)
select = """SELECT state,
            CAST((pop2020*1.0/pop2000) * pop2020 AS INTEGER) AS pop2040
            FROM states ORDER BY pop2040 DESC"""

# Execute the select statement.
cursor.execute(select)
# Fetch the rows into a variable.
# Close the cursor and connection.

results = cursor.fetchall()
cursor.close()
connection.close()

# Print out the results.
for result in results:
    state = result['state']
    p40 = result['pop2040']
    print(f'the projected 2040 population of {state} is {p40:,}.')
