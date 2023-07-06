import matplotlib.pyplot as plt

class Temperature:
    def freeze(self, x):
        if x <= 10:
            return 1
        elif x >= 15:
            return 0
        else:
            return (15 - x) / (15 - 10)

    def cold(self, x):
        if x <= 10 or x >= 25:
            return 0
        elif x >= 15 and x <= 20:
            return 1
        elif x > 10 and x < 15:
            return (x - 10) / (15 - 10)
        else:
            return (25 - x) / (25 - 20)

    def warm(self, x):
        if x <= 15 or x >= 30:
            return 0
        elif x >= 20 and x <= 25:
            return 1
        elif x > 15 and x < 20:
            return (x - 15) / (20 - 15)
        else:
            return (30 - x) / (30 - 25)

    def hot(self, x):
        if x <= 25:
            return 0
        elif x >= 35:
            return 1
        else:
            return (x - 25) / (35 - 25)


class Pressure:
    def very_low(self, x):
        if x <= 5 or x >= 15:
            return 0
        elif x >= 8 and x <= 10:
            return 1
        elif x > 5 and x < 8:
            return (x - 5) / (8 - 5)
        else:
            return (15 - x) / (15 - 10)

    def low(self, x):
        if x <= 5 or x >= 28:
            return 0
        elif x >= 15 and x <= 20:
            return 1
        elif x > 5 and x < 15:
            return (15 - x) / (15 - 5)
        elif x > 20 and x < 28:
            return (x - 20) / (28 - 20)
        else:
            return (40 - x) / (40 - 28)

    def medium(self, x):
        if x <= 8 or x >= 37:
            return 0
        elif x >= 20 and x <= 28:
            return 1
        elif x > 8 and x < 20:
            return (x - 8) / (20 - 8)
        elif x > 28 and x < 37:
            return (37 - x) / (37 - 28)
        else:
            return (40 - x) / (40 - 37)

    def high(self, x):
        if x <= 20:
            return 0
        elif x >= 40:
            return 1
        else:
            return (x - 20) / (40 - 20)

    def very_high(self, x):
        if x <= 28:
            return 0
        elif x >= 40:
            return 1
        else:
            return (x - 28) / (40 - 28)


class FuzzySystem:
    def __init__(self):
        self.temperature = Temperature()
        self.pressure = Pressure()

    def fuzzy_rules(self, temperature_value, pressure_value):
        temperature_value_str = ''
        if temperature_value <= 10:
            temperature_value_str = 'Freeze'
        elif temperature_value >= 15 and temperature_value <= 20:
            temperature_value_str = 'Cold'
        elif temperature_value >= 25 and temperature_value <= 30:
            temperature_value_str = 'Warm'
        else:
            temperature_value_str = 'Hot'

        pressure_value_str = ''
        if pressure_value <= 5:
            pressure_value_str = 'Very Low'
        elif pressure_value >= 8 and pressure_value <= 10:
            pressure_value_str = 'Low'
        elif pressure_value >= 15 and pressure_value <= 20:
            pressure_value_str = 'Medium'
        elif pressure_value >= 28 and pressure_value <= 37:
            pressure_value_str = 'High'
        else:
            pressure_value_str = 'Very High'

        rules = {
            'Rule 1': min(self.temperature.freeze(temperature_value), self.pressure.very_low(pressure_value)),
            'Rule 2': min(self.temperature.freeze(temperature_value), self.pressure.low(pressure_value)),
            'Rule 3': min(self.temperature.cold(temperature_value), self.pressure.medium(pressure_value)),
            'Rule 4': min(self.temperature.warm(temperature_value), self.pressure.medium(pressure_value)),
            'Rule 5': min(self.temperature.hot(temperature_value), self.pressure.high(pressure_value)),
            'Rule 6': min(self.temperature.hot(temperature_value), self.pressure.very_high(pressure_value)),
            'Rule 7': min(self.temperature.cold(temperature_value), self.pressure.high(pressure_value)),
            'Rule 8': min(self.temperature.freeze(temperature_value), self.pressure.very_high(pressure_value)),
            'Rule 9': min(self.temperature.cold(temperature_value), self.pressure.very_high(pressure_value)),
            'Rule 10': min(self.temperature.warm(temperature_value), self.pressure.medium(pressure_value)),
            'Rule 11': min(self.temperature.hot(temperature_value), self.pressure.medium(pressure_value)),
            'Rule 12': min(self.temperature.hot(temperature_value), self.pressure.very_low(pressure_value))
        }

        return rules, temperature_value_str, pressure_value_str

    def defuzzification(self, rules):
        numerator_sum = 0
        denominator_sum = 0

        for rule in rules:
            if rule == 'Rule 1':
                numerator_sum += rules[rule] * 0
                denominator_sum += rules[rule]

            if rule == 'Rule 2':
                numerator_sum += rules[rule] * 2.5
                denominator_sum += rules[rule]

            if rule == 'Rule 3':
                numerator_sum += rules[rule] * 7.5
                denominator_sum += rules[rule]

            if rule == 'Rule 4':
                numerator_sum += rules[rule] * 15
                denominator_sum += rules[rule]

            if rule == 'Rule 5':
                numerator_sum += rules[rule] * 22.5
                denominator_sum += rules[rule]

            if rule == 'Rule 6':
                numerator_sum += rules[rule] * 30
                denominator_sum += rules[rule]

            if rule == 'Rule 7':
                numerator_sum += rules[rule] * 20
                denominator_sum += rules[rule]

            if rule == 'Rule 8':
                numerator_sum += rules[rule] * 17.5
                denominator_sum += rules[rule]

            if rule == 'Rule 9':
                numerator_sum += rules[rule] * 32.5
                denominator_sum += rules[rule]

            if rule == 'Rule 10':
                numerator_sum += rules[rule] * 22.5
                denominator_sum += rules[rule]

            if rule == 'Rule 11':
                numerator_sum += rules[rule] * 30
                denominator_sum += rules[rule]

            if rule == 'Rule 12':
                numerator_sum += rules[rule] * 5
                denominator_sum += rules[rule]

        speed_value = numerator_sum / denominator_sum

        if speed_value <= 10:
            speed_str = "slow"
        elif speed_value >= 20 and speed_value <= 30:
            speed_str = "steady"
        else:
            speed_str = "fast"

        return speed_str

    def control(self, temperature_value, pressure_value):
        rules, temperature_value_str, pressure_value_str = self.fuzzy_rules(temperature_value, pressure_value)
        speed_value = self.defuzzification(rules)

        # print('Temperature:', temperature_value_str)
        # print('Pressure:', pressure_value_str)
        print('The Speed is:', speed_value)

        self.plot_graph(temperature_value, pressure_value, rules)

    def plot_graph(self, temperature_value, pressure_value, rules):
        temperature = range(0, 40)
        temperature_membership = [self.temperature.freeze(x) for x in temperature]

        pressure = range(0, 50)
        pressure_membership = [self.pressure.very_low(x) for x in pressure]

        speed = [self.defuzzification(rules)] * len(temperature)

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.plot(temperature, temperature_membership, label='Temperature')
        plt.axvline(x=temperature_value, color='r', linestyle='--')
        plt.legend()
        plt.xlabel('Temperature')
        plt.ylabel('Membership')
        plt.title('Temperature Membership')

        plt.subplot(1, 2, 2)
        plt.plot(pressure, pressure_membership, label='Pressure')
        plt.axvline(x=pressure_value, color='r', linestyle='--')
        plt.plot(temperature, speed, label='Speed')
        plt.legend()
        plt.xlabel('Pressure')
        plt.ylabel('Membership')
        plt.title('Pressure Membership and Speed')

        plt.tight_layout()
        plt.show()


temperature_input = float(input("Temperature: "))
pressure_input = float(input("Pressure: "))

fis = FuzzySystem()
fis.control(temperature_input, pressure_input)    

