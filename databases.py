#!/usr/bin/env python3

import sqlite3

def main():
    print('connect')
    db = sqlite3.connect('webm2401/15./db-api.db')
    cur = db.cursor()
    print('create')
    #create table
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute(
        """
        CREATE TABLE test (
            first_name TEXT NOT NULL,
	        last_name TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            phone_number NUMERIC NOT NULL UNIQUE,
            zip NUMERIC NOT NULL
            
        )
        """
    )
    #insert rows
    print('insert row 1')
    cur.execute("""
        INSERT INTO test VALUES('Ilona', 'Lenstra', '691 Spring Acres', 'Catalina Foothills', 'North Carolina', '235-461-3598', '5159')
    """
    )
    print('insert row 2')
    cur.execute("""
        INSERT INTO test VALUES('Arica', 'Barnett', '806 Silent Mountain Village', 'New Baden village', 'Vermont', '476-835-2439', '5165')
    """)
    print('insert row 3')
    cur.execute("""
        INSERT INTO test VALUES('Tayna', 'de Graaf', '311 SW Creek Woods', 'Stapleton', 'Colorado', '789-369-6686', '6632')
    """)
    print('insert row 4')
    cur.execute("""
        INSERT INTO test VALUES('Kaleigh', 'Brock', '164 Lodge Tunnel', 'Floresville', 'Florida', '943-753-9048', '5059')
    """)
    #display rows
    cur.execute("SELECT * FROM test")
    print(cur.fetchall())
    #delete one row
    cur.execute(
        """
        DELETE FROM test WHERE first_name='Kaleigh'
        """)
    #display data again
    cur.execute("SELECT * FROM test")
    print(cur.fetchall())

if __name__ == '__main__': main()