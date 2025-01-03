import pandas as pd
import chardet

with open('./data.csv', 'rb') as f:
      f.readline()
      result = chardet.detect(f.read())
      print(result)

# df = pd.read_csv('./data.csv', encoding='utf-8-sig')
# df.head()