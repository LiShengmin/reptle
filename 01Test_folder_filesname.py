import os

def files_name(path):
    for dir in os.listdir(path):
        print dir

if __name__ == "__main__":
    path = "/Users/lishengmin/Desktop/Python/"
    files_name(path)