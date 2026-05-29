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
col1, col2, col3, col4 = st.columns(4)
k = list(MorseCode.keys())

for i in range(0,len(k),4):
    col1.header(MorseCode[k[i]])
    col1.subheader(k[i])

    col2.header(MorseCode[k[i+1]])
    col2.subheader(k[i+1])
    i
    if i >= 23:
        break

    col3.header(MorseCode[k[i+2]])
    col3.subheader(k[i+2])

    col4.header(MorseCode[k[i+3]])
    col4.subheader(k[i+3])
