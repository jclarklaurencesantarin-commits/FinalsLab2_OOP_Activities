class BookPages:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"{self.pages} pages"

    def __add__(self, other):
        total_pages = self.pages + other.pages
        return BookPages(total_pages)

book1 = BookPages(120)
book2 = BookPages(85)

print("Book 1:", book1)
print("Book 2:", book2)

combined = book1 + book2
print("Total:", combined)