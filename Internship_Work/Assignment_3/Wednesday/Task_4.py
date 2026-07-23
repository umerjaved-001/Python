book = {
    "Title": "The Hobbit",
    "Author": "J.R.R. Tolkien",
    "Genre": "Fantasy",
    "Price": 1299
}

print("Book details:")
for key, value in book.items():
    print(f"{key}: {value}")

book["Price"] = 1099
print("\nUpdated price:")
print(f"Price: {book['Price']}")

