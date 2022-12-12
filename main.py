import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle
import math
from sklearn.preprocessing import MinMaxScaler

#######################################################################################

header = st.beta_container()
dataset = st.beta_container()
Exploratory = st.beta_container()
modelTraining = st.beta_container()

with header:
    st.title('Portal Prediksi Mutasi Pegawai BPK RI')
    # st.subheader('Untuk Masyarakat Kelas Ekonomi Menengah Kebawah')

#     image = Image.open('cropped-Logo-BPK-icon.png')
#     st.image(image, caption='')

# st.title('Portal Prediksi Mutasi Pegawai BPK RI')
# image = Image.open('cropped-Logo-BPK-icon.png')
# st.image(image, caption='')

# with dataset:
# 	st.header('Gambaran Umum Data')
# 	st.text('Dataset ini di ambil per tanggal 17 November 2020')
#     dt = pd.read_excel('data_ready_dummy.csv')
#     # dt = pd.read_csv('data_ready_dummy.csv')
#     # dt.drop(['Unnamed: 0','NipBaru'], axis = 1, inplace = True)
#     # data = dt.dropna()
#     # data['KodePangkat'].replace([1,2,3,4,5,6,7,8,9,10,11,12,13], 
#     #        ['I/D',"II/B","II/C","II/D","III/A","III/B","III/C","III/D","IV/A","IV/B","IV/C","IV/D","IV/E"], 
#     #        inplace=True)
#     # data['NamaPendidikan'].replace([1,2,3,4,5,6,7,8,9], 
#     #        ["SD","SMP","SMA","D1","D2","D3","S1/D4","S2","S3"], 
#     #        inplace=True)




# loading the saved model
loaded_model = pickle.load(open('trained_model_fix_banget.sav', 'rb'))

# def mutasi_prediction(input_data):

#     # changing the input_data to numpy array
#     input_data_as_numpy_array = np.asarray(input_data)

#     # reshape the array as we are predicting for one instance
#     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#     scaler = MinMaxScaler(feature_range = (0, 1))
#     input_data_as_numpy_array_scaler = scaler.fit_transform(input_data_reshaped)

#     prediction = loaded_model.predict(input_data_as_numpy_array_scaler)
#     print(prediction)
    
#     if (prediction[0] == 0):
#       return 'Pegawai Tidak Mutasi'
#     else:
#       return 'Pegawai Di Mutasi'
  
  
def main():
    
    

    Nama = st.text_input('Nama Pegawai')
    Nip = st.text_input('NIP Pegawai')
    # giving a title
    # st.title('Portal Prediksi Mutasi Pegawai BPK RI')
    
    
    # getting the input data from the user
    
    
    FreqJamDiklat = st.text_input('Jumlah Jam Diklat')

    NamaJabatan = st.selectbox('Pilih Jabatan', ["Non Pemeriksa","Pemeriksa"])

    if NamaJabatan == "Non Pemeriksa" :
        NamaJabatan = 0
    else :
        NamaJabatan = 1

    SatkerInduk = st.selectbox('Pilih Satuan Kerja Induk', ["Auditorat Utama Investigasi", 
    'Auditorat Utama Keuangan Negara I', 'Auditorat Utama Keuangan Negara II', 'Auditorat Utama Keuangan Negara III',
    'Auditorat Utama Keuangan Negara IV', 'Auditorat Utama Keuangan Negara V', 'Auditorat Utama Keuangan Negara VI',
    'Auditorat Utama Keuangan Negara VII', 'Badan Pemeriksa Keuangan', 
    'Badan Pendidikan dan Pelatihan Pemeriksaan Keuangan Negara', 
    'Direktorat Utama Pembinaan dan Pengembangan Hukum Pemeriksaan Keuangan Negara', 
    'Direktorat Utama Perencanaan, Evaluasi, dan Pengembangan Pemeriksaan Keuangan Negara', 
    'Inspektorat Utama', 'Sekretariat Jenderal BPK RI', 'Staf Ahli'])

    if SatkerInduk == "Auditorat Utama Investigasi":
        SatkerInduk = 0
    elif SatkerInduk == 'Auditorat Utama Keuangan Negara I':
        SatkerInduk = 1
    elif SatkerInduk == 'Auditorat Utama Keuangan Negara II':
        SatkerInduk = 2
    elif SatkerInduk == 'Auditorat Utama Keuangan Negara III':
        SatkerInduk = 3
    elif SatkerInduk == 'Auditorat Utama Keuangan Negara IV':
        SatkerInduk = 4
    elif SatkerInduk == 'Auditorat Utama Keuangan Negara V':
        SatkerInduk = 5
    elif SatkerInduk == 'Auditorat Utama Keuangan Negara VI':
        SatkerInduk = 6
    elif SatkerInduk == 'Auditorat Utama Keuangan Negara VII':
        SatkerInduk = 7
    elif SatkerInduk == 'Badan Pemeriksa Keuangan':
        SatkerInduk = 8
    elif SatkerInduk == 'Badan Pendidikan dan Pelatihan Pemeriksaan Keuangan Negara':
        SatkerInduk = 9
    elif SatkerInduk == 'Direktorat Utama Pembinaan dan Pengembangan Hukum Pemeriksaan Keuangan Negara':
        SatkerInduk = 10
    elif SatkerInduk == 'Direktorat Utama Perencanaan, Evaluasi, dan Pengembangan Pemeriksaan Keuangan Negara':
        SatkerInduk = 11
    elif SatkerInduk == 'Inspektorat Utama':
        SatkerInduk = 12
    elif SatkerInduk == 'Sekretariat Jenderal BPK RI':
        SatkerInduk = 13
    else :
        SatkerInduk = 14

    MasaKerja = st.slider("Masa Kerja",0,65)

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

    NamaJurusan = st.selectbox('Jurusan', ['Akuntansi','Bahasa & Sastra','Jurusan Lainnya','Manajemen','Teknik'])

    if NamaJurusan == 'Akuntansi':
        NamaJurusan = 0
    elif NamaJurusan == 'Bahasa & Sastra':
        NamaJurusan = 1
    elif NamaJurusan == 'Jurusan Lainnya':
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
    
    # code for Prediction
    prediksi = ''
    
    # creating a button for Prediction
    
    if st.button('SUBMIT'):
        prediksi = mutasi_prediction([FreqJamDiklat, NamaJabatan, SatkerInduk, MasaKerja,
       KodePangkat, NamaJurusan, NamaPendidikan])
        
        
    st.success(prediksi)


def mutasi_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    scaler = MinMaxScaler(feature_range = (0, 1))
    input_data_as_numpy_array_scaler = scaler.fit_transform(input_data_reshaped)

    prediction = loaded_model.predict(input_data_as_numpy_array_scaler)
    print(prediction)
    

    if (prediction[0] == 0):
      return 'Pegawai Tidak Mutasi'
    else:
      return 'Pegawai Di Mutasi'
    
    
    
    
if __name__ == '__main__':
    main()
