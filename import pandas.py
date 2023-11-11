import pandas

commute_df = pandas.read_csv('commute_data.csv')

commute_df.columns = ['State', 'Total commuters','FIPS Code']
print(commute_df.head())

