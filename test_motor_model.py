
import numpy as np
from motor_model import simulate_motor


def test_zero_duty_cycle():

    time, current, speed, rpm = simulate_motor(
        duty_cycle=0,
        duration=0.2
    )

    assert np.allclose(rpm, 0)


def test_speed_increases_with_duty_cycle():

    _, _, _, rpm25 = simulate_motor(
        duty_cycle=25,
        duration=0.5
    )

    _, _, _, rpm50 = simulate_motor(
        duty_cycle=50,
        duration=0.5
    )

    _, _, _, rpm75 = simulate_motor(
        duty_cycle=75,
        duration=0.5
    )

    assert rpm25[-1] < rpm50[-1] < rpm75[-1]


def test_current_is_nonnegative():

    _, current, _, _ = simulate_motor(
        duty_cycle=60,
        duration=0.2
    )

    assert np.all(current >= 0)


def test_output_contains_valid_numbers():

    _, current, speed, rpm = simulate_motor(
        duty_cycle=50,
        duration=0.2
    )

    assert np.all(np.isfinite(current))
    assert np.all(np.isfinite(speed))
    assert np.all(np.isfinite(rpm))
