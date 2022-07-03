import pandas as pd
date = ["2022-01-01","2022-01-01","2022-01-01","2022-01-01","2022-01-01","2022-01-02","2022-01-02","2022-01-02","2022-01-02","2022-01-02","2022-01-02"]
fabricant = ["A","B","C","A","A","B","B","A","C","C","B"]
produit = ["S","T","U","V","V","R","R","Q","S","T","P"]
df = pd.DataFrame({"date":date, "fabricant":fabricant, "produit":produit})
df.date=pd.to_datetime(df.date)
# nombre de produits différents par fabricant par jour
df.set_index(['date','fabricant'], inplace= True)
df['type de produit par fabricant par jour'] = df.groupby(['date','fabricant'])['produit'].unique().str.len()
df.reset_index(inplace= True)
