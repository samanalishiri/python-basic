from unittest import TestCase

from step_g_database.sqlite import PersonRepository, Person


class SqliteTest(TestCase):
    def test_sqlite(self):
        repository = PersonRepository()

        repository.insert(Person("Saman", "Alishiri"))
        repository.insert(Person("Tony", "Cruse"))
        self.assertEqual(repository.select_all().__str__(), "[('Saman', 'Alishiri'), ('Tony', 'Cruse')]")

        repository.close()
