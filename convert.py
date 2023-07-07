import os
import cgi

def change_notepad_format(file_path, output_format):
    # Get the directory and filename
    directory, filename = os.path.split(file_path)

    # Create the new output file name with the desired format
    new_filename = os.path.splitext(filename)[0] + "." + output_format

    # Create the new output file path
    output_file = os.path.join(directory, new_filename)

    try:
        # Rename the file to change the format
        os.rename(file_path, output_file)
        return output_file
    except OSError as e:
        return str(e)

# Main entry point
if __name__ == "__main__":
    form = cgi.FieldStorage()
    input_file = form["file"].file
    output_format = form.getvalue("output-format")

    # Save the uploaded file to a temporary location
    file_path = "0/download"  # Replace with your desired temporary file location
    with open(file_path, "wb") as file:
        file.write(input_file.read())

    # Perform file format conversion
    converted_file = change_notepad_format(file_path, output_format)

    if isinstance(converted_file, str):
        print(f"An error occurred: {converted_file}")
    else:
        print(converted_file)