from database import Database
from writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self._database = database

    def getPokemonByName(self, nome: str):
        pokemon = self._database.collection.find_one({"name": nome})
        writeAJson(pokemon, "pokemon")

    def getPokemonsByType(self, types: list):
        pokemonByType = self._database.collection.find({"type": {"$in": types}})
        writeAJson(pokemonByType, "pokemon_type")

    def getPokemonsByWeakness(self, weaknesses: list):
        pokemonByWeakness = self._database.collection.find({"weaknesses": {"$in": weaknesses}})
        writeAJson(pokemonByWeakness, "pokemon_by_weakness")

    def getPokemonsByWeaknessCount(self, counter: int):
        pokemonByWeaknessCount = self._database.collection.find({"weaknesses": {"$size": counter}})
        writeAJson(pokemonByWeaknessCount, "pokemon_by_weakness_count")

    def getAllPokemons(self):
        pokemons = self._database.collection.find()
        writeAJson(pokemons, "all_pokemons")
