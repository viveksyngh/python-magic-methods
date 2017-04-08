# Making instance of any object callable

class Callable(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __call__(self, a, b):
        self.a = a
        self.b = b
    

if __name__ == '__main__':
    obj = Callable(1, 2)
    print "Before call"
    print obj.a, obj.b
    print "After call"
    obj(3, 4)
    print obj.a, obj.b
