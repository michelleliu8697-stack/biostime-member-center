import pandas as pd

xl = pd.ExcelFile('e:/workbuddy/biostime-member-center/member-benefits.xlsx')
print('Sheets:', xl.sheet_names)

for name in xl.sheet_names:
    print(f'\n=== {name} ===')
    df = pd.read_excel(xl, sheet_name=name, header=None)
    print(df.to_string())
