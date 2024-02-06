import pandas as pd
import tabula

def pdf_df(path_pdf):
    tables = tabula.read_pdf(path_pdf, pages="all", lattice=True)

    df_combined = pd.DataFrame()

    for table in tables:
        print(table)
        df = table.copy()
        df_combined = pd.concat([df_combined, df], ignore_index=True)

    return df_combined

path_pdf = './testPages3.pdf'

df_combined2 = pdf_df(path_pdf)
print(df_combined2)

df_combined2.to_excel("prueba2.xlsx", index=False)