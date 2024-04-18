import pandas as pd

df = pd.read_parquet(r'D:\ChromeDownload\train-00000-of-00053.parquet')

df.to_excel('output.xlsx', index=False)
