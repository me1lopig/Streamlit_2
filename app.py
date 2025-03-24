import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_mohrs_circle(sigma_1, sigma_2):
    # Calculate the center and radius of Mohr's circle
    center = (sigma_1 + sigma_2) / 2
    radius = (sigma_1 - sigma_2) / 2

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot Mohr's circle
    circle = plt.Circle((center, 0), radius, color='b', fill=False, linestyle='-', linewidth=2)
    ax.add_artist(circle)

    # Plot the principal stresses
    ax.plot(sigma_1, 0, 'ro')  # Maximum principal stress
    ax.plot(sigma_2, 0, 'ro')  # Minimum principal stress

    # Set the limits and labels
    ax.set_xlim(sigma_2 - radius * 1.1, sigma_1 + radius * 1.1)
    ax.set_ylim(-radius * 1.1, radius * 1.1)
    ax.set_xlabel('Normal Stress (σ)')
    ax.set_ylabel('Shear Stress (τ)')
    ax.set_title("Mohr's Circle")
    ax.grid(True)

    # Display the plot
    st.pyplot(fig)

# Streamlit app
st.title("Mohr's Circle Plotter")

# Input fields for principal stresses
sigma_1 = st.number_input("Maximum Principal Stress (σ₁)", value=100.0)
sigma_2 = st.number_input("Minimum Principal Stress (σ₂)", value=50.0)

# Plot the circle
plot_mohrs_circle(sigma_1, sigma_2)
