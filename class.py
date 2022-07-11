class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


class MoreCalculator(Calculator):
    def sub(self, num):
        self.result -= num
        return self.result


cal1 = MoreCalculator()
cal2 = MoreCalculator()

print(cal1.sub(3))
print(cal1.sub(4))
print(cal2.sub(3))
print(cal2.sub(7))
