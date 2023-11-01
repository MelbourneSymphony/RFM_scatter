import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/Melsuser5/RFM_labels/main/23_q4_cleaned.csv')
custom_palette = ["#5a8eb8", "#5ab874", "#bf3636", "#f08922", "#8146d4", "#e3528e", "#2a9ac7"]
fig_all = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment',width=1600, height=800,color_continuous_scale=custom_palette)
log_fig = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment', log_x=False,log_y=True,log_z=True, width=1600, height=800,color_continuous_scale=custom_palette)

st.set_page_config(layout="centered")
st.set_option('deprecation.showPyplotGlobalUse', True)
st.title("MSO RFM Segmentation Dashboard")
option = st.selectbox("Use the dropdown to see how dense each segment is", ("Segments", "Show Density of Segments"))
if option == "Segments":
    st.markdown(''' This 3D scatter plot visualises the segments and where they fall in terms of the three measures of RFM''')
    st.plotly_chart(fig_all, use_container_width=True)
elif option == "Show Density of Segments":
    st.markdown('''This plot expands the axis scale based on the size of the clusters, allowing us see that clusters 0 and 1 are quite dense and are larger than the other clusters''')
    st.plotly_chart(log_fig, use_container_width=True)

st.header("Segment Descriptions and Database Count")

segment_data = [
    {"Segment": "0 – Slipping", "Description": "Customers who have not purchased within the last year", "Customer Count": 31020},
    {"Segment": "1 - Lost Touch", "Description": "Customers who have not purchased since 2020", "Customer Count": 336456},
    {"Segment": "2 - New Customers", "Description": "Customers that have made at least one purchase in the last year", "Customer Count": 46943},
    {"Segment": "3 - Faithful", "Description": "Customers who return often, but do not spend as much in each transaction compared to other segments (average of $118)", "Customer Count": 3077},
    {"Segment": "4 - Loyal Purchasers", "Description": "Purchase most often compared to other segments (top 5% frequency)", "Customer Count": 436},
    {"Segment": "5 - Affluent", "Description": "Customers who spend over $1,200 per transaction", "Customer Count": 1176},
    {"Segment": "6 - 'Top Tier’", "Description": "Top 5% total ticket spend", "Customer Count": 407}
]
seg_count = pd.DataFrame(segment_data)
seg_count.set_index(['Segment'],inplace=True)
st.markdown('''The below segments have been identified, applicable to customers with purchase history within the last five years.''')
st.table(seg_count)

st.header("Number of Subscribers vs Non Subscribers in each Segment")
segment_counts = df.groupby(['Segment', 'subscriber']).size().reset_index(name='count')
plt.figure(figsize=(5, 3))
sns.barplot(x='Segment', y='count', hue='subscriber', data=segment_counts)
plt.xlabel('Segment')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot(plt)
