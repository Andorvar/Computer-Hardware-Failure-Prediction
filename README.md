# Tīkla uzbrukumu noteikšana, izmantojot mašīnmācīšanos

## 1. Projekta apraksts

Projekta mērķis ir izveidot mašīnmācīšanās modeli, kas spēj noteikt tīkla datplūsmas veidu un atšķirt parastu datplūsmu no DDoS uzbrukumiem.

Modelis izmanto tīkla datplūsmas parametrus, lai klasificētu savienojumus divās klasēs:
- `normal` - parasta tīkla datplūsma
- `attack` - DDoS uzbrukums

## 2. Izmantotie dati

Projektā izmantota CIC-IDS2017 datu kopa, ko izveidojis Canadian Institute for Cybersecurity.

Izmantotais fails: `Friday-WorkingHours-Afternoon-DDoS.pcap_ISCX.csv`.

Sākotnējā datu kopa saturēja 225745 ierakstus.

Pēc datu apstrādes tika izveidota izlase ar 1000 rindām un 79 kolonnām.

## 3. Izmantotās tehnoloģijas

- Python 3
- Pandas
- NumPy
- Scikit-learn

## 4. Projekta faili

- `dati/` - sākotnējā datu kopa un tās avots
- `dati/AVOTS.txt` - informācija par datu kopas avotu
- `dati/Friday-WorkingHours-Afternoon-DDoS.pcap_ISCX.csv` - sākotnējais datu fails
- `tīrīšana.py` - datu apstrāde un sagatavošana
- `modelis.py` - mašīnmācīšanās modeļa izveide un apmācība
- `parbaude.py` - apstrādāto datu pārbaude
- `tirs.csv` - apstrādātie dati
- `rezultati.md` - projekta rezultāti un secinājumi
- `README.md` - projekta apraksts un palaišanas instrukcijas

## 5. Programmas palaišana

Nepieciešamo bibliotēku instalēšana:

```bash
pip install pandas numpy scikit-learn
```

Datu apstrāde:

```bash
python tīrīšana.py
```

Apstrādāto datu pārbaude:

```bash
python parbaude.py
```

Modeļa apmācība un pārbaude:

```bash
python modelis.py
```

## 6. Modeļa rezultāti

Projektā tika salīdzināti divi modeļi:

| Modelis | Precizitāte |
|---|---:|
| Random Forest | 99,5% |
| Baseline | 57,5% |

Random Forest modelis sasniedza par 42 procentpunktiem augstāku precizitāti nekā bāzes modelis.

### Klasifikācijas kļūdu matrica

| Faktiskā klase | Normal | Attack |
|---|---:|---:|
| Normal | 85 | 0 |
| Attack | 1 | 114 |

Modelis pareizi klasificēja 199 no 200 testa piemēriem.

Viens DDoS uzbrukums tika kļūdaini klasificēts kā parasta datplūsma. Viltus trauksmes gadījumi netika konstatēti.

## 7. Secinājumi

Projekta laikā tika izveidots un apmācīts Random Forest klasifikācijas modelis tīkla uzbrukumu noteikšanai.

Modelis sasniedza 99,5% precizitāti, kas ir ievērojami labāks rezultāts nekā Baseline modelim ar 57,5% precizitāti.

Darba rezultāti parāda, ka mašīnmācīšanos var izmantot tīkla datplūsmas analīzei un DDoS uzbrukumu noteikšanai.

Turpmākai modeļa pārbaudei būtu nepieciešams izmantot lielāku datu kopu un pārbaudīt modeli ar neatkarīgiem tīkla datiem.