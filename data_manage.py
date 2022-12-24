# This class uses Pokemon data generated by scrapy and convert it in usable form of Panda dataframe


import csv
import pandas as pd


def clean_data(file_name, clean=False):
    if not clean:
        return pd.read_csv(file_name)

    name_ls, secondary_ls, type1_ls, type2_ls, hp_ls, attack_ls, defense_ls, sa_ls, sd_ls, speed_ls, total_ls = \
        ([] for i in range(11))

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        _ = next(csv_reader)
        for pokemon in csv_reader:
            name, stats, types, secondary = pokemon
            total, hp, attack, defense, special_attack, special_defense, speed = list(map(int, stats[1:-1].split(",")))
            assert total == hp + attack + defense + special_attack + special_defense + speed

            if len(types.split(",")) == 2:
                type1 = types.split(",")[0]
                type2 = types.split(",")[1]
            else:
                type1 = types
                type2 = None
            if secondary == "":
                secondary = None
            name_ls.append(name)
            secondary_ls.append(secondary)
            type1_ls.append(type1)
            type2_ls.append(type2)
            hp_ls.append(hp)
            attack_ls.append(attack)
            defense_ls.append(defense)
            sa_ls.append(special_attack)
            sd_ls.append(special_defense)
            speed_ls.append(speed)
            total_ls.append(total)

    pokemon_df = pd.DataFrame({
        "Poke_ID": [i for i in range(1,len(name_ls)+1)],
        "Name": name_ls,
        "Extra Name": secondary_ls,
        "Type One": type1_ls,
        "Type Two": type2_ls,
        "HP": hp_ls,
        "Attack": attack_ls,
        "Defense": defense_ls,
        "Special Attack": sa_ls,
        "Special Defense": sd_ls,
        "Total": total_ls
    })

    pokemon_df.set_index("Poke_ID", inplace=True)

    pokemon_df.to_csv(file_name, mode="w+")
    return pokemon_df
