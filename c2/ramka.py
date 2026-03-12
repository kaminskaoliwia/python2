
# tekst - może być wielolinijkowy, ale linijki są tej samej długości
# znr - znak ramki
# znm - wypelnienie miedzy tekstem a ramką
# sz - szerokość marginesu

CZ1 = False
CZ2 = True

def ramka(tekst, znr, znm, sz):
    t = tekst.splitlines()
    n = max(len(linia) for linia in t)
    marg_1 = (znr*(n+2*sz)) + '\n' + (znr + 2*znm*(sz-1) + n*znm + znr + '\n' )*(sz-1) # margines górny/dolny
    marg_2 = znr + (sz-1)*znm # margines boczny
    s = marg_1
    
    for linia in t:
        linia = marg_2 + linia + marg_2[::-1] + '\n'
        s = s + linia
        
    s = s + marg_1[-2::-1]
    # dodanie marginesu dolnego zaczynając od przedostatniego elementu (-1 ostatni,
    # -2 przedostatni) od tyłu
    
    return s

def s_ramka(tekst, znr, znm, sz):
    r = ramka(tekst, znr, znm, sz)
    print('\n' + r + '\n')

if CZ1:
    T=['w'] + 5*['s']
    w = '#'.join(T)
    print(T)
    print(w)

if CZ2:
    txt = 'hej\nhej'
    txt1 = 'agh\nagh\nagh\n'
    a = s_ramka(txt, '0', '1', 3)
    b = s_ramka(txt1, '0','1', 4)
