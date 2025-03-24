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
        return center, radius

    # Plot circles and get their centers and radii
    center_13, radius_13 = plot_circle(sigma_1, sigma_3, 'b')
    center_12, radius_12 = plot_circle(sigma_1, sigma_2, 'g')
    center_23, radius_23 = plot_circle(sigma_2, sigma_3, 'r')

    # Calculate the overall bounds for the axes
    all_centers = [center_13, center_12, center_23]
    all_radii = [radius_13, radius_12, radius_23]
    max_radius = max(all_radii)
    min_center = min(all_centers) - max_radius
    max_center = max(all_centers) + max_radius

    # Set the limits and labels
    ax.set_xlim(min_center, max_center)
    ax.set_ylim(-max_radius * 1.1, max_radius * 1.1)
    ax.set_xlabel('Tensión Normal (σ)')
    ax.set_ylabel('Tensión Cortante (τ)')
    ax.set_title("Círculo de Mohr")
    ax.grid(True)

    # Ensure equal scaling of x and y axes
    ax.set_aspect('equal', adjustable='box')

    # Display the plot
    st.pyplot(fig)

def main():
    # Streamlit app
    st.title("Representación del círculo de Mohr")

    # Numeric input fields for principal stresses
    sigma_1 = st.number_input("Tensión Principal (σ₁)", value=100.0)
    sigma_2 = st.number_input("Tensión Principal (σ₂)", value=75.0)
    sigma_3 = st.number_input("Tension Principal (σ₃)", value=50.0)

    # Plot the circles
    plot_mohrs_circles(sigma_1, sigma_2, sigma_3)

if __name__ == "__main__":
    main()
