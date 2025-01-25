import streamlit as st
from streamlit_lottie import st_lottie
import requests
from ollama import chat
import time
import speech_recognition as sr

def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        st.write(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        st.write("Sorry, there was an issue with the speech recognition service.")
        return ""

def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def stream_response(user_input):
    try:
        response = ""
        stream = chat(model='llama2', messages=[{'role': 'user', 'content': user_input}], stream=True)
        for chunk in stream:
            content = chunk['message']['content']
            response += content
            yield response
    except Exception as e:
        yield f"Error: {str(e)}"

def main():
    st.set_page_config(page_title="Interactive AI Chatbot", page_icon="🤖")
    
    ai_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_t9gkkhz4.json")

    st.markdown(
        """
        <style>
        .stApp {
        background-image: url('\1.webp');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Dr. AIML: Your AI Companion")
    st.markdown("""
        Welcome to Dr. AIML! Ask me anything about AI, machine learning, or robotics, and I'll provide real-time answers.
        - Type `exit` or `quit` to end the session.
    """)

    st_lottie(ai_animation, height=200, key="ai_animation")

    if st.button("Speak"):
        user_input = voice_input()
    else:
        user_input = st.text_input("You:", placeholder="Type your question here...", key="text_input")

    if user_input:
        if user_input.lower() in {"exit", "quit"}:
            st.write("Goodbye!")
        else:
            with st.spinner("Thinking..."):
                response_container = st.empty()
                response = ""
                for partial_response in stream_response(user_input):
                    response = partial_response
                    response_container.markdown(response.replace('\n', '  '))
                    time.sleep(0.01)

if __name__ == "__main__":
    main()



# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests
# from ollama import chat
# import time
# import speech_recognition as sr

# def voice_input():
#     """Capture voice input and convert it to text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         audio = recognizer.listen(source)
#     try:
#         user_input = recognizer.recognize_google(audio)
#         st.write(f"You said: {user_input}")
#         return user_input
#     except sr.UnknownValueError:
#         st.write("Sorry, I could not understand the audio.")
#         return ""
#     except sr.RequestError:
#         st.write("Sorry, there was an issue with the speech recognition service.")
#         return ""


# def load_lottie_url(url):
#     """Fetch Lottie animation JSON from a URL."""
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# def stream_response(user_input):
#     """Stream the response from the chat model and display it in the Streamlit app."""
#     try:
#         response = ""
#         stream = chat(model='llama2', messages=[{'role': 'user', 'content': user_input}], stream=True)
#         for chunk in stream:
#             content = chunk['message']['content']
#             response += content
#             yield response
#     except Exception as e:
#         yield f"Error: {str(e)}"

# def main():
#     st.set_page_config(page_title="Interactive AI Chatbot", page_icon="🤖")
    
#     # Load Lottie animations
#     ai_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_t9gkkhz4.json")
#     ml_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json")
#    # robotics_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_kkflmtur.json")

#     # Add background styling
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: #2b2d42;
#             color: white;
#             font-family: 'Comic Sans MS', cursive, sans-serif;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.title("Dr. AIML: Your AI Companion")
#     st.markdown("""
#         Welcome to Dr. AIML! Ask me anything about AI, machine learning, or robotics, and I'll provide real-time answers.
#         - Type `exit` or `quit` to end the session.
#     """)

#     # Display animations on the homepage
#     st_lottie(ai_animation, height=200, key="ai_animation")
#     # st_lottie(ml_animation, height=200, key="ml_animation")
#     # st_lottie(robotics_animation, height=200, key="robotics_animation")

#     user_input = st.text_input("You:", placeholder="Type your question here...")
#     if st.button("Speak"):
#         user_input = voice_input()
#     else:
#         user_input = st.text_input("You:", placeholder="Type your question here...")

#     if user_input:
#         if user_input.lower() in {"exit", "quit"}:
#             st.write("Goodbye!")
#         else:
#             with st.spinner("Thinking..."):
#                 response_container = st.empty()
#                 response = ""
#                 for partial_response in stream_response(user_input):
#                     response = partial_response
#                     response_container.markdown(response.replace('\n', '  '))
#                     time.sleep(0.01)  # Adjusted for faster rendering
#     # if user_input:
#     #     if user_input.lower() in {"exit", "quit"}:
#     #         st.write("Goodbye!")
#     #     else:
#     #         with st.spinner("Thinking..."):
#     #             response_container = st.empty()
#     #             response = ""
#     #             for partial_response in stream_response(user_input):
#     #                 response = partial_response
#     #                 response_container.markdown(response.replace('\n', '  '))
#     #                 time.sleep(0.01)  # Adjusted for faster rendering

# if __name__ == "__main__":
#     main()


# import streamlit as st
# from ollama import chat

# def stream_response(user_input):
#     """Stream the response from the chat model and display it in the Streamlit app."""
#     try:
#         response = ""
#         stream = chat(model='llama2', messages=[{'role': 'user', 'content': user_input}], stream=True)
#         for chunk in stream:
#             content = chunk['message']['content']
#             response += content
#         return response
#     except Exception as e:
#         return f"Error: {str(e)}"

# def main():
#     st.set_page_config(page_title="Interactive AI Chatbot", page_icon="🤖")
    
#     # Add background image
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-image: url('https://via.placeholder.com/1920x1080.png?text=Background+Image');
#             background-size: cover;
#             color: white;
#             font-family: 'Comic Sans MS', cursive, sans-serif;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.title("Interactive AI Chatbot")
#     st.markdown("""
#         Welcome to your AI-powered chatbot! Type your questions below and get real-time answers.
#         - **Animations** and **visuals** will adapt based on your queries.
#         - Type `exit` or `quit` to end the session.
#     """)

#     user_input = st.text_input("You:", placeholder="Type your question here...")
#     if user_input:
#         if user_input.lower() in {"exit", "quit"}:
#             st.write("Goodbye!")
#         else:
#             with st.spinner("Thinking..."):
#                 response = stream_response(user_input)
#                 st.success("AI Response:")
#                 st.write(response)

#     # Add animations or visuals based on user input
#     if "weather" in user_input.lower():
#         st.image("https://via.placeholder.com/400x200.png?text=Weather+Animation", caption="Weather Animation")
#     elif "finance" in user_input.lower():
#         st.image("https://via.placeholder.com/400x200.png?text=Finance+Chart", caption="Finance Chart")
#     elif "science" in user_input.lower():
#         st.image("https://via.placeholder.com/400x200.png?text=Science+Graphic", caption="Science Graphic")

# if __name__ == "__main__":
#     main()
