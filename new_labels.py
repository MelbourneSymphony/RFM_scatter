import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/Melsuser5/RFM_labels/main/rfm_data_clean_segments.csv')
custom_palette = ["#5a8eb8", "#5ab874", "#bf3636", "#f08922", "#8146d4", "#e3528e", "#2a9ac7"]
fig_all = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment',width=1600, height=800,color_continuous_scale=custom_palette)
log_fig = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment', log_x=False,log_y=True,log_z=True, width=1600, height=800,color_continuous_scale=custom_palette)

st.set_page_config(layout="centered")
st.set_option('deprecation.showPyplotGlobalUse', True)
st.title("MSO RFM Segmentation Dashboard")
option = st.selectbox("Use the dropdown to see how dense each segment is", ("Segments", "Show Density of Segments"))
if option == "Segments":
    st.plotly_chart(fig_all, use_container_width=True)
elif option == "Show Density of Segments":
    st.plotly_chart(log_fig, use_container_width=True)

st.header("Number of Customers by Segment (Subscriber Vs Non Subscribers")
segment_counts = df.groupby(['Segment', 'subscriber']).size().reset_index(name='count')

plt.figure(figsize=(5, 3))
sns.barplot(x='Segment', y='count', hue='subscriber', data=segment_counts)
plt.xlabel('Segment')
plt.ylabel('Count')
st.pyplot(plt)


segment_data = [
    {"Segment": "0 – Slipping", "Description": "Customers who have not purchased within the last year", "Customer Count": 45800},
    {"Segment": "1 - Lost Touch", "Description": "Customers who have not purchased since 2020", "Customer Count": 34126},
    {"Segment": "2 - New Customers", "Description": "Customers that have made at least one purchase in the last year", "Customer Count": 18174},
    {"Segment": "3 - Faithful", "Description": "Customers who return often, but do not spend as much in each transaction compared to other segments (average of $118)", "Customer Count": 2951},
    {"Segment": "4 - Loyal Purchasers", "Description": "Purchase most often compared to other segments (top 5% frequency)", "Customer Count": 1013},
    {"Segment": "5 - Affluent", "Description": "Customers who spend over $1,200 per transaction", "Customer Count": 563},
    {"Segment": "6 - 'Top Tier’", "Description": "Top 5% total ticket spend", "Customer Count": 274}
]
seg_count = pd.DataFrame(segment_data)
seg_count.set_index(['Segment'])

st.write(seg_count)
