import streamlit as st
import algorithm as algo
import visualizer as viz


algo_name = st.sidebar.selectbox(
    'Select Sorting Algorithm',
    ('Quick Sort', 'Merge Sort', 'Bubble Sort')
)

array_length = st.sidebar.slider('Select Array Length'
    , value=(viz.Visualier.MAX_ARRAY_LENGTH+viz.Visualier.MIN_ARRAY_LENGTH)//2
    , min_value=viz.Visualier.MIN_ARRAY_LENGTH
    , max_value=viz.Visualier.MAX_ARRAY_LENGTH)
st.sidebar.write('Array Length is ', array_length)

run = st.sidebar.button('Run')

if run:
    algorithm = algo.create_algorithm(algo_name)
    algorithm.set_random_array(array_length)
    algorithm.sort()
