import plotly.express as px
import streamlit as st
import streamlit_antd_components as sac
import pandas as pd
from plotly.subplots import make_subplots
from millify import millify

# Styling of metric container
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #424b43;
   border: 3px solid #111212;
   padding: 5% 5% 5% 10%;
   border-radius: 10px;
   color: white;
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: #B7e493;
}
</style>
""", unsafe_allow_html=True)

# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide"
#     # initial_sidebar_state="expanded"
#     # }
# )

with st.sidebar:
  st.header("Navigation:")
  st.markdown("""
  - [Introduction](#wsj-s-crypto-terrorism-claims-under-scrutiny-after-on-chain-analysis)
  - [Sam's Findings Using Flipsidecrypto Data](#sam-s-findings-using-flipsidecrypto-data)
    - [Elliptic's Methdology](#elliptic-s-methdology)
    - [BitOK's Methodology](#bitok-s-methdology)
  - [THE REALITY](#the-reality)
    - [Crypto Aid Israel](#crypto-aid-israel)
    - [UkraineDAO](#ukrainedao)
    - [Top High Impact Crypto Based Humanitarian Projects](#top-high-impact-crypto-based-humanitarian-projects)
  - [CONCLUSION](#conclusion)
  """)

st.markdown(f'<h1 style="background-image:url(https://imageio.forbes.com/specials-images/imageserve/5f6e5a2d793c5299630c7bf3/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds);font-weight:bold;font-family:Georgia;font-size:40px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"Exploring the Positive Impacts of Crypto: Debunking WSJs Crypto-Terrorism Claims"}</h1>', unsafe_allow_html=True)

# st.image("https://static.timesofisrael.com/www/uploads/2023/07/hamas.jpg", width=1000, use_column_width=False)


#   sellected = sac.menu([
#       sac.MenuItem('home', icon='house-fill'),
#       sac.MenuItem('products', icon='box-fill', children=[
#           sac.MenuItem('apple', icon='apple', tag=sac.Tag('USA', color='green', bordered=False)),
#           sac.MenuItem('other', icon='git', children=[
#               sac.MenuItem('google', icon='google'),
#               sac.MenuItem('gitlab', icon='gitlab'),
#               sac.MenuItem('wechat' * 5, icon='wechat'),
#           ]),
#       ]),
#       sac.MenuItem('disabled', icon='send', disabled=True),
#       sac.MenuItem(type='divider'),
#       sac.MenuItem('reference', type='group', children=[
#           sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
#           sac.MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),
#       ]),
#   ], format_func='title', open_all=True)

# if sellected == "home":
# else:
# st.write("settings is my bettings")




st.markdown("""
###  **:red[WSJ's Crypto-Terrorism Claims Under Scrutiny After On-Chain Analysis]**

The Wall Street Journal (WSJ) recently published a series of articles and an [op-ed by Senator Elizabeth Warren](https://www.wsj.com/articles/cryptocurrency-feeds-hamass-terrorism-e0db54f5), alleging that Hamas and other militant groups have raised over $130 million in cryptocurrency since 2021 to fund their attacks on Israel. The WSJ cited data from [Elliptic](https://www.elliptic.co/blog/analysis/israel-orders-seizure-of-crypto-wallets-worth-94-million-linked-to-palestinian-islamic-jihad), a blockchain analytics firm, and [BitOK](https://twitter.com/BitOK_org/status/1717245964061127042) as the main sources of its reporting. However, a closer examination of the on-chain data by independent researchers has cast doubt on the accuracy and validity of the WSJ's claims.
""")

st.markdown("""
### :red[Sam's Findings Using Flipsidecrypto Data]
""")


st.markdown("""
Sam, a data analyst and crypto enthusiast, used [Flipside Crypto](flipsidecrypto.xyz), a platform that allows anyone to access and analyze blockchain data, to verify the findings of Elliptic and BitOK. Check out his [dashboard](https://flipsidecrypto.xyz/sam/verifying-elliptic-bitok-claims-VpBJs2) providing details of his findings and the process involved.
""")

st.markdown("""
#### :blue[Elliptic's Methdology]
""")

st.markdown("""
Sam found that Elliptic's methodology was flawed and resulted in significant overestimation of the amounts and volumes of crypto transactions linked to Hamas and its affiliates. For example, Elliptic claimed that the wallets associated with Hamas received 93 million USD in crypto between August 2021 and June 2023, but Sam's analysis showed that the actual amount was about $83 million, excluding transfers among the same wallets.
""")

urla = "https://api.flipsidecrypto.com/api/v2/queries/74d6eac1-e07f-49a3-b953-24706071b99a/data/latest"
dfa = pd.read_json(urla)

subfig = make_subplots(specs=[[{"secondary_y": True}]])

# create two independent figures with px.line each containing data from multiple columns
fig = px.line(dfa, x="MONTH", y=["MONTHLY_USD"])
fig2 = px.line(x=dfa['MONTH'], y=dfa['CUMULATIVE_USD'])
# name="CUMUL_NETFLOW", line_color="yellow")

fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Timespan"
subfig.layout.yaxis.title="User Count"
# subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="CUMUL_USD"
subfig.update_layout(hovermode="x unified", title="Monthly and cumulative USD received from addresses in ASO 34/23", height=400)
# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
st.plotly_chart(subfig, use_container_width=True)

# figa = px.bar(dfa, x="MONTH", y="MONTHLY_USD", title="Monthly and cumulative USD received from addresses in ASO 34/23", height=500)
# figa.update_layout(hovermode="x unified")
# figa.add_scatter(x=dfa['MONTH'], y=dfa['CUMULATIVE_USD'], name="CUMULATIVE_USD", line_color="yellow", secondary_y=True)
# st.plotly_chart(figa, use_container_width=True)

st.markdown("""
Similarly, Elliptic reported a peak transaction count of over 30,000 in May 2022, while Sam's analysis revealed that the highest number of transactions was around 4,000 in January 2033.
""")

st.image("https://www.elliptic.co/hs-fs/hubfs/Newterrorist.png?width=2342&height=1326&name=Newterrorist.png")

subfig = make_subplots(specs=[[{"secondary_y": True}]])

# create two independent figures with px.line each containing data from multiple columns
fig = px.line(dfa, x="MONTH", y=["MONTHLY_USD"])
fig2 = px.line(x=dfa['MONTH'], y=dfa['TRANSACTIONS_COUNT'])
# name="CUMUL_NETFLOW", line_color="yellow")

fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Timespan"
subfig.layout.yaxis.title="User Count"
# subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="Transaction Count"
subfig.update_layout(hovermode="x unified", title="Monthly USD & transfers count", height=400)
# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
st.plotly_chart(subfig, use_container_width=True)


st.markdown("""
#### :blue[BitOK's Methdology]
""")


st.markdown("""
Sam also compared the data from BitOK about seizure orders ASO 15/22 and ASO 19/23, which claimed to have identified $35.3 million worth of transfers into the wallets on a [twitter post](https://twitter.com/BitOK_org/status/1717245964061127042) and 5.6 million USD associated with each case. Sam found that BitOK's data was more accurate than Elliptic's, but still had some minor discrepancies. For instance, Sam's analysis showed that the total amount transferred into the wallets ASO 15/22 was 33.6 million USD, slightly lower than BitOK's figure. Sam attributed these differences to BitOK's lack of clarity on the exact tokens considered in their analysis.
""")

cola, colb = st.columns(2, gap='large')

with cola:
  urlb = "https://api.flipsidecrypto.com/api/v2/queries/a7cf4aa2-0f04-49c0-81f0-6c8f53772617/data/latest"
  dfb = pd.read_json(urlb)

  st.metric(label="ASO 15/22", value=(millify(dfb["TOTAL_USD"][1], precision=2)))

with colb:
  urlb = "https://api.flipsidecrypto.com/api/v2/queries/74e4e927-cca2-437a-8ac5-1449fa10ab0c/data/latest"
  dfb = pd.read_json(urlb)

  st.metric(label="ASO 15/22", value=(millify(dfb["TOTAL_USD"][1], precision=2)))

st.markdown("""
Sam's analysis demonstrates the importance of verifying the data and methodology used by blockchain analytics firms before drawing conclusions and making policy recommendations based on them. The WSJ's reporting and Senator Warren's letter relied heavily on Elliptic's data, which was shown to be inaccurate and misleading by Sam's analysis. The WSJ has not updated or retracted its articles despite the evidence presented by Sam and other researchers. Senator Warren has also not acknowledged or addressed the flaws in her letter, which called for more regulation and oversight of the crypto industry based on her claim that crypto feeds Hamas's terrorism.
""")

st.markdown("""
## :red[THE REALITY]
""")

st.markdown("""
However, not all crypto transactions are related to terrorism or illicit activities. In fact, crypto can also be used for good causes and humanitarian projects. 
""")

st.markdown("""
#### :blue[Crypto Aid Israel]
""")


st.markdown("""
For example, Crypto Aid Israel is a fund raising campaign that has raised over $84,900 in crypto assets as of today for supporting Israel in the ongoing war. Crypto Aid Israel accepts donations in various cryptocurrencies such as Bitcoin, Ethereum, USDT, USDC, DAI, BNB, XRP, LTC, BCH and DOGE. Crypto Aid Israel is an example of how crypto can be used for positive social impact and solidarity.
""")

urlc = "https://api.flipsidecrypto.com/api/v2/queries/906c37ca-36d1-4d1c-b777-3373b8a1232f/data/latest"
dfc = pd.read_json(urlc)

subfig = make_subplots(specs=[[{"secondary_y": True}]])

# create two independent figures with px.line each containing data from multiple columns
fig = px.line(dfc, x="TIMESPAN", y=["VOLUME"])
fig2 = px.line(x=dfc['TIMESPAN'], y=dfc['CUMUL_VOLUME'])
# name="CUMUL_NETFLOW", line_color="yellow")

fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Timespan"
subfig.layout.yaxis.title="Volume"
# subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="CUMUL_VOLUME"
subfig.update_layout(hovermode="x unified", title="Crypto Aid Israel Donations Till Date.", height=400)
# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
st.plotly_chart(subfig, use_container_width=True)

st.markdown("""
#### :blue[UkraineDAO]
""")


st.markdown("""
Another example is the Ukraine government and organizations supporting its fight against a Russia invasion. An article published by [Forbes](https://www.forbes.com/sites/jonathanponciano/2022/03/02/crypto-donations-to-ukraine-top-52-million-as-funds-pour-in-from-bitcoin-ether-polkadot-and-nfts/?sh=6a34bdd774e5) wrote that Ukraine have amassed more than 52 million USD in cryptocurrency donations—and already deployed at least 14 million USD—amid an influx of support as the country starts accepting a wider array of tokens and digital assets. The donations include proceeds from the sale of one of the most expensive non-fungible tokens (NFTs) in history. The NFT was created by Beeple, a digital artist who sold his artwork "Everydays: The First 5000 Days" for 69 million USD in March 2022. Beeple donated $5 million worth of Ether from his sale to Ukraine. The Ukraine government and organizations have also received donations in Bitcoin, Polkadot, Cardano and other cryptocurrencies. These donations show how crypto can be used to support democracy and freedom.

Below is on-chain representation of the timeseries and cumulative amount that has been generated over time.
""")

urld = "https://api.flipsidecrypto.com/api/v2/queries/a15233ff-b518-4813-a2ee-33e4293f6b95/data/latest"
dfd = pd.read_json(urld)

subfig = make_subplots(specs=[[{"secondary_y": True}]])

# create two independent figures with px.line each containing data from multiple columns
fig = px.line(dfd, x="TIMESPAN", y=["VOLUME"])
fig2 = px.line(x=dfd['TIMESPAN'], y=dfd['CUMUL_VOLUME'])
# name="CUMUL_NETFLOW", line_color="yellow")

fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Timespan"
subfig.layout.yaxis.title="Volume"
# subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="CUMUL_VOLUME"
subfig.update_layout(hovermode="x unified", title="Ukraine Support Donations.", height=400)
# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
st.plotly_chart(subfig, use_container_width=True)

st.write(":red[NOTE:] On-chain data presented above only tracks Ethereum based tokens and Bitcoin.")

st.markdown("""
#### :blue[Top High Impact Crypto Based Humanitarian Projects]
""")

st.markdown("""
Amidst all this saga, I think it is important to highlight the positive impact that crypto can have on the world, especially in times of crisis and conflict. Crypto can enable people to donate and receive funds in a fast, secure, and transparent way, without intermediaries or censorship. Crypto can also empower communities and individuals to create and participate in innovative solutions for social and environmental problems. Crypto can also foster creativity and expression through digital art and culture.

Some of the projects mentioned in a post by [dailycoin](https://dailycoin.com/top-10-crypto-projects-dedicated-to-socio-humanitarian-causes/) about the top 10 crypto projects dedicated to socio humanitarian causes are using crypto to help people in need, such as UkraineDAO, Habitat for Humanity, and Built With Bitcoin Foundation. These projects are providing humanitarian aid, relief, and development to countries and regions that are facing war, poverty, and disaster. They are accepting donations in various cryptocurrencies and using them to fund their missions and activities.

Some of the projects mentioned are using crypto to advance scientific research and innovation, such as VitaDAO, Molecule, and Klima DAO. These projects are creating decentralized platforms and communities that enable collaborative funding and governance of life science and climate change projects. They are using tokens and smart contracts to incentivize and reward contributors and stakeholders.

Some of the projects mentioned are using crypto to create social impact NFTs, such as Impact, ARTXV, and Blockchain for Humanity. These projects are using NFTs as a medium to raise awareness and funds for various causes, such as education, health, diversity, inclusion, and sustainability. They are creating and selling digital artworks that represent their values and vision.
""")

st.markdown("""
### :red[CONCLUSION]
""")

st.markdown("""
Moreover, crypto transactions are more transparent and traceable than other forms of money transfers. Blockchain technology allows anyone to access and analyze the public ledger of transactions on various networks. This makes it easier to identify and track the sources and destinations of funds. On the other hand, traditional financial systems are often opaque and complex, making it harder to follow the money trail. Terrorist organizations have been funding their illegal activities for years with or without crypto. Crypto is not the root cause of terrorism; it is just a tool that can be used for good or evil.

The WSJ's crypto-terrorism claims have been challenged by on-chain analysis, which revealed that the amounts and volumes of crypto transactions linked to Hamas and its affiliates were much lower than reported. The WSJ and Senator Warren should correct their errors and apologize for spreading misinformation that could harm the crypto industry and its users. Crypto is not a threat; it is an opportunity for innovation and social good.
""")

# : https://www.forbes.com/sites/jonathanponciano/2022/03/02/crypto-donations-to-ukraine-top-52-million-as-funds-pour-in-from-bitcoin-ether-polkadot-and-nfts/?sh=6a34bdd774e5
# : https://www.bbc.com/news/technology-56371912
