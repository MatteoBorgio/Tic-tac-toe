from random import shuffle

def inizializza_tabellone() -> list[list[str]]:
    """Crea e restituisce una matrice 3x3 vuota."""
    matrice = []
    for _ in range(3):
        riga = []
        for _ in range(3):
            riga.append('')
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
                if riga > len(tabellone) or riga < 0:
                    raise ValueError
                break
            except ValueError:
                print("Inserisci un numero valido!")
        while True:
            try:
                colonna = int(input("Inserisci la colonna in cui vuoi inserire il simbolo: "))
                if colonna > len(tabellone[0] or colonna < 0):
                    raise ValueError
                break
            except:
                print("Inserisci un numero valido!")
        if tabellone[riga][colonna] != '':
            print("Questa casella è già occupata!")
        else:
            tabellone[riga][colonna] = giocatore
            print(tabellone)
            return None
def verifica_vittoria(tabellone: list[list[str]], tris_vincente: list) -> bool:
    """Verifica se c'è un vincitore e restituisce True in caso affermativo."""
    for i in range(len(tabellone)):
        if tabellone[i][0] == tabellone[i][1] and tabellone[i][1] == tabellone[i][2]:
            tris_vincente = [tabellone[i][0], tabellone[i][0], tabellone[i][0]]
            return True
        elif tabellone[0][i] == tabellone[1][i] and tabellone[1][i] == tabellone[2][i]:
            tris_vincente = [tabellone[0][i], tabellone[0][i], tabellone[0][i]]
            return True
        elif tabellone[0][0] == tabellone[1][1] and tabellone[1][1] == tabellone[2][2]:
            tris_vincente = [tabellone[0][0], tabellone[0][0], tabellone[0][0]]
            return True
        elif tabellone[2][0] != ' ' and tabellone[2][0] == tabellone[1][1] and tabellone[1][1] == tabellone[0][2]:
            tris_vincente = [tabellone[0][2], tabellone[0][2], tabellone[0][2]]
            return True
    return False

def aggiorna_punteggio(giocatori: dict, tris_vincente: list) -> None:
    """Aggiorna il punteggio del giocatore vincente."""
    if tris_vincente:
        if tris_vincente[0] == giocatori["player1"]["simbolo"]:
            giocatori["player1"]["vittorie"] += 1
            print(f"Ha vinto {giocatori['player1']['nome']}!")
        elif tris_vincente[0] == giocatori["player2"]["simbolo"]:
            print(f"Ha vinto {giocatori['player2']['name2']}!")
            giocatori["player2"]["vittorie"] += 1
        else:
            print("Pareggio!")
    return None

def partita(giocatori: dict) -> None:
    """Gestisce il flusso principale del gioco, alternando i turni e determinando il risultato finale."""
    tris_vincente = []
    tabellone = inizializza_tabellone()
    turni = 0
    while True:
        turni += 1
        if turni > 3:
            if verifica_vittoria(tabellone, tris_vincente):
                break
        gioca_turno(tabellone, giocatori["player1"]["simbolo"])
        gioca_turno(tabellone, giocatori["player2"]["simbolo"])
        if any('' in riga for riga in tabellone) == False:
            break
    aggiorna_punteggio(giocatori, tris_vincente)

def main() -> None:
    """Gestisce la sfida al meglio dei tre e dichiara il vincitore finale."""
    print("Benvenuti in tic tac toe! \n")
    simboli = ["0", "X"]
    shuffle(simboli)
    name_player1 = input("Inserisci il nome del primo giocatore: ")
    name_player2 = input("Inserisci il nome del secondo giocatore: ")
    giocatori = {
        "player1": {
            "nome": name_player1,
            "simbolo": simboli[0]
            },
        "player2": {
            "nome": name_player2,
            "simbolo": simboli[1]
        }
    }
    partita(giocatori)

if __name__ == "__main__":
    main()
