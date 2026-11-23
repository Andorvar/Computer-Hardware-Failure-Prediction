
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Nolasa sākotnējos datus no CSV faila
dati = pd.read_csv(
    "dati/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
    low_memory=False
)

# Noņem liekās atstarpes kolonnu nosaukumos, lai tos varētu pareizi izmantot kodā
dati.columns = dati.columns.str.strip()

print("DATU TĪRĪŠANA")
print("----------------------")
print("Rindu skaits pirms tīrīšanas:", len(dati))

# Izņem dublikātus, jo tie var ietekmēt modeļa apmācību
dati = dati.drop_duplicates()

# Aizstāj bezgalīgās vērtības ar trūkstošajām vērtībām,
# lai tās netraucētu datu apstrādei
dati = dati.replace([np.inf, -np.inf], np.nan)

# Sakārto klašu nosaukumus, lai vienādi nosaukumi neatšķirtos
dati["Label"] = dati["Label"].astype(str).str.strip().str.upper()

# Atstāj tikai parasto datplūsmu un DDoS uzbrukumus,
# jo projektā tiek atpazītas tikai šīs divas klases
dati = dati[dati["Label"].isin(["BENIGN", "DDOS"])]

# Nosaka skaitliskās kolonnas, lai varētu aizpildīt to trūkstošās vērtības
skaitliskas_kolonnas = dati.select_dtypes(include="number").columns

# Aizpilda trūkstošās skaitliskās vērtības ar mediānu,
# jo tā ir mazāk jutīga pret ļoti lielām vai mazām vērtībām
for kolonna in skaitliskas_kolonnas:
    dati[kolonna] = dati[kolonna].fillna(
        dati[kolonna].median()
    )

# Nosaka teksta kolonnas, izņemot Label, jo tā ir prognozējamā vērtība
teksta_kolonnas = dati.select_dtypes(include="object").columns.drop("Label")

# Aizpilda trūkstošās teksta vērtības ar biežāko vērtību,
# lai datos nepaliktu tukši lauki
for kolonna in teksta_kolonnas:
    moda = dati[kolonna].mode()
    if not moda.empty:
        dati[kolonna] = dati[kolonna].fillna(moda[0])

# Pārvērš klašu nosaukumus saprotamākā formā
dati["Label"] = dati["Label"].map({
    "BENIGN": "normal",
    "DDOS": "attack"
})

# Izveido 1000 rindu izlasi, saglabājot klašu proporcijas,
# lai abas klases būtu pārstāvētas līdzīgā proporcijā kā sākotnējos datos
izlase, _ = train_test_split(
    dati,
    train_size=1000,
    stratify=dati["Label"],
    random_state=42
)

# Saglabā apstrādātos datus atsevišķā failā, nemainot sākotnējo CSV
izlase.to_csv("tirs.csv", index=False)

print("\nRindu skaits pēc tīrīšanas:", len(izlase))
print("Apstrādāto datu izmērs:", izlase.shape)

print("\nKlašu sadalījums:")
print(izlase["Label"].value_counts())

print("\nDati saglabāti failā tirs.csv")
