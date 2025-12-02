# Kääntäjä säännöllisestä lausekkeesta DFA:ksi

[![codecov](https://codecov.io/gh/Kaabero/regular_expression_to_DFA/graph/badge.svg?token=3N53H23IEM)](https://codecov.io/gh/Kaabero/regular_expression_to_DFA)

![GitHub Actions](https://github.com/Kaabero/regular_expression_to_DFA/workflows/CI/badge.svg)

Projekti koskee Helsingin yliopiston Tietojenkäsittelytieteen kandiohjelman (TKT) aineopintojen harjoitustyötä (Algoritmit ja tekoäly). 

## Dokumentaatio
[Määrittelydokumentti](./dokumentaatio/M%C3%A4%C3%A4rittelydokumentti.md)

[Testausdokumentti](./dokumentaatio/Testausdokumentti.md)

[Toteutusdokumentti](./dokumentaatio/Toteutusdokumentti.md)

## Viikkoraportit

[Viikkoraportti 1](./dokumentaatio/Viikkoraportti1.md)

[Viikkoraportti 2](./dokumentaatio/Viikkoraportti2.md)

[Viikkoraportti 3](./dokumentaatio/Viikkoraportti3.md)

[Viikkoraportti 4](./dokumentaatio/Viikkoraportti4.md)

[Viikkoraportti 5](./dokumentaatio/Viikkoraportti5.md)

## Käynnistysohjeet

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

Suorita testit hakemistossa Compiler komennolla:

```bash
poetry run invoke test
```

Luo testikattavuusraportti hakemistossa Compiler komennolla:

```bash
poetry run invoke coverage
```

Suorita tiedoston [.pylintrc](https://github.com/Kaabero/regular_expression_to_DFA/blob/main/Compiler/.pylintrc) määrittelemät tarkistukset hakemistossa Compiler komennolla:

```bash
poetry run invoke lint
```

## Käyttö

Ohjelmalle syötetään säännöllinen lauseke, josta ohjelma rakentaa ja näyttää käyttäjälle samat merkkijonot hyväksyvän deterministisen äärellisen automaatin (DFA). Säännöllisen lausekkeen sallitut operaatiot ovat yhdiste (|), konkatenaatio (jätetään merkitsemättä) sekä tähti (*). Aakkosto voi sisältää isoja ja pieniä kirjaimia (a-z ja A-Z) sekä numeroita. Lisäksi lauseke voi sisältää tyhjä merkin (€) sekä sulkumerkit. Sulkeita on käytettävä aina, kun * ja | -operaatioihin liittyvien operandien pituus ylittää yhden merkin. 

