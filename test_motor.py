
import matplotlib.pyplot as plt
from motor_model import simulate_motor

time, current, speed, rpm = simulate_motor(50)

plt.figure(figsize=(10, 5))
plt.plot(time, rpm)

plt.xlabel("Time (seconds)")
plt.ylabel("Motor Speed (RPM)")
plt.title("DC Motor Speed Response - 50% Duty Cycle")

plt.grid()
plt.show()

print("Final Motor Speed:", round(rpm[-1], 2), "RPM")
