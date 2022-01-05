#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[3]:


aarti = pd.read_csv('spotify Aarti.csv')
navratri = pd.read_csv('spotify Navratri_songs.csv')
devotional = pd.read_csv('spotify---devotional song.csv')
assame = pd.read_csv('spotify_Assamese_music.csv')
bengali = pd.read_csv('spotify_Bengali_music.csv')
bhojpuri = pd.read_csv('spotify_Bhojpuri_music.csv')
english = pd.read_csv('spotify_English_music.csv')
malyalam = pd.read_csv('spotify_Malyalam_music.csv')
marathi = pd.read_csv('spotify_Marathi_music.csv')
hindi = pd.read_csv('spotify_musicdev.csv')
hindi2 = pd.read_csv('spotify_musicdev2.csv')
rajasthani = pd.read_csv('spotify_Rajasthani_music.csv')
telugu = pd.read_csv('spotify_Telugu_music.csv')


# ## DATA ANALYSIS

# In[4]:


aarti.shape, navratri.shape, devotional.shape, assame.shape, bengali.shape, bhojpuri.shape, english.shape, malyalam.shape, marathi.shape, hindi.shape, hindi2.shape, rajasthani.shape,telugu.shape


# In[5]:


aarti.dtypes, navratri.dtypes, devotional.dtypes, assame.dtypes, bengali.dtypes, bhojpuri.dtypes, english.dtypes, malyalam.dtypes, marathi.dtypes, hindi.dtypes, hindi2.dtypes, rajasthani.dtypes,telugu.dtypes


# In[6]:


aarti.isna().sum()


# In[7]:


navratri.isna().sum()


# In[8]:


devotional.isna().sum()


# In[9]:


assame.isna().sum()


# In[10]:


bengali.isna().sum()


# In[11]:


bhojpuri.isna().sum()


# In[12]:


english.isna().sum()


# In[13]:


malyalam.isna().sum()


# In[14]:


marathi.isna().sum()


# In[15]:


hindi.isna().sum()


# In[16]:


hindi2.isna().sum()


# In[17]:


rajasthani.isna().sum()


# In[18]:


telugu.isna().sum()


# In[19]:


# removing Null value from telugu song dataset
telugu.dropna(axis=0, how="any", inplace=True)
telugu.isna().sum()


# In[20]:


# checking dataset shape of telugu song after removing the Null value.
telugu.shape


# In[21]:


aarti.duplicated().sum() , navratri.duplicated().sum(),assame.duplicated().sum(), bengali.duplicated().sum(), bhojpuri.duplicated().sum(), english.duplicated().sum(), malyalam.duplicated().sum(), marathi.duplicated().sum(), hindi.duplicated().sum(), hindi2.duplicated().sum(),rajasthani.duplicated().sum(),telugu.duplicated().sum(), devotional.duplicated().sum()


# In[22]:


#dropping unwanted column.
aarti = aarti.drop(['track_number'], axis = 1)
aarti = aarti.drop(['uri'], axis = 1)

navratri = navratri.drop(['track_number'], axis = 1)
navratri = navratri.drop(['uri'], axis = 1)

assame = assame.drop(['track_number'], axis = 1)
assame = assame.drop(['uri'], axis = 1)

bengali = bengali.drop(['track_number'], axis = 1)
bengali = bengali.drop(['uri'], axis = 1)

bhojpuri = bhojpuri.drop(['track_number'], axis = 1)
bhojpuri = bhojpuri.drop(['uri'], axis = 1)

english = english.drop(['track_number'], axis = 1)
english = english.drop(['uri'], axis = 1)

malyalam = malyalam.drop(['track_number'], axis = 1)
malyalam = malyalam.drop(['uri'], axis = 1)

marathi = marathi.drop(['track_number'], axis = 1)
marathi = marathi.drop(['uri'], axis = 1)

hindi = hindi.drop(['track_number'], axis = 1)
hindi = hindi.drop(['uri'], axis = 1)

hindi2 = hindi2.drop(['track_number'], axis = 1)
hindi2 = hindi2.drop(['uri'], axis = 1)

rajasthani = rajasthani.drop(['track_number'], axis = 1)
rajasthani = rajasthani.drop(['uri'], axis = 1)

telugu = telugu.drop(['track_number'], axis = 1)
telugu = telugu.drop(['uri'], axis = 1)

devotional = devotional.drop(['track_number'], axis = 1)
devotional = devotional.drop(['uri'], axis = 1)


# In[23]:


corr1 = aarti.corr()
corr2 = navratri.corr()
corr3 = assame.corr()
corr4 = bengali.corr()
corr5 = bhojpuri.corr()
corr6 = english.corr()
corr7 = malyalam.corr()
corr8 = marathi.corr()
corr9 = hindi.corr()
corr10 = hindi2.corr()
corr11 = rajasthani.corr()
corr12 = telugu.corr()
corr13 = devotional.corr()


# In[24]:


aarti.describe()
navratri.describe()
assame.describe()
bengali.describe()
bhojpuri.describe()
english.describe()
malyalam.describe()
marathi.describe()
hindi.describe()
hindi2.describe()
rajasthani.describe()
telugu.describe()
devotional.describe()



# In[25]:


aarti.nunique()
navratri.nunique()
assame.nunique()
bengali.nunique()
bhojpuri.nunique()
english.nunique()
malyalam.nunique()
marathi.nunique()
hindi.nunique()
hindi2.nunique()
rajasthani.nunique()
telugu.nunique()
devotional.nunique()


# In[ ]:





# ## Model Building - Recommendation

# #### 1. Aarti Song

# In[26]:


aarti_pop = pd.DataFrame(aarti.groupby('name')['popularity'].mean())
aarti_pop


# In[27]:


aarti_matrix = aarti.pivot_table(index = 'album', columns = 'name', values ='popularity')
aarti_matrix.head()


# In[28]:


aarti_matrix2 = aarti_matrix.fillna(0)
aarti_matrix2


# In[29]:


aarti_pop.sort_values('popularity', ascending = False).head(10)


# In[30]:


abc1 = aarti_matrix2["Aarti Kije Hanuman"]


# In[31]:


similar_to_abc1 = aarti_matrix2.corrwith(abc1)
similar_to_abc1


# In[32]:


corr_abc1 = pd.DataFrame(similar_to_abc1 , columns=['corr'])
corr_abc1.dropna(inplace=True)
corr_abc1.head()


# In[33]:


corr_abc_aarti = corr_abc1.join(aarti_pop['popularity'])
corr_abc_aarti


# In[34]:


final_aarti = corr_abc_aarti[corr_abc_aarti['popularity']>40].sort_values(by='corr', ascending = False)
final_aarti


# In[35]:


final_aarti_1 = final_aarti.drop('corr', axis=1)
final_aar = final_aarti_1.head()
final_aar


# In[253]:


#final_aarti_2 = final_aarti_1.drop('popularity', axis=1)
#final_aarti_2


# In[ ]:





# In[ ]:





# #### 2. Navratri Song

# In[36]:


nav_pop = pd.DataFrame(navratri.groupby('name')['popularity'].mean())
nav_pop


# In[37]:


nav_matrix = navratri.pivot_table(index = 'album', columns = 'name', values ='popularity')
nav_matrix.head()


# In[38]:


nav_matrix2 = nav_matrix.fillna(0)
nav_matrix2.head()


# In[39]:


nav_pop.sort_values('popularity', ascending = False).head(10)


# In[40]:


abc2 = nav_matrix2["Sare Tirath Dham"]


# In[41]:


similar_to_abc2 = nav_matrix2.corrwith(abc2)
similar_to_abc2


# In[42]:


corr_abc2 = pd.DataFrame(similar_to_abc2 , columns=['corr'])
corr_abc2.dropna(inplace=True)
corr_abc2.head()


# In[43]:


corr_abc_nav = corr_abc2.join(nav_pop['popularity'])
corr_abc_nav


# In[44]:


final_nav = corr_abc_nav[corr_abc_nav['popularity']>10].sort_values(by='corr', ascending = False)
final_nav


# In[45]:


final_nav_1 = final_nav.drop('corr', axis=1)
final_nav_1


# In[46]:


#final_nav_2 = final_nav_1.drop('popularity', axis=1)
#final_nav_2


# In[ ]:





# #### Devotional Song

# In[47]:


# Devotional song
devo_pop = pd.DataFrame(devotional.groupby('name')['popularity'].mean())
devo_matrix = devotional.pivot_table(index='album', columns='name', values='popularity')
devo_matrix2 = devo_matrix.fillna(0)
devo_pop.sort_values('popularity', ascending=False).head(10)
abc3 = devo_matrix2["Radhe Radhe Govind"]
similar_to_abc3 = devo_matrix2.corrwith(abc3)
corr_abc3 = pd.DataFrame(similar_to_abc3, columns=['corr'])
corr_abc3.dropna(inplace=True)
corr_abc_devo = corr_abc3.join(devo_pop['popularity'])
final_devo = corr_abc_devo[corr_abc_devo['popularity'] > 12].sort_values(by='corr', ascending=False)
final_devo_1 = final_devo.drop('corr', axis=1)
final_devotional = final_devo_1.head()
final_devotional


# #### Assame Song

# In[48]:


assame_pop = pd.DataFrame(assame.groupby('name')['popularity'].mean())
assame_matrix = assame.pivot_table(index='album', columns='name', values='popularity')
assame_matrix2 = assame_matrix.fillna(0)
assame_pop.sort_values('popularity', ascending=False).head(10)
abc4 = assame_matrix2["Kemon Paibe Hori"]
similar_to_abc4 = assame_matrix2.corrwith(abc4)
corr_abc4 = pd.DataFrame(similar_to_abc4, columns=['corr'])
corr_abc4.dropna(inplace=True)
corr_abc_assame = corr_abc4.join(assame_pop['popularity'])
final_assame= corr_abc_assame[corr_abc_assame['popularity'] > 2].sort_values(by='corr', ascending=False)
final_assame_1 = final_assame.drop('corr', axis=1)
final_assame_1 = final_assame_1.head()
final_assame_1


# #### Bengali Song

# In[49]:


ben_pop = pd.DataFrame(bengali.groupby('name')['popularity'].mean())
ben_matrix = bengali.pivot_table(index='album', columns='name', values='popularity')
ben_matrix2 = ben_matrix.fillna(0)
ben_pop.sort_values('popularity', ascending=False).head(10)
abc5 = ben_matrix2["Sakhi Loke Bale Kalo"]
similar_to_abc5 = ben_matrix2.corrwith(abc5)
corr_abc5 = pd.DataFrame(similar_to_abc5, columns=['corr'])
corr_abc5.dropna(inplace=True)
corr_abc_ben = corr_abc5.join(ben_pop['popularity'])
final_ben = corr_abc_ben[corr_abc_ben['popularity'] > 5].sort_values(by='corr', ascending=False)
final_ben_1 = final_ben.drop('corr', axis=1)
final_bengali = final_ben_1.head()
final_bengali


# #### Bhojpuri Song

# In[50]:


bhoj_pop = pd.DataFrame(bhojpuri.groupby('name')['popularity'].mean())
bhoj_matrix = bhojpuri.pivot_table(index='album', columns='name', values='popularity')
bhoj_matrix2 = bhoj_matrix.fillna(0)
bhoj_pop.sort_values('popularity', ascending=False).head(10)
abc6 = bhoj_matrix2["Madaiya Keenaram Ki"]
similar_to_abc6 = bhoj_matrix2.corrwith(abc6)
corr_abc6 = pd.DataFrame(similar_to_abc6, columns=['corr'])
corr_abc6.dropna(inplace=True)
corr_abc_bhoj = corr_abc6.join(bhoj_pop['popularity'])
final_bhoj = corr_abc_bhoj[corr_abc_bhoj['popularity'] > 5].sort_values(by='corr', ascending=False)
final_bhojpuri_1 = final_bhoj.drop('corr', axis=1)
final_bhojpuri = final_bhojpuri_1.head()
final_bhojpuri


# #### English Song

# In[51]:


eng_pop = pd.DataFrame(english.groupby('name')['popularity'].mean())
eng_matrix = english.pivot_table(index='album', columns='name', values='popularity')
eng_matrix2 = eng_matrix.fillna(0)
eng_pop.sort_values('popularity', ascending=False).head(10)
abc7 = eng_matrix2["Surrounds Me - Live"]
similar_to_abc7 = eng_matrix2.corrwith(abc7)
corr_abc7 = pd.DataFrame(similar_to_abc7, columns=['corr'])
corr_abc7.dropna(inplace=True)
corr_abc_eng = corr_abc7.join(eng_pop['popularity'])
final_eng = corr_abc_eng[corr_abc_eng['popularity'] > 55].sort_values(by='corr', ascending=False)
final_english_1 = final_eng.drop('corr', axis=1)
final_english = final_english_1.head()
final_english


# #### Malyalam Song

# In[52]:


mal_pop = pd.DataFrame(malyalam.groupby('name')['popularity'].mean())
mal_matrix = malyalam.pivot_table(index='album', columns='name', values='popularity')
mal_matrix2 = mal_matrix.fillna(0)
mal_pop.sort_values('popularity', ascending=False).head(10)
abc8 = mal_matrix2["Ethramel"]
similar_to_abc8 = mal_matrix2.corrwith(abc8)
corr_abc8 = pd.DataFrame(similar_to_abc8, columns=['corr'])
corr_abc8.dropna(inplace=True)
corr_abc_mal = corr_abc8.join(mal_pop['popularity'])
final_mal = corr_abc_mal[corr_abc_mal['popularity'] > 5].sort_values(by='corr', ascending=False)
final_malyalam_1 = final_mal.drop('corr', axis=1)
final_malyalam= final_malyalam_1.head()
final_malyalam


# #### Marathi Song

# In[53]:


mara_pop = pd.DataFrame(marathi.groupby('name')['popularity'].mean())
mara_matrix = marathi.pivot_table(index='album', columns='name', values='popularity')
mara_matrix2 = mara_matrix.fillna(0)
mara_pop.sort_values('popularity', ascending=False).head(10)
abc9 = mara_matrix2["Hare Ram Hare Krishna (Dhun)"]
similar_to_abc9 = mara_matrix2.corrwith(abc9)
corr_abc9 = pd.DataFrame(similar_to_abc9, columns=['corr'])
corr_abc9.dropna(inplace=True)
corr_abc_mara = corr_abc9.join(mara_pop['popularity'])
final_mara = corr_abc_mara[corr_abc_mara['popularity'] > 5].sort_values(by='corr', ascending=False)        
final_marathi_1 = final_mara.drop('corr', axis=1)
final_marathi = final_marathi_1.head()
final_marathi


# #### Hindi Song

# In[54]:


hin_pop = pd.DataFrame(hindi.groupby('name')['popularity'].mean())
hin_matrix = hindi.pivot_table(index='album', columns='name', values='popularity')
hin_matrix2 = hin_matrix.fillna(0)
hin_pop.sort_values('popularity', ascending=False).head(10)
abc10 = hin_matrix2["KALAVATI"]
similar_to_abc10 = hin_matrix2.corrwith(abc10)
corr_abc10 = pd.DataFrame(similar_to_abc10, columns=['corr'])
corr_abc10.dropna(inplace=True)
corr_abc_hin = corr_abc10.join(hin_pop['popularity'])
final_hin = corr_abc_hin[corr_abc_hin['popularity'] > 5].sort_values(by='corr', ascending=False)
final_hindi_1 = final_hin.drop('corr', axis=1)
final_hindi = final_hindi_1.head()
final_hindi


# #### Hindi 2

# In[55]:


hin2_pop = pd.DataFrame(hindi2.groupby('name')['popularity'].mean())
hin2_matrix = hindi2.pivot_table(index='album', columns='name', values='popularity')
hin2_matrix2 = hin2_matrix.fillna(0)
hin2_pop.sort_values('popularity', ascending=False).head(10)
abc11 = hin2_matrix2["Vandhanam"]
similar_to_abc11 = hin2_matrix2.corrwith(abc11)
corr_abc11 = pd.DataFrame(similar_to_abc11, columns=['corr'])
corr_abc11.dropna(inplace=True)
corr_abc_hin2 = corr_abc11.join(hin2_pop['popularity'])
final_hin2 = corr_abc_hin2[corr_abc_hin2['popularity'] > 11].sort_values(by='corr', ascending=False)
final_hindi2_1 = final_hin2.drop('corr', axis=1)
final_hindi2 = final_hindi2_1.head()
final_hindi2


# #### Rajasthani Song

# In[56]:


rajas_pop = pd.DataFrame(rajasthani.groupby('name')['popularity'].mean())
rajas_matrix = rajasthani.pivot_table(index='album', columns='name', values='popularity')
rajas_matrix2 = rajas_matrix.fillna(0)
rajas_pop.sort_values('popularity', ascending=False).head(10)
abc12 = rajas_matrix2["Mor Ko Pankho"]
similar_to_abc12 = rajas_matrix2.corrwith(abc12)
corr_abc12 = pd.DataFrame(similar_to_abc12, columns=['corr'])
corr_abc12.dropna(inplace=True)
corr_abc_rajas = corr_abc12.join(rajas_pop['popularity'])
final_rajas = corr_abc_rajas[corr_abc_rajas['popularity'] > 5].sort_values(by='corr', ascending=False)
final_rajas_1 = final_rajas.drop('corr', axis=1)
final_rajasthani = final_rajas_1.head()
final_rajasthani


# #### Telugu Song

# In[101]:


tel_pop = pd.DataFrame(telugu.groupby('name')['popularity'].mean())
tel_matrix = telugu.pivot_table(index='album', columns='name', values='popularity')
tel_matrix2 = tel_matrix.fillna(0)
tel_pop.sort_values('popularity', ascending=False).head(10)
abc13 = tel_matrix2["Gaalilo Naa Brathuku"]
        #selected_song_name = st.selectbox('Song Name', telugu['name'].values)
        #abc13 = tel_matrix2[selected_song_name]
similar_to_abc13 = tel_matrix2.corrwith(abc13)
corr_abc13 = pd.DataFrame(similar_to_abc13, columns=['corr'])
corr_abc13.dropna(inplace=True)
corr_abc_tel = corr_abc13.join(tel_pop['popularity'])
final_tel = corr_abc_tel[corr_abc_tel['popularity'] > 5].sort_values(by='corr', ascending=False)
        #selected_song_popularity = st.selectbox('Popularity', telugu['popularity'].values)
        #final_tel = corr_abc_tel[corr_abc_tel['popularity'] > selected_song_popularity].sort_values(by='corr',
       #                                                                                                ascending=False)
final_telugu_1 = final_tel.drop('corr', axis=1)
final_telugu = final_telugu_1.head()
final_telugu


# In[ ]:




