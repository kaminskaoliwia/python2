# obsługa programu interaktywnego IDLE
# alt + p <-- przeglądanie cykliczne
# alt + n <-- przeglądanie zwykłe
# kursor na poprzedniej linijce + enter <-- skopiowanie zawartości
# alt + 3 <-- zakomentowanie

# konwencja spacje vs tabulatory, zaleca się 4 spacje
#! rozdzielamy generacje od prezentacji

CZ1 = False
CZ2 = True

def trojkat_GL(N):
    T = s_trojkat_GL(N)
    print(T)

def s_trojkat_GL(N):
    s=""
    for i in range(N):
        s = s + "*"*(N-i) + " "*i + "\n"
    return s

def trojkat_DP(N):
    T = s_trojkat_GL(N)
    print(T[::-1])

def trojkat_DL(N):
    T = s_trojkat_GL(N)
    linie = T.splitlines()
    for linia in linie[::-1]:
        print(linia)

def trojkat_GP(N):
    T = s_trojkat_GL(N)
    linie = T.splitlines()
    for linia in linie:
        print(linia[::-1])

if CZ1:
    t1 = trojkat_GL(5)
    t2 = trojkat_GL(10)

if CZ2:
    t3 = trojkat_DL(6)
    t4 = trojkat_DP(20)
    print('\n')
    t5 = trojkat_GP(16)
