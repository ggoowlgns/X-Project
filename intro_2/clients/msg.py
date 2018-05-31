import random

def msgs(n, max_length = 1000):
    """Generate n messages of length <= max_length"""

    contents = max_length * b'a'
    r = random.Random(113)

    for i in range(1, n+1):
        length = r.randint(1, max_length-4)
        msg = b'%4.4d %s\n' %(i, contents[:length])
        yield msg

class Msgs:
    """Iterator implementation"""

    def __init__(self, n, max_length=1000):
        """Generate n messages of length <= max_length"""
        self.n = n
        self.i = 0
        self.max_length = max_length
        self.contents = max_length * b'a'
        self.r = random.Random(113)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        self.i += 1
        length = self.r.randint(1, self.max_length - 4)
        msg = b'%4.4d %s\n' %(self.i, self.contents[:length])
        return msg

if __name__ == '__main__':
    for msg in msgs(5):
        print(msg)
    print()
    for msg in Msgs(5):
        print(msg)
