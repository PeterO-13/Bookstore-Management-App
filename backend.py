import sqlite3


def connect():
    # Establishes a connection to the database or creates a new one if it doesn't exist
    conn = sqlite3.connect("textbook.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books "
                "(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    # Inserts a new book record into the database
    conn = sqlite3.connect("textbook.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    # Fetches and returns all book records from the database
    conn = sqlite3.connect("textbook.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    # Searches for books based on provided parameters and returns matching records
    conn = sqlite3.connect("textbook.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    # Deletes a book record with the specified ID from the database
    conn = sqlite3.connect("textbook.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    # Updates the details of a specific book record in the database
    conn = sqlite3.connect("textbook.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


# Create or connect to the database
connect()

# Perform operations (for demonstration purposes)
# insert("The sea", "John Tablet", 123, 23456)
# delete(1)  # Using correct ID for deletion
# update(2, "The moon", "Johnson", 1920, 412)
# print(view())
# print(search(title="The sea", author="John Tablet", year=123, isbn=23456))
