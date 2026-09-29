
# library_system.py

# 1. Parent class: Item
# Demonstrates encapsulation.
class Item:
    def __init__(self, title: str, item_id: str):
        self.title = title
        self._item_id = item_id
        self.is_borrowed = False

    def get_details(self) -> str:
        return f"Generic Library Item: {self.title}"


# 2. Child class: Book
# Demonstrates inheritance and polymorphism.
class Book(Item):
    def __init__(self, title: str, item_id: str, author: str):
        super().__init__(title, item_id)
        self.author = author

    # Override the parent class method.
    def get_details(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: {self.title} by {self.author} [{status}]"


# 3. Member class
# Demonstrates private data and borrowing operations.
class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.__borrowed_items = []

    def borrow_item(self, item: Item) -> bool:
        if not item.is_borrowed:
            item.is_borrowed = True
            self.__borrowed_items.append(item)
            return True
        return False

    def get_borrowed_count(self) -> int:
        return len(self.__borrowed_items)