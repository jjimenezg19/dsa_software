class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


Cookie_one = Cookie("green")
Cookie_two = Cookie("red")
Cookie_one.set_color("blue")

print(f"The Color of the cookie one is: {Cookie_one.get_color()}")
print(f"The Color of the cookie two is: {Cookie_two.get_color()}")