class Knapsack():

    # items example: ('itemName', value, weight)
    def calculate(self, items, max_weight):
        if len(items) == 0 or max_weight <= 0:
            return (0, ())

        value1, item1 = self.calculate(items[1:], max_weight)
        value2, item2 = self.calculate(items[1:], max_weight - items[0][2])
        value2 += items[0][1]
        item2 += (items[0],)

        return (value2, item2) if items[0][2] <= max_weight and value2 >= value1 else (value1, item1)
