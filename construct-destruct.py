from os.path import join

class FileObject:

    def __init__(self, filepath='', filename='a.txt'):
        self.file = open(join(filepath, filename), 'w+')
    
    def __del__(self):
        print "Closing the file."
        self.file.close()
        print "Deleting the file instance."
        del self.file


if __name__ == '__main__':
    print "Opening file"
    file_obj = FileObject()
    print "Started writing"
    file_obj.file.write("Hello, World")
    
