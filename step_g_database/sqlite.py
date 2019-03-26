import sqlite3


class ConnectionPool:
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')

    def get(self):
        return self.connection


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return '{} {}'.format(self.name, self.surname)


class PersonRepository:
    def __init__(self):
        connection_pool = ConnectionPool()
        self.connection = connection_pool.get()
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE person (name text, surname text)""")
        self.connection.commit()

    def insert(self, person):
        self.cursor.execute("INSERT INTO person VALUES (:name, :surname)", {'name':person.name, 'surname':person.surname})
        self.connection.commit()

    def select_all(self):
        self.cursor.execute("SELECT * FROM person")
        self.connection.commit()
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
