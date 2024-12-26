def main1(list):

    düz_liste = []
    
    for a in list:
        if isinstance(a, list):
            düz_liste.extend(main1(a))
        else:
            düz_liste.append(a)
    
    return düz_liste

def main2(list):
    
    ters_liste = []

    for a in reversed(list):
        if isinstance(a, list):
            ters_liste.append(main2(a))
        else:
            ters_liste.append(a)

    return ters_liste
