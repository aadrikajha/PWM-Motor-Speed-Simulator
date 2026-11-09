
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from pwm_generator import generate_pwm
from motor_model import simulate_motor

# Page configuration
st.set_page_config(
    page_title="PWM Motor Simulator",
    page_icon="⚙️",
    layout="wide"
)

st.title("DC Motor Speed Control Simulator")
st.write("Simulating DC motor speed using Pulse Width Modulation (PWM).")

# Sidebar controls
st.sidebar.header("Motor Parameters")

duty = st.sidebar.slider(
    "PWM Duty Cycle (%)", 0, 100, 50
)

voltage = st.sidebar.slider(
    "Supply Voltage (V)", 6, 24, 12
)

frequency = st.sidebar.slider(
    "PWM Frequency (Hz)", 100, 5000, 1000
)

# Run motor simulation
time, current, speed, rpm = simulate_motor(
    duty_cycle=duty,
    supply_voltage=voltage,
    frequency=frequency
)

# Display metrics
col1, col2, col3 = st.columns(3)

col1.metric("Duty Cycle", f"{duty}%")
col2.metric("Average Voltage", f"{duty/100*voltage:.2f} V")
col3.metric("Motor Speed", f"{rpm[-1]:.2f} RPM")

st.divider()

# Motor speed graph
st.subheader("Motor Speed Response")

fig1, ax1 = plt.subplots()

ax1.plot(time, rpm)
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Speed (RPM)")
ax1.set_title("Motor Speed vs Time")
ax1.grid()

st.pyplot(fig1)
plt.close(fig1)

# Current graph
st.subheader("Armature Current")

fig2, ax2 = plt.subplots()

ax2.plot(time, current)
ax2.set_xlabel("Time (seconds)")
ax2.set_ylabel("Current (A)")
ax2.set_title("Armature Current vs Time")
ax2.grid()

st.pyplot(fig2)
plt.close(fig2)

# PWM waveform
st.subheader("PWM Signal")

pwm_time, pwm = generate_pwm(
    duty_cycle=duty,
    frequency=frequency,
    duration=0.005,
    sampling_rate=100000
)

fig3, ax3 = plt.subplots()

ax3.plot(pwm_time, pwm * voltage)
ax3.set_xlabel("Time (seconds)")
ax3.set_ylabel("Voltage (V)")
ax3.set_title("PWM Waveform")
ax3.grid()

st.pyplot(fig3)
plt.close(fig3)

st.success("Simulation completed successfully!")

# Duty Cycle Comparison
st.divider()

st.subheader("Duty Cycle vs Motor Speed Comparison")

duty_values = [25, 50, 75, 100]

fig4, ax4 = plt.subplots(figsize=(10, 5))

final_speeds = []

for d in duty_values:

    t, i, w, motor_rpm = simulate_motor(
    duty_cycle=d,
    supply_voltage=voltage,
    frequency=frequency
)

    ax4.plot(
        t,
        motor_rpm,
        label=f"{d}% Duty Cycle"
    )

    final_speeds.append(motor_rpm[-1])

ax4.set_xlabel("Time (seconds)")
ax4.set_ylabel("Motor Speed (RPM)")
ax4.set_title("Motor Speed Comparison")
ax4.legend()
ax4.grid()

st.pyplot(fig4)
plt.close(fig4)

# Final speed comparison
st.subheader("Final Speed at Different Duty Cycles")

fig5, ax5 = plt.subplots()

ax5.bar(
    [str(d) + "%" for d in duty_values],
    final_speeds
)

ax5.set_xlabel("PWM Duty Cycle")
ax5.set_ylabel("Final Motor Speed (RPM)")
ax5.set_title("Duty Cycle vs Final RPM")
ax5.grid(axis="y")

st.pyplot(fig5)
plt.close(fig5)

# Current Ripple Analysis
st.divider()

st.subheader("PWM Armature Current Ripple Analysis")

# Display the first 5 milliseconds
zoom_time = 0.005

mask = time <= zoom_time

fig6, ax6 = plt.subplots(figsize=(10, 5))

ax6.plot(
    time[mask] * 1000,
    current[mask]
)

ax6.set_xlabel("Time (ms)")
ax6.set_ylabel("Armature Current (A)")
ax6.set_title("Zoomed PWM Current Ripple")
ax6.grid()

st.pyplot(fig6)
plt.close(fig6)

# Calculate current ripple
ripple = (
    np.max(current[mask]) -
    np.min(current[mask])
)

st.metric(
    "Current Ripple (First 5 ms)",
    f"{ripple:.4f} A"
)

# Switching Frequency Comparison
st.divider()

st.subheader("Effect of Switching Frequency")

frequencies = [500, 1000, 2000, 5000]

fig7, ax7 = plt.subplots(figsize=(10, 5))

for f in frequencies:

    t, i, w, r = simulate_motor(
        duty_cycle=duty,
        supply_voltage=voltage,
        frequency=f,
        duration=0.05,
        dt=0.000005
    )

    ax7.plot(
        t * 1000,
        i,
        label=f"{f} Hz"
    )

ax7.set_xlabel("Time (ms)")
ax7.set_ylabel("Current (A)")
ax7.set_title("Current Response at Different PWM Frequencies")
ax7.legend()
ax7.grid()

st.pyplot(fig7)
plt.close(fig7)
