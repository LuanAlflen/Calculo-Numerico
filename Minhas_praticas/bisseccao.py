def bisseccao(function, a, b, e):
    n=0
    an = a
    bn = b
    #ponto medio
    pn = an + (bn-an)/2
    #tolerancia
    en = (bn-an)/2
    # print("funcao: \n", function(pn))
    # print("tolerancia: \n", en)
    while function(pn) != 0 and en >= e:
        sinal = function(pn)*function(an)
        if(sinal >= 0):
            an = pn
        else:
            bn = pn
        # ponto medio
        pn = an + (bn - an) / 2
        # tolerancia
        en = (bn - an) / 2
        print("%3d          %.8f     %.6f" % (n, pn, en))
        n += 1

