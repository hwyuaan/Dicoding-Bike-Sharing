import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as mticker
sns.set(style='dark')

st.title ("Data Peminjaman Sepeda Tahun 2011-2012")
df = pd.read_csv("all_data.csv")

st.subheader("Rekap Data ")
st.write(df)

st.subheader("Jumlah Data Bikers")
def jumlah(df):
    if 'yr' in df.columns and 'cnt' in df.columns:
        jumlah=df.groupby(by='yr')['cnt'].sum().reset_index()

        fig, ax = plt.subplots(figsize=(16, 10))
        ax.plot(
            jumlah['yr'], 
            jumlah['cnt'], 
            color='#72BCD4',
            marker='o')
        ax.set_title('Kuantitas jumlah Peminjaman Sepeda per Jam')
        ax.set_xlabel('Tahun Peminjaman')
        ax.set_ylabel('Rata-rata Jumlah Peminjaman')
        ax.grid()

        ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
       
        
        st.pyplot(fig)

    else:
          st.error("Kolom 'hr' atau 'cnt' tidak ditemukan dalam dataset.")  

st.text("Terjadi pelonjakan peminjam di 2012 dengan jumlah yaitu dari 1.243.103 menjadi 2.049.576 peminjam. Grafik menunjukan kenaikan yang signifikan tinggi")

def bar(df):
        
        st.subheader("Kapan dan pada jam berapa peminjaman sepeda melonjak tinggi pada tahun 2011??")
        result = '2011-07-04'
        result2 =df[df['dteday']==result]
        result2

        plt.figure(figsize=(15, 10))
        colors=['#72BCD4']
        sns.barplot(
            x='hr',
            y='cnt',
            data=result2, palette=colors)
        plt.title('Peminjaman Sepeda pada 2011-07-04 berdasarkan Jam', fontsize=16)
        plt.xlabel('Jam', fontsize=14)
        plt.ylim(0,500)
        plt.ylabel('Jumlah Peminjaman Sepeda', fontsize=14)
        plt.show()

        st.pyplot(plt)
        st.text("Pelonojakan paling tinggi pada tahun 2011 terjadi pada bulan Juli 2024 tanggal 4 jam 21.00 dengan kuantitas peminjam adalah 457")


def bar(df):
        
        st.subheader("Kapan dan pada jam berapa peminjaman sepeda melonjak tinggi pada tahun 2011??")
        result = '2011-07-04'
        result2 =df[df['dteday']==result]
        result2

        plt.figure(figsize=(15, 10))
        colors=['#72BCD4']
        sns.barplot(
            x='hr',
            y='cnt',
            data=result2, palette=colors)
        plt.title('Peminjaman Sepeda pada 2011-07-04 berdasarkan Jam', fontsize=16)
        plt.xlabel('Jam', fontsize=14)
        plt.ylim(0,500)
        plt.ylabel('Jumlah Peminjaman Sepeda', fontsize=14)
        plt.show()

        st.pyplot(plt)
        st.text("Pelonojakan paling tinggi pada tahun 2011 terjadi pada bulan Juli 2024 tanggal 4 jam 21.00 dengan kuantitas peminjam adalah 457")


def bar(df):
        
        st.subheader("Kapan dan pada jam berapa peminjaman sepeda melonjak tinggi pada tahun 2011??")
        result = '2011-07-04'
        result2 =df[df['dteday']==result]
        result2

        plt.figure(figsize=(15, 10))
        colors=['#72BCD4']
        sns.barplot(
            x='hr',
            y='cnt',
            data=result2, palette=colors)
        plt.title('Peminjaman Sepeda pada 2011-07-04 berdasarkan Jam', fontsize=16)
        plt.xlabel('Jam', fontsize=14)
        plt.ylim(0,500)
        plt.ylabel('Jumlah Peminjaman Sepeda', fontsize=14)
        plt.show()

        st.pyplot(plt)
        st.text("Pelonojakan paling tinggi pada tahun 2011 terjadi pada bulan Juli 2024 tanggal 4 jam 21.00 dengan kuantitas peminjam adalah 457")


def bar2(df):
    group_df = df.groupby('yr')['cnt'].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(data=group_df, x='yr', y='cnt', hue='yr', palette='Set1')
    plt.title('Perbandingan Peminjaman Sepeda antara Tahun 2011 dan 2012', fontsize=16)
    plt.xlabel('Tahun', fontsize=14)
    plt.ylabel('Jumlah Peminjaman Sepeda', fontsize=14)
    plt.legend(title='Tahun')
    plt.show()
    st.pyplot(plt)

    st.text("2. Apakah terdapat perbedaan pelonjakan yang terjadi di tahun 2011 dan 2012?")


      




jumlah(df)
bar(df)
bar2(df)




# plt.figure(figsize=(15, 10))
# colors = ['#72BCD4']
# sns.barplot(x='hr', y='cnt', data=result2, palette=colors)
# plt.title('Peminjaman Sepeda pada 2011-07-04 berdasarkan Jam', fontsize=16)
# plt.xlabel('Jam', fontsize=14)
# plt.ylim(0, 500)
# plt.ylabel('Jumlah Peminjaman Sepeda', fontsize=14)
# st.pyplot(plt)
