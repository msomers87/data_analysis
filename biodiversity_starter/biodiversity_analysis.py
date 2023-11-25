#%%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Laad de gegevens in DataFrames
observations = pd.read_csv('C:/Users/SMR/data_analysis/biodiversity_starter/observations.csv')
species_info = pd.read_csv('C:/Users/SMR/data_analysis/biodiversity_starter/species_info.csv')

# Combineer de DataFrames op basis van de kolom 'scientific_name'
observations_species = pd.merge(observations, species_info, on='scientific_name')
observations_species = observations_species[['scientific_name', 'common_names', 'category', 'conservation_status', 'park_name', 'observations']]

# Maak een bar plot van categorie van observaties
plt.figure(figsize=(10, 6))  # Optioneel: bepaal de grootte van het plot
sns.countplot(x='category', data=observations_species, order=observations_species['category'].value_counts().index)
plt.xticks(rotation=45)  # Optioneel: roteer de labels voor betere leesbaarheid
plt.show()

# Maak een bar plot van conservations status van observaties
plt.figure(figsize=(10, 6))  # Optioneel: bepaal de grootte van het plot
sns.countplot(x='conservation_status', data=observations_species, order=observations_species['conservation_status'].value_counts().index)
plt.xticks(rotation=45)  # Optioneel: roteer de labels voor betere leesbaarheid
plt.show()

# %%
