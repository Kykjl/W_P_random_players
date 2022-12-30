import random

def us_input():
    stage = input("Стадия турнира (Начало/Финал): ").lower()
    if stage == "начало":
        user_input_start()
    elif stage == "финал":
        final()
    else:
        print("Ошибка ввода!\n")

def user_input_start():
    players = dict()
    quantity = int(input('Кол-во игроков: '))
    for number_players in range(1, quantity + 1):
        print(f"{number_players} игрок: ", end="")
        player = input()
        players[number_players] = player

    rivals(players, quantity)


def rivals(players, quantity):
    number_players = 1
    players_number = [random.sample(range(1, quantity + 1), quantity)]
    for count in range(1, quantity, 2):
        print(f"\n{number_players} пара:")
        print(f"{players[players_number[0][count - 1]]} VS {players[players_number[0][count]]}")
        number_players += 1
    print()


def final():
    final_dict = dict()
    players_number_f = [random.sample(range(1, 4), 2)]
    for number_p in range(1, 4):
        print(f"{number_p} игрок: ", end="")
        player_f = input()
        final_dict[number_p] = player_f

    print(f"Первая пара полуфинала: {final_dict[players_number_f[0][0]]} VS {final_dict[players_number_f[0][1]]}")
    print()



if __name__ == "__main__":
    while True:
        us_input()
