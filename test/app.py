# librerias

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_mohrs_circles(sigma_1, sigma_2, sigma_3):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot Mohr's circles for each pair of principal stresses
    def plot_circle(sigma_a, sigma_b, color):
        center = (sigma_a + sigma_b) / 2
        radius = (sigma_a - sigma_b) / 2
        circle = plt.Circle((center, 0), radius, color=color, fill=False, linestyle='-', linewidth=2)
        ax.add_artist(circle)
        ax.plot([sigma_a, sigma_b], [0, 0], 'ro')  # Principal stresses

    # Plot circles
    plot_circle(sigma_1, sigma_3, 'b')  # Circle for sigma_1 and sigma_3
    plot_circle(sigma_1, sigma_2, 'g')  # Circle for sigma_1 and sigma_2
    plot_circle(sigma_2, sigma_3, 'r')  # Circle for sigma_2 and sigma_3

    # Set the limits and labels
    max_sigma = max(sigma_1, sigma_2, sigma_3)
    min_sigma = min(sigma_1, sigma_2, sigma_3)
    max_radius = max_sigma - min_sigma
    ax.set_xlim(min_sigma - max_radius * 0.1, max_sigma + max_radius * 0.1)
    ax.set_ylim(-max_radius * 0.6, max_radius * 0.6)
    ax.set_xlabel('Normal Stress (σ)')
    ax.set_ylabel('Shear Stress (τ)')
    ax.set_title("Mohr's Circles for Three Principal Stresses")
    ax.grid(True)

    # Display the plot
    st.pyplot(fig)

def main():
    # Streamlit app
    st.title("Mohr's Circles Plotter")

    # Slider inputs for principal stresses
    sigma_1 = st.slider("Maximum Principal Stress (σ₁)", 0.0, 200.0, 100.0)
    sigma_2 = st.slider("Intermediate Principal Stress (σ₂)", 0.0, 200.0, 75.0)
    sigma_3 = st.slider("Minimum Principal Stress (σ₃)", 0.0, 200.0, 50.0)

    # Plot the circles
    plot_mohrs_circles(sigma_1, sigma_2, sigma_3)

if __name__ == "__main__":
    main()

