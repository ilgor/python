class LCS:
    def __init__(self):
        self.arr = []
        self.lcs = ""

    def length(self, string1, string2):
        s1 = len(string1)
        s2 = len(string2)

        self.arr = [[None] * (s2 + 1) for _ in range(s1 + 1)]

        for i in range(s1+1):
            for j in range(s2+1):
                if i == 0 or j == 0:
                    self.arr[i][j] = 0
                elif string1[i-1] == string2[j-1]:
                    self.arr[i][j] = self.arr[i-1][j-1] + 1
                else:
                    self.arr[i][j] = max(self.arr[i-1][j], self.arr[i][j-1])

        return self.arr[s1][s2]

    def word(self, X, Y):
        self.length(X, Y)
        self.word_helper(Y, len(X), len(Y))
        return self.lcs

    def word_helper(self, string1, i, j):
        if i == 0 or j == 0:
            return
        elif self.arr[i][j] > max(self.arr[i-1][j], self.arr[i][j-1]):
            self.word_helper(string1, i-1, j-1)
            self.lcs += string1[j-1]
        elif self.arr[i-1][j] >= self.arr[i][j-1]:
            self.word_helper(string1, i-1, j)
        else:
            self.word_helper(string1, i, j-1)

