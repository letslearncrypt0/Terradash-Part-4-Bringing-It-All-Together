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
st.set_page_config(page_title='Supply', page_icon=':bar_chart:', layout='wide')
st.title('💰 Supply')

st.write("")
st.write("")
st.subheader('LUNA 2.0 Price')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Average Price':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/e2677d46-f41b-4301-9115-c3965f913e02/data/latest'
        )

price = gat_data('Average Price')
df = price
fig = px.area(df, x='DATE', y=['LUNA2.0 Price($)'])
fig.update_layout(title_text='Daily Average Price', showlegend=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write("")
st.write("")
st.write("")
st.write("")
st.subheader('Supply Metrics')

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'LUNA2.0 Circulating Supply':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/df220987-cdf7-46cc-9ccc-1018513b205f/data/latest'
        )


circulating_supply = gat_data('LUNA2.0 Circulating Supply')
df = circulating_supply
c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label='**Circulating Supply**', value=str(df['Circulating Supply'].map('{:,.0f}'.format).values[0]))

with c2:
    st.metric(label='**Circulating Supply/Total Supply(%)**', value=str(df['Circulating Supply/Total Supply'].map('{:,.2f}'.format).values[0]))

with c3:
    st.metric(label='**Total Supply**', value=str(df['Total Supply'].map('{:,.0f}'.format).values[0]))

st.write("")
st.write("")
st.write("")
st.write("")

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Circulating Supply Over Time':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/b90a6160-6419-42b9-8d09-e55ee26e9419/data/latest'
        )

circulating_supply_daily = gat_data('Circulating Supply Over Time')
df = circulating_supply_daily
fig = px.area(df, x='DATE', y='Circulating Supply')
fig.update_layout(title_text='Circulating Supply Over Time', showlegend=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.scatter(df, x='DATE', y='Circulating Supply/Total Supply(%)')
fig.update_layout(title_text='Percentage of Circulating Supply/Total Supply Ratio Over Time', showlegend=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")
st.write("")
st.write("")
st.subheader('Stablecoins Turnover')
st.write("")
st.write("")

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Stablecoins Turnover':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/29720342-f682-49cf-8f0b-7e6e86d1f03f/data/latest'
        )

Stablecoins_turnover = gat_data('Stablecoins Turnover')
df = Stablecoins_turnover
fig = px.bar(df, x='DATE', y=['Inflow Transfers', 'Outflow Transfers'])
fig.update_layout(title_text='Inflow/Outflow Transfer Txs Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['Inflowed Users', 'Outflowed Users'])
fig.update_layout(title_text='Inflow/Outflow Transferrer Coun')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['Inflowed Volume', 'Outflowed Volume'])
fig.update_layout(title_text='Inflow/Outflow Transferred Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='DATE', y=['Net Transfers', 'Netflow Users', 'Netflowed Volume'], log_y=True)
fig.update_layout(title_text='Net Inflow/Outflow Txs, Usres & Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)