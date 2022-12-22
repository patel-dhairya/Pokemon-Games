from scrapy import Item, Field
from itemloaders.processors import TakeFirst
from scrapy.loader.processors import Compose


def int_stats(ls):
    return list(map(int, ls))

#
# def dual_types(ls):
#     if len(ls) == 1:
#         return ls[0], None
#     return ls


class PokemonDataItem(Item):
    main_name = Field(
        output_processor=TakeFirst()
    )
    secondary_name = Field(
        output_processor=TakeFirst()
    )
    pokemon_type = Field(
        # input_processor=Compose(dual_types, )
    )
    pokemon_stats = Field(
        input_processor=Compose(int_stats, )
    )
