# Testausdokumentti


## Yksikkötestaus

Yksikkötestauksessa käytetään Unittest-kehystä. Yksikkötestit suoritetaan Compiler/src hakemiston koodille. Käyttölittymään liittyvä koodi jätetään yksikkötestauksen ulkopuolelle, koska se ei ole olennainen varsinaisen ohjelmalogiikan kannalta.


Automaattisilla testeillä testataan tässä vaiheessa (18.11.2025) eritysesti SyntaxTree-luokan toimintaa oikeanmuotoisilla syötteillä sekä DFA-luokan toimintaa erilaisilla säännöllisillä lausekkeilla. Näissä testeissä on pyritty erilaisia operaatioita ja sulkulausekkeita sisältävin syöttein varmistamaan, että ohjelma rakentaa syntaksipuun sekä dfa:n oikein. Lisäksi tässä vaiheessa testataan, että käyttäjän antaman syötteen validointi sekä sen muuttaminen infix-muotoon toimii oikein. Testauksessa käytetyt syötteet on pyritty valitsemaan siten, että erilaiset väärää muotoa olevat syötteet ovat edustettuina mahdollisimman kattavasti.

Testit voidaan ajaa testikattavuusraportin kera Compiler kansiossa komennolla

```bash
poetry run invoke coverage
```


### Testikattavuusraportti

Automaattisia testejä on 30 kappaletta. Testien haarautumakattavuus on 99%.

![Testikattavuusraportti](https://github.com/Kaabero/regular_expression_to_DFA/blob/main/dokumentaatio/kuvat/Testikattavuusraportti.png)

Testikattavuusraportti ajettu 18.11.2025

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

- Testattu, että ohjelma rakentaa syntaksipuun perusteella dfa:n oikein: 
    - Kun syötteenä on tyhjä merkki
    - Kun syötteenä on tyhjän merkin sisältävä lauseke
    - Kun syötteenä on lauseke, joka sisältää tähti, konkatenaatio ja union operaatiot
    - Kun syötteenä on vain yksi aakkostoon kuuluva merkki
    - Kun syötteenä on yksi aakkostoon kuuluva merkki sekä tähti operaattori
    - Kun syötteenä on säännöllinen lauseke, joka hyväksyy ne aakkoston {0, 1} parillisen mittaiset merkkijonot jotka päättyvät merkkiin 0 ja parittoman mittaiset merkkijonot, jotka päättyvät merkkiin 1.
    - Kun syötteenä on säännöllinen lauseke, joka hyväksyy ne aakkoston {a, b, c} merkkijonot, joissa ei esiinny osamerkkijonoa ab eikä ba.
    - Kun syötteenä on säännöllinen lauseke, joka hyväksyy ne aakkoston {0, 1, 2} merkkijonot, jotka eivät ala merkillä 0 ja joissa on pariton määrä merkkejä 1.
    


   

## Käyttöliittymän testaus

Käyttöliittymän toiminnot testataan myöhemmin mahdollisesti e2e-testien avulla.




