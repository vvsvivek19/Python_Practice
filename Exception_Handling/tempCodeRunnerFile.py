def fetch_data(database, key):
    try:
        # Simulate accessing a key in a dictionary (acting as a database)
        value = database[key]
        return value
    except KeyError as original_exception:
        # Handle KeyError and raise a more meaningful exception
        raise ValueError(f"Data for key '{key}' is missing") from original_exception

# Simulated database
database = {"name": "Alice", "age": 25}

try:
    # Attempt to fetch a non-existent key
    print(fetch_data(database, "address"))
except ValueError as e:
    print("Caught Exception:", e)
    print("Original Exception:", e.__cause__)
    