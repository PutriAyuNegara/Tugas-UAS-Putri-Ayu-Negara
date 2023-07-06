# pip install matplotlib
from matplotlib import pyplot as plt

class BaseFuzzy():
    def __init__(self):
        self.maximum = 0
        self.minimum = 0

    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)

    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)


class Speed(BaseFuzzy):
    def __init__(self):
        self.s1 = 40
        self.s2 = 60
        self.s3 = 80
        self.s4 = 100
        self.sn = 200

    def slow(self, x):
        if x < self.s1:
            return 1
        elif self.s1 <= x <= self.s2:
            self.maximum = self.s2
            self.minimum = self.s1
            return self.down(x)
        else:
            return 0

    def steady(self, x):
        if self.s1 <= x <= self.s2:
            self.maximum = self.s2
            self.minimum = self.s1
            return self.up(x)
        elif self.s2 <= x <= self.s3:
            return 1
        elif self.s3 <= x <= self.s4:
            self.maximum = self.s4
            self.minimum = self.s3
            return self.down(x)
        else:
            return 0

    def fast(self, x):
        if x > self.s4:
            return 1
        elif self.s3 <= x <= self.s4:
            self.maximum = self.s4
            self.minimum = self.s3
            return self.up(x)
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        # slow
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        plt.plot(x_slow, y_slow, label='slow')
        # steady
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')
        # fast
        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='fast')

        if value:
            slow_value = self.slow(value)
            steady_value = self.steady(value)
            fast_value = self.fast(value)
            x_param = [0, value, value]
            # slow
            y_slowvalue = [slow_value, slow_value, 0]
            plt.plot(x_param, y_slowvalue, label='slow value')
            # steady
            y_steadyvalue = [steady_value, steady_value, 0]
            plt.plot(x_param, y_steadyvalue, label='steady value')
            # fast
            y_fastvalue = [fast_value, fast_value, 0]
            plt.plot(x_param, y_fastvalue, label='fast value')

        plt.legend(loc='upper right')
        plt.show()


class Pressure(BaseFuzzy):
    def __init__(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 22
        self.p4 = 27
        self.p5 = 30
        self.p6 = 40
        self.p7 = 50
        self.p8 = 55
        self.p9 = 60

    def very_low(self, x):
        if x < self.p1:
            return 1
        elif self.p1 <= x <= self.p3:
            self.maximum = self.p3
            self.minimum = self.p1
            return self.down(x)
        else:
            return 0

    def low(self, x):
        if self.p2 <= x <= self.p3:
            self.maximum = self.p3
            self.minimum = self.p2
            return self.up(x)
        elif self.p3 <= x <= self.p4:
            return 1
        elif self.p4 <= x <= self.p5:
            self.maximum = self.p5
            self.minimum = self.p4
            return self.down(x)
        else:
            return 0

    def medium(self, x):
        if self.p3 <= x <= self.p5:
            self.maximum = self.p5
            self.minimum = self.p3
            return self.up(x)
        elif self.p5 <= x <= self.p6:
            return 1
        elif self.p6 <= x <= self.p7:
            self.maximum = self.p7
            self.minimum = self.p6
            return self.down(x)
        else:
            return 0

    def high(self, x):
        if self.p6 <= x <= self.p7:
            self.maximum = self.p7
            self.minimum = self.p6
            return self.up(x)
        elif self.p7 <= x <= self.p9:
            return 1
        else:
            return 0

    def very_high(self, x):
        if self.p8 <= x <= self.p9:
            self.maximum = self.p9
            self.minimum = self.p8
            return self.up(x)
        else:
            return 0

    def graph(self):
        plt.figure(figsize=(15, 10))
        # very low
        x_very_low = [0, self.p1, self.p3]
        y_very_low = [1, 1, 0]
        plt.plot(x_very_low, y_very_low, label='very low')
        # low
        x_low = [self.p2, self.p3, self.p4, self.p5]
        y_low = [0, 1, 1, 0]
        plt.plot(x_low, y_low, label='low')
        # medium
        x_medium = [self.p3, self.p5, self.p6, self.p7]
        y_medium = [0, 1, 1, 0]
        plt.plot(x_medium, y_medium, label='medium')
        # high
        x_high = [self.p6, self.p7, self.p9]
        y_high = [0, 1, 1]
        plt.plot(x_high, y_high, label='high')
        # very high
        x_very_high = [self.p8, self.p9]
        y_very_high = [0, 1]
        plt.plot(x_very_high, y_very_high, label='very high')

        plt.legend(loc='upper right')
        plt.show()


class Temperature(BaseFuzzy):
    def hot(self, speed, pressure):
        return min(speed.slow(x_speed), pressure.very_low(x_pressure)) or \
               min(speed.steady(x_speed), pressure.very_low(x_pressure)) or \
               min(speed.fast(x_speed), pressure.very_low(x_pressure)) or \
               min(speed.slow(x_speed), pressure.low(x_pressure))

    def warm(self, speed, pressure):
        return min(speed.steady(x_speed), pressure.low(x_pressure)) or \
               min(speed.fast(x_speed), pressure.low(x_pressure)) or \
               min(speed.slow(x_speed), pressure.medium(x_pressure)) or \
               min(speed.steady(x_speed), pressure.medium(x_pressure))

    def cold(self, speed, pressure):
        return min(speed.fast(x_speed), pressure.medium(x_pressure)) or \
               min(speed.slow(x_speed), pressure.high(x_pressure)) or \
               min(speed.steady(x_speed), pressure.high(x_pressure)) or \
               min(speed.fast(x_speed), pressure.high(x_pressure))

    def freeze(self, speed, pressure):
        return min(speed.slow(x_speed), pressure.very_high(x_pressure)) or \
               min(speed.steady(x_speed), pressure.very_high(x_pressure)) or \
               min(speed.fast(x_speed), pressure.very_high(x_pressure))



speed = Speed()
pressure = Pressure()
temperature = Temperature()

x_speed = float(input('Speed: '))
x_pressure = float(input('Pressure: '))

output_hot = temperature.hot(speed, pressure)
output_warm = temperature.warm(speed, pressure)
output_cold = temperature.cold(speed, pressure)
output_freeze = temperature.freeze(speed, pressure)

if output_hot:
    print("The Temperature is HOT")
elif output_warm:
    print("The Temperature is WARM")
elif output_cold:
    print("The Temperature is COLD")
elif output_freeze:
    print("The Temperature is FREEZE")

speed.graph(x_speed)
pressure.graph()
