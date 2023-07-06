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
        # 0 - s1 = 1
        # s1- s2 = down
        if x < self.s1:
            return 1
        elif self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.down(x)
        else:
            return 0
    
    def steady(self, x):
        # s1- s2 = up
        # s2- s3 = 1
        # s3- s4 = down
        if self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.up(x)
        elif self.s2 <= x <= self.s3:
            return 1
        elif self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.down(x)
        else:
            return 0
    
    def fast(self, x):
        # s3- s4 = up
        # s4 - ..... =1
        if x > self.s4:
            return 1
        elif self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.up(x)
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        # slow
        # 0 - s1 = 1 [1, 1]
        # s1- s2 = down [1, 0]
        # s2-sn = 0 [0, 0]
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        plt.plot(x_slow, y_slow, label='slow')

        # steady
        # 0-s1 = 0 [0-0]
        # s1- s2 = up [0-1]
        # s2- s3 = 1 [1-1]
        # s3- s4 = down [1-0]
        # s4- sn = 0 [0-0]
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')
        # fast
        # 0-s3 = 0 [0-0]
        # s3- s4 = up [0-1]
        # s4 - sn =1 [1-1]
        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='fast')
        if value:
            x_param = [0, value, value]
            y_slow = self.slow(value)
            y_steady = self.steady(value)
            y_fast = self.fast(value)
            y_param_slow = [y_slow, y_slow, 0]
            y_param_steady = [y_steady, y_steady, 0]
            y_param_fast = [y_fast, y_fast, 0]
            plt.plot(x_param, y_param_slow, label='slow value')
            plt.plot(x_param, y_param_steady, label='steady value')
            plt.plot(x_param, y_param_fast, label='fast value')

        plt.legend(loc='upper right')
        plt.show()

class Pressure:
    def __init__(self):
        self.p1 = 0
        self.p2 = 2
        self.p3 = 4
        self.p4 = 6
        self.p5 = 8
        self.p6 = 10
        self.p7 = 12
        self.p8 = 14
        self.p9 = 16
        self.p10 = 18

    def very_low(self, value):
        if value <= self.p1 or value >= self.p3:
            return 1
        elif self.p1 < value < self.p3:
            return (self.p3 - value) / (self.p3 - self.p1)
        else:
            return 0

    def low(self, value):
        if value <= self.p2 or value >= self.p4:
            return 0
        elif self.p2 < value < self.p4:
            return (value - self.p2) / (self.p4 - self.p2)
        elif self.p4 < value < self.p5:
            return (self.p5 - value) / (self.p5 - self.p4)
        else:
            return 0

    def medium(self, value):
        if value <= self.p4 or value >= self.p6:
            return 0
        elif self.p4 < value < self.p6:
            return (value - self.p4) / (self.p6 - self.p4)
        elif self.p6 < value < self.p8:
            return (self.p8 - value) / (self.p8 - self.p6)
        else:
            return 0

    def high(self, value):
        if value <= self.p7 or value >= self.p9:
            return 0
        elif self.p7 < value < self.p9:
            return (value - self.p7) / (self.p9 - self.p7)
        elif self.p9 < value < self.p10:
            return (self.p10 - value) / (self.p10 - self.p9)
        else:
            return 0

    def very_high(self, value):
        if value <= self.p9:
            return 0
        elif self.p9 < value < self.p10:
            return (value - self.p9) / (self.p10 - self.p9)
        else:
            return 1

    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        x_very_low = [0, self.p1, self.p3]
        y_very_low = [1, 1, 0]
        plt.plot(x_very_low, y_very_low, label='very_low')

        x_low = [self.p2, self.p4, self.p5, self.p6]
        y_low = [0, 1, 1, 0]
        plt.plot(x_low, y_low, label='low')

        x_medium = [self.p4, self.p6, self.p8]
        y_medium = [0, 1, 0]
        plt.plot(x_medium, y_medium, label='medium')

        x_high = [self.p7, self.p9, self.p10]
        y_high = [0, 1, 1]
        plt.plot(x_high, y_high, label='high')

        x_very_high = [self.p9, self.p10]
        y_very_high = [1, 1]
        plt.plot(x_very_high, y_very_high, label='very_high')

        if value is not None:
            plt.plot(value, 0, 'ro', label='input')
            plt.annotate(f'{value}', (value, 0), textcoords="offset points", xytext=(0, 10), ha='center')

        plt.xlabel('Pressure')
        plt.ylabel('Membership Degree')
        plt.title('Pressure Membership')
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.show()

def get_temperature(speed_value, pressure_value):
    speed = Speed()
    pressure = Pressure()
    speed.graph(speed_value)
    pressure.graph(pressure_value)

    # Fuzzy rules
    # If speed is slow and pressure is very_low, then temperature is cold
    if speed.slow(speed_value) and pressure.very_low(pressure_value):
        return 'cold'
    # If speed is slow and pressure is low, then temperature is cold
    elif speed.slow(speed_value) and pressure.low(pressure_value):
        return 'cold'
    # If speed is steady and pressure is low, then temperature is warm
    elif speed.steady(speed_value) and pressure.low(pressure_value):
        return 'warm'
    # If speed is fast and pressure is low, then temperature is warm
    elif speed.fast(speed_value) and pressure.low(pressure_value):
        return 'warm'
    # If speed is fast and pressure is medium, then temperature is hot
    elif speed.fast(speed_value) and pressure.medium(pressure_value):
        return 'hot'
    # If speed is fast and pressure is high, then temperature is hot
    elif speed.fast(speed_value) and pressure.high(pressure_value):
        return 'hot'
    # If speed is fast and pressure is very_high, then temperature is hot
    elif speed.fast(speed_value) and pressure.very_high(pressure_value):
        return 'hot'
    else:
        return 'unknown'

# Contoh penggunaan:
speed_value = float(input('Speed: '))
pressure_value = float(input('Pressure: '))
temperature = get_temperature(speed_value, pressure_value)
print("The Temperatur is:", temperature)
