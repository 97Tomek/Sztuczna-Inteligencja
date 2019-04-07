jablko(X) :- rozmiar(bmaly), ksztalt(okragly), (kolor(zielony) ; kolor(czerwony)), faktura(gladka), waga(blekka)
banan(X) :- rozmiar(bmaly), ksztalt(podluzny), kolor(zolty), faktura(gladka), waga(blekka)
cytryna(X) :- rozmiar(bmaly), ksztalt(owalny), kolor(zolty), faktura(chropowata), waga(blekka)
pomarancza(X) :- rozmiar(bmaly), ksztalt(okragly), kolor(pomaranczowy), faktura(chropowata), waga(blekka)
koszula(X) :- rozmiar(sredni), ksztalt(koszuli), kolor(_), faktura(_), waga(lekka)
spodnie(X) :- rozmiar(sredni), ksztalt(spodni), kolor(_), faktura(_), waga(dosclekka)
plaszcz(X) :- rozmiar(duzy), ksztalt(plaszcza), kolor(_), faktura(_), waga(srednia)
czapka(X) :- rozmiar(maly), ksztalt(czapki), kolor(_), faktura(_), waga(lekka)
odtwarzacz(X) :- rozmiar(maly), ksztalt(plaski), kolor(czarny), (faktura(chropowata) ; faktura(gladka)), waga(lekka)
telefon(X) :- rozmiar(bmaly), ksztalt(plaski), kolor(_), faktura(gladka), waga(lekka)
telewizor(X) :- rozmiar(duzy), (ksztalt(prostopadloscienny) ; ksztalt(plaski)), kolor(czarny), faktura(gladka), waga(bciez)
radio(X) :- rozmiar(sredni), ksztalt(plaski) , kolor(czarny), (faktura(chropowata) ; faktura(gladka)), waga(srednia)
