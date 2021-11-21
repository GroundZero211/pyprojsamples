class Calc:
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return self.data + other

    def __sub__(self, other):
        return self.data - other

    def __mul__(self, other):
        return self.data * other

    def __truediv__(self, other):
        try:
            return self.data / other
        except ZeroDivisionError:
            return "Cannot divided by zero"

    def __str__(self):
        return 'instance attr. data: {}'.format(self.data)

class Comparisons:
    def __init__(self, value):
        self.data = value
    
    def __lt__(self, other):
        return self.data < other

    def __gt__(self, other):
        return self.data > other

    def __eq__(self, other):
        return self.data == other

    def __ne__(self, other):
        return self.data != other

class String:
    def __init__(self, value):
        self.data = value

    def __str__(self, value):
        return 'Instance attr. {}'.format(self.data)

    def __len__(self, value):
        return len(self.data)

if __name__ == '__main__':
    print(Calc(100))
    print(Calc(5) + 4)
    print(Comparisons(5) > 6)