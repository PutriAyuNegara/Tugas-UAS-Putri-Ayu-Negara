from matplotlib import pyplot as plt

class BaseFuzzy():
    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)
    
    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)

class Speed(BaseFuzzy):
    def __init__(self):
        self.s1 = 20
        self.s2 = 40
        self.s3 = 60
        self.s4 = 80
        self.sn = 100

    def slow(self, x):
        if x < self.s1:
            return 1
        elif self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.down(x)
        else:
            return 0

    def steady(self, x):
        if self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.up(x)
        if self.s2 <= x <= self.s3:
            return 1
        if self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.down(x)
        else:
            return 0

    def fast(self, x):
        if self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.up(x)
        elif x > self.s4:
            return 1
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        plt.plot(x_slow, y_slow, label='slow')

        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')

        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='fast')

        if value:
            value_slow = self.slow(value)
            value_steady = self.steady(value)
            value_fast = self.fast(value)
            x_param = [0, value, value]
            y_slowvalue = [value_slow, value_slow, 0]
            plt.plot(x_param, y_slowvalue, label='slow value')

            y_steadyvalue = [value_steady, value_steady, 0]
            plt.plot(x_param, y_steadyvalue, label='steady value')

            y_fastvalue = [value_fast, value_fast, 0]
            plt.plot(x_param, y_fastvalue, label='fast value')

        plt.legend(loc='upper right')
        plt.show()

class Pressure(BaseFuzzy):
    def __init__(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 15
        self.p4 = 20
        self.p5 = 23
        self.p6 = 27
        self.p7 = 32
        self.p8 = 37
        self.p9 = 40

    def very_low(self, x):
        if x <= self.p1:
            return 1
        elif self.p1 < x < self.p3:
            self.minimum = self.p1
            self.maximum = self.p3
            return self.down(x)
        else:
            return 0

    def low(self, x):
        if self.p2 <= x <= self.p3:
            self.minimum = self.p2
            self.maximum = self.p3
            return self.up(x)
        if self.p3 <= x <= self.p4:
            self.minimum = self.p3
            self.maximum = self.p4
            return self.down(x)
        else:
            return 0

    def medium(self, x):
        if self.p3 <= x <= self.p5:
            self.minimum = self.p3
            self.maximum = self.p5
            return self.up(x)
        if self.p5 <= x <= self.p6:
            return 1
        if self.p6 <= x <= self.p7:
            self.minimum = self.p6
            self.maximum = self.p7
            return self.down(x)
        else:
            return 0

    def high(self, x):
        if self.p6 <= x <= self.p7:
            self.minimum = self.p6
            self.maximum = self.p7
            return self.up(x)
        if self.p7 <= x <= self.p9:
            self.minimum = self.p7
            self.maximum = self.p9
            return self.down(x)
        else:
            return 0

    def very_high(self, x):
        if self.p8 <= x <= self.p9:
            self.minimum = self.p8
            self.maximum = self.p9
            return self.up(x)
        elif x > self.p9:
            return 1
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        x_very_low = [0, self.p1, self.p3]
        y_very_low = [1, 1, 0]
        plt.plot(x_very_low, y_very_low, label='very low')

        x_low = [self.p2, self.p3, self.p4]
        y_low = [0, 1, 0]
        plt.plot(x_low, y_low, label='low')

        x_medium = [self.p3, self.p5, self.p6, self.p7]
        y_medium = [0, 1, 1, 0]
        plt.plot(x_medium, y_medium, label='medium')

        x_high = [self.p6, self.p7, self.p9]
        y_high = [0, 1, 0]
        plt.plot(x_high, y_high, label='high')

        x_very_high = [self.p8, self.p9]
        y_very_high = [0, 1]
        plt.plot(x_very_high, y_very_high, label='very high')

        if value:
            value_very_low = self.very_low(value)
            value_low = self.low(value)
            value_medium = self.medium(value)
            value_high = self.high(value)
            value_very_high = self.very_high(value)

            x_param = [0, value, value]

            y_very_low_value = [value_very_low, value_very_low, 0]
            plt.plot(x_param, y_very_low_value, label='very low value')

            y_low_value = [value_low, value_low, 0]
            plt.plot(x_param, y_low_value, label='low value')

            y_medium_value = [value_medium, value_medium, 0]
            plt.plot(x_param, y_medium_value, label='medium value')

            y_high_value = [value_high, value_high, 0]
            plt.plot(x_param, y_high_value, label='high value')

            y_very_high_value = [value_very_high, value_very_high, 0]
            plt.plot(x_param, y_very_high_value, label='very high value')

        plt.legend(loc='upper right')
        plt.show()

class Temperature(BaseFuzzy):
    def __init__(self):
        self.c1 = 40
        self.c2 = 60
        self.c3 = 80
        self.c4 = 100

    def hot(self, x):
        if x <= self.c1:
            return 1
        elif self.c1 < x < self.c2:
            self.minimum = self.c1
            self.maximum = self.c2
            return self.down(x)
        else:
            return 0

    def warm(self, x):
        if self.c1 <= x <= self.c2:
            self.minimum = self.c1
            self.maximum = self.c2
            return self.up(x)
        if self.c2 <= x <= self.c3:
            return 1
        if self.c3 <= x <= self.c4:
            self.minimum = self.c3
            self.maximum = self.c4
            return self.down(x)
        else:
            return 0

    def cold(self, x):
        if self.c2 <= x <= self.c3:
            self.minimum = self.c2
            self.maximum = self.c3
            return self.up(x)
        if self.c3 <= x <= self.c4:
            self.minimum = self.c3
            self.maximum = self.c4
            return self.down(x)
        else:
            return 0

    def freeze(self, x):
        if self.c3 <= x <= self.c4:
            self.minimum = self.c3
            self.maximum = self.c4
            return self.up(x)
        elif x > self.c4:
            return 1
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        x_hot = [0, self.c1, self.c2]
        y_hot = [1, 1, 0]
        plt.plot(x_hot, y_hot, label='hot')

        x_warm = [self.c1, self.c2, self.c3, self.c4]
        y_warm = [0, 1, 1, 0]
        plt.plot(x_warm, y_warm, label='warm')

        x_cold = [self.c2, self.c3, self.c4]
        y_cold = [0, 1, 0]
        plt.plot(x_cold, y_cold, label='cold')

        x_freeze = [self.c3, self.c4]
        y_freeze = [0, 1]
        plt.plot(x_freeze, y_freeze, label='freeze')

        if value:
            value_hot = self.hot(value)
            value_warm = self.warm(value)
            value_cold = self.cold(value)
            value_freeze = self.freeze(value)

            x_param = [0, value, value]

            y_hot_value = [value_hot, value_hot, 0]
            plt.plot(x_param, y_hot_value, label='hot value')

            y_warm_value = [value_warm, value_warm, 0]
            plt.plot(x_param, y_warm_value, label='warm value')

            y_cold_value = [value_cold, value_cold, 0]
            plt.plot(x_param, y_cold_value, label='cold value')

            y_freeze_value = [value_freeze, value_freeze, 0]
            plt.plot(x_param, y_freeze_value, label='freeze value')

        plt.legend(loc='upper right')
        plt.show()

class FIS:
    # ...

    def defuzzification(self, speed, pressure):
        temperature = ""

        if speed == 'slow' and pressure == 'very low':
            temperature = 'HOT'
            self.graph(speed, pressure, temperature)

        if speed == 'slow' and pressure == 'low':
            temperature = 'HOT'
            self.graph(speed, pressure, temperature)

        if speed == 'slow' and pressure == 'medium':
            temperature = 'HOT'
            self.graph(speed, pressure, temperature)

        if speed == 'slow' and pressure == 'high':
            temperature = 'HOT'
            self.graph(speed, pressure, temperature)

        if speed == 'slow' and pressure == 'very high':
            temperature = 'FREEZE'
            self.graph(speed, pressure, temperature)

        if speed == 'steady' and pressure == 'very low':
            temperature = 'HOT'
            self.graph(speed, pressure, temperature)

        if speed == 'steady' and pressure == 'low':
            temperature = 'WARM'
            self.graph(speed, pressure, temperature)

        if speed == 'steady' and pressure == 'medium':
            temperature = 'WARM'
            self.graph(speed, pressure, temperature)

        if speed == 'steady' and pressure == 'high':
            temperature = 'COLD'
            self.graph(speed, pressure, temperature)

        if speed == 'steady' and pressure == 'very high':
            temperature = 'FREEZE'
            self.graph(speed, pressure, temperature)

        if speed == 'fast' and pressure == 'very low':
            temperature = 'HOT'
            self.graph(speed, pressure, temperature)

        if speed == 'fast' and pressure == 'low':
            temperature = 'WARM'
            self.graph(speed, pressure, temperature)

        if speed == 'fast' and pressure == 'medium':
            temperature = 'COLD'
            self.graph(speed, pressure, temperature)

        if speed == 'fast' and pressure == 'high':
            temperature = 'COLD'
            self.graph(speed, pressure, temperature)

        if speed == 'fast' and pressure == 'very high':
            temperature = 'FREEZE'
            self.graph(speed, pressure, temperature)

        return temperature

    def graph(self, speed, pressure, temperature):
        plt.figure(figsize=(15, 10))

        plt.plot([0, 1, 2, 3, 4], [0, 0.5, 1, 0.5, 0], label='Speed')
        plt.plot([0, 1, 2, 3, 4], [0, 1, 0, 0, 0], label='Pressure')

        plt.title(f"Speed: {speed} - Pressure: {pressure} - Temperature: {temperature}")
        plt.legend()
        plt.show()


fis = FIS()
speed = 'fast'
pressure = 'low'
output = fis.defuzzification(speed, pressure)
print("The Temperature is: ", output)

