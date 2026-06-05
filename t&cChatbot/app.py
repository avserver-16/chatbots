import streamlit as st
import ollama

# Page Setup
st.set_page_config(page_title="T&C Shortener Bot", page_icon="PAGE")
st.title("Terms & Conditions Shortener")
st.write("Paste any long text and I'll summarize it clearly!")

# Text Input
user_text = st.text_area(
    "Paste your Terms & Conditions here:",
    height=250,
    placeholder="Paste your long text here..."
)

detail_level = st.selectbox(
    "How detailed should the summary be?",
    ["Very Short (3 bullet points)", "Medium (key points)", "Detailed (full breakdown)"]
)

# Summarize Button
if st.button("Summarize"):
    if not user_text.strip():
        st.warning("Please paste some text first!")
    else:
        # Build the prompt based on detail level
        if detail_level == "Very Short (3 bullet points)":
            prompt = f"Summarize the following text into exactly 3 clear bullet points a normal person can understand:\n\n{user_text}"
        elif detail_level == "Medium (key points)":
            prompt = f"Extract the most important points from this text in simple language. Use bullet points:\n\n{user_text}"
        else:
            prompt = f"Give a detailed plain-English breakdown of this text. Explain each major point simply:\n\n{user_text}"

        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="mistral",
                messages=[{"role": "user", "content": prompt}]
            )
            summary = response["message"]["content"]

        st.success("Done!")
        st.markdown("### Summary:")
        st.markdown(summary)

        # Chat follow-up
        st.markdown("---")
        st.markdown("### Ask a follow-up question:")
        follow_up = st.text_input("e.g. 'What happens if I cancel?' or 'Is there a refund policy?'")
        if follow_up:
            with st.spinner("Answering..."):
                follow_response = ollama.chat(
                    model="mistral",
                    messages=[
                        {"role": "user", "content": f"Here is a document:\n\n{user_text}"},
                        {"role": "assistant", "content": summary},
                        {"role": "user", "content": follow_up}
                    ]
                )
            st.markdown("**Answer:**")
            st.markdown(follow_response["message"]["content"])