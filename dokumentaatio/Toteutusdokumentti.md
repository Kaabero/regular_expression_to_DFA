# Toteutusdokumentti

## Ohjelman yleisrakenne

Sovellus on kääntäjä, joka annetun säännölisen lausekkeen perusteella tuottaa deterministisen äärellisen automaatin (DFA:n), joka hyväksyy samat merkkijonot, kuin lauseke. Ohjelma tarkistaa ensin käyttäjän antaman syötteen oikean muodon ja muuttaa sen sitten postfix-muotoon käyttäen hyväksi Shunting Yard -algorimtia. Postfix-muotoa olevasta lausekkeesta ohjelma muodostaa syntaksipuun, jonka perusteella se muodostaa deterministinen äärellisen automaatin. Käyttäjä voi tarkastella muodostetun DFA:n rakennetta käyttöliittymässä sekä tekstimuodossa että kaaviokuvana.

Varsinainen ohjelmalogiikka sijaitsee Compiler-hakemistossa. Tiedostossa main.py käytetään hyväksi FastAPIa vastaanottamaan käyttäjän syöttämä säännöllinen lauseke käyttöliittymän puolelta ja lopuksi lähettämään muodostettu DFA käyttöliittymän puolelle. Syötteen validointiin ja sen muodon muuntamiseen liittyvät funktiot sijatsevat tiedostossa utils.py, joka käyttää hyväkseen pinotietorakennetta kuvaavaa luokkaa Stack. Syntaksipuun rakentamista varten on ohjelmassa luokka SyntaxTree, joka hyödyntää puun muodostamisessa yksittäistä solmua kuvaavaa luokkaa Node. Lopullisen DFA:n muodostamista varten on ohjelmassa luokka DFA. Käyttöliittymään liittyvä koodi sijaitsee UI-hakemistossa.

## Aikavaativuudet

Syötteen validointi, muokkaaminen ja muuttaminen postfix-muotoon perustuvat syötteen läpikäyntiin ja ovat aikavaativuudeltaan O(n), missä n on syötteen koko. Pino-operaatiot toimivat aikavaativuudella O(1). Syntaksipuun rakentaminen perustuu muokatun syötteen läpikäyntiin ja on aikavaativuudeltaan O(m), missä m on muokatun syötteen pituus ja m > n. Syntaksipuun solmujen firtspos, lastpos ja nullable sekä followpos arvojen asettamisessa käydään läpi kaikki syntakipuun solmut ja käytetään rekursiota, joten näiden aikavaativuus on molempien O(k^2), missä k on solmujen määrä ja k <= n, eli pahimmillaan aikavaativuus on O(n^2). Syntaksipuun palautus sanakirjamuodossa perustuu puun jokaisen solmun läpikäyntiin ja on aikavaativuudeltaan pahimmillaan O(n). DFA:n rakentamisessa käydään läpi kaikki DFA:n tilat ja tilojen rakentamisessa käytetään rekursiota ja tällöin toiminnon aikavaativuus on pahimmillaan O(2^n), sillä tilojen lukumäärä on pahimmillaan 2^n. Lisäksi ohjelmakoodi sisältää muodostetun DFA:n muokkausta käyttöliittymän tarvitsemaan muotoon, mikä on jätetty tässä laskennassa huomiotta.


## Työn mahdolliset puutteet ja parannusehdotukset

Ohjelma voisi tukea kattavammin erilaisia operaatioita tähden, konkatenaation ja yhdisteen lisäksi. Tuotettu deterministinen automaatti ei myöskään ole aina tilamäärältään optimaalinen, vaan se voi sisältää ylimääräisiä tiloja, joita olisi mahdollista yhdistää. 


## Suurten kielimallien käyttö

- Käytin ChatGPT:tä suomentamaan minulle joitain lähteissä olevia kohtia
- Käytin ChatGPT:tä ehdottamaan, miten kommunikointi Pythonilla tehdyn backendin ja Reactilla+Javascriptillä tehdyn frontendin välillä kannattaa toteuttaa.
- Käytin ChatGPT:tä apuna joissain CSS-ongelmissa (info-ikoni)
- Käytin ChatGPT:tä apuna joissain ReactFlow-ongelmissa (symbolin asettelu)

## Käyteyt lähteet 

- [YouTube: RE to DFA Direct Method (Anita Ramesh)](https://www.youtube.com/watch?v=p5MbSZ4nBho)
- [Building a syntax tree from scratch using André’s Method (André Ovalle)](https://dev.to/andro095/building-a-syntax-tree-from-scratch-using-andres-method-5a54)
- [GeeksForGeeks: Regular Expression to DFA](https://www.geeksforgeeks.org/compiler-design/regular-expression-to-dfa/)
- [Stackoverflow: Time Complexity DFA construction from regex directly](https://stackoverflow.com/questions/21854074/time-complexity-dfa-construction-from-regex-directly)
- [ReactFlow](https://reactflow.dev/learn)
- [ReactFlow Custom Edges](https://reactflow.dev/examples/edges/custom-edges)