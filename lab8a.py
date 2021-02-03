class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img


    def __str__(self):
        return str(self.real) + "+" + str(self.img) + "i"


    def sum(self, real2, img2):
        r = self.real + real2
        i = self.img + img2
        return self.__str__() + " + " + Complex(real2, img2).__str__() + " = " + str(r) + "+" + str(i) + "i"



num = Complex(2, 2)
num2 = Complex(3, 3)
print(num.sum(num2.real, num2.img))