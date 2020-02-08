class PedalPressure():
    def __init__(self):
        while True:
            x = int(input('Pedal pressure: '))
            if x > 0 and x < 100: break
            print("pedal pressure: [0, 100]")
        self.low = round(-x/50 + 1, 3)
        if x > 50: self.medium = round(-x/20 + 7/2, 3)
        else: self.medium = round(x/20 - 3/2, 3)
        self.high = round(x/50 - 1, 3)
        self.input = x

    def normalize(self):
        if self.low < 0: self.low = 0
        if self.medium < 0: self.medium = 0
        if self.high < 0: self.high = 0


class SpeedCar():
    def __init__(self):
        while True:
            x = int(input('Speed car: '))
            if x > 0 and x < 100: break
            print("Speed car: [0, 100]")
        self.low = round(-x/60 + 1, 3)
        if x > 50: self.medium = round(-x/30 + 8/3, 3)
        else: self.medium = round(x/30 - 2/3, 3)
        self.high = round(x/60 - 2/3, 3)
        self.input = x

    def normalize(self):
        if self.low < 0: self.low = 0
        if self.medium < 0: self.medium = 0
        if self.high < 0: self.high = 0


class SpeedWheel():
    def __init__(self):
        while True:
            x = int(input('Speed wheel: '))
            if x > 0 and x < 100: break
            print("Speed car: [0, 100]")
        self.low = round(-x/60 + 1, 3)
        if x > 50: self.medium = round(-x/30 + 8/3, 3)
        else: self.medium = round(x/30 - 2/3, 3)
        self.high = round(x/60 - 2/3, 3)
        self.input = x

    def normalize(self):
        if self.low < 0: self.low = 0
        if self.medium < 0: self.medium = 0
        if self.high < 0: self.high = 0


def f_belongs_press(final_press, x):
	if x >= 0 and x <= final_press*100: return x/100
	elif x <= 100: return final_press


def f_belongs_drop(final_drop, x):
	if x >= 0 and x <= 100-final_drop*100: return final_drop
	elif x <= 100: return 1-((x)/100)


def balance_press_drop(final_press, final_drop):
    y_final_press, y_final_drop, y_final = [], [], []
    for i in range(0, 101):
        press = f_belongs_press(final_press, i)
        drop = f_belongs_drop(final_drop, i)
        y_final_press.append(press)
        y_final_drop.append(drop)
        if press > drop:
            y_final.append(press)
        else:
            y_final.append(drop)
    return y_final, y_final_press, y_final_drop,


def calc_intensity(y_final):
    intens = 0
    for i in range(0, 101): 
        intens = intens + i * y_final[i]
    return round(intens/sum(y_final)+0.01, 3)
        