from pandas_datareader import data

df = data.DataReader('2158.JP', 'stooq')

# df = web.DataReader('2158.JP', 'stooq')

df.to_csv('./output_sumitomo.csv')

print('finish')