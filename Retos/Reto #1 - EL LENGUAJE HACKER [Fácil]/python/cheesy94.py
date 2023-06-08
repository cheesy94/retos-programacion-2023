# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337").
# Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 

def natural2hacker(text):
    
    dictionary = {
        "a":"4",
        "b":"|3",
        "c":"[",
        "d":"|)",
        "e":"3",
        "f":"|=",
        "g":"6",
        "h":"#",
        "i":"1",
        "j":"_|",
        "k":"|<",
        "l":"1",
        "m":"/\/\\",
        "n":"/\/",
        "o":"0",
        "p":"?",
        "q":"9",
        "r":"12",
        "s":"5",
        "t":"7",
        "u":"(_)",
        "v":"\/",
        "w":"\/\/",
        "x":"><",
        "y":"`/",
        "z":"2"
    }
    
    text = text.lower()
    
    for lin,lout in dictionary.items():
        text = text.replace(lin,lout)
        
    return text

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et."

print(natural2hacker(text))