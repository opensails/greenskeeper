import pandas as pd
import random
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st

filename = 'fulldata_brokedown.csv'
# n = sum(1 for line in open(filename))-1  # count number of rows in column
# s = n//10  # sample size of 10%
# skip = sorted(random.sample(range(1, n+1), n-s))

sample_data = pd.read_csv(filename, index_col='player')
# cols = []
# pd.options.display.float_format = '{:, .2f}'.format
# for column in sample_data:
#     cols.append(str(sample_data[column]))
st.title('Sample Data')
columns = st.sidebar.multiselect('Columns', options=list(sample_data.columns),
                                 default=['Scoring Average (Actual)-AVG', 'SG: Tee-to-Green-AVERAGE', 'SG: Tee-to-Green-SG:OTT', 'SG: Tee-to-Green-SG:APR', 'SG: Tee-to-Green-SG:ARG', 'SG: Off-the-Tee-AVERAGE'])

st.write('Sample Data Table')
st.dataframe(sample_data[columns].style.highlight_max(
    axis=0).format('{:.2f}'), width=4500, height=400)


def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val >= 0.90 else 'black'
    return 'color: %s' % color


if st.sidebar.checkbox("Spearman Correlation"):
    st.header('Spearman Correlation')
    st.write(sample_data.corr(
        method='spearman').style.applymap(color_negative_red))
if st.sidebar.checkbox("Pearson Correlation"):
    st.header('Pearson Correlation')
    st.write(sample_data.corr(method='pearson'))
if st.sidebar.checkbox("Kendall Correlation"):
    st.header('Kendall Correlation')
    st.write(sample_data.corr(method='kendall'))


if st.sidebar.checkbox('Show Correlation Heat Map'):
    st.write('Correlations')
    corr = sample_data.corr()
    mask = np.triu(np.ones_like(corr, dtype=np.bool))
    f, ax = plt.subplots(figsize=(20, 15))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    st.write(sns.heatmap(corr, mask=mask, cmap=cmap))
    st.pyplot()

if st.sidebar.checkbox("Simple Correlation Plot with Matplotlib "):
    plt.matshow(sample_data.corr())
    st.pyplot()

if st.sidebar.checkbox("Bar Graph"):
    sample_size = st.sidebar.slider('Set your Sample Size', 1, 25)
    skip = sorted(random.sample(range(1, 223), 223-int(sample_size)))
    columns3 = st.sidebar.multiselect(
        'Select Columns for Bar Graph', options=sample_data.columns)
    sample_set = pd.read_csv(filename, skiprows=skip, index_col='player')
    st.bar_chart(sample_set[columns3])
