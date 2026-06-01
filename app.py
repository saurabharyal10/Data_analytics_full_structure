import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

from sqlalchemy import create_engine

DATABASE_URL = f'postgresql://readonly_student:StudentRead123!@db.tyxjmbptftftcqgozyfc.supabase.co:5432/postgres'
engine = create_engine(DATABASE_URL)
df_artists = pd.read_sql("SELECT * FROM artist LIMIT 5", engine)
print(df_artists)

