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
if 'answer' in st.session_state:
    answer = st.session_state['answer']
    answer
    st.session_state['sentence']
    if st.session_state['sentence'].lower().strip()==answer.lower().strip():
        st.success('Your answer was correct')
    else:
        st.error(f'The correct answer was {st.session_state.sentence}')
 

system_prompt = """
You're gonna generate one simmple sentence in morse code no punctuation and under 6 words is optimal. Also dont give numbers.
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
'morse':'.. / .-.. .. -.- . / .--. .. --.. --.. .-',
'sentence':"i like pizza"
}
"""



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
    st.session_state['answer'] = user_answer       