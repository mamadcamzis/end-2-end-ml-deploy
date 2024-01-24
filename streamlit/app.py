import numpy as np
import pandas as pd
import streamlit as st
import time


"""
### Block Comment
You can use python's block commeents in order to put some text in your app
using Makdown.

* Bullet point 1
* Bullet point 2
* Bullet point 3

1. Enumerate 1
2. Enumerate 2
3. Enumerate 3

"""

df = pd.DataFrame({"first": [1, 2, 3, 4],
                   "second": [10, 20, 30, 40]})



st.write("A magical method to write different type on screen!")

st.write(df)
st.table(df)
st.write("### You can streamlit to draw charts and maps")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [36.76, -122.4], columns=["lat", "lon"])
st.map(map_data)

st.write("### Streamlit Widgets ! ")
slider = st.slider(label="Number x",
min_value=1,
max_value=100,
value=10,
step=1
)
st.write(f"{slider} squared is {slider ** 2}")

st.write("### Button ! ")
button = st.button(label="A button")
if button:
    st.write("Button was clicked!")

st.write("### SelectBox ! ")
selectbox = st.selectbox(label="A select box",
options=["option 1", "option 2", "option 3"])
if selectbox == "option 1":
    st.write("Option 1 was selected")
elif selectbox == "option 2":
    st.write("Option 2 was selected")
elif selectbox == "option 3":
    st.write("Option 3 was selected")

st.write("### You can assign keys to widgets to select them ! ")
st.text_input("Please enter your name !", key="name")
st.session_state.name
#st.write(f"Your name is {st.session_state.name}")
st.write("### Using Checkbox to show or hide data !")
if st.checkbox("Show chart data"):
    st.line_chart(chart_data)

st.write("### Layout our app !")
st.write("You can use `st.sidebar.<st component>` to add streamlit component to sidebar")

add_selectbox = st.sidebar.selectbox("How would you like to be contacted ?",
                                     ("Email", "Home phone", "Mobile phone"))

add_slider = st.sidebar.slider(label="Select a range of values", min_value=0.,
                                max_value=100., value=(25.0, 75.0))

st.write("### You can also use `st.columns` to layout your app !")

left_column, right_column = st.columns(2)

left_column.button("Press me !")
with right_column:
    chosen = st.radio(label="Chosen color ",
                      options=("Yellow", "Blue", "Red", "Green"))
    st.write(f"Your chosen color is {chosen}")

st.write("### Showing progress in tour app !")

"""Starting a long computation ..."""

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration -> {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"""... long computation has been completed"""


