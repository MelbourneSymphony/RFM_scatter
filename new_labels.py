import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/MelbourneSymphony/RFM_scatter/refs/heads/main/predictions_july_V3.csv')
custom_palette = ["#5a8eb8", "#5ab874", "#bf3636", "#f08922", "#8146d4", "#e3528e", "#2a9ac7"]
fig_all = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment',width=1600, height=800,color_continuous_scale=custom_palette)
log_fig = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment', log_x=False,log_y=True,log_z=True, width=1600, height=800,color_continuous_scale=custom_palette)

st.set_page_config(layout="centered")
st.title("MSO RFM Segmentation Dashboard")
option = st.selectbox("Use the dropdown to see how dense each segment is", ("Segments", "Show Density of Segments"))
if option == "Segments":
    st.markdown(''' This 3D scatter plot visualises the segments and where they fall in terms of the three measures of RFM
    - Last Updated 02/07/2025''')
    st.plotly_chart(fig_all, use_container_width=True)
elif option == "Show Density of Segments":
    st.markdown('''This plot expands the axis scale based on the size of the clusters, allowing us see that 'New Customers' and 'Slipping' are quite dense and are larger than the other clusters
    - Last Updated 02/07/2025''')
    st.plotly_chart(log_fig, use_container_width=True)

st.write("Segmentation Flows Click [here](https://mso-rfmflow.streamlit.app/)")
st.header("Segment Descriptions and Database Count")

segment_data = [
    {"Segment": "Slipping", "Description": "Customers who have not made a purchase within the last year", "Customer Count": 64386},
    {"Segment": "Lost Touch", "Description": "Customers who have not made a purchase in the last 3 years", "Customer Count": 14072},
    {"Segment": "New Customers", "Description": "Customers that have made a purchase in the last year", "Customer Count": 46881},
    {"Segment": "Faithful", "Description": "Customers who return often, but do not spend as much in each transaction compared to other segments", "Customer Count": 2339},
    {"Segment": "Affluent", "Description": "Customers who Purchase in higher reserves", "Customer Count": 2903},
    {"Segment": "Top Tier", "Description": "Top 5% total ticket spend", "Customer Count": 307}
]
seg_count = pd.DataFrame(segment_data)
seg_count.set_index(['Segment'],inplace=True)
st.markdown('''The below segments have been identified, applicable to customers with purchase history within the last five years.''')
st.table(seg_count)

