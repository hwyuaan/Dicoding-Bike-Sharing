import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as mticker
sns.set(style='dark')

st.title ("Bike Sharing 2011-2012 ✨")
df1 = pd.read_csv("dashboard/main_hour.csv")
df2 = pd.read_csv("dashboard/main_day.csv")

st.write(df2)

datetime_columns = ["dteday"]
df1.sort_values(by="dteday", inplace=True)
df1.reset_index(inplace=True)
 
for column in datetime_columns:
    df1[column] = pd.to_datetime(df1[column])


min_date = df1["dteday"].min().date()
max_date = df1["dteday"].max().date()
with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date) 
    )

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

main_df = df1[(df1["dteday"] >= start_date) & (df1["dteday"] <= end_date)]



st.subheader("Jumlah Data Bikers rentang waktu 2011 - 2012")
def jumlah(df2):
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

    else:
          st.error("Kolom 'hr' atau 'cnt' tidak ditemukan dalam dataset.")  



def daily(df2):
    st.subheader('Monthly Sharing')
 
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



def harian(df1):
    st.subheader('Pola waktu peminjaman harian paling tinggi rentang tahun 2011-2012')
    hari = df1[df1['dteday'] == '2012-09-15']
    
    # Mengelompokkan data berdasarkan jam dan menjumlahkan peminjam
    monthly_data = hari.groupby('hr')['cnt'].sum().reset_index() 

    plt.figure(figsize=(15, 10))
    plt.bar(monthly_data['hr'], monthly_data['cnt'], color='red', width=0.5)  # Bar plot
    plt.title("Pola Waktu Peminjaman Sepeda Harian pada 2012-09-15", fontsize=18, fontweight='bold')
    plt.ylabel("Jumlah Peminjam", fontsize=16)
    plt.xlabel("Jam", fontsize=16)
    plt.xticks(monthly_data['hr']) 
    plt.grid(axis='y') 
    
    st.pyplot(plt)





def p2(df2):
    st.subheader('Faktor- Faktor yang mempengaruhi Bike Sharing')
    by2012 = df2[df2['yr'] == 2012]
    weather= by2012.groupby('weathersit')['cnt'].mean().reset_index()
    print(weather)

    holiday = by2012.groupby('holiday')['cnt'].mean().reset_index()
    print(holiday)

    work = by2012.groupby('workingday')['cnt'].mean().reset_index()
    print(work)

    st.text('Rata-rata Peminjaman Berdasarkan Cuaca')
    plt.figure(figsize=(12, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather, palette='viridis')
    plt.title('Rata-rata Peminjaman Sepeda Berdasarkan Cuaca pada 2012')
    plt.xlabel('Situasi Cuaca')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Clear', 'Mist', 'Light Snow', 'Heavy Rain'], rotation=45)
    plt.tight_layout() 
    st.pyplot(plt)  
    plt.clf()  

    st.text('Rata-rata Peminjaman Berdasarkan Status Hari Libur')
    plt.figure(figsize=(12, 6))
    sns.barplot(x='holiday', y='cnt', data=holiday, palette='viridis')
    plt.title('Rata-rata Peminjaman Sepeda Berdasarkan Status Hari Libur')
    plt.xlabel('Status Hari (0 = Selain Holiday, 1 = Holiday)')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    plt.xticks(ticks=[0, 1], labels=['Bukan Holiday', 'Holiday'])
    plt.tight_layout()  
    st.pyplot(plt)  
    plt.clf()  


    st.text('Presentasi peminjam di Hari Kerja')
    total = work.set_index('workingday')['cnt']
    plt.figure(figsize=(5, 5))
    plt.pie(total, labels=['Hari Kerja', 'Libur'], autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107'])
    plt.title('Proporsi Peminjaman Sepeda Berdasarkan Hari Kerja')
    plt.axis('equal')  
    plt.tight_layout()  
    st.pyplot(plt)  # 


def rfm(df1):
    st.subheader('RFM Analisis')
    st.text('Recency: Mengetahui jumlah hari yang berlalu sejak transaksi terakhir yang dilakukan oleh pelanggan')
    st.text('Frequency: total jumlah transaksi yang dilakukan oleh setiap pelanggan yang terdaftar')
    st.text('Monetary: total dari semua  peminjaman yang dilakukan oleh pelanggan')


    latest_date = df1['dteday'].max()
    rfm_df = df1.groupby(by='registered', as_index=False).agg({
        'dteday': lambda x: (latest_date - x.max()).days,  
        'instant': 'count',  # Frequency
        'cnt': 'sum'  # Monetary
    }).rename(columns={
        'dteday': 'recency', 
        'instant': 'frequency', 
        'cnt': 'monetary'
    })

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))
    
    colors = ["#72BCD4"] * 5  
    # Plot Recency
    sns.barplot(y="recency", x="registered", data=rfm_df.sort_values(by="recency", ascending=False).head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
    ax[0].tick_params(axis='x', labelsize=15)

    # Plot Frequency
    sns.barplot(y="frequency", x="registered", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].set_title("By Frequency", loc="center", fontsize=18)
    ax[1].tick_params(axis='x', labelsize=15)

    # Plot Monetary
    sns.barplot(y="monetary", x="registered", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
    ax[2].set_ylabel(None)
    ax[2].set_xlabel(None)
    ax[2].set_title("By Monetary", loc="center", fontsize=18)
    ax[2].tick_params(axis='x', labelsize=15)

    plt.tight_layout()  
    st.pyplot(plt) 

jumlah(df2)
daily(df2)
harian(df1)
p2(df2)
rfm(df1)
