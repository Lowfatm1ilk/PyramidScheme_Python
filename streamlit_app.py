import streamlit as st
from openai import OpenAI
import json
if 'left' not in st.session_state:

    st.session_state['left']=0
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
col1, col2, col3, col4 = st.columns(4)
k = list(MorseCode.keys())

for i in range(0,len(k),4):
    col1.header(MorseCode[k[i]])
    col1.subheader(k[i])

    col2.header(MorseCode[k[i+1]])
    col2.subheader(k[i+1])
    if i >= 23:
        break

    col3.header(MorseCode[k[i+2]])
    col3.subheader(k[i+2])

    col4.header(MorseCode[k[i+3]])
    col4.subheader(k[i+3])

system_prompt = """Create a json object of three similar sentences. 
These sentences should be similar but have slight differences
Here is an example output:
{ 
    "s": "I like pizza", 
    "op": ["i like pizzas","i like pineapples","I like pizza"]
}
the correct sentence s should be part of the three sentences on op, but in random position
"""

client = OpenAI(api_key=st.secrets['json'] )
chat_history = [
    {"role": "system", "content": system_prompt}]
response = client.chat.completions.create(
                response_format={'type':'json_object'},
                model='gpt-4o',
                messages=chat_history)
ops = json.loads(response.choices[0].message.content)['op']
s = json.loads(response.choices[0].message.content)['s']

for c in s:
    st.write(MorseCode[c.upper()])
for i in  range(len(ops)):
    if ops[i] ==s:
        st.session_state['left'] = i
b1 = st.button(json.loads(response.choices[0].message.content)['op'][0])

b2 = st.button(json.loads(response.choices[0].message.content)['op'][1])
b3 = st.button(json.loads(response.choices[0].message.content)['op'][2])


if b1:
    if st.session_state['left'] ==0:
        st.success('You did it!')
                 

if b2:
    if st.session_state['left'] ==1:
        st.success('You did it!')
                 

if b3:
    if st.session_state['left'] ==2:
        st.success('You did it!')
                 