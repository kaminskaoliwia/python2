# % jako znak interpolacji lancucha zamiast dzielenie z reszta
'ab%deg' % 11
'a%db%04de%-6df' % (4,12,134) # krotka
'%.4f %6s %.4s' % (123.456789, 'abc', '+X-' * 10) # kropka oznacza MAX ilosc znakow, sama 4 to MIN ilosc miejsca
'%.4f %6s %34.5s' % (123.456789, 'abc', '+X-' * 10)
'%d %d %d' % (1,2,3)

'%(zm1)d %(zm2)f %(zm1)5d' %{'zm1':123, 'zm2':3.1415} # słownik
'a{}b{}c'.format(1,"2",3.1415, 'x') # w przeciwienstwie do pozostalych, mozna podac wiecej argumentow, ktore zostana pominiete   
'a{1}b{3}c'.format(1,"2",3.1415, 'x') # indeksowanie
'a{1}b{zmienna}c'.format(1,"2",3.1415, 'x', zmienna = 'wielkosc do wyswietlenia', inne = 'pomin mnie')
'{0:o},{0:x},{0:#X}'.format(71)

zm = 108
f'A {zm} B' # wszystkie parametry musza byc dostarczone
f'A {1} B' # 1 nie oznacza juz indeksu, tylko wyrazenie
f'A {1 << 16} B' # wyrazenie musi zwracac jakis wynik
z='male litery'
f'A {z.upper()} B'
f'A {zm:f} B'
f'A {1 << 16:018} B'
# f'A {3.1415:s} B' nie da sie zamienic

zm5 = "108"
f'{zm5}, {zm5!s}, {zm5!r}, {zm!a}'

# print(zm) -> print(str(zm))
# zm -> rerp(zm)
# !a <-- funkcja ascii

f'{zm5}, {zm5!s:.2}'
f'{zm5:7}'
f'{zm5:>7}'
f'{zm5:^7}'
f'{zm5:*^7}'
# f'{zm5 = }
f'{zm*(12**4) =: 8,}'

# funkcja w matematyce = relacja, podzbior iloczynu kartezjanskiego, zbioru dziedziny i przeciwdziedziny,
# w ktorej dla kazdej pary jezeli pierwsza jest taka sama, to druga

# funkcja w informatyce = opis realizacji relacji jak przyporzadkowac jednej wartosci inna wartosc
# identyfikowina sekwencja instrukcji ktora moze byc wykonywana w dowolnym momencie

# funkcja w pythonie = obiekt, ktory przechowuje sekwencje

# "funkcja" ktora nie zwraca wynikow = procedura
# void = zwraca wynik ze zbioru pustego

# pass = nie jest funkcja ktora przypisuje wartosc
# None <- jedna instancja klasy NoneType
# python kazda funkcja zwraca jakis obiekt np None

# def = instrukcja 
# instrukcja prosta (dziala sama) vs zlozona (steruje wynikiem innych instrukcji) np if
