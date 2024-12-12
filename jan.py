import streamlit as st
import random

# Set the title of the web page
st.title("Santa Claus Greets You!")

# Display a greeting from Santa Claus
st.write("Ho Ho Ho! 🎅🎄")

# Ask for the user's name
name = st.text_input("What's your name?", "")

# If a name is provided, greet the user
if name:
    st.write(f"Ho Ho Ho, {name}! Merry Christmas! 🎅🎁")
else:
    st.write("Please enter your name to receive a personal greeting.")

# List of gift categories and possible presents within each category
gift_categories = {
    "For Gamers": [
        "A gaming console 🎮",
        "A VR headset 🕶️",
        "A gaming chair 🪑",
        "A game gift card 💳"
    ],
    "For Readers": [
        "A bestseller book 📚",
        "A Kindle e-reader 📖",
        "A cozy reading lamp 💡",
        "A book subscription box 📦"
    ],
    "For Food Lovers": [
        "A gourmet chocolate box 🍫",
        "A sushi making kit 🍣",
        "A cookbook 📖",
        "A cheese tasting set 🧀"
    ],
    "For Tech Enthusiasts": [
        "A smartwatch ⌚",
        "A portable speaker 🎶",
        "Wireless earbuds 🎧",
        "A drone 🚁"
    ],
    "For DIY Enthusiasts": [
        "A tool set 🔧",
        "A DIY crafting kit 🎨",
        "A 3D printing pen 🖊️",
        "A woodworking kit 🪚"
    ],
    "For Fashion Lovers": [
        "A stylish scarf 🧣",
        "A designer handbag 👜",
        "A pair of cozy slippers 🥿",
        "A personalized necklace 🏷️"
    ]
}

# Function to suggest presents dynamically
def suggest_presents():
    suggestions = []
    
    # Randomly select 3 categories
    selected_categories = random.sample(list(gift_categories.keys()), 3)
    
    for category in selected_categories:
        present = random.choice(gift_categories[category])
        suggestions.append(f"{category}: {present}")
    
    return suggestions

# Suggest 3 dynamic presents
if name:
    st.write("Here are 3 random Christmas present suggestions for you, " + name + ":")
    selected_presents = suggest_presents()
    
    for present in selected_presents:
        st.write(f"- {present}")
