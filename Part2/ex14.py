# for loop
for i in range(3):
    print(i)
import streamlit as st
import random

# ------------------------------
# Step 1: Sample food database (you can expand this)
# ------------------------------
food_data = [
    {
        "name": "Chicken Rice",
        "location": "Sunway",
        "price": 8,
        "type": "halal",
        "cravings": ["rice", "chicken"],
        "calories": 550,
        "nutrients": "protein",
        "store": "Food Court A",
        "rating": 4.5
    },
    {
        "name": "Vegetarian Salad",
        "location": "KL",
        "price": 12,
        "type": "vegetarian",
        "cravings": ["salad", "healthy"],
        "calories": 350,
        "nutrients": "low fat",
        "store": "Healthy Bites",
        "rating": 4.8
    },
    {
        "name": "Tom Yam Noodles",
        "location": "Sunway",
        "price": 10,
        "type": "spicy",
        "cravings": ["noodles", "soup"],
        "calories": 600,
        "nutrients": "protein",
        "store": "Thai Express",
        "rating": 4.3
    },
    # Add more items...
]

# ------------------------------
# Step 2: User Input Section
# ------------------------------
st.title("🍽️ What to Eat Today?")
st.subheader("Tell us what you're feeling, and we'll recommend something!")

with st.form("food_form"):
    location = st.text_input("📍 Your Location (e.g. Sunway, KL)")
    budget = st.slider("💰 Your Budget (RM)", 5, 30, 15)
    preference = st.selectbox("🍽️ Preference", ["Any", "Vegetarian", "Halal", "Spicy"])
    cravings = st.text_input("😋 Craving (e.g. noodles, rice, soup)")
    calorie_limit = st.slider("🔥 Max Calories", 100, 1000, 600)
    nutrients = st.selectbox("💪 Nutrient Focus", ["Any", "Protein", "Low Fat"])

    submitted = st.form_submit_button("Find Food!")

# ------------------------------
# Step 3: Show Results
# ------------------------------
if submitted:
    matches = []

    for food in food_data:
        if location.lower() in food["location"].lower():
            if food["price"] <= budget:
                if preference == "Any" or preference.lower() in food["type"]:
                    if cravings == "" or any(c in food["cravings"] for c in cravings.lower().split()):
                        if food["calories"] <= calorie_limit:
                            if nutrients == "Any" or nutrients.lower() in food["nutrients"]:
                                matches.append(food)

    if matches:
        selected = random.choice(matches)
        st.success(f"✅ You should try: **{selected['name']}**")
        st.write(f"💰 Price: RM {selected['price']}")
        st.write(f"📍 Nearest Store: {selected['store']}")
        st.write(f"⭐ Rating: {selected['rating']}")
        st.write(f"🔥 Calories: {selected['calories']} kcal")
    else:
        st.warning("❌ No matching food found. Try changing your filters!")

# ------------------------------
# Footer
# ------------------------------
st.caption("Made with ❤️ using Python & Streamlit")
