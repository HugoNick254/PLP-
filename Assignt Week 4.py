def process_and_copy_file():
    """
    A simple program to read from one file and write to another.
    """
    input_file_name = input("Enter the name of the file to read from: ")
    output_file_name = input("Enter a name for the new file: ")

    try:
        with open(input_file_name, 'r') as original_file, open(output_file_name, 'w') as new_file:
            
            text = original_file.read()

            modified_text = text.upper()

            new_file.write(modified_text)

        print(f"Success! Content from '{input_file_name}' was copied to '{output_file_name}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file_name}' was not found. Please check the name and try again.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


process_and_copy_file()