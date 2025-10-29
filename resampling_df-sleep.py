import pandas as pd
import numpy as np

# CSV einlesen
df = pd.read_csv("df_sleep.csv", dayfirst=True)

# Datum und Zeit zu einem kombinierten Zeitstempel zusammenführen
df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str), errors='coerce')

# Zeit auf 5-Minuten-Blöcke runden
df['time_5min'] = df['datetime'].dt.floor('5min')

# Numerische Spalten auswählen
numerical_cols = df.select_dtypes(include='number').columns

# Gruppieren nach Datum + 5-Minuten-Zeit und Mittelwert berechnen
df['date'] = pd.to_datetime(df['date']).dt.date
df_grouped = df.groupby(['date', 'time_5min'])[numerical_cols].mean().reset_index()

# Originaldaten mit den berechneten Mittelwerten zusammenführen
df_final = pd.merge(df, df_grouped, on=['date', 'time_5min'], suffixes=('', '_mean_5min'))

# Neue Excel-Datei exportieren
output_path = "df_sleep_5min_mean.xlsx"
df_final.to_excel(output_path, index=False)

print(f"Excel-Datei erfolgreich erstellt: {output_path}")