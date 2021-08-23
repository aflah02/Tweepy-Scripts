import pandas as pd


with open('file.txt', encoding='utf-8') as f_in:
    lines = list(line for line in (l.strip() for l in f_in) if line)

df = pd.DataFrame(lines, columns=['ABC'])
print(df)
df.to_excel('ABC.xlsx')