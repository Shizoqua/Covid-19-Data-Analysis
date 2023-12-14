import pandas as pd
import requests
from io import StringIO
from sqlalchemy import create_engine
from dotenv import dotenv_values
import psycopg2

def get_database_connection():
    # Get database credentials from environment variable
    config = dict(dotenv_values('.env'))
    db_user_name = config.get('DB_USER_NAME')
    db_password = config.get('DB_PASSWORD')
    db_name = config.get('DB_NAME')
    port = config.get('PORT')
    host = config.get('HOST')
    # Create and return a postgresql database connection object
    return create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')

# Extraction from url 
def extract_data_from_url():
    url ='https://drive.google.com/file/d/1SzmRIwlpL5PrFuaUe_1TAcMV0HYHMD_b/view'
    file_id = url.split('/')[-2]
    dwn_url = f'https://drive.google.com/uc?export=download&id={file_id}'
    url2 = requests.get(dwn_url)
    csv_raw = StringIO(url2.text)
    covid_19_df = pd.read_csv(csv_raw)
    covid_19_df.columns = covid_19_df.columns.str.lower()
    covid_19_df.to_csv('covid_19_data.csv', index=False)
    print('data succefully written in csv file')

# Loading to PostgreSQL Database
def load_to_db():
    covid_19_df = pd.read_csv('covid_19_data.csv')
    covid_19_df.to_sql('covid_19_data', con = get_database_connection(), if_exists = 'replace', index=False)
    print('Data successfully written to PostgreSQL Database')

def main():
    extract_data_from_url()
    load_to_db()

main()



