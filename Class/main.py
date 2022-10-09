class PolynomialADT :
    def __init__(self, num):
        self.list = num
        self.c = int(input("다항식의 최고 차수를 입력하시오 : "))
        self.list = [0] * self.c
        for i in range(self.c, -1, -1):
            list.append(int(input("x^{}의 계수 :".format(i))))

    def degree(self):
        print("다항식의 차수는 {}".format(self.c))

    def add(self, num2):
        t = [] * self.c
        for i in range(self.c):
            t.append(list[i]+num2[i])
        return t

    def display(self, msg):
        print(msg, end='')
        for i in range(c) :
            print("{.2%f} x^{}".format(list[i], c-i), end='')
            if c-1 == i : continue
            else : print(" + ")






list = [0]
a = PolynomialADT(list)
b = PolynomialADT(list)
c = a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
# print("C(2) = ", c.eval(2))
