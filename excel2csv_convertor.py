"""
excel파일 xlsx를 csv로 변환
"""
import pandas as pd

df = pd.read_excel('.xlsx')  # sheetname is optional
df.to_csv('output_file_name', index=False)  # index=False prevents pandas to write row index

# oneliner
pd.read_excel('.xlsx').to_csv('.csv', index=False)

