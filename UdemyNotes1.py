df = pd.read_csv("../data/fb_prices.csv")
print(df.head())

"""
you get the table here
"""

df = df[['Date', 'Adj Close']]
print(df.head())

"""
get two columns to display
"""

df.rename(columns={'Date : date', 'Adj Close' : 'price_t'}, inplace = True)
"""
get two columns to display with different names
"""
print(df.head())

"""
Calculating returns
"""

"""create new column and store in the df variable (hard formula """
df['price_t-1'] = df['price_t].shift(1) #shift(1) is moving 1 index
print(df.head())

df['returns_manual'] = (df['price_t'] / df['price_t-1']) - 1
print(df.head())

"""this returns the end of the file"""
print(df.tail())

"""calcualte the percentage change"""
df['returns_pct_change_method'] = df['price_t'].pct_change(1)
print(df.head())

df['returns'] = (df['price_t'] / df['price_t'].shift(1)) - 1
print(df.head())

"""showing dates"""
df.set_index('date', inplace = True)
print(df.head())

""" price_t plots"""
df['price_t'.plot(12, 8))

""" return plots"""
df['returns'].plot(figsize=(12, 8))




"""we invest on what returns we will earn in the future rather than relying on historic returns"""













































