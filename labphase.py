# -*- coding: utf-8 -*-
"""LabPhase.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t7TcERSDPfgMZH65ydskhyyVmLbukvpL
"""

from pydrive.auth import GoogleAuth

from pydrive.drive import GoogleDrive

from google.colab import auth

from oauth2client.client import GoogleCredentials

auth.authenticate_user()

gauth = GoogleAuth()

gauth.credentials = GoogleCredentials.get_application_default()

drive = GoogleDrive(gauth)
# data_by_artist, data, data_by_genres, data_by_year, data_w_genres
id_list = ['13n6hvWTMIFM1-snta5_BWWKppiW2CMBU', '19Q95OpXrs3Z5xJ7Wg1_4ZcO3gTdSsUvy', '1WEBcdr1VMuKSq_Z7CNCIvsDCi9LUh-6c',
           '1Wg0_PblHBr_wOW_cuqtkz95Jb5o2y_Cs', '1vsXAQpVGCEZ3iZwEKduyMxR5zY79ltCr']
file_list = ['data_by_artist', 'data', 'data_by_genres', 'data_by_year', 'data_w_genres']
for idx in range(len(id_list)):
  file_download = drive.CreateFile({'id':id_list[idx]})
  file_download.GetContentFile(file_list[idx]+'.csv')

"""#**1. Read the data**"""

import pandas as pd

def read_data(files):
  for f in files:
    yield pd.read_csv(f+'.csv')

data_by_artist, data, data_by_genres, data_by_year, data_w_genres = read_data(file_list)

i = 0
for data in read_data(file_list):
  print(file_list[i])
  print(data)
  print('\n------------------------')
  i += 1

"""#**5. Display first two row of data, data_genre, year_data and artist _data**

#**data**
"""

data.head(2)

"""##**data_genre**"""

data_by_genres.head(2)

"""##**year_data**"""

data_by_year.head(2)

"""#**artists_data**"""

data_by_artist.head(2)

"""#**6. Retrieve information about data and genre_data**

##**infromation about data**
"""

data.info()

"""##**information about data_genre**"""

data_by_genres.info()

"""#**7. create decade column in data using apply() and lambda**"""

decade = data_by_year['year'].apply(lambda x: (x//10)*10)
data_by_year['decade'] = decade

data_by_year