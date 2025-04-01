from random import shuffle

def inizializza_tabellone() -> list[list[str]]:
    """Crea e restituisce una matrice 3x3 vuota."""
    matrice = []
    for _ in range(3):
        riga = []
        for _ in range(3):
            riga.append('_')
        matrice.append(riga)
    return matrice 

def mostra_tabellone(tabellone: list[list[str]]) -> None:
    """Stampa la griglia di gioco in modo leggibile."""
    for riga in tabellone:
        print(" ".join(riga))

def gioca_turno(tabellone: list[list[str]], giocatore: str) -> None:
    """Gestisce l'input del giocatore e aggiorna il tabellone."""
    while True:
        while True:
            try:
                riga = int(input("Inserisci la riga in cui vuoi inserire il simbolo: "))
                if riga >= len(tabellone) or riga < 0:
                    raise ValueError
                break
            except ValueError:
                print("Inserisci un numero valido!")
        while True:
            try:
                colonna = int(input("Inserisci la colonna in cui vuoi inserire il simbolo: "))
                if colonna >= len(tabellone[0]) or colonna < 0:
                    raise ValueError
                break
            except:
                print("Inserisci un numero valido!")
        if tabellone[riga][colonna] != '_':
            print("Questa casella è già occupata!")
        else:
            tabellone[riga][colonna] = giocatore
            return None
def verifica_vittoria(tabellone: list[list[str]]) -> None | str:
    """Verifica se c'è un vincitore e restituisce il segno vincente (X, O o None se non trova vincitori)"""
    for i in range(len(tabellone)):
        if tabellone[i][0] != '_' and tabellone[i][0] == tabellone[i][1] and tabellone[i][1] == tabellone[i][2]:
            return tabellone[i][0]
        elif tabellone[0][i] != '_' and tabellone[0][i] == tabellone[1][i] and tabellone[1][i] == tabellone[2][i]:
            return tabellone[0][i]
    if tabellone[0][0] != '_' and tabellone[0][0] == tabellone[1][1] and tabellone[1][1] == tabellone[2][2]:
        return tabellone[0][0]
    elif tabellone[2][0] != '_' and tabellone[2][0] == tabellone[1][1] and tabellone[1][1] == tabellone[0][2]:
        return tabellone[2][0]
    return None

def aggiorna_punteggio(giocatori: dict, segno_vincente: str) -> None:
    """Aggiorna il punteggio del giocatore vincente e stampa il vincitore."""

    for key in ["player1", "player2"]:
        if giocatori[key]["simbolo"] == segno_vincente:
            giocatori[key]["vittorie"] += 1
            print("")
            print(f"Ha vinto {giocatori[key]['nome']}!")
            return None
        
def partita(giocatori: dict, tabellone: list[list[str]]) -> None:
    """Gestisce il flusso principale del gioco, alternando i turni e determinando il risultato finale."""
    segno_vincente = None
    while True:
        gioca_turno(tabellone, giocatori["player1"]["simbolo"])
        mostra_tabellone(tabellone)
        segno_vincente = verifica_vittoria(tabellone)
        if segno_vincente is not None:
            break  
        if all('_' not in riga for riga in tabellone): 
            print("") 
            print("Pareggio!")  
            return  
        gioca_turno(tabellone, giocatori["player2"]["simbolo"])
        mostra_tabellone(tabellone)
        segno_vincente = verifica_vittoria(tabellone)
        if segno_vincente is not None:
            break  
        if all('_' not in riga for riga in tabellone):  
            print("")
            print("Pareggio!")  
            return 

    aggiorna_punteggio(giocatori, segno_vincente)

def main() -> None:
    """Gestisce la sfida al meglio dei tre e dichiara il vincitore finale."""
    print("Benvenuti in tic tac toe! \n")
    for i in range(3):
        tabellone = inizializza_tabellone()
        simboli = ["O", "X"]
        shuffle(simboli)
        name_player1 = input("Inserisci il nome del primo giocatore: ")
        name_player2 = input("Inserisci il nome del secondo giocatore: ")
        print("")
        giocatori = {
            "player1": {
                "nome": name_player1,
                "simbolo": simboli[0],
                "vittorie": 0
                },
            "player2": {
                "nome": name_player2,
                "simbolo": simboli[1],
                "vittorie": 0
            }
        }
        partita(giocatori, tabellone)
    if giocatori["player1"]["vittorie"] > giocatori["player2"]["vittorie"]:
        print("")
        print(f"Il vincitore è {giocatori['player1']['nome']} con {giocatori['player1']['vittorie']} vittorie!")
    elif giocatori["player1"]["vittorie"] < giocatori["player2"]["vittorie"]:
        print("")
        print(f"Il vincitore è {giocatori['player2']['nome']} con {giocatori['player2']['vittorie']} vittorie!")
    else:
        print("")
        print("Pareggio tra i due giocatori!")

if __name__ == "__main__":
    main()
