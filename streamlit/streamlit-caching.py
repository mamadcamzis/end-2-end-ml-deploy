import numpy as np 
import pandas as pd

import streamlit as st
from time import sleep
from transformers import pipeline

@st.cache_data
def load_data(url:  str) -> pd.DataFrame:
    return pd.read_csv(url)

url = "https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv"
df = load_data(url)
st.dataframe(df)
st.button("Rerun")

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()
text = st.text_input("Type some text: ")
if text:
    output = model(text)[0]
    st.write(output)
""" Block comments
`@st.cache_data(max_entries=3)
def get_data(some_integer: int) -> np.ndarray:
    sleep(3)
    return some_integer * np.random.randn(1000)

#some_integer = int(st.number_input("Enter some integer: "))
#st.write(get_data(some_integer))
st.write("### Apply caching if one of parameters change")
@st.cache_data()
def get_data_bis(mean: float, std: float) -> np.ndarray:
    sleep(3)
    return mean + std * np.random.randn(1000)

st.write("### We dont want caching std by using leading character `_sdt`")
@st.cache_data()
def get_data_third(mean: float, _std: float) -> np.ndarray:
    sleep(3)
    return mean + _std * np.random.randn(1000)

mean = float(st.number_input("Enter mean: ", value=0.))
std = float(st.number_input("Enter std: ", value=1.))
st.write(get_data_third(mean, std))
#st.write(get_data())
#st.cache_data
#st.cache_resource`
"""

class SomeClass:
    def __init__(self, some_integer: int) -> None:
        self.some_integer = some_integer

def hash_func(obj: SomeClass) -> int:
    return obj.some_integer

@st.cache_data(hash_funcs={SomeClass: hash_func})
def multiply_with(obj: SomeClass, multiplier: int) -> int:
    return obj.some_integer * multiplier

some_integer = int(st.text_input("Enter some integer: ", value=13))

my_class = SomeClass(some_integer)
multiplier = 3

st.write(multiply_with(my_class, multiplier))