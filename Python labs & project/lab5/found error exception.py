def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
file_path = input("Enter the path to the file: ")

read_file(file_path)
