def process_file(file_path):
    try:
        # Step 1: Open the file
        file = open(file_path, 'r')
        
        # Step 2: Perform some operation (e.g., read a line)
        line = file.readline()
        print("First line of the file:", line)
        
        # Step 3: Introduce an exception
        result = 10 / 0  # Deliberately causing a ZeroDivisionError
        
    except ZeroDivisionError as zde:
        # Step 4: Handle the exception locally
        print("Caught an exception:", zde)
        print("Performing cleanup (e.g., closing the file).")
        file.close()  # Cleanup
        
        # Step 5: Re-raise the exception
        raise
    finally:
        print("This block always executes (even after re-raising).")

# Global Exception Handling
log_file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\Exception_Handling\logs.txt"
try:
    process_file(log_file_path)
except Exception as e:
    print("Global handler caught the exception:", e)

    