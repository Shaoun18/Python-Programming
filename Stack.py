books = []
books.append("Learn C")                       # push the book
books.append("Learn C++")
books.append("Learn Java")
print(books)
books.pop()
print("Now the top value is = ",books[-1])     # Pop the Book
books.pop()
print("Now the top value is = ",books[-1])
books.pop()
if not books :
    print("No Books are Avialable")