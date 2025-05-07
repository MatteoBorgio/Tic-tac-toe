from random import shuffle
from random import choice
from copy import deepcopy

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
    print("")

def trova_mosse_possibili(tabellone: list[list[str]]) -> list[tuple[int, int]]:
    """Restituisce una lista di tuple contenenti le posizioni vuote nel tabellone"""
    mosse_possibili = []
    for i in range(len(tabellone)):
        for j in range(len(tabellone[i])):
            if tabellone[i][j] == '_':
                mosse_possibili.append((i, j))
    return mosse_possibili

def turno_bot(tabellone: list[list[str]], simbolo: str, simbolo_avversario: str, mosse_possibili:list[tuple[int, int]]) -> None:
    """Gestisce il turno del bot, che seleziona una mossa casuale, a meno che non ci sia una mossa vincente o perdente."""
    copia_tabellone = deepcopy(tabellone)
    for mossa in mosse_possibili:
        riga, colonna = mossa
        copia_tabellone[riga][colonna] = simbolo
        if verifica_vittoria(copia_tabellone) == simbolo:
            tabellone[riga][colonna] = simbolo
            return None
        copia_tabellone[riga][colonna] = '_'
        copia_tabellone[riga][colonna] = simbolo_avversario
        if verifica_vittoria(copia_tabellone) == simbolo_avversario:
            tabellone[riga][colonna] = simbolo
            return None
        copia_tabellone[riga][colonna] = '_'
        if tabellone[1][1] == '_':
            tabellone[1][1] = simbolo
            return None
    riga, colonna = choice(mosse_possibili)
    tabellone[riga][colonna] = simbolo
    return None

def turno_umano(tabellone: list[list[str]], giocatore: str) -> None:
    """Gestisce l'input del giocatore e aggiorna il tabellone."""
    while True:
        while True:
            try:
                riga = int(input("Inserisci la riga in cui vuoi inserire il simbolo: ")) 
                if (riga) >= len(tabellone) + 1 or riga < 1:
                    raise ValueError
                break
            except ValueError:
                print("Inserisci un numero valido!")
        while True:
            try:
                colonna = int(input("Inserisci la colonna in cui vuoi inserire il simbolo: "))
                print("")
                if colonna >= len(tabellone[0]) + 1 or colonna < 1:
                    raise ValueError
                break
            except:
                print("Inserisci un numero valido!")
        if tabellone[riga - 1][colonna - 1] != '_':
            print("Questa casella è già occupata!\n")
        else:
            tabellone[riga - 1][colonna - 1] = giocatore
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
    for key in ["umano", "bot"]:
        if giocatori[key]["simbolo"] == segno_vincente:
            giocatori[key]["vittorie"] += 1
            print("")
            print(f"Ha vinto {giocatori[key]['nome']}!\n")
            print(f"{giocatori[key]['nome']} ora ha {giocatori[key]['vittorie']}!")
            print("")
            return None

def trova_vincitore(tabellone: list[list[str]]) -> str|None:
        segno_vincente = verifica_vittoria(tabellone)
        if segno_vincente is not None:
            return segno_vincente
        if all('_' not in riga for riga in tabellone):
            return "pareggio"
        return None
        
def gioca_turno(tabellone: list[list[str]], giocatore: dict, segno_avversario: str) -> None:
    if giocatore["nome"] == "bot":
        print("Turno del bot: \n")
        turno_bot(tabellone, giocatore["simbolo"], segno_avversario, trova_mosse_possibili(tabellone))
    else:
        turno_umano(tabellone, giocatore["simbolo"])
    mostra_tabellone(tabellone)

def partita(giocatori: dict, tabellone: list[list[str]], simboli: list[str]) -> None:
    """Gestisce il flusso principale del gioco, alternando i turni e determinando il risultato finale."""
    gioco_in_corso = True
    segno_vincente = None
    shuffle(simboli)
    giocatori["umano"]["simbolo"] = simboli[0]
    giocatori["bot"]["simbolo"] = simboli[1]
    print(f"Il giocatore {giocatori['umano']['nome']} ha il simbolo {giocatori['umano']['simbolo']}\n")
    print(f"Il giocatore {giocatori['bot']['nome']} ha il simbolo {giocatori['bot']['simbolo']}\n")
    mostra_tabellone(tabellone)
    if giocatori["umano"]["simbolo"] == "X":
        lista_giocatori = ["umano", "bot"]
    else:
        lista_giocatori = ["bot", "umano"]
    while gioco_in_corso:
        for giocatore in lista_giocatori:
            avversario = "umano" if giocatore == "bot" else "bot"
            gioca_turno(tabellone, giocatori[giocatore], giocatori[avversario]["simbolo"])
            segno_vincente = trova_vincitore(tabellone)
            if segno_vincente is not None:
                if segno_vincente == "pareggio":
                    print("Pareggio!\n")
                    gioco_in_corso = False
                    break
                else:
                    print(f"Il vincitore è {giocatori[giocatore]['nome']}!\n")
                    gioco_in_corso = False
                    break
    aggiorna_punteggio(giocatori, segno_vincente)

def main() -> None:
    """Gestisce la sfida al meglio dei tre e dichiara il vincitore finale."""
    print("")
    print("Benvenuti in tic tac toe! \n")
    simboli = ["O", "X"]
    shuffle(simboli)
    name = input("Inserisci il tuo nome: ")
    print("")
    giocatori = {
        "umano": {
            "nome": name,
            "simbolo": simboli[0],
            "vittorie": 0
            },
        "bot": {
            "nome": "bot",
            "simbolo": simboli[1],
            "vittorie": 0
        }
    }
    while True:
        tabellone = inizializza_tabellone()
        if giocatori["umano"]["vittorie"] == 2 or giocatori["bot"]["vittorie"] == 2:
            break
        partita(giocatori, tabellone, simboli)
    if giocatori["umano"]["vittorie"] > giocatori["bot"]["vittorie"]:
        print(f"Il vincitore è {giocatori['umano']['nome']}!")
    else:
        print(f"Il vincitore è {giocatori['bot']['nome']}!")

if __name__ == "__main__":
    main()
