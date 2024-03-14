# given a list of strings reprseneting the file paths .each file path consists of directories separated by slashes / 
# write a function to count the frequency of each directory and return the directory hierarchy as a nested dictionary


file_paths = [
    "/home/user/documents/report.txt",
    "/home/user/documents/project1/specs.txt",
    "/home/user/documents/project1/code/main.py",
    "/home/user/documents/project2/notes.txt",
    "/home/user/pictures/image.jpg"
]

def count_directory_frequency(file_paths):
    directory_frequency = {}

    for file_path in file_paths:
        directories = file_path.split('/')
        directories.pop(0)
        current_directory = directory_frequency

        for directory in directories[:-1]:  # Iterate over directories, excluding the file name
            if directory not in current_directory:
                current_directory[directory] = {}  # Create a nested dictionary for subdirectories
            current_directory = current_directory[directory]

        filename = directories[-1]  # Get the file name
        if filename not in current_directory:
            current_directory[filename] = 0  # Initialize frequency count
        current_directory[filename] += 1  # Increment frequency count

    return directory_frequency



result = count_directory_frequency(file_paths)
print(result)


