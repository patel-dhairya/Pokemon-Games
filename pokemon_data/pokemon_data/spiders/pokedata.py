# This file deals with scrapping Pokemon dataset from website 'pokemondb'
# A custom script for dataset allows to update dataset for game whenever new Pokemons are available

import scrapy
from ..items import PokemonDataItem
from scrapy.loader import ItemLoader


class PokeDataSpider(scrapy.Spider):
    name = "pokedata"

    def start_requests(self):
        url = "https://pokemondb.net/pokedex/all"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        table = response.css("table.data-table")

        for row in table.css("tbody tr"):
            loader = ItemLoader(item=PokemonDataItem())
            loader.add_value("main_name", row.css("td a.ent-name::text").get())
            loader.add_value("secondary_name", row.css("td small.text-muted::text").get())
            loader.add_value("pokemon_type", row.css("td a.type-icon::text").getall())
            loader.add_value("pokemon_stats", row.css("td.cell-num::text").getall())

            yield loader.load_item()
