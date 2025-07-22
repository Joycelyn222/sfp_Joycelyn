import streamlit as st
import random

# Sample food database (you can add more items!)
food_data = [
    {
        "name": "Chicken Rice",
        "price": 8,
        "calories": 550,
        "type": "halal",
        "nutrients": "protein",
        "store": "ABC Food Court",
        "location": "Malaysia",
        "rating": 4.5
    },
    {
        "name": "Vegan Salad",
        "price": 12,
        "calories": 300,
        "type": "vegetarian",
        "nutrients": "low carb",
        "store": "Healthy Bite",
        "location": "Malaysia",
        "rating": 4.7
    },
    {
        "name": "Tom Yam Soup",
        "price": 10,
        "calories": 450,
        "type": "spicy",
        "nutrients": "protein",
        "store": "Thai Express",
        "location": "Thailand",
        "rating": 4.2
    },
    # Add more items...
]

# App title
st.title("🍽️ What to Eat?")
st.write("Tell us what you're looking for, and we'll suggest a meal!")

# User Inputs
with st.form("food_form"):
    location = st.text_input("📍 Where are you?")
    budget = st.slider("💰 Your Budget (RM)", 5, 50, 20)
    preference = st.selectbox("🍽️ Preference", ["Any", "Vegetarian", "Halal", "Spicy"])
    cravings = st.text_input("😋 Craving for something? (e.g. soup, rice, sweet)")
    calories = st.slider("🔥 Max Calories", 100, 1000, 600)
    nutrients = st.selectbox("💪 Nutrient Focus", ["Any", "Protein", "Low Carb", "Low Fat"])

    submit = st.form_submit_button("🔍 Find My Food")

if submit:
    results = []
    for food in food_data:
        if location.lower() in food["location"].lower():
            if food["price"] <= budget:
                if preference == "Any" or preference.lower() in food["type"]:
                    if cravings == "" or cravings.lower() in food["name"].lower():
                        if food["calories"] <= calories:
                            if nutrients == "Any" or nutrients.lower() in food["nutrients"]:
                                results.append(food)

    if results:
        chosen = random.choice(results)
        st.success("✅ Here's your food suggestion!")
        st.write(f"🍛 **Food**: {chosen['name']}")
        st.write(f"💵 **Price**: RM {chosen['price']}")
        st.write(f"🔥 **Calories**: {chosen['calories']} kcal")
        st.write(f"🏪 **Nearest Store**: {chosen['store']}")
        st.write(f"⭐ **Rating**: {chosen['rating']} / 5.0")
    else:
        st.warning("😕 Sorry, no matching food found. Try changing your filters.")

st.caption("Made with ❤️ by a beginner using Streamlit")
