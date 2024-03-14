# given a list of strings reprseneting the file paths .each file path consists of directories separated by slashes / 
# write a function to count the frequency of each directory and return the directory hierarchy as a nested dictionary

file_paths = [
    "/home/user/documents/report.txt",
    "/home/user/documents/project1/specs.txt",
    "/home/user/documents/project1/code/main.py",
    "/home/user/documents/project2/notes.txt",
    "/home/user/pictures/image.jpg"
]


def hierarchy(path):
    '''
    Not Done
    '''
    file_dict = {}
    for files in path:
        files = files.split("/")
        files.pop(0)
        # print(files)
        for file in files:
                if file.isalnum():
                    pass
                else:
                     frequency = 1
                    #  print(frequency)
    print({"home": {"user":{"documents":{"report.txt":frequency,"project1":
                                         {"specs.txt":frequency,"code":{"main.py":frequency}},
                                         "project2":{"notes.txt":frequency}}},
                                         "pictures":{"image.jpg":frequency}}})

    # print(file_dict)
    

hierarchy(file_paths)


