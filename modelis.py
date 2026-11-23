
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Nolasa apstradatos datus
dati = pd.read_csv("tirs.csv")

# Atdala ievades datus un prognozejamo vertibu
X = dati.drop(columns=["Label"])
y = dati["Label"]

# Sadala datus apmacibas un testa dalas
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Nosaka skaitliskas un teksta kolonnas
skaitliskas = X.select_dtypes(include="number").columns
teksta = X.select_dtypes(include="object").columns

# Sagatavo skaitliskos datus
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

skaitliska_apstrade = Pipeline([
    ("missing", SimpleImputer(strategy="median"))
])

teksta_apstrade = Pipeline([
    ("missing", SimpleImputer(strategy="most_frequent")),
    ("encode", OneHotEncoder(handle_unknown="ignore"))
])

apstrade = ColumnTransformer([
    ("skaitli", skaitliska_apstrade, skaitliskas),
    ("teksts", teksta_apstrade, teksta)
])

# Izveido Random Forest modeli
modelis = Pipeline([
    ("apstrade", apstrade),
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ))
])

# Apmacina modeli
modelis.fit(X_train, y_train)

# Veic prognozes
prognozes = modelis.predict(X_test)

# Aprēķina precizitati
modela_precizitate = accuracy_score(y_test, prognozes)

# Izveido bazes linijas modeli
baze = DummyClassifier(strategy="most_frequent")
baze.fit(X_train, y_train)

bazes_prognozes = baze.predict(X_test)
bazes_precizitate = accuracy_score(y_test, bazes_prognozes)

# Parada rezultatus
print("MODELA REZULTATI")
print("----------------------")
print("Random Forest precizitate:", round(modela_precizitate * 100, 2), "%")
print("Bazes linijas precizitate:", round(bazes_precizitate * 100, 2), "%")

# Parada klasifikacijas kludu matricu
print("\nKlasifikacijas kludu matrica:")
print(confusion_matrix(
    y_test,
    prognozes,
    labels=["normal", "attack"]
))
