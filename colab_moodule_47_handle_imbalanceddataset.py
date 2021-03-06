# -*- coding: utf-8 -*-
"""colab_moodule_47_handle_imbalancedDataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MP9VXLv_K62QeJaH2x2m6ciT7uw8VEnI

Handle unequal dataset (unequal class distribution)
"""

#importing data dependency
import numpy as np
import pandas as pd

#loading the credit-card dataset
credit_card_dataset=pd.read_csv('/content/credit_data.csv')

credit_card_dataset.head()

credit_card_dataset['Class'].value_counts()

"""0-legit transaction
1-fraud transaction
"""

#seprating the legit and fraud transaction
legit=credit_card_dataset[credit_card_dataset.Class==0]

fraud=credit_card_dataset[credit_card_dataset.Class==1]
print(legit.shape)
print(fraud.shape)

#undersampling
#Building a sample dataset containing similar distribution of legit & fraud transaction
#number of fraud transaction =25

legit_sample=legit.sample(n=25)
print(legit_sample.shape)

#concatenate two DataFrame
new_dataset=pd.concat([legit_sample,fraud],axis=0)
new_dataset.head()

new_dataset.tail()

new_dataset['Class'].value_counts()

