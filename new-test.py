import streamlit as st
import pandas as pd


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

def main():
    st.title('Song Recommendation App')
    st.subheader("Welcome to the Song App - You've selected the below Menu option")

    menu = ['Aarti','Navratri','Devotional','Assame','Bengali','Bhojpuri','English','Malyalam','Marathi','Hindi','Hindi2','Rajasthani','Telugu']
    choice = st.sidebar.selectbox ("Menu", menu)

    if choice == "Aarti":
        st.subheader("Aarti")
        aarti['name'].values


        # Aarti song
        aarti_pop = pd.DataFrame(aarti.groupby('name')['popularity'].mean())
        aarti_matrix = aarti.pivot_table(index='album', columns='name', values='popularity')
        aarti_matrix2 = aarti_matrix.fillna(0)
        aarti_pop.sort_values('popularity', ascending=False).head(10)
        #abc1 = aarti_matrix2["Aarti Kije Hanuman"]
        selected_song_name = st.selectbox('Song Name', aarti['name'].values)
        abc1 = aarti_matrix2[selected_song_name]
        similar_to_abc1 = aarti_matrix2.corrwith(abc1)
        corr_abc1 = pd.DataFrame(similar_to_abc1, columns=['corr'])
        corr_abc1.dropna(inplace=True)
        corr_abc_aarti = corr_abc1.join(aarti_pop['popularity'])
        #final_aarti = corr_abc_aarti[corr_abc_aarti['popularity'] > 10].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', aarti['popularity'].values)
        final_aar_1 = corr_abc_aarti[corr_abc_aarti['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                          ascending=False)
        final_aarti_1 = final_aar_1.drop('corr', axis=1)
        final_aarti = final_aarti_1.head()


        st.text('Selected Aarti Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_aarti)

    elif choice == "Navratri":
        st.subheader("Navratri")
        navratri['name'].values

        # Navratri Song
        nav_pop = pd.DataFrame(navratri.groupby('name')['popularity'].mean())
        nav_matrix = navratri.pivot_table(index='album', columns='name', values='popularity')
        nav_matrix2 = nav_matrix.fillna(0)
        nav_pop.sort_values('popularity', ascending=False).head(10)
        #abc2 = nav_matrix2["Aaj Tera Jagrata Mata"]
        selected_song_name = st.selectbox('Song Name', navratri['name'].values)
        abc2 = nav_matrix2[selected_song_name]
        similar_to_abc2 = nav_matrix2.corrwith(abc2)
        corr_abc2 = pd.DataFrame(similar_to_abc2, columns=['corr'])
        corr_abc2.dropna(inplace=True)
        corr_abc_nav = corr_abc2.join(nav_pop['popularity'])
        #final_nav = corr_abc_nav[corr_abc_nav['popularity'] > 10].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', navratri['popularity'].values)
        final_nav = corr_abc_nav[corr_abc_nav['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                         ascending=False)
        final_nav_1 = final_nav.drop('corr', axis=1)
        final_navratri = final_nav_1.head()


        st.text('Selected Navratri Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_navratri)


    elif choice == "Devotional":
        st.subheader("Devotional")
        devotional['name'].values

        # Devotional song
        devo_pop = pd.DataFrame(devotional.groupby('name')['popularity'].mean())
        devo_matrix = devotional.pivot_table(index='album', columns='name', values='popularity')
        devo_matrix2 = devo_matrix.fillna(0)
        devo_pop.sort_values('popularity', ascending=False).head(10)
        #abc3 = devo_matrix2["Aarti Shree Banke Bihari Ji"]
        selected_song_name = st.selectbox('Song Name', devotional['name'].values)
        abc3 = devo_matrix2[selected_song_name]
        similar_to_abc3 = devo_matrix2.corrwith(abc3)
        corr_abc3 = pd.DataFrame(similar_to_abc3, columns=['corr'])
        corr_abc3.dropna(inplace=True)
        corr_abc_devo = corr_abc3.join(devo_pop['popularity'])
        #final_devo = corr_abc_devo[corr_abc_devo['popularity'] > 10].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', devotional['popularity'].values)
        final_devo = corr_abc_devo[corr_abc_devo['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                             ascending=False)
        final_devo_1 = final_devo.drop('corr', axis=1)
        final_devotional = final_devo_1.head()


        st.text('Selected Devotional Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_devotional)

    elif choice == "Assame":
        st.subheader("Assame")
        assame['name'].values

        # Assame song
        assame_pop = pd.DataFrame(assame.groupby('name')['popularity'].mean())
        assame_matrix = assame.pivot_table(index='album', columns='name', values='popularity')
        assame_matrix2 = assame_matrix.fillna(0)
        assame_pop.sort_values('popularity', ascending=False).head(10)
        #abc4 = assame_matrix2["Ramo Gokhai"]
        selected_song_name = st.selectbox('Song Name', assame['name'].values)
        abc4 = assame_matrix2[selected_song_name]
        similar_to_abc4 = assame_matrix2.corrwith(abc4)
        corr_abc4 = pd.DataFrame(similar_to_abc4, columns=['corr'])
        corr_abc4.dropna(inplace=True)
        corr_abc_assame = corr_abc4.join(assame_pop['popularity'])
        #final_assame= corr_abc_assame[corr_abc_assame['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', assame['popularity'].values)
        final_assame_1 = corr_abc_assame[corr_abc_assame['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                             ascending=False)
        final_assame_1 = final_assame_1.drop('corr', axis=1)
        final_assame = final_assame_1.head()


        st.text('Selected Assame Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_assame)


    elif choice == "Bengali":
        st.subheader("Bengali")
        bengali['name'].values

        # Bengali song
        ben_pop = pd.DataFrame(bengali.groupby('name')['popularity'].mean())
        ben_matrix = bengali.pivot_table(index='album', columns='name', values='popularity')
        ben_matrix2 = ben_matrix.fillna(0)
        ben_pop.sort_values('popularity', ascending=False).head(10)
        #abc5 = ben_matrix2[""]
        selected_song_name = st.selectbox('Song Name', bengali['name'].values)
        abc5 = ben_matrix2[selected_song_name]
        similar_to_abc5 = ben_matrix2.corrwith(abc5)
        corr_abc5 = pd.DataFrame(similar_to_abc5, columns=['corr'])
        corr_abc5.dropna(inplace=True)
        corr_abc_ben = corr_abc5.join(ben_pop['popularity'])
        #final_ben = corr_abc_ben[corr_abc_ben['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', bengali['popularity'].values)
        final_ben = corr_abc_ben[corr_abc_ben['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                        ascending=False)
        final_ben_1 = final_ben.drop('corr', axis=1)
        final_bengali = final_ben_1.head()


        st.text('Selected Bengali Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_bengali)

    elif choice == "Bhojpuri":
        st.subheader("Bhojpuri")
        bhojpuri['name'].values

        # Bhojpuri song
        bhoj_pop = pd.DataFrame(bhojpuri.groupby('name')['popularity'].mean())
        bhoj_matrix = bhojpuri.pivot_table(index='album', columns='name', values='popularity')
        bhoj_matrix2 = bhoj_matrix.fillna(0)
        bhoj_pop.sort_values('popularity', ascending=False).head(10)
        #abc6 = bhoj_matrix2[""]
        selected_song_name = st.selectbox('Song Name', bhojpuri['name'].values)
        abc6 = bhoj_matrix2[selected_song_name]
        similar_to_abc6 = bhoj_matrix2.corrwith(abc6)
        corr_abc6 = pd.DataFrame(similar_to_abc6, columns=['corr'])
        corr_abc6.dropna(inplace=True)
        corr_abc_bhoj = corr_abc6.join(bhoj_pop['popularity'])
        #final_bhoj = corr_abc_bhoj[corr_abc_bhoj['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', bhojpuri['popularity'].values)
        final_bhoj = corr_abc_bhoj[corr_abc_bhoj['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                           ascending=False)

        final_bhojpuri_1 = final_bhoj.drop('corr', axis=1)
        final_bhojpuri = final_bhojpuri_1.head()

        st.text('Selected Bhojpuri Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_bhojpuri)


    elif choice == "English":
        st.subheader("English")
        english['name'].values

        # English song
        eng_pop = pd.DataFrame(english.groupby('name')['popularity'].mean())
        eng_matrix = english.pivot_table(index='album', columns='name', values='popularity')
        eng_matrix2 = eng_matrix.fillna(0)
        eng_pop.sort_values('popularity', ascending=False).head(10)
        #abc7 = eng_matrix2[""]
        selected_song_name = st.selectbox('Song Name', english['name'].values)
        abc7 = eng_matrix2[selected_song_name]
        similar_to_abc7 = eng_matrix2.corrwith(abc7)
        corr_abc7 = pd.DataFrame(similar_to_abc7, columns=['corr'])
        corr_abc7.dropna(inplace=True)
        corr_abc_eng = corr_abc7.join(eng_pop['popularity'])
        #final_eng = corr_abc_eng[corr_abc_eng['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', english['popularity'].values)
        final_eng = corr_abc_eng[corr_abc_eng['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                        ascending=False)
        final_english_1 = final_eng.drop('corr', axis=1)
        final_english = final_english_1.head()


        st.text('Selected English Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_english)


    elif choice == "Malyalam":
        st.subheader("Malyalam")
        malyalam['name'].values

        # Malyalam song
        mal_pop = pd.DataFrame(malyalam.groupby('name')['popularity'].mean())
        mal_matrix = malyalam.pivot_table(index='album', columns='name', values='popularity')
        mal_matrix2 = mal_matrix.fillna(0)
        mal_pop.sort_values('popularity', ascending=False).head(10)
        #abc8 = mal_matrix2[""]
        selected_song_name = st.selectbox('Song Name', malyalam['name'].values)
        abc8 = mal_matrix2[selected_song_name]
        similar_to_abc8 = mal_matrix2.corrwith(abc8)
        corr_abc8 = pd.DataFrame(similar_to_abc8, columns=['corr'])
        corr_abc8.dropna(inplace=True)
        corr_abc_mal = corr_abc8.join(mal_pop['popularity'])
        #final_mal = corr_abc_mal[corr_abc_mal['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', malyalam['popularity'].values)
        final_mal = corr_abc_mal[corr_abc_mal['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                         ascending=False)
        final_malyalam_1 = final_mal.drop('corr', axis=1)
        final_malyalam= final_malyalam_1.head()


        st.text('Selected Malyalam Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_malyalam)


    elif choice == "Marathi":
        st.subheader("Marathi")
        marathi['name'].values

        # Marathi song
        mara_pop = pd.DataFrame(marathi.groupby('name')['popularity'].mean())
        mara_matrix = marathi.pivot_table(index='album', columns='name', values='popularity')
        mara_matrix2 = mara_matrix.fillna(0)
        mara_pop.sort_values('popularity', ascending=False).head(10)
        #abc9 = mara_matrix2[""]
        selected_song_name = st.selectbox('Song Name', marathi['name'].values)
        abc9 = mara_matrix2[selected_song_name]
        similar_to_abc9 = mara_matrix2.corrwith(abc9)
        corr_abc9 = pd.DataFrame(similar_to_abc9, columns=['corr'])
        corr_abc9.dropna(inplace=True)
        corr_abc_mara = corr_abc9.join(mara_pop['popularity'])
        #final_mara = corr_abc_mara[corr_abc_mara['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', marathi['popularity'].values)
        final_mara = corr_abc_mara[corr_abc_mara['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                          ascending=False)
        final_marathi_1 = final_mara.drop('corr', axis=1)
        final_marathi = final_marathi_1.head()


        st.text('Selected Marathi Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_marathi)


    elif choice == "Hindi":
        st.subheader("Hindi")
        hindi['name'].values

        # Hindi song
        hin_pop = pd.DataFrame(hindi.groupby('name')['popularity'].mean())
        hin_matrix = hindi.pivot_table(index='album', columns='name', values='popularity')
        hin_matrix2 = hin_matrix.fillna(0)
        hin_pop.sort_values('popularity', ascending=False).head(10)
        #abc10 = hin_matrix2[""]
        selected_song_name = st.selectbox('Song Name', hindi['name'].values)
        abc10 = hin_matrix2[selected_song_name]
        similar_to_abc10 = hin_matrix2.corrwith(abc10)
        corr_abc10 = pd.DataFrame(similar_to_abc10, columns=['corr'])
        corr_abc10.dropna(inplace=True)
        corr_abc_hin = corr_abc10.join(hin_pop['popularity'])
        #final_hin = corr_abc_hin[corr_abc_hin['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', hindi['popularity'].values)
        final_hin = corr_abc_hin[corr_abc_hin['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                      ascending=False)
        final_hindi_1 = final_hin.drop('corr', axis=1)
        final_hindi = final_hindi_1.head()


        st.text('Selected Hindi Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_hindi)


    elif choice == "Hindi2":
        st.subheader("Hindi2")
        hindi2['name'].values

        # Hindi2 song
        hin2_pop = pd.DataFrame(hindi2.groupby('name')['popularity'].mean())
        hin2_matrix = hindi2.pivot_table(index='album', columns='name', values='popularity')
        hin2_matrix2 = hin2_matrix.fillna(0)
        hin2_pop.sort_values('popularity', ascending=False).head(10)
        #abc11 = hin2_matrix2[""]
        selected_song_name = st.selectbox('Song Name', hindi2['name'].values)
        abc11 = hin2_matrix2[selected_song_name]
        similar_to_abc11 = hin2_matrix2.corrwith(abc11)
        corr_abc11 = pd.DataFrame(similar_to_abc11, columns=['corr'])
        corr_abc11.dropna(inplace=True)
        corr_abc_hin2 = corr_abc11.join(hin2_pop['popularity'])
        #final_hin2 = corr_abc_hin2[corr_abc_hin2['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', hindi2['popularity'].values)
        final_hin2 = corr_abc_hin2[corr_abc_hin2['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                         ascending=False)

        final_hindi2_1 = final_hin2.drop('corr', axis=1)
        final_hindi2 = final_hindi2_1.head()

        st.text('Selected Hindi_2 Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_hindi2)


    elif choice == "Rajasthani":
        st.subheader("Rajasthani")
        rajasthani['name'].values

        # Rajasthani song
        rajas_pop = pd.DataFrame(rajasthani.groupby('name')['popularity'].mean())
        rajas_matrix = rajasthani.pivot_table(index='album', columns='name', values='popularity')
        rajas_matrix2 = rajas_matrix.fillna(0)
        rajas_pop.sort_values('popularity', ascending=False).head(10)
        #abc12 = rajas_matrix2[""]
        selected_song_name = st.selectbox('Song Name', rajasthani['name'].values)
        abc12 = rajas_matrix2[selected_song_name]
        similar_to_abc12 = rajas_matrix2.corrwith(abc12)
        corr_abc12 = pd.DataFrame(similar_to_abc12, columns=['corr'])
        corr_abc12.dropna(inplace=True)
        corr_abc_rajas = corr_abc12.join(rajas_pop['popularity'])
        #final_rajas = corr_abc_rajas[corr_abc_rajas['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', rajasthani['popularity'].values)
        final_rajas = corr_abc_rajas[corr_abc_rajas['popularity'] > selected_song_popularity].sort_values(
            by='corr',ascending=False)
        final_rajas_1 = final_rajas.drop('corr', axis=1)
        final_rajasthani = final_rajas_1.head()


        st.text('Selected Rajasthani Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_rajasthani)


    elif choice == "Telugu":
        st.subheader("Telugu")
        telugu['name'].values

        # Telugu song
        tel_pop = pd.DataFrame(telugu.groupby('name')['popularity'].mean())
        tel_matrix = telugu.pivot_table(index='album', columns='name', values='popularity')
        tel_matrix2 = tel_matrix.fillna(0)
        tel_pop.sort_values('popularity', ascending=False).head(10)
        #abc13 = tel_matrix2[""]
        selected_song_name = st.selectbox('Song Name', telugu['name'].values)
        abc13 = tel_matrix2[selected_song_name]
        similar_to_abc13 = tel_matrix2.corrwith(abc13)
        corr_abc13 = pd.DataFrame(similar_to_abc13, columns=['corr'])
        corr_abc13.dropna(inplace=True)
        corr_abc_tel = corr_abc13.join(tel_pop['popularity'])
        #final_tel = corr_abc_tel[corr_abc_tel['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity', telugu['popularity'].values)
        final_tel = corr_abc_tel[corr_abc_tel['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                       ascending=False)
        final_telugu_1 = final_tel.drop('corr', axis=1)
        final_telugu = final_telugu_1.head()


        st.text('Selected Telugu Song Is')
        st.write(selected_song_name)
        st.text('Top Popular songs are ')
        st.write(final_telugu)


if __name__ == '__main__':
    main()


