# Cântări Creștine pentru Videoproiector

Generator de prezentări PowerPoint pentru cântările de pe [cantari-crestine.com](https://cantari-crestine.com/).

## Cerințe

- Python 3.8 sau mai nou
- pip (Python package installer)

## Instalare

1. Clonați repository-ul:
```bash
git clone https://github.com/radio-crestin/cantari-crestine-videoproiector.git
cd cantari-crestine-videoproiector
```

2. Instalați dependențele Python:
```bash
pip install -r requirements.txt
```

## Utilizare

1. Descărcați cântările de pe cantari-crestine.com:
```bash
python download_songs.py
```

2. Generați prezentările PowerPoint:
```bash
python convert_to_pptx.py
```

3. Verificați rezultatele în directorul `data/pptx/`:
   - Fiecare categorie are propriul său director cu prezentări PowerPoint
   - Arhive zip pentru fiecare categorie
   - O arhivă zip cu toate cântările (`Toate cantarile crestine videoproiector.zip`)
   - Un fișier `index.html` pentru descărcarea arhivelor

## Structura arhivelor

- **CC.zip** - Carte Cântări BER
- **CT.zip** - Cântări tineret
- **COR.zip** - Cântări cor
- **J.zip** - Jubilate
- **CB.zip** - Cântări ale Bisericilor de peste veacuri
- **Toate cantarile crestine videoproiector.zip** - Toate cântările într-o singură arhivă

## Format prezentări

- Format 16:9
- Text centrat pe slide
- Mărime font: 40pt
- "Amin!" în colțul din dreapta jos pe ultimul slide
