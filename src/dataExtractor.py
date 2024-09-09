import pandas as pd
import json

class DataExtractor:
    def __init__(self, imposto, data_source):
        self.imposto = imposto
        self.data_source = data_source

    def extractor(self):
        df = pd.read_excel(self.data_source)

        # Clean up the 'EMPRESA' column
        df['EMPRESA'] = df['EMPRESA'].str.strip().replace('\u00a0', ' ')

        # Convert the 'TELEFONE' column to string
        df['TELEFONE'] = df['TELEFONE'].astype(str)

        # Extract the 'EMPRESA' and 'TELEFONE' columns
        data = df[['EMPRESA', 'TELEFONE']]

        # Convert the DataFrame to a dictionary
        contacts_dict = data.set_index('EMPRESA')['TELEFONE'].to_dict()

        return contacts_dict