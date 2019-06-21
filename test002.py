class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    def method(self, arg):
        # sqt
        return arg*arg

    x = property(getx, setx, delx, "I'm the 'x' property.")


c = C

c.x = 1000
print(c.x)


class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        self._voltage = value

    @voltage.deleter
    def voltage(self):
        del self._voltage

    def method(self, arg):
        # sqt
        return arg*arg


p = Parrot


p.voltage = 100
print(p.voltage)
p.voltage = 200
print(p.voltage)
# del p.voltage
# print(p.voltage)
setattr(p, 'voltage', 123)


print(p.voltage)


class D(C):
    def method(self, arg):
        super().method(arg)
