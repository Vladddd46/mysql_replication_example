from Database import *

databaseForReplication = "replication"
tableForReplication = "users"

# master database #
host = "127.0.0.1"
user = "root"
password = "password"
port = 3306
###################

# slave database #
slaveHost = "127.0.0.1"
slaveUser = "root"
slavePassword = "password"
slavePort = 6603
###################


class DatabaseBuilder:
	def __init__(self, db):
		self.db = db

	def insertData(self, name, surname, age):
		query = f"INSERT INTO {tableForReplication} (name, surname, age) VALUES ('{name}', '{surname}', {age})"
		self.db.execute(query)

	def useDatabase(self, databaseName):
		query = f"USE {databaseName}"
		self.db.execute(query)

	def printFullTable(self):
		query = f"SELECT * FROM {tableForReplication}"
		res = self.db.getExecute(query)
		flag = False
		for row in res:
			flag = True
			print(
				f"id: {row[0]} | Name: {row[1]} | Surname: {row[2]} | Age: {row[3]}\n"
			)
		if not flag:
			print("=Result is empty=")


class MenuOptions:
	@staticmethod
	def insertOption(masterDbBuilder):
		name = input("Write name: ")
		surname = input("Write surname: ")
		try:
			age = int(input("Write age: "))
		except:
			print("Error: Age must be integer.")
			return
		masterDbBuilder.insertData(name, surname, age)
		print("=Data Inserted=")

	@staticmethod
	def printOption(dbBuilder):
		dbBuilder.printFullTable()


def menu(masterDbBuilder, slaveDbBuilder):
	while True:
		print("=============")
		print("1. Insert data in master database")
		print("2. Read data from slave database")
		print("3. Read data from master database")

		option = input("Select option: ")
		try:
			option = int(option)
			if option == 1:
				masterDbBuilder.useDatabase(databaseForReplication)
				MenuOptions.insertOption(masterDbBuilder)
			elif option == 2:
				slaveDbBuilder.useDatabase(databaseForReplication)
				MenuOptions.printOption(slaveDbBuilder)
			elif option == 3:
				masterDbBuilder.useDatabase(databaseForReplication)
				MenuOptions.printOption(masterDbBuilder)
			else:
				raise Exception("Invalid command")
		except Exception as e:
			print("Wrong input: ", e)


def main():
	#
	masterDb = MySqlDatabase(host, user, password, port)
	slaveDb = MySqlDatabase(slaveHost, slaveUser, slavePassword, slavePort)

	#
	masterDbBuilder = DatabaseBuilder(masterDb)
	slaveDbBuilder = DatabaseBuilder(slaveDb)

	menu(masterDbBuilder, slaveDbBuilder)


if __name__ == "__main__":
	main()
