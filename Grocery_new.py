class Vegetable:
    def __init__(self, freshness, price):
        self.par1 = freshness
        self.par2 = price


class Tomato(Vegetable):
    def Fresh_control(self):
        if self.par1 == True:
            return "Tomato`s fresh"
        else:
            return "Tomato is rotten"

    def Check_out(self):
        return "Tomato costs %s" % self.par2


if __name__ == "__main__":
    product = Tomato(bool(input()), 100.50)
    print(product.Fresh_control())
    print(product.Check_out())
