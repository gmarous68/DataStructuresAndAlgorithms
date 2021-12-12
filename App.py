class Test(object):
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


test1 = Test("Green")
print("Test 1 is {}".format(test1.get_color()))
test1.set_color("Blue")
print("Test 2 is {}".format(test1.get_color()))

print('*' * 40)