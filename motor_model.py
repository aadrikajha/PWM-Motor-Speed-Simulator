
import numpy as np

def simulate_motor(
    duty_cycle,
    supply_voltage=12,
    resistance=2,
    inductance=0.01,
    back_emf_constant=0.05,
    torque_constant=0.05,
    inertia=0.005,
    friction=0.002,
    frequency=1000,
    duration=2,
    dt=0.00001
):

    # Generate time values
    time = np.arange(0, duration, dt)

    # Calculate PWM period
    period = 1 / frequency

    # Generate actual switching voltage
    pwm_voltage = np.where(
        (time % period) < (duty_cycle / 100) * period,
        supply_voltage,
        0
    )

    # Initialize motor variables
    current = np.zeros(len(time))
    speed = np.zeros(len(time))

    # Simulate motor behaviour
    for k in range(1, len(time)):

        # Electrical equation
        di = (
            pwm_voltage[k-1]
            - resistance * current[k-1]
            - back_emf_constant * speed[k-1]
        ) / inductance

        # Mechanical equation
        dw = (
            torque_constant * current[k-1]
            - friction * speed[k-1]
        ) / inertia

        # Numerical integration
        current[k] = max(
    0,
    current[k-1] + di * dt
)
        speed[k] = speed[k-1] + dw * dt

    # Convert rad/s to RPM
    rpm = speed * 60 / (2 * np.pi)

    return time, current, speed, rpm
