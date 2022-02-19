# -*- coding: utf-8 -*-
"""colab_Module41_42.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hpSapd_b-bE4AJJTmPSvFc_kV4W0IfZZ
"""

import pandas as pd

#Loading a dataset to a pandas datafreame
dataset=pd.read_csv('/content/housing.csv')
dataset.head()

#uploading kaggel.json file
#Configuring the path of kaggle.json file
! mkdir -p ~/.kaggle/
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

! kaggle competitions download -c titanic

#extracting the compressed Dataset (when file is ZipFile)
##from zipfile import ZipFile
#dataset = "/content/train.csv"
#with ZipFile(dataset, 'r') as zip:
 # zip.extractall()
  #print('The dataset is extracted')

