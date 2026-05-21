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
"""
user_answer = st.text_input("Type the English translation:")
client = OpenAI(api_key=st.secrets['json'] )
chat_history = [
    {"role": "system", "content": system_prompt}
]
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
response = client.chat.completions.create(
            response_format={'type':'json_object'},
            model='gpt-4o',
            messages=chat_history
        )

st.write(json.loads(response.choices[0].message.content))
if st.button("Submit"):
    if user_answer.upper().strip() == st.session_state.sentence:
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The answer was: {st.session_state.sentence}")


