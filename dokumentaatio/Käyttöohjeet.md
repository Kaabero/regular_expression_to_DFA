# Käynnistysohjeet

Lataa sovellus koneellesi GitHubista ja siirry sen juurihakemistoon.

Siirry hakemistoon UI ja asenna riippuvuudet komennolla:

```bash
npm install
```
Siirry hakemistoon Compiler ja asenna riippuvuudet komennolla:

```bash
poetry install
```

Siirry juurihakemistoon ja käynnistä sovellus osoitteeseen http://localhost:5173/ komennolla:

```bash
bash ./start.sh
```

Suorita yksikkötestit hakemistossa Compiler komennolla:

```bash
poetry run invoke test
```

Luo yksikkötestien testikattavuusraportti hakemistossa Compiler komennolla:

```bash
poetry run invoke coverage
```

Sovelluksen ollessa käynnissä, suorita end to end -testit UI hakemistossa komennolla:

```bash
npm run test
```

Suorita tiedoston [.pylintrc](https://github.com/Kaabero/regular_expression_to_DFA/blob/main/Compiler/.pylintrc) määrittelemät tarkistukset hakemistossa Compiler komennolla:

```bash
poetry run invoke lint
```

# Käyttö

Ohjelmalle syötetään säännöllinen lauseke, josta ohjelma rakentaa ja näyttää käyttäjälle samat merkkijonot hyväksyvän deterministisen äärellisen automaatin (DFA). Säännöllisen lausekkeen sallitut operaatiot ovat yhdiste (|), konkatenaatio (jätetään merkitsemättä) sekä tähti (*). Aakkosto voi sisältää isoja ja pieniä kirjaimia (a-z ja A-Z) sekä numeroita. Lisäksi lauseke voi sisältää tyhjä merkin (€) sekä sulkumerkit. Sulkeita on käytettävä aina, kun * ja | -operaatioihin liittyvien operandien pituus ylittää yhden merkin. Säännöllisen lausekkeen syötön jälkeen sitä vastaavan DFA:n tietoja voi tarkastella joko tekstimuodossa tai kuvakaaviona valitsemalla haluttu esitystapa. Kaaviota on mahdollista tutkia tarkemmin lähentämällä, loitontamalla tai siirtämällä kaaviota sekä siirtelemällä tilojen sijainteja. Hyväksyvät tilat on väritetty vihreiksi ja aloitustila on merkitty tekstillä "Aloitustila".