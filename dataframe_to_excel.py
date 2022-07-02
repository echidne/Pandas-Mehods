import pandas as pd

# method1 (doesn't work with large dataframe)
df.to_excel("path/file.xlsx")

# method2 (with large dataframe but can take long time)
writer = pd.ExcelWriter("path/file.xlsx", engine="xlsxwriter")
df.to_excel(writer)
writer.save()
