import sqlite3
from sqlite3 import Error

class SQLite3:
	create_table_messages = '''	BEGIN TRANSACTION;
								CREATE TABLE IF NOT EXISTS `messages` (
									`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
									`message`	TEXT NOT NULL,
									`reply`	TEXT NOT NULL
								);
								COMMIT; '''

	def __init__(self, db_file):
		self.db_file = db_file

		self.create_connection()

		if self.conn is not None:
			self.create_table(self.create_table_messages)
			self.close()
		else:
			print("Error! cannot create the database connection.")

	def create_connection(self):
	    """ create a database connection to the SQLite database
	        specified by db_file
	    :return: Connection object or None
	    """
	    try:
	        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
	    except Error as e:
	        print(e)
	 
	    return None

	def create_table(self, create_table_sql):
		""" create a table from the create_table_sql statement
		:param create_table_sql: a CREATE TABLE statement
		:return:
		"""
		try:
		    c = self.conn.cursor()
		    c.executescript(create_table_sql)
		except Error as e:
		    print(e)
	    
	def query_select(self, expression):
		self.create_connection()
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM messages WHERE " + expression)
		rows = cur.fetchall()
		self.close()

		return rows

	def query_insert(self, message, reply):
		self.create_connection()
		cur = self.conn.cursor()
		cur.execute("INSERT INTO messages (message, reply) VALUES('"+reply+"', '"+message+"')")
		self.conn.commit()
		self.close()

	def close(self):
		self.conn.close()