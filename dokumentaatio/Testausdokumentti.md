# Testausdokumentti


## Yksikkötestaus

Yksikkötestauksessa käytetään Unittest-kehystä. Yksikkötestit suoritetaan Compiler/src hakemiston koodille. Käyttölittymään liittyvä koodi jätetään yksikkötestauksen ulkopuolelle, koska se ei ole olennainen varsinaisen ohjelmalogiikan kannalta.


Automaattisilla testeillä testataan tässä vaiheessa (12.11.2025) eritysesti SyntaxTree-luokan toimintaa oikeanmuotoisilla syötteillä. Näissä testeissä on pyritty erilaisia operaatioita ja sulkulausekkeita sisältävin syöttein varmistamaan, että ohjelma rakentaa syntaksi puun oikein. Lisäksi tässä vaiheessa testataan, että käyttäjän antaman syötteen validointi sekä sen muuttaminen infix-muotoon toimii oikein. Testauksessa käytetyt syötteet on pyritty valitsemaan siten, että erilaiset väärää muotoa olevat syötteet ovat edustettuina mahdollisimman kattavasti.

Testit voidaan ajaa testikattavuusraportin kera Compiler kansiossa komennolla

```bash
poetry run invoke coverage
```


### Testikattavuusraportti

Automaattisia testejä on 22 kappaletta. Testien haarautumakattavuus on 99%.

![Testikattavuusraportti](https://github.com/Kaabero/regular_expression_to_DFA/blob/main/dokumentaatio/kuvat/Testikattavuusraportti.png)

Testikattavuusraportti ajettu 12.11.2025

### Testitapaukset

- Testattu, että ohjelma nostaa virheen (ValueError) käyttäjän annettua syötteen seuraavissa tapauksissa:
    - Kielletty symboli
    - Tyhjä syöte
    - Syöte sisältää välilyöntejä
    - Tyhjä sulkulauseke ()
    - Virheellinen sulkujen, tähden * tai unionin | käyttö
    - Virheellinen alku- tai loppusymboli

- Testattu, että ohjelma muuttaa käyttäjän antaman syötteen infix-muotoon:
    - Ohjelma lisää sulkeet syötteen ympärille
    - Ohjelma lisää aakkoston symbolien, tähtioperaation sekä sulkevan sulkumerkin perään konkatenaatiomerkin (.)
    - Ohjelma lisää suluissa olevan syötteen perään konkatenaatiomerkin (.) sekä #-merkin.

- Testattu, että ohjelma rakentaa infix-muotoa olevasta säännöllisestä lausekkeesta syntaksipuun oikein: 
    - Solmuilla, joiden merkki on konkatenaatio tai yhdiste on aina kaksi lasta
    - Solmuilla, joiden merkki on tähti, on aina vain vasen lapsi
    - Solmuilla, joiden merkki on aakkoston symboli, ei ole lapsia
    - Ekvivalentit säännölliset lausekkeet tuottavat samanlaisen syntaksipuun
    - Solmujen nullable, firstpos, lastpos ja followpos arvot asettuvat oikein

   

## Käyttöliittymän testaus

Käyttöliittymän toiminnot testataan myöhemmin mahdollisesti e2e-testien avulla.




