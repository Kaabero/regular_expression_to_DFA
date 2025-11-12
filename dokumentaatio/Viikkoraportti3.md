# Viikkoraportti 3

Viikon aluksi laadin toiminnallisuudet, joiden avulla syntaksipuun solmuille voidaan määrittää nullable, firstpos, lastpos ja followpos. Lisäsin SyntaxTree luokalle myös lisää yksikkötestejä. Seuraavana päivänä keskityin käyttöliittymän toimivuuteen: tein funktion, jolla validoidaan käyttäjän antaman syötteen oikea muoto ja toisen funtktion, jolla syöte muunnetaan syntaksipuun rakentamista varten oikeaan muotoon. Tein tähän liittyen myös yksikkötestejä. Lisäsin myös pylintin ylläpitämään koodin laatua. Käyttöliittymää koodasin hieman eteenpäin siten, että se kertoo, millaisia syötteitä ohjelma hyväksyy. Käyttäjälle myös näytetään tällä hetkellä syötetyn säännöllisen lausekkeen syntaksipuun rakenne tekstimuodossa.

Tällä viikolla opin erityisesti sen, miten syntaksipuun solmuille voidaan määrittää nullable, firstpos, lastpos ja followpos. Mielenkiintoista oli myös miettiä, miten tällaisissa ohjelmissa olisi hyvä toteuttaa yksikkötestausta. Olen hieman epävarma siitä, toimiikohan tähän mennessä toteuttamani ohjelma kaikissa tapauksissa oikein.


Seuraavaksi tarkoitus on alkaa muodostamaan syntaksipuun avulla DFA:ta. 


## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
| ----- | ------------- | ------ |
|10.11.  | 7 h            | Toiminnalisuus, jolla saadaan määritettyä solmuille nullable, firstpos, lastpos ja followpos. Testejä. |
|11.11.  | 7 h            | Käyttöliittymän parantelua ja syötteen validointia. Pylint. |
| 12.11 | 2 h | Testausdokumentti. Testejä.  |
| Yhteensä | 16 h         |        |