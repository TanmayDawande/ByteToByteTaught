#importing all the necessary libraries
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

#loading the environment variables from .env file
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# Setting up a more visually appealing page configuration
st.set_page_config(
    page_title="AI Recipe Generator",
    page_icon=":fork_and_knife:",
    layout="centered"
)

# App Title and Description with emojis
st.title("AI Recipe Generator 🥑🥗")
st.markdown("##### Get healthy recipe ideas powered by Gemini-2.5")

# Using st.form for better input handling and to clear the input after submission
with st.form(key='recipe_form'):
    user_input = st.text_input("Enter ingredients or a dish idea:", 
                               placeholder="e.g., chicken, broccoli, pasta or easy vegetarian meals",
                               key="user_input")
    submit_button = st.form_submit_button(label="Generate Recipe", type="primary")

# Logic to generate and display the recipe
if submit_button and user_input:
    # Adding a loading spinner
    with st.spinner("Cooking up a delicious recipe for you... 👨‍🍳"):
        # The prompt is now dynamic, using the user's input
        prompt = f"Based on '{user_input}', what are some healthy dinner ideas? Include a name for the dish, a brief description, ingredients with specific measurements, step-by-step instructions, and nutritional information."
        try:
            response = model.generate_content(prompt)
            # Displaying the generated content with improved formatting
            st.markdown("---") # Add a separator
            st.markdown("### Your Custom Recipe! 🎉")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
elif submit_button and not user_input:
    st.warning("Please enter some ingredients or a dish idea to get a recipe!")