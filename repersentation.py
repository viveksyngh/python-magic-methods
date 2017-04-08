
class MyList(object):

    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def __str__(self):
        """Defines behavior for when str() is called on an instance of this class"""
        return ' '.join(self.items)
    
    def __repr__(self):
        """Defines behavior for when repr() is called on an instance of this class"""
        return ' '.join(self.items)
    
    def __unicode__(self):
        """Defines behavior for when unicode() is called on an instance of this class"""
        return ' '.join(self.items)
    
    def __format__(self, formatstr):
        """Defines behavior for when format() is called on an instance of this class"""
        return str(self) + formatstr
    
    def __hash__(self):
        """Defines behavior for when bool() is called on an instance of this class"""
        return len(self.items)
    
    def __nonzero__(self):
        """Defines behavior for when dir() is called on an instance of this class"""
        return bool(self.items)
    

if __name__ == '__main__':
    obj = MyList()
    obj.add("Foo")
    obj.add("Bar")
    print str(obj)
    print repr(obj)
    print unicode(obj)
    print "Hello, World {0}".format(obj)
    print hash(obj)
    print bool(obj)

