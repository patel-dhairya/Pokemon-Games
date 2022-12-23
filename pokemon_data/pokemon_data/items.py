from scrapy import Item, Field
from itemloaders.processors import TakeFirst, Compose


def int_stats(ls):
    return list(map(int, ls))


class PokemonDataItem(Item):
    main_name = Field(
        output_processor=TakeFirst()
    )
    secondary_name = Field(
        output_processor=TakeFirst()
    )
    pokemon_type = Field(
    )
    pokemon_stats = Field(
        input_processor=Compose(int_stats, )
    )
