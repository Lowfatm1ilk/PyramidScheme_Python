import streamlit as st
from openai import OpenAI
import json

def text_to_morse(text):
    morse = []

    for char in text.upper():
        if char in MORSE_CODE:
            morse.append(MORSE_CODE[char])

    return " ".join(morse)

st.subheader("Translate this Morse code:")

system_prompt = """
You're gonna generate one simmple sentence in morse code no punctuation and under 6 words is optimal.

Return back as a json object only in the following format:

{
'morse':'.. / .-.. .. -.- . / .--. .. --.. --.. .-',
'sentence':"i like pizza"
}
"""

MorseCode = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}


user_answer = st.text_input("Type the English translation:")



client = OpenAI(api_key=st.secrets['json'] )
chat_history = [
    {"role": "system", "content": system_prompt}]

response = client.chat.completions.create(
            response_format={'type':'json_object'},
            model='gpt-4o',
            messages=chat_history)
morse = json.loads(response.choices[0].message.content)['morse']
st.session_state['sentence'] =  json.loads(response.choices[0].message.content)['sentence']
st.write(morse)
if st.button("Submit"):
    if user_answer.lower().strip() == st.session_state.sentence:
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The answer was: {st.session_state.sentence}")
