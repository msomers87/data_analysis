import pandas as pd

# CSV laden in dataframe met puntkomma als scheidingsteken
kdv_dataset = pd.read_csv("C:\\Users\\SMR\\data_analysis\\kdv.csv", delimiter=';')

# Maak aparte kolommen voor elke unieke waarde in de 'Dag' kolom als boolean-kolommen
kdv_dataset = pd.get_dummies(kdv_dataset, columns=['Dag'])

# De volgorde van de kolommen wijzigen op basis van de dagen van de week
desired_order = ['Dag_Maandag', 'Dag_Dinsdag', 'Dag_Woensdag', 'Dag_Donderdag', 'Dag_Vrijdag']
kdv_dataset = kdv_dataset[[col for col in kdv_dataset.columns if col not in desired_order] + desired_order]

# Groepeer op unieke combinatie van 'groep', 'naam', 'geboortedatum' en 'datum_4jaar'
grouped = kdv_dataset.groupby(['Groep', 'Naam', 'Geboortedatum', 'Datum_4jaar']).max().reset_index()

# Nu zou je een rij per kind moeten hebben met True/False voor elke dag van de week
print(grouped.head())  # Laat de eerste paar rijen zien van het gegroepeerde dataframe

# Nu zou het dataframe de kolommen in de gewenste volgorde moeten hebben
#print(kdv_dataset.head())  # Laat de eerste paar rijen van het nieuwe dataframe zien

# Schrijf het gegroepeerde dataframe naar een nieuwe CSV-bestand
grouped.to_csv("C:\\Users\\SMR\\data_analysis\\gegroepeerd_kdv.csv", index=False)

