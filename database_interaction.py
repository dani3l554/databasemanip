import sqlite3
import os
import errno

class Database:
	def __init__(self, path):
		self.path = path
		if os.path.isfile(self.path):
			self.establish_connection()
		else:
			raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.path)
		print(self.read_all_data("table1"))
		self.close_connection()

	def establish_connection(self):
		self.conn = sqlite3.connect(self.path)

	def close_connection(self):
		self.conn.close()

	def read_all_data(self,table):
		c = self.conn.cursor()
		query = f"SELECT * FROM {table};"
		response = c.execute(query)
		return response
