from pwm_generator import generate_pwm
import matplotlib.pyplot as plt

t, pwm = generate_pwm(
    duty_cycle=50,
    frequency=1000,
    duration=0.01,
    sampling_rate=100000
)

plt.plot(t, pwm)
plt.xlabel("Time (seconds)")
plt.ylabel("PWM Output")
plt.title("PWM Signal - 50% Duty Cycle")
plt.grid()
plt.show()