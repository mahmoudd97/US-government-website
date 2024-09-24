#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import time
from datetime import datetime as dt
from IPython.display import display
from urllib.parse import urlparse

file_types = ['csv', 'excel', 'json']

def read_data():
    file_type = input('Choose file type: csv, excel, or json\n').lower()
    print('-'*60)
    
    while file_type not in file_types:
        print('Please choose a valid file type\n')
        file_type = input('Choose file type: csv, excel, or json\n').lower()
        print('-'*60)
    
    name_file = input('Enter file name:-')
    print('-'*60)
    
    while True:
        try:
            if file_type == 'csv':
                df = pd.read_csv(f'{name_file}.csv')
            elif file_type == 'excel':
                df = pd.read_excel(f'{name_file}.xlsx')
            elif file_type == 'json':
                df = pd.read_json(f'{name_file}.json', lines=True)
            return df
        except FileNotFoundError:
            print("File not found, please enter a valid file name.")
            name_file = input('Enter file name:-')

def missing_values(df, path, format_time):
    try:
        col = 'c,nk,gr,g,h,l,al,hh'
        col = col.split(',')
        df = df.drop(columns=col, errors='ignore')  # Ignore errors if columns not found
        print(f'Columns "{col}" have been deleted.\n')
        print('*'*60)
        
        # Handle URLs
        df['r'] = df['r'].apply(lambda i: urlparse(i).netloc if pd.notnull(i) else i)
        df['u'] = df['u'].apply(lambda i: urlparse(i).netloc if pd.notnull(i) else i)
        
        # Renaming columns
        col_name = 'a,tz,r,u,t,hc,cy'
        old_col = col_name.split(',')
        new_col = 'Web browser_Operating_system,Time zone,URL_comes,URL_where_the_user_headed_to,Timestamp_starts,Timestamp_exits,City'
        col_new = new_col.split(',')
        df = df.rename(columns=dict(zip(old_col, col_new)))
        print(f'Columns "{old_col}" have been renamed.\n')
        print('*'*60)
        
        # Split the 'Web browser_Operating_system' column into 'Web browser' and 'Operating system'
        df[['Web browser', 'Operating system']] = df['Web browser_Operating_system'].str.split('(',expand=True).drop(columns=2)
        df = df.drop(columns=['Web browser_Operating_system'])  # Remove the original combined column
        print('Column "Web browser_Operating_system" has been split into "Web browser" and "Operating system".\n')
        print('*'*60)
        
        # Convert timestamps if not in unix format
        if format_time != 'u':
            df['Timestamp_starts'] = pd.to_datetime(df['Timestamp_starts']).dt.strftime('%d-%m-%Y %H:%M')
            df['Timestamp_exits'] = pd.to_datetime(df['Timestamp_exits']).dt.strftime('%d-%m-%Y %H:%M')

        # Remove missing values and count them
        null_count = df.isnull().sum().sum()
        df = df.dropna()
        print(f'Missing values removed: {null_count}')
        
        # Save cleaned data
        file_save = f'{path}/cleaned_data.csv'
        df.to_csv(file_save, index=False)
        print(f'Data has been saved to "{file_save}".')
        display(df.head(1))
        print('*'*60)
    except Exception as e:
        print(f'Error: {e}')
    
    print('Data Shape After Cleaning:', df.shape)
    return df

def main():
    while True:
        df = read_data()
        start_time = time.time()
        path = input('Output path:-')  # Get path after reading data
        format_time = input('To show time in unix format enter "u", otherwise enter anything else: ').lower()
        df = missing_values(df, path, format_time)
        restart = input('\nWould you like to restart? Enter yes or no :- ')
        if restart.lower() != 'yes':
            print(f'Elapsed time: {round(time.time()-start_time, 4)} seconds')
            print('*'*60)
            break

main()


# In[ ]:





# In[ ]:




