from data_manage import clean_data
import random
import time


def rules():
    print("You will be given two pokemon names and one stat name")
    print("You have to guess which pokemon has higher given stat")
    print("Write 1 if first pokemon is your answer else write 2")
    print("Each correct answer will earn you 1 point and wrong answer will earn -0.25 point")
    print("Final score will be declared after 1 minute")


def introduction():
    print("What is your name? ")
    player_name = input()
    assert type(player_name) == str
    print(f"Hello {player_name}, welcome to the game.")
    print("Press 1 to start game")
    print("Press 2 to read rules")
    number_choice = input()
    try:
        number_choice = int(number_choice)
    except TypeError:
        print("Please write 1 or 2 to continue the game")
    if number_choice == 1:
        return player_name
    else:
        rules()
        return player_name


def gameloop():
    poke_data = clean_data("pokemon_table.csv")
    poke_data.set_index("Poke_ID", inplace=True)

    # To make game easy, I am not using any pokemon with extra version such as Mega pokemons to avoid confusion
    poke_data = poke_data[poke_data['Extra Name'].isnull()]
    poke_data.drop("Extra Name", axis=1, inplace=True)
    poke_data.reset_index(drop=True, inplace=True)

    score = 0
    time_end = time.time() + 60

    while time.time() < time_end:
        poke1, poke2 = random.sample(range(1, poke_data.shape[0] + 1), k=2)
        stat_question = random.choice(["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Total"])

        poke1_stat = poke_data.loc[poke1][stat_question]
        poke2_stat = poke_data.loc[poke2][stat_question]
        print(f"Between {poke_data.loc[poke1]['Name']} and {poke_data.loc[poke2]['Name']} who has higher"
              f" {stat_question}?")
        print(f"Press 1 for {poke_data.loc[poke1]['Name']} or Press 2 for {poke_data.loc[poke2]['Name']}")
        try:
            answer = int(input())
            if answer == 1:
                if poke1_stat >= poke2_stat:
                    score += 1
                else:
                    score -= 0.25
            elif answer == 2:
                if poke2_stat >= poke1_stat:
                    score += 1
                else:
                    score -= 0.25
            else:
                score += 0
        except ValueError:
            print("Answer not in correct format. No point will be given")
            print("Write 1 or 2 to earn point next time")

    return score


if __name__ == "__main__":
    name = introduction()
    score = gameloop()
    print(f"Congratulation {name}, your score is {score}")
    print(f"Play again to score more points!")

    print(f"Final score = {score}")
