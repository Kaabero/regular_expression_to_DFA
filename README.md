# Kääntäjä säännöllisestä lausekkeesta DFA:ksi

[![codecov](https://codecov.io/gh/Kaabero/regular_expression_to_DFA/graph/badge.svg?token=3N53H23IEM)](https://codecov.io/gh/Kaabero/regular_expression_to_DFA)

![GitHub Actions](https://github.com/Kaabero/regular_expression_to_DFA/workflows/CI/badge.svg)

## Dokumentaatio
[Määrittelydokumentti](./dokumentaatio/M%C3%A4%C3%A4rittelydokumentti.md)

[Testausdokumentti](./dokumentaatio/Testausdokumentti.md)

[Toteutusdokumentti](./dokumentaatio/Toteutusdokumentti.md)

[Viikkoraportti 1](./dokumentaatio/Viikkoraportti1.md)

[Viikkoraportti 2](./dokumentaatio/Viikkoraportti2.md)

[Viikkoraportti 3](./dokumentaatio/Viikkoraportti3.md)

[Viikkoraportti 4](./dokumentaatio/Viikkoraportti4.md)

## Käynnistysohjeet

Lataa sovellus koneellesi GitHubista ja siirry sen juurihakemistoon.

Asenna riippuvuudet komennolla:

```bash
./setup.sh
```

Käynnistä sovellus osoitteeseen http://localhost:5173/ komennolla:

```bash
./start.sh
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

