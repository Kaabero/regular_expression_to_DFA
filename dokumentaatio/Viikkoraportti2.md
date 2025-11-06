# Viikkoraportti 2

Viikon aluksi yritin ensin ilman ohjeita muodostaa säännöllisestä lausekkeesta syntaksipuun. Tämä osoittautui hankalaksi, joten etsin ohjeet syntaksipuun muodostamiseksi. Loin ensin löytämieni ohjeiden avulla funktion, joka käyttää Shunting Yard algoritmia infix-muotoisen säännöllisen lausekkeen muuttamiseksi postfix-muotoon. Tämän jälkeen kirjoitin ohjeiden avulla funktion, joka rakentaa postfix-muodossa olevasta säännöllisestä lausekkeesta syntaksipuun. Ohjelmassa on siis nyt valmiina syntaksipuun muodostaminen. Laadin myös testejä syntaksipuuhun ja säännöllisen lausekkeen postfix-muotoon muuttamiseen liittyen. 

Opin tällä viikolla, että kaikkea ei kannata yrittää keksiä itse, vaan ohjeita seuraamalla pääsee pitkälle. Opin myös miten Shunting Yard algoritmi toimii. 

Olen hieman epävarma siitä, toimiikohan tähän mennessä toteuttamani algoritmi kaikissa tapauksissa oikein.

Seuraavaksi tarkoitus on alkaa määritäämään solmuille nullable, firstpos, lastpos ja followpos. Followpos tuntuu tässä vaiheessa näistä epäselvimmältä. 


## Tuntikirjanpito

| Päivä | Käytetty aika | Kuvaus |
| ----- | ------------- | ------ |
|4.11.  | 7 h            | Syntaksipuun muodostamisen yritelmiä |
|5.11.  | 2 h            | Funktio säännöllisen lausekkeen saamiseksi postfix-muotoon |
| 6.11 | 7 h | Syntaksipuun muodostaminen postfix-muotoa olevasta säännöllisestä lausekkeesta. Testejä.  |
| Yhteensä | 16 h         |        |