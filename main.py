def calcule_lancer(lancer):
    if len(lancer) > 1:
        return len(lancer)
    else:
        return lancer[0]

def calcule_multiple_lancers(lancers):
    score = 0
    for lancer in lancers:
        score += calcule_lancer(lancer)
        if score > 50:
            score = 25
    return score

def est_gagnant(lancers):
    return calcule_multiple_lancers(lancers) == 50

def est_elimine(lancers):
    rate_affile = 0
    for lancer in lancers:
        if len(lancer) == 0:
            rate_affile += 1
        else:
            rate_affile = 0

        if rate_affile == 3:
            return True
    return False 
