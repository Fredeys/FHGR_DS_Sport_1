import pandas as pd

# Excel-Datei einlesen
df = pd.read_excel("/Users/michellearn/Documents/Privat/FHGR CDS/Data-Science/04_Projekt/Daten_edited/df_sleep_5min_mean.xlsx")

# Prüfen, welche Spalten verfügbar sind
print(df.columns)

# Gruppierung nach Datum und 5-Minuten-Intervall
# Wir nehmen die Mittelwerte der numerischen Spalten
numerical_cols = df.select_dtypes(include='number').columns
df_5min = df.groupby(['date', 'time_5min'])[numerical_cols].mean().reset_index()

# Neue Excel-Datei (oder neues Arbeitsblatt) erstellen
output_path = "/Users/michellearn/Documents/Privat/FHGR CDS/Data-Science/04_Projekt/Daten_edited/df_sleep_5min_mean.xlsx"

# In die bestehende Excel-Datei schreiben – in ein neues Sheet
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Originaldaten')
    df_5min.to_excel(writer, index=False, sheet_name='5min_Mittelwerte')

print(f"Neue Datei erstellt: {output_path}")