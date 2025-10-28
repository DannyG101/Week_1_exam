from Week_1_exam.utils.deck import *

def create_player(name:str="AI") -> dict:
    player_profile = {"name" : name, "hand" : [], "won_pile" : []}
    return player_profile

def init_game() -> dict:

    #Create players
    human_player = create_player(input("Please enter your name: "))
    ai_player = create_player()


    #Create deck
    current_deck = create_deck()

    #Shuffle deck
    current_deck = shuffle(current_deck)

    #Distribute deck between both players
    human_player["hand"] = current_deck[:26]
    ai_player["hand"] = current_deck[26:]


    #Create game dict
    game = {"deck" : current_deck, "player_1" : human_player, "player_2" : ai_player}

    return game

def play_round(p1:dict,p2:dict):
    p1_card = p1["hand"].pop()
    p2_card = p2["hand"].pop()
    current_round_results = compare_cards(p1_card, p2_card)

    if current_round_results == "p1":
        print("Player 1 takes the cards")
        p1["won_pile"].append(p1_card)
        p1["won_pile"].append(p2_card)

    elif current_round_results =="p2":
        print("Player 2 takes the cards")
        p2["won_pile"].append(p1_card)
        p2["won_pile"].append(p2_card)

    elif current_round_results == "WAR":
        print("No one takes the cards")







