# Crea un programa que calcule quién gana más partidas a
# piedra, papel, tijera, lagarto, spock.
# - El resultado puede ser "P1", "P2", "Tie"
# - El input es un listado de pares/jugadas

# piedra gana tijera, lagarto
# tijera gana lagarto, papel
# lagarto gana papel, spock
# papel gana spock, piedra
# spock gana piedra, tijera

def game(turno):
    
    options = ["piedra","tijera","lagarto","papel","spock"]
    
    p1 = options.index(turno[0])
    p2 = options.index(turno[1])
    
    if p1==p2:
        return 0
    
    if (abs(p1-p2)>2 and p1==max(p1,p2)) or (abs(p1-p2)<=2 and p1==min(p1,p2)):
        return 1
    
    return -1


plays = [("piedra","tijera"),("spock","piedra"),("lagarto","tijera"),("lagarto","tijera")]

score = 0
for p in plays:
    score += game(p)
    
if score>0:
    print("Player 1")
elif score<0:
    print("Player 2")
else:
    print("Tie")