#d'aprés Thierry Parmentelat (https://app-learninglab.inria.fr/forums/moocpython/t/besoin-dun-peu-daide-avec-pandas/16849)
import pandas as pd
date = ["2022-01-01","2022-01-01","2022-01-01","2022-01-01","2022-01-01","2022-01-02","2022-01-02","2022-01-02","2022-01-02","2022-01-02","2022-01-02"]
fabricant = ["A","B","C","A","A","B","B","A","C","C","B"]
produit = ["S","T","U","V","V","R","R","Q","S","T","P"]
nombre=[2,1,4,2,3,7,1,5,5,6,1]
df = pd.DataFrame({"date":date, "fabricant":fabricant, "produit":produit, "nombre":nombre})
df.date=pd.to_datetime(df.date)

# somme si date = date et fabricant = fabricant
df.set_index(["date", "fabricant"], inplace= True)
df['total/fab/jour'] = df.groupby(['date', 'fabricant'])['nombre'].sum()
df.reset_index(inplace= True)

# nombre de produits fabriqués par jour et par fabricant
df.set_index(["date", "fabricant","produit"], inplace= True)
df['produit/fab/jour'] = df.groupby(['date', 'fabricant', 'produit'])['nombre'].sum()
df.reset_index(inplace= True)
