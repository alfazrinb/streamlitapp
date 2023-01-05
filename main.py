# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: siddhardhan
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
mutasi_model = pickle.load(open("C:\\Users\\Miqbalkt\\OneDrive\\Documents\\DAC\\model_mutasi_pegawai_fix_banget.sav", "rb"))
mutasi_Satker_model = pickle.load(open("C:\\Users\\Miqbalkt\\OneDrive\\Documents\\DAC\\model_mutasi_satker.sav", "rb"))

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('BC6.jpeg')   

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Sistem Rekomendasi Mutasi Pegawai (SI-REMPA)',
                          
                          ['Prediksi Mutasi',
                          'Prediksi Satuan Kerja'],
                          icons=['person','activity'],
                          default_index=0
                          )

# Mutasi Prediction Page
if (selected == 'Prediksi Mutasi'):
    
    # page title
    # st.title('Prediksi Mutasi Pegawai Dengan Machine Learning')
    st.markdown("<h1 style='text-align: center; color: Black;'>Prediksi Mutasi Pegawai Dengan Machine Learning</h1>", unsafe_allow_html=True)
    
    
    # getting the input data from the user
    # col1, col2, col3 = st.columns(3)
    Nama = st.text_input('Nama Pegawai')
    Nip = st.text_input('NIP Pegawai')
    
    Umur = st.slider("Umur",21,65)

    NamaJabatan = st.selectbox('Jabatan', ["Non Pemeriksa","Pemeriksa"])
        
    if NamaJabatan == "Non Pemeriksa" :
        NamaJabatan = 0
    else :
        NamaJabatan = 1

    KodePangkat = st.selectbox('Pangkat/Golongan',["II/A",'II/B',"II/C","II/D","III/A","III/B","III/C",
    "III/D",'IV/A','IV/B','IV/C','IV/D','IV/E'])

    # if KodePangkat == "I/D":
    #     KodePangkat = 1
    if KodePangkat == "II/B":
        KodePangkat = 2
    elif KodePangkat == "II/C":
        KodePangkat = 3
    elif KodePangkat == "II/D":
        KodePangkat = 4
    elif KodePangkat == "III/A":
        KodePangkat = 5
    elif KodePangkat == "II/B":
        KodePangkat = 6
    elif KodePangkat == "III/C":
        KodePangkat = 7
    elif KodePangkat == "III/D":
        KodePangkat = 8
    elif KodePangkat == "IV/A":
        KodePangkat = 9
    elif KodePangkat == "IV/B":
        KodePangkat = 10
    elif KodePangkat == "IV/C":
        KodePangkat = 11
    elif KodePangkat == "IV/D":
        KodePangkat = 12
    elif KodePangkat == "IV/E":
        KodePangkat = 13
    else :
        KodePangkat = 0

    MasaKerja = st.slider("Masa Kerja",0,46)
    
    # with col3:
    Satker = st.selectbox('Pilih Satuan Kerja', ['Auditorat Utama Investigasi', 'Auditorat Utama Keuangan Negara I', 
    'Auditorat Utama Keuangan Negara II', 'Auditorat Utama Keuangan Negara III', 'Auditorat Utama Keuangan Negara IV', 
    'Auditorat Utama Keuangan Negara V', 'Auditorat Utama Keuangan Negara VI', 'Auditorat Utama Keuangan Negara VII', 
    'BPK Perwakilan Provinsi Aceh', 'BPK Perwakilan Provinsi Bali', 'BPK Perwakilan Provinsi Banten', 
    'BPK Perwakilan Provinsi Bengkulu', 'BPK Perwakilan Provinsi D.I. Yogyakarta', 'BPK Perwakilan Provinsi DKI Jakarta', 
    'BPK Perwakilan Provinsi Gorontalo', 'BPK Perwakilan Provinsi Jambi', 'BPK Perwakilan Provinsi Jawa Barat', 
    'BPK Perwakilan Provinsi Jawa Tengah', 'BPK Perwakilan Provinsi Jawa Timur', 'BPK Perwakilan Provinsi Kalimantan Barat', 
    'BPK Perwakilan Provinsi Kalimantan Selatan', 'BPK Perwakilan Provinsi Kalimantan Tengah', 'BPK Perwakilan Provinsi Kalimantan Timur', 
    'BPK Perwakilan Provinsi Kalimantan Utara', 'BPK Perwakilan Provinsi Kepulauan Bangka Belitung', 'BPK Perwakilan Provinsi Kepulauan Riau', 
    'BPK Perwakilan Provinsi Lampung', 'BPK Perwakilan Provinsi Maluku', 'BPK Perwakilan Provinsi Maluku Utara', 
    'BPK Perwakilan Provinsi Nusa Tenggara Barat', 'BPK Perwakilan Provinsi Nusa Tenggara Timur', 'BPK Perwakilan Provinsi Papua', 
    'BPK Perwakilan Provinsi Papua Barat', 'BPK Perwakilan Provinsi Riau', 'BPK Perwakilan Provinsi Sulawesi Barat', 
    'BPK Perwakilan Provinsi Sulawesi Selatan', 'BPK Perwakilan Provinsi Sulawesi Tengah', 'BPK Perwakilan Provinsi Sulawesi Tenggara', 
    'BPK Perwakilan Provinsi Sulawesi Utara', 'BPK Perwakilan Provinsi Sumatera Barat', 'BPK Perwakilan Provinsi Sumatera Selatan', 
    'BPK Perwakilan Provinsi Sumatera Utara', 'Badan Pendidikan dan Pelatihan Pemeriksaan Keuangan Negara', 'Sekretariat Jendral'])


    if Satker == "Auditorat Utama Investigasi":
        Satker = 0
    elif Satker == 'Auditorat Utama Keuangan Negara I':
        Satker = 1
    elif Satker == 'Auditorat Utama Keuangan Negara II':
        Satker = 2
    elif Satker == 'Auditorat Utama Keuangan Negara III':
        Satker = 3
    elif Satker == 'Auditorat Utama Keuangan Negara IV':
        Satker = 4
    elif Satker == 'Auditorat Utama Keuangan Negara V':
        Satker = 5
    elif Satker == 'Auditorat Utama Keuangan Negara VI':
        Satker = 6
    elif Satker == 'Auditorat Utama Keuangan Negara VII':
        Satker = 7
    elif Satker == 'BPK Perwakilan Provinsi Aceh':
        Satker = 8
    elif Satker == 'BPK Perwakilan Provinsi Bali':
        Satker = 9
    elif Satker == 'BPK Perwakilan Provinsi Banten':
        Satker = 10
    elif Satker == 'BPK Perwakilan Provinsi Bengkulu':
        Satker = 11
    elif Satker == 'BPK Perwakilan Provinsi D.I. Yogyakarta':
        Satker = 12
    elif Satker == 'BPK Perwakilan Provinsi DKI Jakarta':
        Satker = 13
    elif Satker == 'BPK Perwakilan Provinsi Gorontalo':
        Satker = 14
    elif Satker == 'BPK Perwakilan Provinsi Jambi':
        Satker = 15
    elif Satker == 'BPK Perwakilan Provinsi Jawa Barat':
        Satker = 16
    elif Satker == 'BPK Perwakilan Provinsi Jawa Tengah':
        Satker = 17
    elif Satker == 'BPK Perwakilan Provinsi Jawa Timur':
        Satker = 18
    elif Satker == 'BPK Perwakilan Provinsi Kalimantan Barat':
        Satker = 19
    elif Satker == 'BPK Perwakilan Provinsi Kalimantan Selatan':
        Satker = 20
    elif Satker == 'BPK Perwakilan Provinsi Kalimantan Tengah':
        Satker = 21
    elif Satker == 'BPK Perwakilan Provinsi Kalimantan Timur':
        Satker = 22
    elif Satker == 'BPK Perwakilan Provinsi Kalimantan Utara':
        Satker = 23
    elif Satker == 'BPK Perwakilan Provinsi Kepulauan Bangka Belitung':
        Satker = 24
    elif Satker == 'BPK Perwakilan Provinsi Kepulauan Riau':
        Satker = 25
    elif Satker == 'BPK Perwakilan Provinsi Lampung':
        Satker = 26
    elif Satker == 'BPK Perwakilan Provinsi Maluku':
        Satker = 27
    elif Satker == 'BPK Perwakilan Provinsi Maluku Utara':
        Satker = 28
    elif Satker == 'BPK Perwakilan Provinsi Nusa Tenggara Barat':
        Satker = 29
    elif Satker == 'BPK Perwakilan Provinsi Nusa Tenggara Timur':
        Satker = 30
    elif Satker == 'BPK Perwakilan Provinsi Papua':
        Satker  =31
    elif Satker == 'BPK Perwakilan Provinsi Papua Barat':
        Satker  = 32 
    elif Satker == "BPK Perwakilan Provinsi Riau":
        Satker = 33
    elif Satker == 'BPK Perwakilan Provinsi Sulawesi Barat':
        Satker = 34
    elif Satker == 'BPK Perwakilan Provinsi Sulawesi Selatan':
        Satker = 35
    elif Satker == 'BPK Perwakilan Provinsi Sulawesi Tengah':
        Satker = 36 
    elif Satker == 'BPK Perwakilan Provinsi Sulawesi Tenggara':
        Satker = 37
    elif Satker == 'BPK Perwakilan Provinsi Sulawesi Utara':
        Satker = 38
    elif Satker == 'BPK Perwakilan Provinsi Sumatera Barat':
        Satker = 39
    elif Satker == 'BPK Perwakilan Provinsi Sumatera Selatan':
        Satker = 40
    elif Satker == 'BPK Perwakilan Provinsi Sumatera Utara':
        Satker = 41
    elif Satker == 'Badan Pendidikan dan Pelatihan Pemeriksaan Keuangan Negara':
        Satker = 42
    else :
        Satker = 43

    NamaJurusan = st.selectbox('Jurusan', ['Akuntansi','Bahasa & Sastra','Jurusan Lainnya','Manajemen','Teknik'])

    if NamaJurusan == 'Akuntansi':
        NamaJurusan = 0
    elif NamaJurusan == 'Bahasa':
        NamaJurusan = 1
    elif NamaJurusan == 'Lainnya':
        NamaJurusan = 2
    elif NamaJurusan == 'Manajemen':
        NamaJurusan = 3
    else :
        NamaJurusan = 4
    
    NamaPendidikan = st.selectbox('Strata Pendidikan',['D1','D2','D3','D4/S1','S2','S3'])

    # if NamaPendidikan == 'SD':
    #     NamaPendidikan =1
    # if NamaPendidikan == 'SMP':
    #     NamaPendidikan =2
    # if NamaPendidikan == 'SMA':
        # NamaPendidikan =3
    if NamaPendidikan == 'D1':
        NamaPendidikan =4
    elif NamaPendidikan == 'D2':
        NamaPendidikan =5
    elif NamaPendidikan == 'D3':
        NamaPendidikan =6
    elif NamaPendidikan == 'D4/S1':
        NamaPendidikan =7
    elif NamaPendidikan == 'S2':
        NamaPendidikan =8
    else :
        NamaPendidikan = 9

    JamDiklat = st.text_input('Jumlah Jam Diklat')
    
    # code for Prediction
    prediksi = ''
    
    # creating a button for Prediction
    
    if st.button('Submit'):
        prediksi_mutasi = mutasi_model.predict([[
            Umur, 
            NamaJabatan, 
            KodePangkat, 
            MasaKerja, 
            Satker, 
            NamaJurusan, 
            NamaPendidikan, 
            JamDiklat]])
        

        if (prediksi_mutasi[0] == 0):
          prediksi = f'Pegawai atas Nama {Nama} dengan NIP : {Nip} __Tidak Direkomendasikan untuk Mutasi__'
        else:
          prediksi = f'Pegawai atas Nama {Nama} dengan NIP : {Nip} __Direkomendasikan untuk Mutasi__'
        
    st.success(prediksi)

def get_str(n,Nama,Nip):
    if (n == 0):
        prediksi_satker = f'Auditorat Utama Investigasi'
    elif (n == 1):
        prediksi_satker = f'Auditorat Utama Keuangan Negara I'
    elif (n == 2):
        prediksi_satker = f'Auditorat Utama Keuangan Negara II'
    elif (n == 3):
        prediksi_satker = f'Auditorat Utama Keuangan Negara III'
    elif (n == 4):
        prediksi_satker = f'Auditorat Utama Keuangan Negara IV'
    elif (n == 5):
        prediksi_satker = f'Auditorat Utama Keuangan Negara V'
    elif (n == 6):
        prediksi_satker = f'Auditorat Utama Keuangan Negara VI'
    elif (n == 7):
        prediksi_satker = f'Auditorat Utama Keuangan Negara VII'
    elif (n == 8):
        prediksi_satker = f'BPK Perwakilan Provinsi Aceh'
    elif (n == 9):
        prediksi_satker = f'BPK Perwakilan Provinsi Bali'
    elif (n == 10):
        prediksi_satker = f'BPK Perwakilan Provinsi Banten'
    elif (n == 11):
        prediksi_satker = f'BPK Perwakilan Provinsi Bengkulu'
    elif (n == 12):
        prediksi_satker = f'BPK Perwakilan Provinsi D.I. Yogyakarta'
    elif (n == 13):
        prediksi_satker = f'BPK Perwakilan Provinsi DKI Jakarta'
    elif (n == 14):
        prediksi_satker = f'BPK Perwakilan Provinsi Gorontalo'
    elif (n == 15):
        prediksi_satker = f'BPK Perwakilan Provinsi Jambi'
    elif (n == 16):
        prediksi_satker = f'BPK Perwakilan Provinsi Jawa Barat'
    elif (n == 17):
        prediksi_satker = f'BPK Perwakilan Provinsi Jawa Tengah'
    elif (n == 18):
        prediksi_satker = f'BPK Perwakilan Provinsi Jawa Timur'
    elif (n == 19):
        prediksi_satker = f'BPK Perwakilan Provinsi Kalimantan Barat'
    elif (n == 20):
        prediksi_satker = f'BPK Perwakilan Provinsi Kalimantan Selatan'
    elif (n == 21):
        prediksi_satker = f'BPK Perwakilan Provinsi Kalimantan Tengah'
    elif (n == 22):
        prediksi_satker = f'BPK Perwakilan Provinsi Kalimantan Timur'
    elif (n == 23):
        prediksi_satker = f'BPK Perwakilan Provinsi Kalimatan Utara'
    elif (n == 24):
        prediksi_satker = f'BPK Perwakilan Provinsi Kepulauan Bangka Belitung'
    elif (n == 25):
        prediksi_satker = f'BPK Perwakilan Provinsi Kepulauan Riau'
    elif (n == 26):
        prediksi_satker = f'BPK Perwakilan Provinsi Lampung'
    elif (n == 27):
        prediksi_satker = f'BPK Perwakilan Provinsi Maluku'
    elif (n == 28):
        prediksi_satker = f'BPK Perwakilan Provinsi Maluku Utara'
    elif (n == 29):
        prediksi_satker = f'BPK Perwakilan Provinsi Nusa Tenggara Barat'
    elif (n == 30):
        prediksi_satker = f'BPK Perwakilan Provinsi Nusa Tenggara Timur'
    elif (n == 31):
        prediksi_satker = f'BPK Perwakilan Provinsi Papua'
    elif (n == 32):
        prediksi_satker = f'BPK Perwakilan Provinsi Papua Barat'
    elif (n == 33):
        prediksi_satker = f'BPK Perwakilan Provinsi Riau'
    elif (n == 34):
        prediksi_satker = f'BPK Perwakilan Provinsi Sulawesi Barat'
    elif (n == 35):
        prediksi_satker = f'BPK Perwakilan Provinsi Sulawesi Selatan'
    elif (n == 36):
        prediksi_satker = f'BPK Perwakilan Provinsi Sulawesi Tengah'
    elif (n == 37):
        prediksi_satker = f'BPK Perwakilan Provinsi Sulawesi Tenggara'
    elif (n == 38):
        prediksi_satker = f'BPK Perwakilan Provinsi Sulawesi Utara'
    elif (n == 39):
        prediksi_satker = f'BPK Perwakilan Provinsi Sumatera Barat'
    elif (n == 40):
        prediksi_satker = f'BPK Perwakilan Provinsi Sumatera Selatan'
    elif (n == 41):
        prediksi_satker = f'BPK Perwakilan Provinsi Sumatera Utara'
    elif (n == 42):
        prediksi_satker = f'Badan Pendidikan dan Pelatihan Pemeriksaan Keuangan Negara'
    else:
        prediksi_satker = f'Sekretariat Jendral'
    return prediksi_satker


# Heart Disease Prediction Page
if (selected == 'Prediksi Satuan Kerja'):
    
    # page title
    # st.title('Heart Disease Prediction using ML')
    st.markdown("<h1 style='text-align: center; color: Black;'>Prediksi Mutasi Satuan Kerja Dengan Machine Learning</h1>", unsafe_allow_html=True)
    
    Nama = st.text_input('Nama Pegawai')
    Nip = st.text_input('NIP Pegawai')

    Umur = st.slider("Umur",21,65)
        
    NamaJabatan = st.selectbox('Jabatan', ["Non Pemeriksa","Pemeriksa"])
        
    if NamaJabatan == "Non Pemeriksa" :
        NamaJabatan = 0
    else :
        NamaJabatan = 1

    KodePangkat = st.selectbox('Pangkat/Golongan',["II/A",'II/B',"II/C","II/D","III/A","III/B","III/C",
    "III/D",'IV/A','IV/B','IV/C','IV/D','IV/E'])

    # if KodePangkat == "I/D":
    #     KodePangkat = 1
    if KodePangkat == "II/B":
        KodePangkat = 2
    elif KodePangkat == "II/C":
        KodePangkat = 3
    elif KodePangkat == "II/D":
        KodePangkat = 4
    elif KodePangkat == "III/A":
        KodePangkat = 5
    elif KodePangkat == "II/B":
        KodePangkat = 6
    elif KodePangkat == "III/C":
        KodePangkat = 7
    elif KodePangkat == "III/D":
        KodePangkat = 8
    elif KodePangkat == "IV/A":
        KodePangkat = 9
    elif KodePangkat == "IV/B":
        KodePangkat = 10
    elif KodePangkat == "IV/C":
        KodePangkat = 11
    elif KodePangkat == "IV/D":
        KodePangkat = 12
    elif KodePangkat == "IV/E":
        KodePangkat = 13
    else :
        KodePangkat = 0
    
    MasaKerja = st.slider("Masa Kerja",0,46)

    NamaJurusan = st.selectbox('Jurusan', ['Akuntansi','Bahasa & Sastra','Jurusan Lainnya','Manajemen','Teknik'])

    if NamaJurusan == 'Akuntansi':
        NamaJurusan = 0
    elif NamaJurusan == 'Bahasa':
        NamaJurusan = 1
    elif NamaJurusan == 'Lainnya':
        NamaJurusan = 2
    elif NamaJurusan == 'Manajemen':
        NamaJurusan = 3
    else :
        NamaJurusan = 4
    
    NamaPendidikan = st.selectbox('Strata Pendidikan',['D1','D2','D3','D4/S1','S2','S3'])

    # if NamaPendidikan == 'SD':
    #     NamaPendidikan =1
    # if NamaPendidikan == 'SMP':
    #     NamaPendidikan =2
    # if NamaPendidikan == 'SMA':
        # NamaPendidikan =3
    if NamaPendidikan == 'D1':
        NamaPendidikan =4
    elif NamaPendidikan == 'D2':
        NamaPendidikan =5
    elif NamaPendidikan == 'D3':
        NamaPendidikan =6
    elif NamaPendidikan == 'D4/S1':
        NamaPendidikan =7
    elif NamaPendidikan == 'S2':
        NamaPendidikan =8
    else :
        NamaPendidikan = 9

    JamDiklat = st.text_input('Jumlah Jam Diklat')
     
    # code for Prediction
    prediksi_satker = ''
    
    # creating a button for Prediction
    s1=None
    s2=None
    s3=None
    if st.button('Submit'):
        Satker = mutasi_Satker_model.predict_proba([[Umur, NamaJabatan, KodePangkat, MasaKerja, NamaJurusan, NamaPendidikan, JamDiklat]])                          
        a,b,c = np.argsort(Satker,axis=1)[0][-3:]
        s1=get_str(c,Nama, Nip)
        s2=get_str(b,Nama, Nip)
        s3=get_str(a,Nama, Nip)

    f'Pegawai atas Nama {Nama} dengan NIP : {Nip} Direkomendasikan untuk Mutasi ke Satuan Kerja berikut:'    
    st.success(s1)
    st.success(s2)
    st.success(s3)
