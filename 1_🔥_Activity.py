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
st.set_page_config(page_title='Activiy', page_icon=':bar_chart:', layout='wide')
st.title('🔥 Activity')

st.write("")
st.write("")
st.subheader('Network Performance Overall View')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Network Performance Overall View':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/5ded7578-a189-4cf3-a365-8c4666c88e49/data/latest'
        )


network_performance = gat_data('Network Performance Overall View')
df = network_performance
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(label='**Total Blocks**', value=str(df['Total # of Blocks'].map('{:,.0f}'.format).values[0]))

with c2:
    st.metric(label='**Blocks/Minute**', value=str(df['Blocks/Minute'].map('{:,.0f}'.format).values[0]))

with c3:
    st.metric(label='**Total # of Transactions**',
              value=str(df['Total # of Transactions'].map('{:,.0f}'.format).values[0]))

with c4:
    st.metric(label='**Transactions/Block**', value=str(df['Transactions/Block'].map('{:,.0f}'.format).values[0]))

c1, c2 = st.columns(2)
with c1:
    st.metric(label='**Transactions/Second(TPS)**', value=str(df['Transactions/Second'].map('{:,.2f}'.format).values[0]))

with c2:
    st.metric(label='**Average Block Height**', value=str(df['Average Block Height'].map('{:,.0f}'.format).values[0]))

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(label='**Total # of Users**', value=str(df['Total # of Users'].map('{:,.0f}'.format).values[0]))

with c2:
    st.metric(label='**Users/Day**', value=str(df['Users/Day'].map('{:,.0f}'.format).values[0]))

with c3:
    st.metric(label='**Total Transactions Fee($)**',
              value=str(df['Total Transactions Fee($)'].map('{:,.0f}'.format).values[0]))

with c4:
    st.metric(label='**Average Transaction Fees($)**',
                        value=str(df['Average Transaction Fees($)'].map('{:,.2f}'.format).values[0]))

st.write("")
st.write("")
st.write("")
st.write("")
st.subheader('Transaction Overall View')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Transaction Overall View':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/8cb48ee7-6b78-4444-a943-120a2c0aa28e/data/latest'
        )


transaction = gat_data('Transaction Overall View')
df = transaction
fig = px.bar(df, x='DATE', y=['Tx Count', 'User Count'])
fig.update_layout(title_text='Transaction & User Traffic per day')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['Succeed Tx Count', 'Failed Tx Count'])
fig.update_layout(title_text='Daily # of Succeed vs. Failed Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)
with c1:
    fig = px.bar(df, x='DATE', y=['Transactions Fee($)'])
    fig.update_layout(title_text='Daily Transaction Fess Volume($)', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.bar(df, x='DATE', y=['Transactions Fee(LUNA)'])
    fig.update_layout(title_text='Daily Transaction Fess Volume(LUNA2.0)', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    fig = px.area(df, x='DATE', y=['Cumulative Transactions Fee($)'])
    fig.update_layout(title_text='Cumulative Transactions Fee Volume($)', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.area(df, x='DATE', y=['Cumulative Transactions Fee(LUNA)'])
    fig.update_layout(title_text='Cumulative Transactions Fee Volume(LUNA2.0)', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y=['Success Rate', 'Failed Rate'])
fig.update_layout(title_text='Daily Rate of Success vs. Fail Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='DATE', y=['MA7-D Tx Count', 'MA15-D Tx Count', 'MA30-D Tx Count'])
fig.update_layout(title_text='Tx Count Moving Averages')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='DATE', y=['MA7-D User Count', 'MA15-D User Count', 'MA30-D User Count'])
fig.update_layout(title_text='User Count Moving Averages')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='DATE', y=['MA7-D Transactions Fee($)', 'MA15-D Transactions Fee($)', 'MA30-D Transactions Fee($)'])
fig.update_layout(title_text='Transactions Fee($) Moving Averages')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'whales Behaviour':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/e791b70e-5aba-4e15-a9e2-35dcf3d1b73e/data/latest'
        )


st.subheader('Specific whales Behaviour analysis')

whales_behaviour = gat_data('whales Behaviour')
df = whales_behaviour
fig = px.bar(df, x='DATE', y=['Whales Selling Cnt', 'Whales Buying Cnt'])
fig.update_layout(title_text='Whales Behaviour by day')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='DATE', y=['Tx Count','Volume Moved', 'Net Whales Behavior'], log_y=True)
fig.update_layout(title_text='Transaction, NET Behaving & Moved Volume per day')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Activity per Platform':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/7c48c10b-c85d-4859-8f51-ec00e6619977/data/latest'
        )


st.subheader('Activity per Platform')

activity_per_platform = gat_data('Activity per Platform')
df = activity_per_platform
fig = px.bar(df, x='DATE', y=['Tx Count'], color='LABEL', log_y=True)
fig.update_layout(title_text='Tx Count per Platform by Week(Log Scale)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['User Count'], color='LABEL', log_y=True)
fig.update_layout(title_text='User Count per Platform by Week(Log Scale)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['VOLUME'], color='LABEL', log_y=True)
fig.update_layout(title_text='VOLUME(LUNA2.0) per Platform by Week(Log Scale)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='DATE', y=['Cumulative Tx Count'], color='LABEL', log_y=True)
fig.update_layout(title_text='Cumulative Tx Count per Platform by Week(Log Scale)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='DATE', y=['CUM_VOLUME'], color='LABEL', log_y=True)
fig.update_layout(title_text='Cumulative VOLUME(LUNA2.0) per Platform by Week(Log Scale)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.subheader('New Users Over Time')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'New Users':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/6eefb37b-f12f-4854-ad3a-bcd9801db701/data/latest'
        )


new_users = gat_data('New Users')
df = new_users
fig = px.bar(df, x='DATE', y=['ACTIVE_USERS', 'NEW_USERS'])
fig.update_layout(title_text='Active & New User per day')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='DATE', y=['CUM_NEW_USERS', 'ACTIVE_USERS', 'AVG_TX_PER_USER'], log_y=True)
fig.update_layout(title_text='Cumulative New User vs. Average Tx per Users by day')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(
         """
***Note:***
The dot graphs below by color assigned has been used for each individual dot over the past two months. 
The values of the related measurements are shown in the dot graphs, with the hours of the day and days of the 
week indicated by their positions along the **x-** and **y-axes**, respectively.
In the dot plots, when the  dot’s color become darker the rate went up and vice versa.
         """
         )


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Success transactions per Minute & Failed Rate':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/341befa4-ba82-4401-b4da-bd260aa0ff63/data/latest'
        )


transaction_heatmap = gat_data('Success transactions per Minute & Failed Rate')
df = transaction_heatmap
c1, c2 = st.columns(2)
with c1:
    fig = px.scatter(df, x='HOUR_OF_DAY', y='DAY_OF_WEEK', color='STPM',
                                 title='Success transactions per minute on hour of day (UTC)')
    fig.update_layout(legend_title=None, xaxis_title='Hour', yaxis_title='Days of Week',
                          coloraxis_colorbar=dict(title='STPM'))
    fig.update_xaxes(categoryorder='category ascending')
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.scatter(df, x='HOUR_OF_DAY', y='DAY_OF_WEEK', color='TFR',
                                 title='Transactions fail rate on hours of day(UTC)')
    fig.update_layout(legend_title=None, xaxis_title='Hour', yaxis_title=None, coloraxis_colorbar=dict(title='TFR'))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Success Tx/Minute & Failed Rate in Total':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/1a8b0b5b-b41f-43f2-af96-a9eb445edaa1/data/latest'
        )


success_fail_tx_rate = gat_data('Success Tx/Minute & Failed Rate in Total')
df = success_fail_tx_rate
c1, c2 = st.columns(2)
with c1:
    st.metric(label='**Success Tx/Minute**', value=str(df['Succeed Tx/Minute'].map('{:,.2f}'.format).values[0]))

with c2:
    st.metric(label='**Failed Transaction Rate(%)**', value=str(df['Failed Rate'].map('{:,.2f}'.format).values[0]))


