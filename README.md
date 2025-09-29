# AI Recipe Generator 🍳
<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge">
<img src="https://img.shields.io/badge/Google_Gemini-3F83F8?style=for-the-badge&logo=google&logoColor=white" alt="Gemini API Badge">
</p>

Tired of staring at your fridge wondering what to make? This AI-powered recipe generator, built with Streamlit and the Google Gemini API, creates healthy and personalized recipes from the ingredients you already have.

A quick demo of the AI Recipe Generator in action.
![](https://github.com/ByteToByteTaught/ByteByteTaught/raw/main/assets/GIF.gif)

## ✨ Features
👨‍🍳 Intelligent Recipe Generation: Leverages the advanced Gemini model to create unique and delicious recipes.

### 🥗 Dynamic & Personalized: Get recipes based on your specific ingredients, dietary needs (vegetarian, low-carb), or meal types (quick dinner, healthy breakfast).

### 📋 Complete Guidance: Each recipe includes a detailed ingredient list, step-by-step instructions, and nutritional information.

### 💻 User-Friendly Interface: A clean and intuitive UI built with Streamlit makes finding your next meal a breeze.

### 🛠️ Tech Stack
Backend: Python

AI Model: Google Gemini Pro

Frontend: Streamlit

API Key Management: python-dotenv

## 🚀 Getting Started
Follow these steps to get the project running on your local machine.

Prerequisites
Python 3.8+

A Google Gemini API key. You can get one from Google AI Studio.

Installation & Setup
Clone the repository:

Bash
```
git clone https://github.com/TanmayDawande/ByteByteTaught.git
cd ByteByteTaught
```
Create and activate a virtual environment (recommended):

On Windows:

Bash
```
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:

Bash
```
python -m venv venv
source venv/bin/activate
Install the required packages:
```
Bash
```
pip install -r requirements.txt
```
Set up your environment variables:
Create a file named '.env' in the root project directory and add your API key:
```
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```
Run the Streamlit app:

Bash
```
streamlit run main.py
```
The application will open in your default web browser.

## 📄 Core Logic Snippet
The app takes user input from the Streamlit interface and dynamically builds a prompt for the Gemini API.

Python

import google.generativeai as genai
import streamlit as st

# ... (setup and API key configuration) ...

# Get user input from a text box
user_input = st.text_input("Enter ingredients or meal type:", "chicken, rice, broccoli")

if st.button("Generate Recipe"):
    with st.spinner("Cooking up a delicious recipe..."):
        # Create a dynamic prompt with the user's input
        prompt = f"""
        Generate a healthy recipe based on the following: '{user_input}'.
        Please provide:
        1. A creative recipe title.
        2. A list of ingredients.
        3. Step-by-step instructions.
        4. A brief nutritional information summary (calories, protein, etc.).
        """
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
##🤝 Contributing
Contributions, issues, and feature requests are welcome! Please check the issues page.

$$📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
