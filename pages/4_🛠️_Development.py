# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import numpy as np
from pandas.core.reshape.reshape import unstack

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Development', page_icon=':bar_chart:', layout='wide')
st.title('🛠️ Development')

st.write("")
st.write("")
st.write(
    """
    **Overview** 
    Growth and success in the blockchain industry are often measured by how quickly the ecosystem grows and how many 
    new features are added. Here you can see a snapshot of all the contracts that have been deployed and are actively 
    being used on the Terra blockchain. The provided charts show how the total number of current contracts and the 
    total number of newly deployed contracts have evolved over time.

    Adoption by users, or the number of people who start using a blockchain project, is also crucial to its development
    and expansion. The dashboard also tracks the number of new users and identifies the contracts/protocols through 
    which they are recruited by showing which contracts are most frequently used by new users.

    This dashboard also displays daily data on the most popular contracts according to the number of users and the
    number of transactions, further segmented by new and returning users.
    """
)
st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('Active Contracts, Daily & Total New Deployed Contracts Over Time')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Contracts':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/ffb41146-0e2c-4543-b72d-fad6a418fd22/data/latest'
        )


contracts = gat_data('Contracts')
df = contracts
fig = px.bar(df, x='DATE', y='Activ Contract Cnt')
fig.update_layout(title_text='Daily # of Active Contracts')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='New Contract Cnt')
fig.update_layout(title_text='Daily # of New Deployed Contracts')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y='Cumulative New Contract Cnt')
fig.update_layout(title_text='Total # of New Deployed Contracts Over Time')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y=['Activ Contract Cnt', 'New Contract Cnt'])
fig.update_layout(title_text='Daily # of Active vs. New Deployed Contracts')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)



st.write("")
st.write("")
st.write("")

st.subheader('Top 10 Deployed Contract by the Most Trafic')

st.write("")
st.write("")
@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Top T0 Contract':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/01bbafe0-3125-4b57-8726-156cc97756dd/data/latest'
        )

top10_contract = gat_data('Top T0 Contract')
df = top10_contract
c1, c2 = st.columns(2)
with c1:
    fig = px.bar(df, x='PROJECT_NAME', y=['TX_CNT', 'USR_CNT'])
    fig.update_layout(title_text='Daily # of Txs & Usres by Contracts')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.pie(df, values='TX_CNT', names='PROJECT_NAME', title='Total # & % of Txs by Contracts')
    fig.update_layout(legend_title='Contracts', legend_y=1)
    fig.update_traces(textinfo='value+percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write("")
st.write("")
st.write("")

st.subheader('Distribution of Deployed Contracts Type by User & Txs Count')

st.write("")
st.write("")
@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Contracts Type':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/45d815c2-3a2c-43cd-8720-75d49609d5c1/data/latest'
        )

contract_type = gat_data('Contracts Type')
df = contract_type
c1, c2 = st.columns(2)
with c1:
    fig = px.pie(df, values='TX_CNT', names='LABEL_TYPE', title='Distribution of Deployed Contracts Type by Txs Count')
    fig.update_layout(legend_title='Contracts Type', legend_y=1)
    fig.update_traces(textinfo='value+percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.pie(df, values='USR_CNT', names='LABEL_TYPE', title='Distribution of Deployed Contracts Type by User Count')
    fig.update_layout(legend_title='Contracts Type', legend_y=1)
    fig.update_traces(textinfo='value+percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    fig = px.bar(df, x='LABEL_TYPE', y=['TX_CNT'])
    fig.update_layout(title_text='Total # of Txs by Contracts Type')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.bar(df, x='LABEL_TYPE', y=['USR_CNT'])
    fig.update_layout(title_text='Total # of Users by Contracts Type')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)



