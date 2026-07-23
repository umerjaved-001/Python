# Movie Watch List

movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump",
    "Inception",
    "Interstellar",
    "The Matrix",
    "Titanic",
    "Avatar"
]

print("=== Movie Watch List ===")
print(f"Total movies available: {len(movies)}\n")

while True:
    search_query = input("Search for a movie (or type 'quit' to exit): ").strip()
    
    if search_query.lower() == 'quit':
        print("Goodbye!")
        break
    
    if not search_query:
        print("Please enter a valid movie name.\n")
        continue
    
    for movie in movies:
        if search_query.lower() in movie.lower():
            print(f"✓ '{movie}' is AVAILABLE in the watch list!\n")
            break
    else:
        print(f"✗ '{search_query}' is NOT available in the watch list.\n")
