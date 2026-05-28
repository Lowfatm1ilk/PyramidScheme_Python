import streamlit as st
from openai import OpenAI
import json


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



def text_to_morse(text):
    morse = []

    for char in text.upper():
        if char in MorseCode:
            morse.append(MorseCode[char])

    return " ".join(morse)

st.subheader("Translate this Morse code:")


system_prompt = """
You're gonna generate one common word in morse code no punctuation and under 4-7 letters is optimal. Also dont give numbers.
also here's a dicitionary for you "A": ".-",
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
Return back as a json object only in the following format:

{
'morse':'.--. .. --.. --.. .-',
'word':"pizza"
}
"""



user_answer = st.text_input("Type the English translation:")
morse = "press button to create word"
get_word = st.button("Press to get new word")

client = OpenAI(api_key=st.secrets['json'] )
chat_history = [
    {"role": "system", "content": system_prompt}]
if get_word:
    response = client.chat.completions.create(
                response_format={'type':'json_object'},
                model='gpt-4o',
                messages=chat_history)
    morse = json.loads(response.choices[0].message.content)['morse']
    word = json.loads(response.choices[0].message.content)['word']
st.write(morse)
if user_answer == word:
    st.succes("You translated correctly")
else:
    st.error('Wrong!')