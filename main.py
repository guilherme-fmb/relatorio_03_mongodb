from database import Database
from pokedex import Pokedex
from writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(db)
pokedex.getPokemonByName("Pikachu")
pokedex.getAllPokemons()
pokedex.getPokemonsByType(["Grass", "Fire"])
pokedex.getPokemonsByWeaknessCount(3)
pokedex.getPokemonsByWeakness(["Fire", "Ice"])