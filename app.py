import streamlit as st
from groq import Groq

# Groq client
client = Groq(
    api_key="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"
)

# Page settings
st.set_page_config(
    page_title="CreatorFlow AI",
    page_icon="✨"
)

# Heading
st.title("✨ CreatorFlow AI")
st.subheader("AI Content Planner for Creators")

# Inputs
niche = st.text_input("Enter your niche")

platform = st.selectbox(
    "Choose platform",
    ["Instagram", "YouTube", "LinkedIn", "Twitter"]
)

audience = st.text_input("Target audience")

goal = st.selectbox(
    "Your goal",
    ["Growth", "Engagement", "Sales", "Brand Awareness"]
)

tone = st.selectbox(
    "Content tone",
    ["Professional", "Funny", "Educational", "Creative"]
)

# Button
if st.button("🚀 Generate Content Plan"):

    prompt = f"""
You are an expert content strategist.

Create a detailed content plan for a creator.

Niche: {niche}
Platform: {platform}
Audience: {audience}
Goal: {goal}
Tone: {tone}

Give:

1. 30-Day Content Calendar
2. 10 Content Ideas
3. 10 Viral Hooks
4. Caption Ideas
5. Hashtag Suggestions
6. Growth Tips

Make everything detailed and practical.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

        st.success("✅ Content Plan Generated Successfully!")
        st.write(result)

    except Exception as e:
        st.error(f"❌ Error: {e}")