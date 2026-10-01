import unittest
from library_system import Book, Member


class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.book = Book("Clean Code", "B771", "Robert Martin")
        self.member = Member("Alice Smith", "M202")

    def test_polymorphism_output(self):
        self.assertIn("Robert Martin", self.book.get_details())

    def test_borrowing_encapsulation(self):
        success = self.member.borrow_item(self.book)

        self.assertTrue(success)
        self.assertTrue(self.book.is_borrowed)
        self.assertEqual(self.member.get_borrowed_count(), 1)


if __name__ == "__main__":
    unittest.main()