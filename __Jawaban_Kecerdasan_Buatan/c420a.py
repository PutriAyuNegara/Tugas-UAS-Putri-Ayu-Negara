# pip install matplotlib

from matplotlib import pyplot as plt

class BaseFuzzy():

    def __init__(self):
        self.max = 0
        self.min = 0

    def up(self, x):
        return (x - self.min) / (self.max - self.min)
    
    def down(self, x):
        return (self.max - x) / (self.max - self.min)

class Temp(BaseFuzzy):

    def __init__(self):
        self.t1 = 5
        self.t2 = 15
        self.t3 = 25
        self.t4 = 35
        self.tn = 50

    def freeze(self, x):
        if x < self.t1:
            return 1
        elif self.t1 <= x <= self.t2:
            self.min = self.t1
            self.max = self.t2
            return self.down(x)
        else:
            return 0
    
    def cold(self, x):
        if self.t1 <= x <= self.t2:
            self.min = self.t1
            self.max = self.t2
            return self.up(x)
        elif self.t2 <= x <= self.t3:
            self.min = self.t2
            self.max = self.t3
            return self.down(x)
        else:
            return 0

    def warm(self, x):
        if self.t2 <= x <= self.t3:
            self.min = self.t2
            self.max = self.t3
            return self.up(x)
        elif self.t3 <= x <= self.t4:
            self.min = self.t3
            self.max = self.t4
            return self.down(x)
        else:
            return 0
    
    def hot(self, x):
        if self.t3 <= x <= self.t4:
            self.min = self.t3
            self.max = self.t4
            return self.up(x)
        elif x > self.t4:
            return 1
        else:
            return 0

    def graph(self, value=None):
        x_freeze = [0, self.t1, self.t2, self.tn]
        y_freeze = [1, 1, 0, 0]

        plt.plot(x_freeze, y_freeze, label='freeze')

        x_cold = [0, self.t1, self.t2, self.t3, self.tn]
        y_cold = [0, 0, 1, 0, 0]
        plt.plot(x_cold, y_cold, label='cold')

        x_warm = [0, self.t2, self.t3, self.t4, self.tn]
        y_warm = [0, 0, 1, 0, 0]
        plt.plot(x_warm, y_warm, label='warm')

        x_hot = [0, self.t3, self.t4, self.tn]
        y_hot = [0, 0, 1, 1]
        plt.plot(x_hot, y_hot, label='hot')

        plt.title('Temperature [Output]')
        plt.xticks([self.t1, self.t2, self.t3, self.t4])

        if value:
            x_param = [0, value, value]

            freeze_value = self.freeze(value)
            y_freeze_v = [freeze_value, freeze_value, 0]
            plt.plot(x_param, y_freeze_v, label=f'v_freeze[{freeze_value}]')

            cold_value = self.cold(value)
            y_cold_v = [cold_value, cold_value, 0]
            plt.plot(x_param, y_cold_v, label=f'v_cold[{cold_value}]')

            warm_value = self.warm(value)
            y_warm_v = [warm_value, warm_value, 0]
            plt.plot(x_param, y_warm_v, label=f'v_warm[{warm_value}]')

            hot_value = self.hot(value)
            y_hot_v = [hot_value, hot_value, 0]
            plt.plot(x_param, y_hot_v, label=f'v_hot[{hot_value}]')

        plt.legend(loc='upper right')
        plt.show()


class Pressure(BaseFuzzy):

    def __init__(self):
        self.p1 = 5
        self.p2 = 8
        self.p3 = 15
        self.p4 = 20
        self.p5 = 28
        self.p6 = 30
        self.p7 = 37
        self.p8 = 40
        self.p9 = 47

    def very_low(self, x):
        if x <= self.p1:
            return 1
        elif self.p1 < x < self.p3:
            self.min = self.p1
            self.max = self.p3
            return self.down(x)
        else:
            return 0

    def low(self, x):
        if self.p2 <= x <= self.p3:
            self.min = self.p2
            self.max = self.p3
            return self.up(x)
        elif self.p3 < x < self.p4:
            self.min = self.p3
            self.max = self.p4
            return self.down(x)
        else:
            return 0

    def medium(self, x):
        if self.p3 <= x <= self.p4:
            self.min = self.p3
            self.max = self.p4
            return self.up(x)
        elif self.p4 < x < self.p5:
            self.min = self.p4
            self.max = self.p5
            return self.down(x)
        elif self.p6 <= x <= self.p7:
            self.min = self.p6
            self.max = self.p7
            return self.down(x)
        else:
            return 0

    def high(self, x):
        if self.p5 <= x <= self.p8:
            self.min = self.p5
            self.max = self.p8
            return self.up(x)
        elif self.p8 < x < self.p9:
            self.min = self.p8
            self.max = self.p9
            return self.down(x)
        else:
            return 0

    def very_high(self, x):
        if self.p8 <= x < self.p9:
            self.min = self.p8
            self.max = self.p9
            return self.up(x)
        else:
            return 0
        
    def graph(self, x):
        x_very_low = [0, self.p1, self.p3, self.p9]
        y_very_low = [1, 1, 0, 0]
        plt.plot(x_very_low, y_very_low, label='very_low')

        x_low = [self.p2, self.p3, self.p4, self.p9]
        y_low = [0, 1, 0, 0]
        plt.plot(x_low, y_low, label='low')

        x_medium = [self.p3, self.p4, self.p5, self.p7, self.p9]
        y_medium = [0, 1, 0, 0, 0]
        plt.plot(x_medium, y_medium, label='medium')

        x_high = [self.p5, self.p8, self.p9]
        y_high = [0, 1, 0]
        plt.plot(x_high, y_high, label='high')

        x_very_high = [self.p8, self.p9]
        y_very_high = [0, 1]
        plt.plot(x_very_high, y_very_high, label='very_high')

        plt.title('Pressure [Input]')
        plt.xticks([self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9])

        plt.axvline(x=x, color='red', linestyle='--')

        plt.legend(loc='upper right')
        plt.show()


class System():

    def __init__(self):
        self.temp = Temp()
        self.pressure = Pressure()

    def control(self, temp_value, press_value):
        self.temp.graph(temp_value)
        self.pressure.graph(press_value)

        speed = self.calculate_speed(temp_value, press_value)
        print('Speed:', speed)

    def calculate_speed(self, temp_value, press_value):
        # Rules for determining the speed based on temperature and pressure values
        if (self.temp.freeze(temp_value) and self.pressure.very_low(press_value)) or \
                (self.temp.cold(temp_value) and self.pressure.very_low(press_value)) or \
                (self.temp.warm(temp_value) and self.pressure.very_low(press_value)) or \
                (self.temp.hot(temp_value) and self.pressure.very_low(press_value)):
            return 'FAST'
        elif (self.temp.freeze(temp_value) and self.pressure.low(press_value)) or \
                (self.temp.cold(temp_value) and self.pressure.low(press_value)):
            return 'FAST'
        elif (self.temp.warm(temp_value) and self.pressure.low(press_value)) or \
                (self.temp.hot(temp_value) and self.pressure.low(press_value)):
            return 'STEADY'
        elif (self.temp.freeze(temp_value) and self.pressure.medium(press_value)) or \
                (self.temp.cold(temp_value) and self.pressure.medium(press_value)) or \
                (self.temp.warm(temp_value) and self.pressure.medium(press_value)) or \
                (self.temp.hot(temp_value) and self.pressure.medium(press_value)):
            return 'STEADY'
        elif (self.temp.freeze(temp_value) and self.pressure.high(press_value)) or \
                (self.temp.cold(temp_value) and self.pressure.high(press_value)) or \
                (self.temp.warm(temp_value) and self.pressure.high(press_value)):
            return 'STEADY'
        elif (self.temp.hot(temp_value) and self.pressure.high(press_value)):
            return 'SLOW'
        elif (self.temp.freeze(temp_value) and self.pressure.very_high(press_value)) or \
                (self.temp.cold(temp_value) and self.pressure.very_high(press_value)) or \
                (self.temp.warm(temp_value) and self.pressure.very_high(press_value)) or \
                (self.temp.hot(temp_value) and self.pressure.very_high(press_value)):
            return 'SLOW'

        return 'Unknown'

if __name__ == "__main__":
    system = System()
    temperature = float(input('Temperature: '))
    pressure = float(input('Pressure: '))
    system.control(temperature, pressure)
