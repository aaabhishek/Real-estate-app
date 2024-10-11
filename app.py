import streamlit as st
import os
import importlib.util

st.set_page_config(page_title="Real Estate App", layout="wide")

# Function to dynamically load and execute a page by its file path
def load_page(page_path):
    spec = importlib.util.spec_from_file_location("page_module", page_path)
    page_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(page_module)

# Main function to handle navigation
def navigation():
    st.sidebar.title("Navigation")

    # Define the page paths
    pages = {
        "Home": "Home.py",
        "Price Prediction": "pages/1_Price Predictor.py",
        "Analysis": "pages/2_Analysis App.py",
        "Recommended Apartments": "pages/3_Recommend Appartments.py",
    }

    # Sidebar for page navigation
    page = st.sidebar.radio("Go to", list(pages.keys()))

    # Load the selected page using its path
    page_path = pages[page]
    load_page(page_path)

if __name__ == "__main__":
    navigation()
