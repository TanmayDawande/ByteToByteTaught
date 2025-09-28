AI Recipe Generator
<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge">
<img src="https://img.shields.io/badge/Google_Gemini-3F83F8?style=for-the-badge&logo=google&logoColor=white" alt="Gemini API Badge">
</p>

This is a simple yet powerful AI-powered recipe generator built with Streamlit and the Google Gemini API. It allows users to get healthy and personalized recipe ideas by simply typing in a few ingredients or their meal preferences.

✨ Features
Intelligent Recipe Generation: Uses the advanced Gemini model to create unique recipes.

Dynamic and Personalized: Get recipe ideas based on your specific ingredients, dietary preferences, or meal types (e.g., "vegetarian pasta," "quick dinner," "low-carb breakfast").

Clear Instructions: Recipes include ingredients, step-by-step instructions, and nutritional information for a complete guide.

User-Friendly Interface: A clean and intuitive UI makes it easy to use for anyone.

🚀 How to Run Locally
Follow these steps to get a copy of the project up and running on your local machine.

Prerequisites
You'll need a Google Gemini API key. If you don't have one, you can get one from the Google AI Studio.

Python 3.8+

pip

Installation
Clone the repository to your local machine:

Bash

git clone https://github.com/TanmayDawande/ByteByteTaught.git
cd ByteByteTaught
Create a virtual environment and activate it (optional but recommended):

Bash

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install the required Python packages:

Bash

pip install -r requirements.txt
Create a .env file in the root directory of the project and add your Gemini API key:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
Running the App
Run the following command from your terminal:

Bash

streamlit run main.py
This will open the application in your default web browser.

📄 Code Snippet
The core of the application uses the Gemini API to generate content. Here's a look at how it works:

Python

import google.generativeai as genai
import streamlit as st

# ... (setup and UI code) ...

if st.button("Generate Recipe"):
    with st.spinner("Cooking up a delicious recipe..."):
        prompt = "What are some healthy dinner ideas? Include ingredients, instructions, and nutritional information."
        try:
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

Remember to:
Replace your-username/your-repo-name with your actual GitHub username and repository name.

Make sure you have a requirements.txt file listing all the Python libraries (e.g., streamlit, google-generativeai, python-dotenv). You can generate this with pip freeze > requirements.txt.

Replace your_app_file_name.py with the name of your main Python script (e.g., app.py or recipe_generator.py).

Create a LICENSE file if you don't have one, as it's good practice for open-source projects.
