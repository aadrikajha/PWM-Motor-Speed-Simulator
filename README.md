**Live Demo:** [Try the PWM Motor Speed Simulator](https://pwm-motor-speed-simulator.streamlit.app/)

# PWM-Based DC Motor Speed Control Simulator

An interactive engineering simulation that demonstrates DC motor speed control using Pulse Width Modulation (PWM). Built using Python, NumPy, Matplotlib and Streamlit.

## Project Overview

This project simulates the behaviour of a DC motor under different PWM duty cycles and switching frequencies. It demonstrates how electrical and mechanical motor parameters influence motor speed and armature current.

The simulator includes an interactive dashboard for experimenting with motor parameters and visualizing the resulting waveforms.

## Features

- PWM signal generation with adjustable duty cycle.
- DC motor mathematical modelling.
- Interactive motor speed control dashboard.
- Motor speed vs time visualization.
- Armature current response analysis.
- Current ripple visualization.
- Switching frequency comparison.
- Automated testing using Pytest.

## Mathematical Model

### 1. PWM Average Voltage

\[
V_{avg}=D \times V_s
\]

Where:
- D = Duty cycle (fraction)
- Vs = Supply voltage

### 2. Electrical Equation

\[
L\frac{di}{dt}=V-Ri-K_e\omega
\]

### 3. Mechanical Equation

\[
J\frac{d\omega}{dt}=K_ti-b\omega
\]

### 4. Angular Speed Conversion

\[
RPM=\frac{60\omega}{2\pi}
\]

## Technologies Used

- Python
- NumPy
- Matplotlib
- Streamlit
- Pytest
- Git and GitHub

## Project Structure

```text
PWM-Motor-Speed-Simulator/
├── app.py
├── pwm_generator.py
├── motor_model.py
├── test_pwm.py
├── test_motor.py
├── test_motor_model.py
├── requirements.txt
├── README.md
├── .gitignore
└── outputs/
```

## Installation and Execution

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd PWM-Motor-Speed-Simulator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulator:

```bash
streamlit run app.py
```

Run automated tests:

```bash
python -m pytest -v
```

## Testing

The motor model is verified using automated tests covering:

- Zero duty cycle behaviour.
- Motor speed response to increasing duty cycles.
- Nonnegative armature current.
- Valid numerical simulation outputs.

## Future Improvements

- Freewheeling diode and H-bridge modelling.
- Switching losses and efficiency analysis.
- Closed-loop motor speed control using PID.
- Hardware implementation using Arduino or ESP32.
- Advanced motor parameter customization.

## Author

Aadrika Jha: ECE Student
