import pandas as pd
import os

path = os.path.join(os.getcwd(), "files", 'rcer-2015.pdf_76.xlsx')

df = pd.read_excel(path)
df = df.rename(columns={'PARAMETER(4)': 'PARAMETER', 'UNITS': 'unit' ,'Maximum Allowable': 'limt'})

df['limt'] = pd.to_numeric(df['limt'], errors='coerce')

def check_for_exceedance(parameter, unit, concentration):
    exceeded = False
    
    filtered = df[(df['PARAMETER'] == parameter) & 
                     (df['unit'] == unit) &
                     (df['limt'] < concentration)]
    
    if not filtered.empty:
        exceeded = True
        print(f"Exceedance found for parameter: {parameter}")
    else:
        print(f"No exceedance found for parameter: {parameter}")

print("This script filters data and checks for exceedances bassed on RCER-2015 Regulations within given data.")



check_for_exceedance('Aluminum', "mg/l", 25)
