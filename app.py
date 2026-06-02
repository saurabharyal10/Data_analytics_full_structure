import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from sqlalchemy import create_engine

DATABASE_URL = f'postgresql://readonly_student:StudentRead123!@db.tyxjmbptftftcqgozyfc.supabase.co:5432/postgres'
engine = create_engine(DATABASE_URL)
query = """ SELECT
	t."name", t.album_id, a.title AS album_title, a2."name" AS artist_name,
	g."name" AS genre_name,
	mt."name" AS media_name,
	t.bytes, t.composer, t.genre_id, t.media_type_id, t.milliseconds, t.track_id, t.unit_price
 
    FROM track t
    JOIN album a
        ON t.album_id = a.album_id
    JOIN artist a2
        ON a2.artist_id = a.artist_id
    JOIN genre g
        ON g.genre_id = t.genre_id
    JOIN media_type mt
        ON mt.media_type_id = t.media_type_id """
 
df = pd.read_sql(query, engine)

df_count_by_genre = df.groupby('genre_name').agg(num_tracks = ('track_id', 'count')).reset_index()
print(df_count_by_genre)

fig, ax = plt.subplots()
sns.barplot(data=df_count_by_genre.sort_values('num_tracks', ascending=False), y="genre_name", x="num_tracks", ax=ax)
st.pyplot(fig)

artist = st.selectbox('Select artist', df['artist_name'].unique())
filtered_df = df[df['artist_name'] == artist]
st.dataframe(filtered_df[['name', 'album_title', 'artist_name', 'genre_name']])


# st.columns
# tukeys law
	
 
#  add more filters
#  add buttons
#  add slides
#  show more graphs