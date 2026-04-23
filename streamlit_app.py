import streamlit as st
from openai import OpenAI
import json
system_prompt = """
You are gonna give the user a stock that has the most positive change within this week
Respond in a json in the following format: 
{Name: stock abbreviation,
percent change: +%,
dollar change: +$,
current value: #,
daterange: mm/dd/yyyy -mm/dd/yyyy
}
"""
client = OpenAI(api_key=st.secrets['json'] )
chat_history = [
    {"role": "system", "content": system_prompt}


]

response = client.chat.completions.create(
            response_format={'type':'json_object'},
            model='gpt-4o',
            messages=chat_history
        )

st.write(json.loads(response.choices[0].message.content))