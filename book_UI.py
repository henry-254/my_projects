import csv

def load_books():
    with open('main_dataset.csv') as file:
        reader = csv.DictReader(file)
        return list(reader)

def search_by_author(books, author):
    return [book for book in books if book['author'].lower() == author.lower()]


def search_by_isbn(books, isbn):
    return [book for book in books if book['isbn'] == isbn]


def search_by_price_range(books, min_price, max_price):
    return [book for book in books if float(book['Price']) >= min_price and float(book['Price']) <= max_price]

# user interface loop
while True:
    print("Welcome to the book search app!")
    print("1. Search by author")
    print("2. Search by ISBN")
    print("3. Search by price range")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        author = input("Enter the author name: ")
        books = load_books()
        results = search_by_author(books, author)
        if len(results) == 0:
            print("No books found for that author.")
        else:
            print("Search results:")
            for book in results:
                print(f"{book['name']} by {book['author']}")
    elif choice == "2":
        isbn = input("Enter the ISBN: ")
        books = load_books()
        results = search_by_isbn(books, isbn)
        if len(results) == 0:
            print("No books found with that ISBN.")
        else:
            print("Search results:")
            for book in results:
                print(f"{book['name']}  (Price: ${book['price']})\n")
    elif choice == "3":
        min_price = float(input("Enter the minimum price: "))
        max_price = float(input("Enter the maximum price: "))
        books = load_books()
        results = search_by_price_range(books, min_price, max_price)
        if len(results) == 0:
            print("No books found in that price range.")
        else:
            print("Search results:")
            for book in results:
                print(f"{book['name']} (Price: ${book['price']})")
    elif choice == "4":
        print("Thank you for using the book search app!")
        break
    else:
        print("Invalid choice. Please try again.")
