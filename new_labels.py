import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/Melsuser5/RFM_labels/main/rfm_data_with_new_labels.csv')
custom_palette = ["#5a8eb8", "#5ab874", "#bf3636", "#f08922", "#8146d4", "#e3528e", "#2a9ac7"]
fig_all = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment',width=1600, height=800,color_continuous_scale=custom_palette)
log_fig = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment', log_x=False,log_y=True,log_z=True, width=1600, height=800,color_continuous_scale=custom_palette)

st.set_page_config(layout="centered")
st.set_option('deprecation.showPyplotGlobalUse', True)
st.title("MSO RFM Segmentation Dashboard")
option = st.selectbox("Select Plot", ("Default", "Show Density of Segments"))
if option == "Default":
    st.plotly_chart(fig_all, use_container_width=True)
elif option == "Show Density of Segments":
    st.plotly_chart(log_fig, use_container_width=True)

"""
Use the dropdown to see how dense each Segment is
"""
st.header("Number of Customers by Segment (Subscriber Vs Non Subscribers")
segment_counts = df.groupby(['Segment', 'subscriber']).size().reset_index(name='count')

plt.figure(figsize=(5, 3))
sns.barplot(x='Segment', y='count', hue='subscriber', data=segment_counts)
plt.xlabel('Segment')
plt.ylabel('Count')
st.pyplot(plt)

st.write(
"""
This Graph shows the number of customers in each segment. Ive also made some preliminary labels for each segment.  \n

0 = 'Low Value customers 21-22' \n
1 = 'low value customers Pre 2020' \n
2 = 'Low Value recent/Mid value past' \n
3 = 'Mid value customers' \n
4 = 'Low Reserve Purchasers' \n
5 = 'High revenue less frequent, recent' \n
6 = 'High reveuene, frequent, recent' \n

Given how few customers are in segments 5 and 6 i think that should merged into a single segment of High Value Subscribers.
There is also not alot of difference between segments 0 and 1 and could also be grouped together.
""")
