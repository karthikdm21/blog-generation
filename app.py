import streamlit as st
from langchain.prompts import PromptTemplate
import cohere  # Import Cohere

# Function to get response from Cohere model
def get_cohere_response(input_text, no_words, blog_style):
    # Initialize the Cohere API client with your API key
    co = cohere.Client("your-cohere-api-key")  # Replace with your actual Cohere API key
    
    # Construct the prompt
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """
    
    prompt = template.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
    
    # Generate the response using Cohere's language model
    response = co.generate(
        model="command-xlarge-20221108",  # You can adjust the model based on your requirements
        prompt=prompt,
        max_tokens=256,  # Maximum tokens for response
        temperature=0.7  # Controls the randomness of the response
    )

    return response.generations[0].text.strip()  # Extracting the generated text

# Streamlit UI setup
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

# User inputs
input_text = st.text_input("Enter the Blog Topic")

# Two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

# Generate and display the response when the button is clicked
if submit:
    st.write(get_cohere_response(input_text, no_words, blog_style))
