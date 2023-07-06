import numpy as np
import matplotlib.pyplot as plt

class Pressure:
    def __init__(self):
        self.o1 = 30
        self.o2 = 70

    def low(self, x):
        if x < self.o1:
            return 1
        elif self.o1 <= x <= self.o2:
            return (self.o2 - x) / (self.o2 - self.o1)
        else:
            return 0

    def medium(self, x):
        if self.o1 <= x <= self.o2:
            return (x - self.o1) / (self.o2 - self.o1)
        else:
            return 0

    def high(self, x):
        if x > self.o2:
            return 1
        elif self.o1 <= x <= self.o2:
            return (x - self.o1) / (self.o2 - self.o1)
        else:
            return 0

    def fuzzify(self, x):
        return self.low(x), self.medium(x), self.high(x)

    def graph(self):
        x = np.linspace(0, 100, 500)
        y_low = [self.low(i) for i in x]
        y_medium = [self.medium(i) for i in x]
        y_high = [self.high(i) for i in x]

        plt.figure(figsize=(8, 5))
        plt.plot(x, y_low, label='low')
        plt.plot(x, y_medium, label='medium')
        plt.plot(x, y_high, label='high')
        plt.xlabel('Pressure')
        plt.ylabel('Membership Degree')
        plt.title('Membership Function - Pressure')
        plt.legend()
        plt.show()


class Temperature:
    def __init__(self):
        self.o1 = 30
        self.o2 = 60
        self.o3 = 90

    def cold(self, x):
        if x < self.o1:
            return 1
        elif self.o1 <= x <= self.o2:
            return (self.o2 - x) / (self.o2 - self.o1)
        else:
            return 0

    def moderate(self, x):
        if self.o1 <= x <= self.o2:
            return (x - self.o1) / (self.o2 - self.o1)
        elif self.o2 <= x <= self.o3:
            return (self.o3 - x) / (self.o3 - self.o2)
        else:
            return 0

    def hot(self, x):
        if x > self.o3:
            return 1
        elif self.o2 <= x <= self.o3:
            return (x - self.o2) / (self.o3 - self.o2)
        else:
            return 0

    def fuzzify(self, x):
        return self.cold(x), self.moderate(x), self.hot(x)

    def graph(self):
        x = np.linspace(0, 100, 500)
        y_cold = [self.cold(i) for i in x]
        y_moderate = [self.moderate(i) for i in x]
        y_hot = [self.hot(i) for i in x]

        plt.figure(figsize=(8, 5))
        plt.plot(x, y_cold, label='cold')
        plt.plot(x, y_moderate, label='moderate')
        plt.plot(x, y_hot, label='hot')
        plt.xlabel('Temperature')
        plt.ylabel('Membership Degree')
        plt.title('Membership Function - Temperature')
        plt.legend()
        plt.show()


class Output:
    def __init__(self):
        self.o1 = 0
        self.o2 = 50
        self.o3 = 100

    def low(self, x):
        if x < self.o1:
            return 1
        elif self.o1 <= x <= self.o2:
            return (self.o2 - x) / (self.o2 - self.o1)
        else:
            return 0

    def moderate(self, x):
        if self.o1 <= x <= self.o2:
            return (x - self.o1) / (self.o2 - self.o1)
        elif self.o2 <= x <= self.o3:
            return (self.o3 - x) / (self.o3 - self.o2)
        else:
            return 0

    def high(self, x):
        if x > self.o3:
            return 1
        elif self.o2 <= x <= self.o3:
            return (x - self.o2) / (self.o3 - self.o2)
        else:
            return 0

    def fuzzify(self, x):
        return self.low(x), self.moderate(x), self.high(x)

    def graph(self):
        x = np.linspace(0, 100, 500)
        y_low = [self.low(i) for i in x]
        y_moderate = [self.moderate(i) for i in x]
        y_high = [self.high(i) for i in x]

        plt.figure(figsize=(8, 5))
        plt.plot(x, y_low, label='low')
        plt.plot(x, y_moderate, label='moderate')
        plt.plot(x, y_high, label='high')
        plt.xlabel('Output')
        plt.ylabel('Membership Degree')
        plt.title('Membership Function - Output')
        plt.legend()
        plt.show()


def fuzzification(x, variables):
    values = []
    for variable in variables:
        values.append(variable.fuzzify(x))
    return values


def inference(value1, value2, rules):
    activation_rules = []
    for i, rule in enumerate(rules):
        activation_rule = min(value1[rule[0]], value2[rule[1]])
        activation_rules.append(activation_rule)
    return activation_rules


def defuzzification(activation_rule, output):
    x = np.linspace(0, 100, 500)
    y_low = [output.low(i) for i in x]
    y_moderate = [output.moderate(i) for i in x]
    y_high = [output.high(i) for i in x]

    aggregated = np.zeros_like(x)
    for i in range(len(activation_rule)):
        if activation_rule[i] > 0:
            if i < 3:
                aggregated = np.fmax(aggregated, np.fmin(activation_rule[i], y_low))
            elif i < 6:
                aggregated = np.fmax(aggregated, np.fmin(activation_rule[i], y_moderate))
            else:
                aggregated = np.fmax(aggregated, np.fmin(activation_rule[i], y_high))

    return x[np.argmax(aggregated)]


def get_temperature_string(value):
    if value < 30:
        return "FREEZE"
    elif 30 <= value < 60:
        return "COLD"
    elif 60 <= value < 90:
        return "Warm"
    else:
        return "Hot"


# Inisialisasi variabel
speed = float(input('Speed: '))
pressure = float(input('Pressure: '))

# Inisialisasi objek
pressure_obj = Pressure()
temperature_obj = Temperature()
output_obj = Output()

# Fuzzifikasi
speed_values = fuzzification(speed, [pressure_obj])
pressure_values = fuzzification(pressure, [temperature_obj])

# Inferensi
rules = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
activation_rules = inference(speed_values[0], pressure_values[0], rules)

# Defuzzifikasi
output_value = defuzzification(activation_rules, output_obj)
temperature_string = get_temperature_string(output_value)

# Tampilkan hasil
print("The Temperature is: ", temperature_string)

# Tampilkan grafik
pressure_obj.graph()
temperature_obj.graph()
output_obj.graph()
