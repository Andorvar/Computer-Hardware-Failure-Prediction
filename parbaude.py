import pandas as pd

# Nolasa apstradatos datus
dati = pd.read_csv("tirs.csv")

print("APSTRADATO DATU PARBAUDE")
print("------------------------")

# Datu izmers
print("\nRindu un kolonnu skaits:", dati.shape)

# Kolonnu nosaukumi
print("\nKolonnu nosaukumi:")
print(dati.columns.tolist())

# Trukstosas vertibas
print("\nTrukstoso vertibu skaits:")
print(dati.isnull().sum().sum())

# Dublikati
print("\nDublikatu skaits:")
print(dati.duplicated().sum())

# Datu tipi
print("\nDatu tipi:")
print(dati.dtypes)

# Uzbrukumu sadalijums
print("\nUzbrukumu sadalijums:")
print(dati["Label"].value_counts())

print("\nParbaude pabeigta!")