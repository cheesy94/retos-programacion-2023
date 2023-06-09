# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.
#
# Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja

def play(game):
    
    scores = ["Love","15","30","40"]
    
    player1 = 0
    player2 = 0
    
    for point in game:
        
        if point=="P1":
            player1 += 1
        if point=="P2":
            player2 += 1
        
        diff = abs(player1-player2)
        
        if diff==0 and (player1>=3 or player2>=3):
            player1 = 3
            player2 = 3
            print("Deuce")
            continue               
            
        if player1>3 or player2>3:
            
            if diff==1:
                print("Advantage",point)
                continue
            
            if diff>=2:
                print("Winner",point)
                break
    
        print(scores[player1],"-",scores[player2])
        
    return


game = ["P1","P1","P2","P2","P1","P2","P1","P1"]

play(game)