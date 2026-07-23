library = {
    "The Alchemist": {
        "author": "Paulo Coelho",
        "price": 1299,
        "available_copies": 5,
    },
    "1984": {
        "author": "George Orwell",
        "price": 999,
        "available_copies": 8,
    },
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "price": 115,
        "available_copies": 4,
    },
    "The Great Gatsby": {
        "author": "F. Scott Fitzgerald",
        "price": 100,
        "available_copies": 6,
    },
}


def display_library(library_data):
    print("Library Inventory:")
    for title, details in library_data.items():
        author = details["author"]
        price = details["price"]
        copies = details["available_copies"]
        print(f"- {title}: Author={author}, Price=${price:.2f}, Available Copies={copies}")
    print()


def update_copies(library_data, title, new_count):
    if title in library_data:
        library_data[title]["available_copies"] = new_count
        print(f"Updated '{title}' available copies to {new_count}.")
    else:
        print(f"Book '{title}' not found in the library.")
    print()


def add_book(library_data, title, author, price, copies):
    library_data[title] = {
        "author": author,
        "price": price,
        "available_copies": copies,
    }
    print(f"Added new book '{title}'.")
    print()


def remove_book(library_data, title):
    if title in library_data:
        del library_data[title]
        print(f"Removed book '{title}'.")
    else:
        print(f"Book '{title}' not found in the library.")
    print()


if __name__ == "__main__":
    display_library(library)

    update_copies(library, "1984", 10)

    add_book(library, "Sapiens", "Yuval Noah Harari", 14.99, 7)

    remove_book(library, "The Great Gatsby")

    print("Updated Library Inventory:")
    display_library(library)
