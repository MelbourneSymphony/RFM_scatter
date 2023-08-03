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


segment_counts = df['overall_score'].value_counts()
segment_counts_df = pd.DataFrame({'Segment': segment_counts.index, 'Number of Customers': segment_counts.values})
st.table(segment_counts_df)


st.write(
"""
This Graph shows the number of customers in each segment. Ive also made some preliminary labels for each segment.  \n

0 = 'Slipping - past customers who havent bought in awhile' \n
1 = 'Lost Touch - past customers who havent bought since 2020' \n
2 = 'Rookies - New Customers' \n
3 = 'Faithful - Customers who return often, but do not spend a lot' \n
4 = 'Loyal Purchasers - purchase most often' \n
5 = 'Affluent - Customers who are willing to pay a premium' \n
6 = 'S Tier - Highest paying' \n

""")
