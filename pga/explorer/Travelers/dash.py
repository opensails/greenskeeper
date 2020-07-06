import pandas as pd
import random
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st

filename = 'travelers_data_cleaned.csv'

travelers = pd.read_csv(filename)

st.title('Travels Championship Data')
columns = st.sidebar.multiselect('Select Columns', options=list(
    travelers.columns), default=['Scoring Average (Actual)-AVG'])

st.write('Travelers Data Table')
st.dataframe(travelers[columns].style.highlight_max(axis=0).format('{:.2f}'))


def color_high_corrs_green(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'green' if val >= 0.90 else 'black'
    return 'color: %s' % color


corr = travelers.corr()

top_corr = corr[corr >= 0.9].fillna(0)

if st.sidebar.checkbox("Spearman Correlation"):
    st.header('Spearman Correlation')
    st.write(travelers.corr(
        method='spearman').style.applymap(color_high_corrs_green))
if st.sidebar.checkbox("Pearson Correlation"):
    st.header('Pearson Correlation')
    st.write(travelers.corr(method='pearson').style.applymap(
        color_high_corrs_green))
if st.sidebar.checkbox("Kendall Correlation"):
    st.header('Kendall Correlation')
    st.write(travelers.corr(method='kendall').style.applymap(
        color_high_corrs_green))
if st.sidebar.checkbox("Top Correlations"):
    st.header('Top Correlations')
    st.write(top_corr.style.applymap(
        color_high_corrs_green))
