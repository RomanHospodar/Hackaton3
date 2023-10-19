# Hackathon

Vítejte v README pro hackathon, do kterého jste se přihlásili. Tento repozitář obsahuje vše, co budete potřebovat pro Vaši účast.

## Zdroje

### Trénovací Dataset

V tomto repozitáři jsme pro Vás předpřipravili složky pro trénovací dataset. Ten si prosím stáhněte ze sharepointu [zde](https://generali-my.sharepoint.com/personal/jsekula_cpas_cz/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjsekula%5Fcpas%5Fcz%2FDocuments%2Fsolar%5Fhackathon&view=0&OR=Teams%2DHL&CT=1696853214592&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzA5MDExMjI3OCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D) a zkopírujte do repozitáře. Upozornění: Pro větší soubory prosím nepoužívejte push na bitbucket.

### Skripty a soubory pro vyhodnocení

Další soubory, které se v repozitáři vyskytují, jsou popsané v sekci 'Vyhodnocení'.

### Zadání
Vaším cílem je vytvořit model, který bude na základě vstupního obrázku schopný rozpoznat, zda se na něm vyskytuje solární panel či nikoliv. Je to koncipováno jako klasifikační úloha. Kromě vytvoření modelu, očekáváme, že:

- Zahrnete soubor s modelem: prosíme, abyste svůj natrénovaný model uložili jako `model.joblib` nebo `model.pkl` (či případně jiný formát) a zahrnuli jej v odevzdaném řešení.

- Dokumentace: popište Váš projekt ve formě souboru `Documentation.md`. Chceme porozumět Vašemu myšlenkovému procesu a přístupu k řešení.

- `requirements.txt`: Vytvořte soubor requirements.txt, kde specifikujete verze všech použitých knihoven. Doporučujeme vytvořit a použít virtuální prostředí.

### Vyhodnocení

- Testovací soubory: naplníme vaši složku `test_set` testovacími obrázky.

- Skript pro vyhodnocení: spustíme skript `evaluate.py`, který projde obrázky v `test_set` a vytvoří soubor `test_preds.csv`. <b>Tento skript si doplňte sami, aby fungoval dle vašeho řešení.</b>

- Formát výstupu: predikční soubor `test_preds.csv` musí mít právě dva sloupce - `id` obsahující ID obrázku (podle jména) a `pred` obsahující predikci (0 = nemá panel, 1 = má panel).

- Příklady a ukázky: přidáváme ukázkové soubory, skript `evaluate.py`, a ukázku souboru `test_preds.csv` pro účely ladění a testování. Taktéž poskytujeme soubor `generate_sample_test_images.py`, kterým jsme vygenerovali ukázkové testovací příklady.

### Spuštění skriptu
Dbejte na to, abyste nám poskytli vše, co potřebujeme k spuštění vašeho skriptu, zejména `requirements.txt`.

Budeme vyhodnocovat vaše řešení následujícími kroky:
1) vytvoříme virtuální prostředí: `python -m venv venv`
2) aktivujeme virtuální prostředí: `venv\Scripts\activate`
3) spustíme `evaluate.py` příkazem: `python evaluate.py`, kterým dostaneme vás soubor `test_preds.csv`. Ten následně vyhodnotíme podle dosaženého F1 skóre. 

# Kontakt
Pokud jsme na něco zapomněli nebo máte jakékoliv další dotazy, neváhejte nás kontaktovat!