from pychatbotlib.sqlite3_wrapper import SQLite3
import difflib

class Chatbot:
	def __init__(self, dbname):
		self.sqlite_worker = SQLite3(dbname)

	def tokenize_message(self, message):
		return message.replace(',', '').replace('.', '').replace('/', '').replace('?', '').replace('\'', '')\
		.replace('"', '').replace('<', '').replace('>', '').replace('-', '').replace('+', '').replace('=', '')\
		.replace('\\', '').replace('/', '').replace('*', '').replace(':', '').replace(';', '').replace('#', '')\
		.replace('!', '').split(' ')

	def add_data(self, message, reply):
		self.sqlite_worker.query_insert(message, reply)

	def get_reply(self, message):
		words = self.tokenize_message(message)
		query = ''
		for word in words:
			query += "message LIKE '%"+word+"%' OR "
		query = query[0:len(query)-4]
		rows = self.sqlite_worker.query_select(query)
		if len(rows) <= 0:
			return None
		messages = []
		for row in rows:
			messages.append(row[1])

		if len(rows) > 1:
			match = difflib.get_close_matches(message, messages, n=1)
			if match != '':
				return rows[messages.index(''.join(match))][2]
			return None
		return rows[0][2]
		



