# Libraries
import streamlit as st

# [theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

# Layout
st.set_page_config(page_title='Definitions & Data Transparency', page_icon=':bar_chart:', layout='wide')
st.write("### 📜 Definitions & Data Transparency")

st.write("")
st.write("")
st.write("")
st.write("")

st.write(
    """
    The main data source is [**Flipside Crypto**](https://flipsidecrypto.xyz/). They offer free access to blockchain 
    data across a variety of different blockchains. 
    The SQL queries to extract the data to display are written by me and are automatically updated every
    24 hours. They all are open-sourced and feel free to reach out if you need access to anything in
    particular. 
    """
)
st.write(
    """
    #### How are daily transactions counted?    
    To calculate daily transactions on Terra LUNA2.0 (as well as other chains transactions), 
    all transactions that interact with on protocols are included. 

    The users that have had as the first transactions called as **New Users**.
    All addresses that execute a transaction interacting on Terra LUNA2.0s' ecosystem
    for the first time have been counted as **New Users** number.

    #### Popularity assessed by:
    The volume of active users on Terra Luna2.0 per day 
    The adoption by new users per day

    #### How is the users growth(Cumulative) calculated?    
    On a given day, all addresses that execute a transaction interacting for the first time have been counted 
    towards the daily New Users number. 
    The cumulative curve is simply a progressive sum of the new daily users.  

    #### Performance assessed by:
    The success rate of transactions in the Optimism
    The average STPM(Succeed Transactions per Minute) per week
    The average FTR(Failed Transactions Rate) per week
    The average transactions fee($)
    
    #### Circulating Supply
    The amount of coins that are circulating in the market and are tradeable by the public. 
    It is comparable to looking at shares readily available in the market (not held & locked by insiders, governments).
    
    #### Total Supply
    The amount of coins that have already been created, minus any coins that have been burned (removed from circulation).
    It is comparable to outstanding shares in the stock market.
    Total Supply = Onchain supply - burned tokens [1](https://www.coingecko.com/en/coins/terra)
    """

)

st.write("")
st.write("")
st.write("")
st.write("")

st.subheader('Queries')
st.write(
    """
    1. https://app.flipsidecrypto.com/velocity/queries/6eefb37b-f12f-4854-ad3a-bcd9801db701
    2. https://app.flipsidecrypto.com/velocity/queries/e791b70e-5aba-4e15-a9e2-35dcf3d1b73e
    3. https://app.flipsidecrypto.com/velocity/queries/b90a6160-6419-42b9-8d09-e55ee26e9419
    4. https://app.flipsidecrypto.com/velocity/queries/341befa4-ba82-4401-b4da-bd260aa0ff63
    5. https://app.flipsidecrypto.com/velocity/queries/2d41a639-f86a-4d9c-8d74-e3c577fe03ff
    6. https://app.flipsidecrypto.com/velocity/queries/70f60d13-78f5-4fc8-a852-70f3dc5686fa
    7. https://app.flipsidecrypto.com/velocity/queries/ffb41146-0e2c-4543-b72d-fad6a418fd22
    8. https://app.flipsidecrypto.com/velocity/queries/19de1452-a2b8-4ca5-8879-eafee8c6950c
    9. https://app.flipsidecrypto.com/velocity/queries/645b5810-23c2-4112-9774-3d1d5ff6ebc5
    10. https://app.flipsidecrypto.com/velocity/queries/1ef97301-22b8-4c05-8402-a204a68422f7
    11. https://app.flipsidecrypto.com/velocity/queries/7c48c10b-c85d-4859-8f51-ec00e6619977
    12. https://app.flipsidecrypto.com/velocity/queries/cac46f57-ba7c-416c-8dbc-c75aa06997fa
    13. https://app.flipsidecrypto.com/velocity/queries/e0f9f695-ec58-4714-a476-21ae7cf78562
    14. https://app.flipsidecrypto.com/velocity/queries/8cb48ee7-6b78-4444-a943-120a2c0aa28e
    15. https://app.flipsidecrypto.com/velocity/queries/6eefb37b-f12f-4854-ad3a-bcd9801db701
    """
)

st.write("")
st.write("")
st.write("")
st.write("")

fig = st.write(
    """
                     ### Made with :red[❤] & Honor
    """
)