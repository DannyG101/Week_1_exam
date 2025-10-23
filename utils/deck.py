import random

def create_card(rank:str,suite:str) -> dict:
    my_dict = {"rank" : rank, "suite" : suite, "value": rank} ### needs value
    return my_dict

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
    deck = []
    for i in range(1,10):
        deck.append({"rank" : i, "suit" : "C", "value" : i})
    for i in range(1, 10):
        deck.append({"rank": i, "suit": "S", "value": i})
    for i in range(1, 10):
        deck.append({"rank": i, "suit": "D", "value": i})
    for i in range(1, 10):
        deck.append({"rank": i, "suit": "H", "value": i})
    return deck

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
