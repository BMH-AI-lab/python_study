class Book: 
    def __init__(self, title, author, total_pages, current_pages=0):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_pages = current_pages
      

    def read_page(self, pages):
        if pages < 0:
            return 
        self.current_page = min(self.total_pages, self.current_pages + pages)


    def progress(self):
        pct = (self.current_page / self.total_pages) * 100
        return round(pct, 1)
    
    def __repr__(self):
        return f"<Book {self.title} by {self.author}"


b = Book("파이썬 클린코드: ", "홍길동", total_pages=320, current_pages=0)
b.read_page(10)
print(b)
print()
print(b.progress(), "%")
print()
b.read_page(1000)
print()
print(b.progress(), "%")
print()