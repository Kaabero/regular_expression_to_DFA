# Määrittelydokumentti

Projekti koskee Helsingin yliopiston Tietojenkäsittelytieteen kandiohjelman (TKT) aineopintojen harjoitustyötä (Algoritmit ja tekoäly).   

## Aihe
Toteutetaan kääntäjä säännöllisestä lausekkeesta deterministiseksi äärelliseksi automaatiksi (DFA). Ohjelma ottaa syötteenä säännöllisen lausekkeen (aakkosto ∑ = {a,b} sekä operaatiot tähti, konkatenaatio ja yhdiste). Virhetilanteita ovat tyhjä syöte ja vääriä merkkejä sisältävät syötteet. Ohjelma tuottaa annetun säännöllisen lausekkeen perusteella DFA:n, joka hyväksyy samat merkkijonot kuin lauseke. Ohjelma tuottaa tulosteena muodostetun DFA:n, jossa tilat on merkitty ympyröinä ja siirtymät niiden välisillä nuolilla. 

## Toteutus (ydin)

DFA muodostetaan käyttämällä apuna syntaksipuuta (syntax tree), jolloin DFA voidaan määrittää ilman, että ensin muodostettaisiin epädeterministinen äärellinen automaatti (NFA). Syntaksipuu muodostetaan kuvaamaan syötteenä saadun säännöllisen lausekkeen rakennetta ja puuta käytetään DFA:n alkutilan, hyväksyvien tilojen, muiden tilojen sekä siirtymien määrittelemiseksi. 

## Tavoitteena olevat aika- ja tilavaativuudet

Lähteiden mukaan syntaksipuun avulla toteutetun kääntäjän aikavaativuus on O(2^n), sillä muodostetussa DFA:ssa voi pahimmassa tapauksessa olla 2^n eri tilaa.

## Ohjelmointikielet

Algoritmien ja kääntäjän ohjelmointikielenä on Python. Käyttöliittymä toteutetaan Reactilla ja JavaScriptillä. 

Voin vertaisarvioida Pythonilla tehtyjen projektien lisäksi myös JavaScriptillä ja TypeScriptillä tehtyjä projekteja.

## Projektin kieli

Projektin dokumentaatio toteutetaan suomen kielellä, mutta itse koodi ja muuttujanimet ovat englanniksi.


## Lähteet 

- [GeeksForGeeks: Regular Expressions, Regular Grammar and Regular Languages](https://www.geeksforgeeks.org/theory-of-computation/regular-expressions-regular-grammar-and-regular-languages/)
- [GeeksForGeeks: Regular Expression to DFA](https://www.geeksforgeeks.org/compiler-design/regular-expression-to-dfa/)
- [Stackoverflow: Time Complexity DFA construction from regex directly](https://stackoverflow.com/questions/21854074/time-complexity-dfa-construction-from-regex-directly)
- Tietojenkäsittelytieteen kandiohjelman opintojakson Laskennan mallit kurssimateriaali
- [Wikipedia: Deterministic finite automaton](https://en.wikipedia.org/wiki/Deterministic_finite_automaton)
