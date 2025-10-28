import random

def create_card(rank:str,suite:str) -> dict:
   cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
   value = cards.index(rank) + 2
   return {"rank" : rank, "suite" : suite, "value" : value}

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    current_round_result = ""
    if p1_card["value"] > p2_card["value"]:
        current_round_result = "p1"
    elif p2_card["value"] > p1_card["value"]:
        current_round_result = "p2"
    else:
        current_round_result = "WAR"

    return current_round_result

def create_deck() -> list[dict]:
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["D", "H", "S", "C"]
    full_deck = []
    for suit in suits:
        for card in cards:
            full_deck.append(create_card(card, suit))
    return full_deck

def shuffle(deck:list[dict]) -> list[dict]:
    mix_count = 0
    while mix_count < 1000:
        index1 = random.randint(0,51)
        index2 = random.randint(0,51)
        if index1 != index2:
            deck[index1], deck[index2] = deck[index2], deck[index1]
            mix_count += 1
        else:
            continue
    return deck


