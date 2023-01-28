from scipy import signal
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Setting the Page Config
st.set_page_config(page_title="Analisa Sektor Pariwisata Jawa Barat Pra-Pasca Pandemi COVID19", layout="wide" )

# Jumlah Wisatawan Jabar
url_jumlah_wisatawan_jabar = "./dataset/jumlah_wisatawan_jabar_summed.csv"
jumlah_wisatawan_jabar = pd.read_csv(url_jumlah_wisatawan_jabar)


# Load the Images (If Needed)
# Raja Ampat
background = "./images/header.png"

# Header Image dan Judul
st.image(background)
st.title('Mencoba Streamlit pertama kali')

st.subheader("Tren Jumlah Wisatawan di Jawa Barat")

# Dividing Into 2 Columns
col1, col2 = st.columns(2)

with col1:
    st.write("Menurut data jumlah wisatawan pada Open Data Jabar, wisatawan nusantara mengalami **_penurunan mulai tahun 2019 dibanding tahun sebelumnya._** Pada **_tahun 2019 mengalami penurunan sebesar 76.84 persen_** dibanding tahun sebelumnya. **_Tahun 2020 mengalami penurunan sebesar 49.8 persen, tetapi tahun 2021 jumlah wisatawan nusantara mengalami kenaikan sebesar 22.62 persen._** Jadi, Jawa Barat memang mengalami penurunan wisatawan pada tahun 2020. Tetapi, terlepas dari pembatasan sosial yang ketat tahun 2021 tetap ada kenaikan pada jumlah wisatawan nusantara di Jawa Barat.")
    st.write("Tetapi, jumlah wisatawan nusantara di Jawa Barat tetap mengalami penurunan sebelum pandemi terjadi. Jadi bisa diasumsikan bahwa ada penyebab lain yang membuat jumlah wisatawan nusantara turun. Pada report ini belum ada data yang mendukung asumsi tersebut.")
    st.write("Sedangkan wisatawan mancanegara mengalami **_penurunan pada tahun 2020 sebesar 82.8 persen dan tahun 2021 sebesar 95.5 persen._** Pembatasan akses internasional yang ketat menyebabkan jumlah wisatawan mancanegara turun secara signifikan")

with col2:
    fig = px.line(
        jumlah_wisatawan_jabar,
        x='tahun',
        y='f0_',       
        markers=True,
        title="Jumlah Wisatawan di Jawa Barat 2014-2021",
        color="jenis_wisatawan",
        color_discrete_map={
            "NUSANTARA":"#77E9C3",
            "MANCANEGARA":"#41B1F1"
        },
        category_orders={
            "jenis_wisatawan": ["NUSANTARA","MANCANEGARA"]
        },
        labels={
            "tahun":"Tahun",
            "f0_":"Jumlah Pengunjung",
            "jenis_wisatawan":"Jenis Wisatawan"
        })
    fig.update_layout(
        hoverlabel=dict(
            bgcolor='white'
        ))
    fig.update_traces(mode="markers+lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("_Sumber : Open Data Jabar_")
