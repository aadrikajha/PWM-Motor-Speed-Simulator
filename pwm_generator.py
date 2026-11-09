
import numpy as np

def generate_pwm(duty_cycle, frequency, duration, sampling_rate):

    t = np.arange(0, duration, 1 / sampling_rate)

    period = 1 / frequency

    pwm_signal = ((t % period) < (duty_cycle / 100) * period)

    return t, pwm_signal.astype(float)
