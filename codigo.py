import random
import math
from scipy.special import erfinv

def hv():
    return 9999999999

NH = 50
tps = [hv() for i in range(0, NH)]
itea = [0 for i in range(0, NH)]
tpll = 0
t = 0
stea = 0
nho = 0
ns = 0
nt = 0
tf = 9999999
stll = 0
sts = 0
stp = 0
bc = 0
bi = 0
stea = 0

def prox_tps():
    min = hv()
    i = 0
    for j in range(0, NH):
        if tps[j] < min:
            i = j
            min = tps[j]
    return i

def asignar_itea():
    global tpll, sts, stll, stp, t, stea, nho, ns, nt, tf, bc, bi
    for i in range(0, NH):
        if tps[i] == hv() and itea[i] == hv():
            itea[i] = t

def procesar_bloque():
    global tpll, sts, stll, stp, t, stea, nho, ns, nt, tf, bc, bi
    nb = 0
    if NH <= ns:
        nb = NH
        bc += 1
    else:
        nb = ns
        bi += 1
    for i in range(0, nb):
        _tp = tp()
        tps[i] = t + _tp
        stp += _tp
        stea += t - itea[i]
        itea[i] = hv()
    nho = nb

def sumar_espera_activa():
    global tpll, sts, stll, stp, t, stea, nho, ns, nt, tf, bc, bi
    for i in range(0, NH):
        if itea[i] != hv():
            stea += t - itea[i]
            itea[i] = hv()

def ia():
    r = random.randint(0,99) / 100
    return int((math.log(-r+1)/-0.5574)*1000)

def tp():
    r = random.randint(1,99) / 100
    return int((36.9443+6.2993*((2**0.5)*erfinv(2*r-1)))*100)

def llegada():
    global tpll, sts, stll, stp, t, stea, nho, ns, nt, tf, bc, bi
    t = tpll
    stll += t
    tpll = t + ia()
    ns += 1
    nt += 1
    asignar_itea()
    if nho == 0:
        procesar_bloque()

def salida(i):
    global tpll, sts, stll, stp, t, stea, nho, ns, nt, tf, bc, bi
    t = tps[i]
    tps[i] = hv()
    sts += t
    nho -= 1
    ns -= 1
    if ns > nho:
        itea[i] = t
    if nho == 0 and ns >= 1:
        procesar_bloque()

def start():
    global tpll, sts, stll, stp, t, stea, nho, ns, nt, tf, bc, bi
    i = prox_tps()
    if tpll <= tps[i]:
        llegada()
    else:
        salida(i)
    if t < tf:
        return
    else:
        if ns > 0:
            tpll = hv()
            return
        else:
            sumar_espera_activa()
            pec = (sts - stll - stp) / nt
            pbc = (bc * 100) / (bc + bi)
            pea = stea / NH
            print(f"NH = {NH}; PEC = {pec}; PBC = {pbc}; PEA = {pea}")
            exit(1)

if __name__ == "__main__":
    while True:
        start()