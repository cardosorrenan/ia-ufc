import matplotlib.pyplot as plt
from assist_fuzzy import *


pedal_pressure = PedalPressure()
pedal_pressure.normalize()
speed_car = SpeedCar()
speed_car.normalize()
speed_wheel = SpeedWheel()
speed_wheel.normalize()

brake_press, brake_drop = [], []
brake_press.append(pedal_pressure.medium)
brake_press.append(min(pedal_pressure.high, speed_car.high, speed_wheel.high))
final_press = sum(brake_press)
brake_drop.append(min(pedal_pressure.high, speed_car.high, speed_wheel.high))
brake_drop.append(pedal_pressure.low)
final_drop = sum(brake_drop)

p_p, s_c, s_w = pedal_pressure, speed_car, speed_wheel
print(f'Pedal pressure:\n-- Low: {p_p.low} - Med: {p_p.medium} - High: {p_p.high}')
print(f'Speed car:\n-- Low: {s_c.low} - Med: {s_c.medium} - High: {s_c.high}')
print(f'Speed wheel:\n-- Low: {s_w.low} - Med: {s_w.medium} - High: {s_w.high}')

y_final, y_brake_press, y_brake_drop = balance_press_drop(final_press, final_drop)
intensity_brake = calc_intensity(y_final)
print('Brake applied intensity:\n-- {}'.format(intensity_brake))

plt.figure(1)
plt.subplot(221)
plt.axis([0, 100, 0, 1])
plt.plot(range(0, 101), y_brake_press)
plt.subplot(222)
plt.axis([0, 100, 0, 1])
plt.plot(range(0, 101), y_brake_drop)
plt.subplot(223)
plt.axis([0, 100, 0, 1])
plt.plot(range(0, 101), y_final)
plt.show()