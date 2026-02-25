import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="P.S. IntelliTour AI", page_icon="🎓")

st.title("🎓 P.S. IntelliTour AI")
st.subheader("Hospitality | Tourism | Events Academic Assistant")
st.write("Developed by Priyesh Srivastava")

# Enter your OpenAI API key here
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

domain = st.selectbox(
    "Select Domain",
    ["Hospitality", "Tourism", "Events"]
)

user_input = st.text_area("Enter your question:")

if st.button("Generate Response"):

    system_prompt = f"""
    You are an academic expert in {domain}.
    Provide structured answers suitable for students.
    Include:
    - Definition
    - Explanation
    - Practical example
    - 3 Viva questions
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)
api_key="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"