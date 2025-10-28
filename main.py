from Week_1_exam.game_logic.game import *


if __name__ == "__main__":
    current_game = init_game()
    p1_hand = current_game["player_1"]["hand"]
    p2_hand = current_game["player_2"]["hand"]

    while p1_hand:
        play_round(current_game["player_1"], current_game["player_2"])

    if p1_hand > p2_hand:
        print("Player 1 Wins!!")
    else:
        print("Player 2 Wins!!")


