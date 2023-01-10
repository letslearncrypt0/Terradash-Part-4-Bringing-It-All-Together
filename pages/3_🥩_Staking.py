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
st.set_page_config(page_title='Staking', page_icon=':bar_chart:', layout='wide')
st.title('🥩 Staking')

st.write(
    """
    By assigning their LUNA to a validator, LUNA owners can participate in the network and collect incentives.
    The return from staking Luna is figured using the incentives and bonuses earned by validators for their work 
    in mining blocks. As soon as a block is mined, all validators get a proportional share of the reward 
    (based on the number of LUNA staked in their pool, which represents their voting power). 
    After the validator's fee is subtracted from the reward, the remaining funds will be divided among the delegators 
    in proportion to their stake (including the validator).

    What follows is a discussion of the staking behaviors of Terra players. Delegation, redelegation, and undelegation 
    are the three possible user interactions in staking.

    The following visual details the total daily volume, average daily number, and total daily number of 
    wallets participating in all staking actions.
    """
)
st.write("")
st.subheader('Staking Overall View')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Staking in Total':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/11ca3c8d-e786-4378-aa71-77fb321090bc/data/latest'
        )

staking_total = gat_data('Staking in Total')
df = staking_total
c1, c2 = st.columns(2)
with c1:
    fig = px.pie(df, values='Delegation Tx Count', names='ACTION', title='Total Value & Share of Staking Txs')
    fig.update_layout(legend_title='Staking Txs', legend_y=1)
    fig.update_traces(textinfo='value+percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.pie(df, values='Staked Volume', names='ACTION', title='Total Value & Share of Staking Volume')
    fig.update_layout(legend_title='Staking Volume', legend_y=1)
    fig.update_traces(textinfo='value+percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    fig = px.pie(df, values='Delegators', names='ACTION', title='Total Value & Share of Delegator Count')
    fig.update_layout(legend_title='Delegator', legend_y=1)
    fig.update_traces(textinfo='value+percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.pie(df, values='Validators', names='ACTION', title='Total Value & Share of Validator Count')
    fig.update_layout(legend_title='Validators', legend_y=1)
    fig.update_traces(textinfo='value+percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('Staking Metrics Over Time')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Staking Metrics':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/2d41a639-f86a-4d9c-8d74-e3c577fe03ff/data/latest'
        )


stakin_over_time = gat_data('Staking Metrics')
df = stakin_over_time
fig = px.bar(df, x='DATE', y='Tx Count', color='ACTION')
fig.update_layout(title_text='Daily Tx Count per Action')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Delegators', color='ACTION')
fig.update_layout(title_text='Daily Delegators Count per Action')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Validators', color='ACTION')
fig.update_layout(title_text='Daily Validators Count per Action')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Volume(LUNA2.0)', color='ACTION')
fig.update_layout(title_text='Daily Volume(LUNA2.0) per Action')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Volume($)', color='ACTION')
fig.update_layout(title_text='Daily Volume($) per Action')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Net Staked Volume(LUNA2.0)', color='ACTION')
fig.update_layout(title_text='Daily Net Staked Volume(LUNA2.0) per Action')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y='Net Staked Volume($)', color='ACTION')
fig.update_layout(title_text='Daily Net Staked Volume($) per Action')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('New Users as Delegator')


@st.cache(ttl=10000)
def gat_data(query):
    if query == 'New Users':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/70f60d13-78f5-4fc8-a852-70f3dc5686fa/data/latest'
        )


new_users_over_time = gat_data('New Users')
df = new_users_over_time
fig = px.bar(df, x='DATE', y='New Delegators')
fig.update_layout(title_text='Daily New Delegators')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('Staking Metrics in Cumulative State')
st.write("")
st.write("")

stakin_over_time = gat_data('Staking Metrics')
df = stakin_over_time
c1, c2 = st.columns(2)
with c1:
    fig = px.area(df, x='DATE', y='Cumulative Staked Volume(LUNA2.0)', color='ACTION')
    fig.update_layout(title_text='Cumulative Staked Volume(LUNA2.0)')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.area(df, x='DATE', y='Cumulative Staked Volume($)', color='ACTION')
    fig.update_layout(title_text='Cumulative Staked Volume($)')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    fig = px.area(df, x='DATE', y='Cumulative Net Staked Volume(LUNA2.0)')
    fig.update_layout(title_text='Cumulative Net Staked Volume(LUNA2.0)', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.area(df, x='DATE', y='Cumulative Net Staked Volume($)')
    fig.update_layout(title_text='Cumulative Net Staked Volume($)', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    fig = px.area(df, x='DATE', y='Cumulative Delegation Tx Count', color='ACTION')
    fig.update_layout(title_text='Cumulative Delegation Tx Count')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

new_users_over_time = gat_data('New Users')
df = new_users_over_time
with c2:
    fig = px.area(df, x='DATE', y='Cumulative New Delegators')
    fig.update_layout(title_text='Cumulative New Delegators', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('Staking Reward')

st.write("")
st.write("")

@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Reward':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/e0f9f695-ec58-4714-a476-21ae7cf78562/data/latest'
        )


reward = gat_data('Reward')
df = reward
fig = px.bar(df, x='DATE', y='Reciver Count')
fig.update_layout(title_text='Daily Staking Reciver Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='DATE', y=['Reward Volume(LUNA2.0)', 'Reward Volume($)'])
fig.update_layout(title_text='Daily Staking Reciver Volume(in LUNA2.0 & $)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='DATE', y=['Cumulatove Reward Volume(LUNA2.0)', 'Cumulatove Reward Volume($)'])
fig.update_layout(title_text='Cumulative Staking Reciver Volume(in LUNA2.0 & $)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('Top 10 Delegator & Validators by the Most Net Staking Volume(LUNA2.0)')

st.write("")
st.write("")
@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Top T0 Delegators':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/cac46f57-ba7c-416c-8dbc-c75aa06997fa/data/latest'
        )
    elif query == 'Top T0 Validators':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/19de1452-a2b8-4ca5-8879-eafee8c6950c/data/latest'
        )

top10_delegators = gat_data('Top T0 Delegators')
df = top10_delegators
c1, c2 = st.columns(2)
with c1:
    fig = px.pie(df, values='Net Staked Volume', names='Delegators', title='Top T0 Delegators Address')
    fig.update_traces(textinfo='value+percent', textposition='inside', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

top10_validators = gat_data('Top T0 Validators')
df = top10_validators
with c2:
    fig = px.pie(df, values='Net Staked Volume', names='Validators', title='Top T0 Validators Address')
    fig.update_traces(textinfo='value+percent', textposition='inside', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('Top 10 Delegator by the Most Reward Volume($) & Distribution of Reward Recivers')

st.write("")
st.write("")
@st.cache(ttl=10000)
def gat_data(query):
    if query == 'Top T0 Reward Recivers':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/1ef97301-22b8-4c05-8402-a204a68422f7/data/latest'
        )
    elif query == 'Distribution of Reward Recivers':
        return pd.read_json(
            'https://node-api.flipsidecrypto.com/api/v2/queries/645b5810-23c2-4112-9774-3d1d5ff6ebc5/data/latest'
        )

top10_reciver = gat_data('Top T0 Reward Recivers')
df = top10_reciver
c1, c2 = st.columns(2)
with c1:
    fig = px.pie(df, values='Reward Volume($)', names='Reciver', title='Top T0 Reward Recivers Address')
    fig.update_traces(textinfo='value+percent', textposition='inside', showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

distribution = gat_data('Distribution of Reward Recivers')
df = distribution
with c2:
    fig = px.pie(df, values='Reciver Count', names='DITRIBUTION', title='Distribution of Rewards Reciver')
    fig.update_traces(textinfo='value+percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)




