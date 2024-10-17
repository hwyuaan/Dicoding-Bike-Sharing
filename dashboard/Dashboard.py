import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as mticker
sns.set(style='dark')

st.title ("Bike Sharing 2011-2012 ✨")
df1 = pd.read_csv("dt_hour.csv")
df2 = pd.read_csv("dt_day.csv")

st.write(df2)

datetime_columns = ["dteday"]
df1.sort_values(by="dteday", inplace=True)
df1.reset_index(inplace=True)
 
for column in datetime_columns:
    df1[column] = pd.to_datetime(df1[column])


def jumlah(df2):
    st.subheader("Jumlah Data Peminjam Sepeda Harian Tahun 2011 dan 2012")
    if 'yr' in df2.columns and 'cnt' in df2.columns:
        group_df = df2.groupby('yr')['cnt'].sum().reset_index()

        plt.figure(figsize=(15, 10))
        colors = ['#72BCD4', '#FFB74D']

        bar=sns.barplot(
            x='yr',
            y='cnt',
            data=group_df, palette=colors)

        for p in bar.patches:
            bar.annotate(f'{int(p.get_height()):,}', 
                            (p.get_x() + p.get_width() / 2., p.get_height()), 
                            ha='center', va='bottom', fontsize=12)
        plt.title('Customer Bike-Sharing by Year', fontsize=16, fontweight= 'bold')
        plt.xlabel('Tahun', fontsize=14)
        plt.xticks(ticks=[0, 1], labels=['2011', '2012'])
        plt.ylabel('Jumlah Peminjaman Sepeda pertahun', fontsize=14)
        plt.ylim(50000,3500000)
        plt.grid(True)

        bar.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        bar.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
       
        
        st.pyplot(plt)



def daily(df2):
    st.subheader('Data Peminjaman Sepeda Per-Bulan')
 
    col1, col2,col3 = st.columns(3)
 
    with col1:
        total_pinjam = df2.cnt.sum()
        st.metric("Total Peminjam", value=total_pinjam)
    
    with col2:
        total_registered = df2.registered.sum()
        st.metric("Total registered", value=total_registered)

    with col3:
        casual = df2.casual.sum()
        st.metric("Total casual", value=casual)

    monthly_data = df2.groupby(['yr','mnth']).agg({'cnt':'sum'}).reset_index()
    monthly_data['date'] = pd.to_datetime(monthly_data['yr'].astype(str) + '-' + monthly_data['mnth'].astype(str) + '-01')
    
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        monthly_data['date'],
        monthly_data['cnt'],
        marker='o', 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)



def tahun(df2):
    st.subheader('Data lonjakan peminjaman sepeda harian tertinggi untuk setiap tahun.')
    grouped_by_year = df2.groupby('yr')
    group_df = grouped_by_year.apply(lambda x: x.loc[x['cnt'].idxmax()])
    hasil = group_df[['yr', 'cnt']]

    plt.figure(figsize=(8, 6))
    colors = ['#72BCD4', '#FFB74D']

    bar=sns.barplot(
        x='yr',
        y='cnt',
        data=hasil, palette=colors)

    for p in bar.patches:
        bar.annotate(f'{int(p.get_height()):,}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='bottom', fontsize=12)
    plt.title('Customer Bike-Sharing by Year', fontsize=16, fontweight= 'bold')
    plt.xlabel('Tahun', fontsize=14)
    plt.xticks(ticks=[0, 1], labels=['2011 Tertinggi 2011-07-04', '2012 Tertinggi 2012-09-15'])
    plt.ylabel('Jumlah peminjam harian paling tinggi pertahun', fontsize=10)
    plt.ylim(500,9500)

    
    st.pyplot(plt)


def harian(df1):
    st.subheader('Pola waktu peminjaman sepeda harian pada tanggal 2012-09-15 ')
    hari =df1[df1['dteday'] == '2012-09-15']
    jam = hari['hr']
    jumlah = hari['cnt']


    plt.figure(figsize=(10, 8))
    sns.lineplot(data=hari, x='hr', y='cnt', marker='o')
    plt.title ("Pola Waktu peminjaman sepeda harian pada 2012-09-15 ",fontsize=12, fontweight='bold')
    plt.ylabel ("Jumlah Peminjam", fontsize=16)
    plt.ylim(0,800)
    plt.xlabel ("Jam",fontsize=16)
    plt.xticks(jam)
 
    
    st.pyplot(plt)





def p2(df1):
    st.subheader("Faktor yang mempengaruhi peminjaman sepeda harian pada tahun 2012")
    by2012 = df1[df1['yr'] == 2012]

    weather= by2012.groupby('weathersit')['cnt'].mean().reset_index()
    holiday = by2012.groupby('holiday')['cnt'].mean().reset_index()
    work = by2012.groupby('workingday')['cnt'].mean().reset_index()

    #beradasarkan cuaca
    st.text("Pengaruh cuaca pada peminjaman sepeda harian")
    fig, ax = plt.subplots(figsize=(10, 6))
    bar1 = sns.barplot(x='weathersit', y='cnt', data=weather, palette='viridis')
    for a in bar1.patches:
        bar1.annotate(f'{int(a.get_height()):,}',  
                    (a.get_x() + a.get_width() / 2., a.get_height()),  
                    ha='center', va='bottom', fontsize=12) 
    ax.set_title('Rata-rata Peminjaman Sepeda Berdasarkan Cuaca pada 2012')
    ax.set_xlabel('Situasi Cuaca')
    ax.set_ylabel('Rata-rata Jumlah Peminjaman')
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(['Clear', 'Mist', 'Light Snow', 'Heavy Rain'], rotation=45)
    st.pyplot(fig)  # Menampilkan grafik cuaca
    plt.clf() 

    st.text("Pengaruh status hari(Holiday) pada peminjaman sepeda harian")
    fig, ax = plt.subplots(figsize=(10, 6))
    bar2 = sns.barplot(x='holiday', y='cnt', data=holiday, palette='viridis')
    for b in bar2.patches:
        bar2.annotate(f'{int(b.get_height()):,}',  
                    (b.get_x() + b.get_width() / 2., b.get_height()),  
                    ha='center', va='bottom', fontsize=12)
    ax.set_title('Rata-rata Peminjaman Sepeda by holiday')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Peminjaman sepeda selain hari kerja', 'Peminjaman sepeda di hari libur'], rotation=0)
    ax.set_ylabel('Rata-rata Jumlah Peminjaman')
    st.pyplot(fig)  # Menampilkan grafik libur
    plt.clf()  


    total = work.set_index('workingday')['cnt']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(total, labels=['Hari Kerja', 'Libur'], autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107'])
    ax.set_title('Proporsi Peminjaman Sepeda Berdasarkan Hari Kerja')
    ax.axis('equal')  
    st.pyplot(fig)
     


jumlah(df2)
daily(df2)
tahun(df2)
harian(df1)
p2(df2)
