import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_mohrs_circles(sigma_1, sigma_2, sigma_3):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot Mohr's circles for each pair of principal stresses
    def plot_circle(sigma_a, sigma_b, color):
        center = (sigma_a + sigma_b) / 2
        radius = abs(sigma_a - sigma_b) / 2
        circle = plt.Circle((center, 0), radius, color=color, fill=False, linestyle='-', linewidth=2)
        ax.add_artist(circle)
        ax.plot([sigma_a, sigma_b], [0, 0], 'ro')  # Principal stresses

    # Plot circles
    plot_circle(sigma_1, sigma_3, 'b')  # Circle for sigma_1 and sigma_3
    plot_circle(sigma_1, sigma_2, 'g')  # Circle for sigma_1 and sigma_2
    plot_circle(sigma_2, sigma_3, 'r')  # Circle for sigma_2 and sigma_3

    # Calculate limits for the axes
    max_sigma = max(sigma_1, sigma_2, sigma_3)
    min_sigma = min(sigma_1, sigma_2, sigma_3)
    max_radius = max(abs(max_sigma - min_sigma) / 2, abs(max_sigma), abs(min_sigma))

    # Set the limits and labels
    ax.set_xlim(min_sigma - max_radius * 0.1, max_sigma + max_radius * 0.1)
    ax.set_ylim(-max_radius * 1.1, max_radius * 1.1)
    ax.set_xlabel('Normal Stress (σ)')
    ax.set_ylabel('Shear Stress (τ)')
    ax.set_title("Mohr's Circles for Three Principal Stresses")
    ax.grid(True)

    # Ensure equal scaling of x and y axes
    ax.set_aspect('equal', adjustable='box')

    # Display the plot
    st.pyplot(fig)

def main():
    # Streamlit app
    st.title("Mohr's Circles Plotter")

    # Numeric input fields for principal stresses
    sigma_1 = st.number_input("Maximum Principal Stress (σ₁)", value=100.0)
    sigma_2 = st.number_input("Intermediate Principal Stress (σ₂)", value=75.0)
    sigma_3 = st.number_input("Minimum Principal Stress (σ₃)", value=50.0)

    # Plot the circles
    plot_mohrs_circles(sigma_1, sigma_2, sigma_3)

if __name__ == "__main__":
    main()
