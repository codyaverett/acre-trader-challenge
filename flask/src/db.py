import psycopg2
import signal


class Database:
    """
    Minimal CRUD operations for a database table.
    """

    def __init__(self, host, database, user, password, port):
        signal.signal(signal.SIGINT, self.close_connection)
        signal.signal(signal.SIGTERM, self.close_connection)
        self.conn = psycopg2.connect(
            host=host, database=database, user=user, password=password, port=port
        )

    def close_connection(self, *args):
        print("Trying to close db connection.")
        self.conn.close()
        print("Connection closed.")
        exit(1)

    def create_table(self):
        """Create the table"""
        cur = self.conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name VARCHAR(255))"
        )
        self.conn.commit()
        cur.close()

    def get_all(self):
        """Get all rows from the table"""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM test")
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_one(self, id):
        """Get one row from the table"""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM test WHERE id = %s", (id,))
        row = cur.fetchone()
        cur.close()
        return row

    def insert(self, name):
        """Insert a new row into the table"""
        cur = self.conn.cursor()
        cur.execute("INSERT INTO test (name) VALUES (%s)", (name,))
        self.conn.commit()
        cur.close()

    def update(self, id, name):
        """Update a row in the table"""
        cur = self.conn.cursor()
        cur.execute("UPDATE test SET name = %s WHERE id = %s", (name, id))
        self.conn.commit()
        cur.close()

    def delete(self, id):
        """Delete a row in the table"""
        cur = self.conn.cursor()
        cur.execute("DELETE FROM test WHERE id = %s", (id,))
        self.conn.commit()
        cur.close()
