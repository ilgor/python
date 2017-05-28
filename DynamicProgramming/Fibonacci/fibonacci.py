
class Fibonacci():
    def __init__(self):
        self.dict = {}

    def get_nth_fibonacci_number(self, n):
        if n < 1:
            raise Exception("Can't generate less than 1 element. Please enter at least 1.")
        elif n == 1:
            return 0
        elif n == 2:
            return 1

        if n in self.dict:
            return self.dict.get(n)
        new_val = self.get_nth_fibonacci_number(n-1) + self.get_nth_fibonacci_number(n-2)
        self.dict[n] = new_val
        return new_val

    def generate_fibonacci_sequence_for(self, n):
        arr = []
        for i in range(1, n+1):
            arr.append(self.get_nth_fibonacci_number(i))
        return arr