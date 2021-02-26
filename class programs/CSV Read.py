import csv


class Book:
    def __init__(self, title, author, genre, length):
        self.title = title
        self.author = author
        self.genre = genre
        self.length = length
        
    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Genre: {self.genre}"


def LoadBooks():
    books = []
    with open("G:\development\CS2420\projectThree\data.txt", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            books.append(Book(row[0], row[1], row[2], row[3]))
    
    return books


mybooks = LoadBooks()
for book in mybooks:
    print(book)
