
class Word(str):

    def __new__(cls, word):
        if ' ' in word:
            word = word[: word.index(' ')]
        return str.__new__(cls, word)
    
    def __eq__(self, other):
        return len(self) == len(other)
    
    def __ne__(self, other):
        return len(self) != len(other)
    
    def __gt__(self, other):
        return len(self) > len(other)
    
    def __lt__(self, other):
        return len(self) < len(other)
    
    def __ge__(self, other):
        return len(self) >= len(other)
    
    def __le__(self, other):
        return len(self) <= len(other)

if __name__ == '__main__':
    print Word('Foo') == Word('Bar')
    print Word('Foo') != Word('Bar')
    print Word('Foo') > Word('Bar')
    print Word('Foo') < Word('Bar')
    print Word('Foo') >= Word('Bar')
    print Word('Foo') <= Word('Bar')