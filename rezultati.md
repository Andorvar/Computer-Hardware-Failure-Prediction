# Tīkla uzbrukumu noteikšana, izmantojot mašīnmācīšanos

## 1. Projekta mērķis

Projekta mērķis ir izveidot mašīnmācīšanās modeli, kas spēj noteikt DDoS tīkla uzbrukumus un atšķirt tos no parastas tīkla datplūsmas.

## 2. Izmantotie dati

Projektā izmantota CIC-IDS2017 datu kopa, ko izveidojis Canadian Institute for Cybersecurity.

Izmantotais fails: `Friday-WorkingHours-Afternoon-DDoS.pcap_ISCX.csv`.

Sākotnējā datu kopa saturēja 225745 rindas. Pēc datu apstrādes tika izveidota izlase ar 1000 rindām un 79 kolonnām.

Dati tika sadalīti divās klasēs:
- normal - parasta tīkla datplūsma;
- attack - DDoS uzbrukumi.

## 3. Datu apstrāde

Datu apstrādei tika izmantota Python bibliotēka Pandas.

Apstrādes laikā:
- tika izņemti dublikāti;
- tika apstrādātas bezgalīgas vērtības;
- tika aizpildītas trūkstošās vērtības;
- tika atlasītas tikai divas nepieciešamās datplūsmas klases;
- tika izveidota 1000 rindu izlase, saglabājot klašu proporcijas.

Pēc apstrādes dati tika saglabāti failā `tirs.csv`.

## 4. Izmantotā mašīnmācīšanās metode

Modeļa izveidei tika izmantots Random Forest klasifikācijas algoritms.

Dati tika sadalīti apmācības un testa kopās:
- 80% datu tika izmantoti modeļa apmācībai;
- 20% datu tika izmantoti modeļa pārbaudei.

Modeļa rezultāti tika salīdzināti ar bāzes modeli (Baseline), kas vienmēr prognozē biežāk sastopamo klasi.

## 5. Rezultāti

Pēc modeļa apmācības tika iegūti šādi rezultāti:

| Modelis | Precizitāte |
|---|---:|
| Random Forest | 99,5% |
| Baseline | 57,5% |

Random Forest modelis uzrādīja par 42 procentpunktiem augstāku precizitāti nekā bāzes modelis.

### Klasifikācijas kļūdu matrica

| Faktiskā klase | Prognoze: normal | Prognoze: attack |
|---|---:|---:|
| normal | 85 | 0 |
| attack | 1 | 114 |

No 200 testa piemēriem modelis pareizi klasificēja 199 piemērus.

Viens DDoS uzbrukums tika kļūdaini klasificēts kā parasta datplūsma. Viltus trauksmes gadījumi netika konstatēti.

## 6. Rezultātu analīze

Iegūtie rezultāti liecina, ka Random Forest modelis veiksmīgi atšķir parastu tīkla datplūsmu no DDoS uzbrukumiem.

Salīdzinājumā ar Baseline modeli Random Forest uzrādīja ievērojami labāku rezultātu.

Tomēr tika izmantota tikai 1000 rindu izlase no sākotnējās datu kopas. Tāpēc iegūtā precizitāte vēl nepierāda, ka modelis tikpat labi darbosies ar citiem datiem vai reālā tīkla vidē.

### Modeļa izmantošana reālā sistēmā

Ja modelis prognozētu DDoS uzbrukumu, tīkla administratoram tiktu nosūtīts automātisks brīdinājums. Administrators pārbaudītu aizdomīgo datplūsmu un nepieciešamības gadījumā veiktu pasākumus uzbrukuma ierobežošanai.

### Klasifikācijas kļūdu sekas

Pirmais kļūdas veids ir viltus trauksme, kad parasta tīkla datplūsma tiek klasificēta kā uzbrukums. Šādā gadījumā administrators velti patērē laiku pārbaudei, un nevajadzīga datplūsmas ierobežošana var traucēt lietotājiem.

Otrais kļūdas veids ir nepamanīts uzbrukums, kad DDoS datplūsma tiek klasificēta kā parasta datplūsma. Tas var izraisīt tīkla pārslodzi un pakalpojumu nepieejamību.

Šajā gadījumā nepamanīts uzbrukums ir bīstamāks, jo tas var radīt tiešus traucējumus tīkla darbībā.

### Modeļa ierobežojumi

Šo modeli nedrīkst izmantot kā vienīgo pamatu automātiskai tīkla datplūsmas bloķēšanai. Modelis tika apmācīts ar ierobežotu datu izlasi no CIC-IDS2017 datu kopas, tāpēc tā prognozes ne vienmēr būs pareizas reālā tīkla vidē.

## 7. Secinājumi

Projekta laikā tika izveidots un apmācīts Random Forest klasifikācijas modelis tīkla uzbrukumu noteikšanai.

Modelis sasniedza 99,5% precizitāti, kas ir ievērojami labāks rezultāts nekā Baseline modelim ar 57,5% precizitāti.

Darba rezultāti parāda, ka mašīnmācīšanos var izmantot tīkla datplūsmas analīzei un DDoS uzbrukumu noteikšanai.

Turpmākai modeļa pārbaudei būtu nepieciešams izmantot lielāku datu kopu un pārbaudīt modeli ar neatkarīgiem tīkla datiem.

## 8. Pašvērtējums

Man izdevās apstrādāt tīkla datplūsmas datus un izveidot Random Forest klasifikācijas modeli. Neizdevās pārbaudīt modeli ar lielāku un neatkarīgu datu kopu, lai pārliecinātos par tā darbību dažādās situācijās. Nākamreiz izmantotu lielāku datu apjomu un veiktu papildu modeļa pārbaudes.