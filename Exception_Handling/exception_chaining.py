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
    
#Practicing exception chaining

class DiscountCalculationError(Exception):
    def __init__(self, message="Discount Cannot be less than 0 i.e. Negative"):
        self.message = message
        super().__init__(self.message)

def calculate_discount(price, discount):
    try:
        if discount < 0:
            raise ValueError("Discount value must be positive")
    except ValueError as OriginalException:
        raise DiscountCalculationError from OriginalException

try:
    calculate_discount(350,-1)
except ValueError as msg:
    print(f"Caught Exception:{msg}")
    print("Original Exception:",msg.__cause__)