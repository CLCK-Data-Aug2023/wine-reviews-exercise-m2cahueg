import pandas
import zipfile

with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as x:
   with x.open('winemag-data-130k-v2.csv') as y:
       dataframe = pandas.read_csv(y)
summary = dataframe.groupby('country').agg({'points': ['count', 'mean']})
summary.columns = ['count', 'points']
summary['points'] = summary['points'].round(1)
summary.to_csv('data/reviews-per-country.csv', index=True)