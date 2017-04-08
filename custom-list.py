class MyList:

    def __init__(self, values=None):
        if values:
            self.values = values
        else:
            self.values = []
    
    def __len__(self):
        return len(self.values)
    
    def __getiten__(self, key):
        return self.values[key]
    
    def __setitem__(self, key, value):
        self.values[key] = value
    
    def __delitem__(self, key):
        del self.values[key]
    
    def __iter__(self):
        return iter(self.values)
    
    def __contains__(self, item):
        return item in self.values
    
    def __reversed__(self):
        return MyList(reversed(self.values))
    
    def head(self):
        if not self.values:
            return None
        return self.values[0]
    
    def tail(self):
        if not self.values:
            return None
        return self.values[-1]


if __name__ == '__main__':
    my_list = MyList()

    print len(my_list)
    my_list[0] = 'a'
    my_list[1] = 'b'
    my_list[2] = 'c'
    print len(my_list)
    print my_list[1]
    print my_list[2]
    my_list[3] = 'd'
    del my_list[3]
    
    
