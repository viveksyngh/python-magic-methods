
class OpenFile:
    
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.file.close()
        except IOError, e:
            print "File Can not be closed"
        return True


if __name__ == '__main__':
    file_path = 'a.txt'
    print "Started"
    with OpenFile(file_path, 'w') as file:
        file.write("Hello, World!")
    print "Done"
    
