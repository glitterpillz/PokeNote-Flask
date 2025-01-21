from app.models import db, Pokemon, PokemonStat, environment, SCHEMA
# from app.models.db import db, environment, SCHEMA
from sqlalchemy.sql import text


def seed_pokemon():
    bulbasaur = Pokemon(
        name="Bulbasaur",
        types=["Grass", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/001.png"
    )
    ivysaur = Pokemon(
        name="Ivysaur",
        types=["Grass", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/002.png"
    )
    venusaur = Pokemon(
        name="Venusaur",
        types=["Grass", "Poison"],
        is_floating=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/003.png"
    )
    charmander = Pokemon(
        name="Charmander",
        types=["Fire"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/004.png"
    )
    charmeleon = Pokemon(
        name="Charmeleon",
        types=["Fire"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/005.png"
    )
    charizard = Pokemon(
        name="Charizard",
        types=["Fire", "Flying"],
        is_floating=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/006.png"
    )
    squirtle = Pokemon(
        name="Squirtle",
        types=["Water"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/007.png"
    )
    wartortle = Pokemon(
        name="Wartortle",
        types=["Water"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/008.png"
    )
    blastoise = Pokemon(
        name="Blastoise",
        types=["Water"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/009.png"
    )
    caterpie = Pokemon(
        name="Caterpie",
        types=["Bug"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/010.png"
    )
    metapod = Pokemon(
        name="Metapod",
        types=["Bug"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/011.png"
    )
    butterfree = Pokemon(
        name="Butterfree",
        types=["Bug", "Flying"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/012.png"
    )
    weedle = Pokemon(
        name="Weedle",
        types=["Bug", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/013.png"
    )
    kakuna = Pokemon(
        name="Kakuna",
        types=["Bug", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/014.png"
    )
    beedrill = Pokemon(
        name="Beedrill",
        types=["Bug", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/015.png"
    )
    pidgey = Pokemon(
        name="Pidgey",
        types=["Normal", "Flying"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/016.png"
    )
    pidgeotto = Pokemon(
        name="Pidgeotto",
        types=["Normal", "Flying"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/017.png"
    )
    pidgeot = Pokemon(
        name="Pidgeot",
        types=["Normal", "Flying"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/018.png"
    )
    rattata = Pokemon(
        name="Rattata",
        types=["Normal"],
        is_floating=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/019.png"
    )
    #20
    raticate = Pokemon(
        name="Raticate",
        types=["Normal"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/020.png"
    )
    #21
    spearow = Pokemon(
        name="Spearow",
        types=["Normal", "Flying"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/021.png"
    )
    #22
    fearow = Pokemon(
        name="Fearow",
        types=["Normal", "Flying"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/022.png"
    )
    #23
    ekans = Pokemon(
        name="Ekans",
        types=["Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/023.png"
    )
    #24
    arbok = Pokemon(
        name="Arbok",
        types=["Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/024.png"
    )
    #25
    pikachu = Pokemon(
        name="Pikachu",
        types=["Electric"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/025.png"
    )
    #26
    raichu = Pokemon(
        name="Raichu",
        types=["Electric"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/026.png"
    )
    #27
    sandshrew = Pokemon(
        name="Sandshrew",
        types=["Ground"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/027.png"
    )
    #28
    sandslash = Pokemon(
        name="Sandslash",
        types=["Ground"],
        is_floating=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/028.png"
    )
    #29
    nidoran_f = Pokemon(
        name="Nidoran",
        types=["Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/029.png"
    )
    #30
    nidorina = Pokemon(
        name="Nidorina",
        types=["Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/030.png"
    )
    #31
    nidoqueen = Pokemon(
        name="Nidoqueen",
        types=["Poison", "Ground"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/031.png"
    )
    #32
    nidoran_m = Pokemon(
        name="Nidoran",
        types=["Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/032.png"
    )
    #33
    nidorino = Pokemon(
        name="Nidorino",
        types=["Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/033.png"
    )
    #34
    nidoking = Pokemon(
        name="Nidoking",
        types=["Poison", "Ground"],
        is_floating=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/034.png"
    )
    #35
    clefairy = Pokemon(
        name="Clefairy",
        types=["Fairy"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/035.png"
    )
    #36
    clefable = Pokemon(
        name="Clefable",
        types=["Fairy"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/036.png"
    )
    #37
    vulpix = Pokemon(
        name="Vulpix",
        types=["Fire"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/037.png"
    )
    #38
    ninetales = Pokemon(
        name="Ninetales",
        types=["Fire"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/038.png"
    )
    #39
    jigglypuff = Pokemon(
        name="Jigglepuff",
        types=["Normal", "Fairy"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/039.png"
    )
    #40
    wigglytuff = Pokemon(
        name="Wigglytuff",
        types=["Normal", "Fairy"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/040.png"
    )
    #41
    zubat = Pokemon(
        name="Zubat",
        types=["Poison", "Flying"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/041.png"
    )
    #42
    golbat = Pokemon(
        name="Golbat",
        types=["Poison", "Flying"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/042.png"
    )
    #43
    oddish = Pokemon(
        name="Oddish",
        types=["Grass", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/043.png"
    )
    #44
    gloom = Pokemon(
        name="Gloom",
        types=["Grass", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/044.png"

    )
    #45
    vileplume = Pokemon(
        name="Vileplume",
        types=["Grass", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/045.png"
    )
    #46
    paras = Pokemon(
        name="Paras",
        types=["Bug", "Grass"],
        is_floating=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/046.png"
    )
    #47
    parasect = Pokemon(
        name="Parasect",
        types=["Bug", "Grass"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/047.png"
    )
    #48
    venonat = Pokemon(
        name="Venonat",
        types=["Bug", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/048.png"
    )
    #49
    venomoth = Pokemon(
        name="Venomoth",
        types=["Bug", "Poison"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/049.png"
    )
    #50
    diglett = Pokemon(
        name="Diglett",
        types=["Ground"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/050.png"
    )
    #51
    dugtrio = Pokemon(
        name="Dugtrio",
        types=["Ground"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/051.png"
    )
    #52
    meowth = Pokemon(
        name="Meowth",
        types=["Normal"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/052.png"
    )
    #53
    persian = Pokemon(
        name="Persian",
        types=["Normal"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/053.png"
    )
    #54
    psyduck = Pokemon(
        name="Psyduck",
        types=["Water"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/054.png"
    )
    #55
    golduck = Pokemon(
        name="Golduck",
        types=["Water"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/055.png"
    )
    #56
    mankey = Pokemon(
        name="Mankey",
        types=["Fighting"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/056.png"
    )
    #57
    primeape = Pokemon(
        name="Primeape",
        types=["Fighting"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/057.png"
    )
    #58
    growlithe = Pokemon(
        name="Growlithe",
        types=["Fire"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/058.png"
    )
    #59
    arcanine = Pokemon(
        name="Arcanine",
        types=["Fire"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/059.png"
    )
    #60
    poliwag = Pokemon(
        name="Poliwag",
        types=["Water"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/060.png"
    )
    #61
    poliwhirl = Pokemon(
        name="Poliwhirl",
        types=["Water"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/061.png"
    )
    #62
    poliwrath = Pokemon(
        name="Poliwrath",
        types=["Water", "Fighting"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/062.png"
    )
    #63
    abra = Pokemon(
        name="Abra",
        types=["Psychic"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/063.png"
    )
    #64
    kadabra = Pokemon(
        name="Kadabra",
        types=["Psychic"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/064.png"
    )
    #65
    alakazam = Pokemon(
        name="Alakazam",
        types=["Psychic"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/065.png"
    )
    #66
    machop = Pokemon(
        name="Machop",
        types=["Fighting"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/066.png"
    )
    #67
    machoke = Pokemon(
        name="Machoke",
        types=["Fighting"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/067.png"
    )
    #68
    machamp = Pokemon(
        name="Machamp",
        types=["Fighting"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/068.png"
    )
    #69
    bellsprout = Pokemon(
        name="Bellsprout",
        types=["Grass", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/069.png"
    )
    #70
    weepinbell = Pokemon(
        name="Weepinbell",
        types=["Grass", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/070.png"
    )
    #71
    victreebel = Pokemon(
        name="Victreebel",
        types=["Grass", "Poison"],
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    )
    #72
    tentacool = Pokemon(
        name="Tentacool",
        types=["Water", "Poison"],
        can_fly=True,
        image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/072.png"
    )
    #73 ########################################################
    # tentacruel = Pokemon(
    #     name="Tentacruel",
    #     types=["Water", "Poison"],
    #     image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    # )
    # #74
    # geodude = Pokemon(
    #     name="Geodude",
    #     types=["Rock", "Ground"],
    #     image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    # )
    # #75
    # graveler = Pokemon(
    #     name="Graveler",
    #     types=["Rock", "Ground"],
    #     image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    # )
    # #76
    # golem = Pokemon(
    #     name="Golem",
    #     types=["Rock", "Ground"],
    #     image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    # )
    # #77
    # ponyta = Pokemon(
    #     name="Ponyta",
    #     types=["Fire"],
    #     image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    # )
    # #78
    # rapidash = Pokemon(
    #     name="Rapidash",
    #     types=["Grass", "Poison"],
    #     image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    # )
    # #79
    # slowpoke = Pokemon(
    #     name="Slowpoke",
    #     types=["Water", "Psychic"],
    #     image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    # )
    # #80
    # slowbro = Pokemon(
    #     name="Slowbro",
    #     types=["Water", "Psychic"],
    #     image="https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/071.png"
    # )


    
    bulbasaur.stats = [
        PokemonStat(stat_name="hp", stat_value=45),
        PokemonStat(stat_name="attack", stat_value=49),
        PokemonStat(stat_name="defense", stat_value=49),
        PokemonStat(stat_name="sp attack", stat_value=65),
        PokemonStat(stat_name="sp defense", stat_value=65),
        PokemonStat(stat_name="speed", stat_value=45)
    ]
    ivysaur.stats = [
        PokemonStat(stat_name="hp", stat_value=60),
        PokemonStat(stat_name="attack", stat_value=62),
        PokemonStat(stat_name="defense", stat_value=63),
        PokemonStat(stat_name="sp attack", stat_value=80),
        PokemonStat(stat_name="sp defense", stat_value=80),
        PokemonStat(stat_name="speed", stat_value=60)
    ]
    venusaur.stats = [
        PokemonStat(stat_name="hp", stat_value=80),
        PokemonStat(stat_name="attack", stat_value=82),
        PokemonStat(stat_name="defense", stat_value=83),
        PokemonStat(stat_name="sp attack", stat_value=100),
        PokemonStat(stat_name="sp defense", stat_value=100),
        PokemonStat(stat_name="speed", stat_value=80)
    ]
    charmander.stats = [
        PokemonStat(stat_name="hp", stat_value=39),
        PokemonStat(stat_name="attack", stat_value=52),
        PokemonStat(stat_name="defense", stat_value=43),
        PokemonStat(stat_name="sp attack", stat_value=60),
        PokemonStat(stat_name="sp defense", stat_value=50),
        PokemonStat(stat_name="speed", stat_value=65)
    ]
    charmeleon.stats = [
        PokemonStat(stat_name="hp", stat_value=58),
        PokemonStat(stat_name="attack", stat_value=64),
        PokemonStat(stat_name="defense", stat_value=58),
        PokemonStat(stat_name="sp attack", stat_value=80),
        PokemonStat(stat_name="sp defense", stat_value=65),
        PokemonStat(stat_name="speed", stat_value=80)
    ]
    charizard.stats = [
        PokemonStat(stat_name="hp", stat_value=78),
        PokemonStat(stat_name="attack", stat_value=84),
        PokemonStat(stat_name="defense", stat_value=78),
        PokemonStat(stat_name="sp attack", stat_value=109),
        PokemonStat(stat_name="sp defense", stat_value=85),
        PokemonStat(stat_name="speed", stat_value=100)
    ]
    squirtle.stats = [
        PokemonStat(stat_name="hp", stat_value=44),
        PokemonStat(stat_name="attack", stat_value=48),
        PokemonStat(stat_name="defense", stat_value=65),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=64),
        PokemonStat(stat_name="speed", stat_value=43)
    ]
    wartortle.stats = [
        PokemonStat(stat_name="hp", stat_value=59),
        PokemonStat(stat_name="attack", stat_value=63),
        PokemonStat(stat_name="defense", stat_value=80),
        PokemonStat(stat_name="sp attack", stat_value=65),
        PokemonStat(stat_name="sp defense", stat_value=80),
        PokemonStat(stat_name="speed", stat_value=58)
    ]
    blastoise.stats = [
        PokemonStat(stat_name="hp", stat_value=79),
        PokemonStat(stat_name="attack", stat_value=83),
        PokemonStat(stat_name="defense", stat_value=100),
        PokemonStat(stat_name="sp attack", stat_value=85),
        PokemonStat(stat_name="sp defense", stat_value=105),
        PokemonStat(stat_name="speed", stat_value=78)
    ]
    caterpie.stats = [
        PokemonStat(stat_name="hp", stat_value=45),
        PokemonStat(stat_name="attack", stat_value=30),
        PokemonStat(stat_name="defense", stat_value=35),
        PokemonStat(stat_name="sp attack", stat_value=20),
        PokemonStat(stat_name="sp defense", stat_value=20),
        PokemonStat(stat_name="speed", stat_value=45)
    ]
    metapod.stats = [
        PokemonStat(stat_name="hp", stat_value=50),
        PokemonStat(stat_name="attack", stat_value=20),
        PokemonStat(stat_name="defense", stat_value=55),
        PokemonStat(stat_name="sp attack", stat_value=25),
        PokemonStat(stat_name="sp defense", stat_value=25),
        PokemonStat(stat_name="speed", stat_value=30)
    ]
    butterfree.stats = [
        PokemonStat(stat_name="hp", stat_value=60),
        PokemonStat(stat_name="attack", stat_value=45),
        PokemonStat(stat_name="defense", stat_value=50),
        PokemonStat(stat_name="sp attack", stat_value=90),
        PokemonStat(stat_name="sp defense", stat_value=80),
        PokemonStat(stat_name="speed", stat_value=70)
    ]
    weedle.stats = [
        PokemonStat(stat_name="hp", stat_value=40),
        PokemonStat(stat_name="attack", stat_value=35),
        PokemonStat(stat_name="defense", stat_value=30),
        PokemonStat(stat_name="sp attack", stat_value=20),
        PokemonStat(stat_name="sp defense", stat_value=20),
        PokemonStat(stat_name="speed", stat_value=50)
    ]
    kakuna.stats = [
        PokemonStat(stat_name="hp", stat_value=45),
        PokemonStat(stat_name="attack", stat_value=25),
        PokemonStat(stat_name="defense", stat_value=50),
        PokemonStat(stat_name="sp attack", stat_value=25),
        PokemonStat(stat_name="sp defense", stat_value=25),
        PokemonStat(stat_name="speed", stat_value=35)
    ]
    pidgey.stats = [
        PokemonStat(stat_name="hp", stat_value=40),
        PokemonStat(stat_name="attack", stat_value=45),
        PokemonStat(stat_name="defense", stat_value=40),
        PokemonStat(stat_name="sp attack", stat_value=35),
        PokemonStat(stat_name="sp defense", stat_value=35),
        PokemonStat(stat_name="speed", stat_value=56)
    ]
    pidgeotto.stats = [
        PokemonStat(stat_name="hp", stat_value=63),
        PokemonStat(stat_name="attack", stat_value=60),
        PokemonStat(stat_name="defense", stat_value=55),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=50),
        PokemonStat(stat_name="speed", stat_value=71)
    ]
    pidgeot.stats = [
        PokemonStat(stat_name="hp", stat_value=83),
        PokemonStat(stat_name="attack", stat_value=80),
        PokemonStat(stat_name="defense", stat_value=75),
        PokemonStat(stat_name="sp attack", stat_value=70),
        PokemonStat(stat_name="sp defense", stat_value=70),
        PokemonStat(stat_name="speed", stat_value=101)
    ]
    rattata.stats = [
        PokemonStat(stat_name="hp", stat_value=30),
        PokemonStat(stat_name="attack", stat_value=56),
        PokemonStat(stat_name="defense", stat_value=35),
        PokemonStat(stat_name="sp attack", stat_value=25),
        PokemonStat(stat_name="sp defense", stat_value=35),
        PokemonStat(stat_name="speed", stat_value=72)
    ]
    raticate.stats = [
        PokemonStat(stat_name="hp", stat_value=55),
        PokemonStat(stat_name="attack", stat_value=81),
        PokemonStat(stat_name="defense", stat_value=60),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=70),
        PokemonStat(stat_name="speed", stat_value=97)
    ]
    spearow.stats = [
        PokemonStat(stat_name="hp", stat_value=40),
        PokemonStat(stat_name="attack", stat_value=60),
        PokemonStat(stat_name="defense", stat_value=30),
        PokemonStat(stat_name="sp attack", stat_value=31),
        PokemonStat(stat_name="sp defense", stat_value=31),
        PokemonStat(stat_name="speed", stat_value=70)
    ]
    fearow.stats = [
        PokemonStat(stat_name="hp", stat_value=65),
        PokemonStat(stat_name="attack", stat_value=90),
        PokemonStat(stat_name="defense", stat_value=65),
        PokemonStat(stat_name="sp attack", stat_value=61),
        PokemonStat(stat_name="sp defense", stat_value=61),
        PokemonStat(stat_name="speed", stat_value=100)
    ]
    ekans.stats = [
        PokemonStat(stat_name="hp", stat_value=35),
        PokemonStat(stat_name="attack", stat_value=60),
        PokemonStat(stat_name="defense", stat_value=44),
        PokemonStat(stat_name="sp attack", stat_value=40),
        PokemonStat(stat_name="sp defense", stat_value=54),
        PokemonStat(stat_name="speed", stat_value=55)
    ]
    arbok.stats = [
        PokemonStat(stat_name="hp", stat_value=60),
        PokemonStat(stat_name="attack", stat_value=95),
        PokemonStat(stat_name="defense", stat_value=69),
        PokemonStat(stat_name="sp attack", stat_value=65),
        PokemonStat(stat_name="sp defense", stat_value=79),
        PokemonStat(stat_name="speed", stat_value=80)
    ]
    pikachu.stats = [
        PokemonStat(stat_name="hp", stat_value=35),
        PokemonStat(stat_name="attack", stat_value=55),
        PokemonStat(stat_name="defense", stat_value=40),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=50),
        PokemonStat(stat_name="speed", stat_value=90)
    ]
    raichu.stats = [
        PokemonStat(stat_name="hp", stat_value=60),
        PokemonStat(stat_name="attack", stat_value=90),
        PokemonStat(stat_name="defense", stat_value=55),
        PokemonStat(stat_name="sp attack", stat_value=90),
        PokemonStat(stat_name="sp defense", stat_value=80),
        PokemonStat(stat_name="speed", stat_value=110)
    ]
    sandshrew.stats = [
        PokemonStat(stat_name="hp", stat_value=50),
        PokemonStat(stat_name="attack", stat_value=75),
        PokemonStat(stat_name="defense", stat_value=85),
        PokemonStat(stat_name="sp attack", stat_value=20),
        PokemonStat(stat_name="sp defense", stat_value=30),
        PokemonStat(stat_name="speed", stat_value=40)
    ]
    sandslash.stats = [
        PokemonStat(stat_name="hp", stat_value=75),
        PokemonStat(stat_name="attack", stat_value=100),
        PokemonStat(stat_name="defense", stat_value=110),
        PokemonStat(stat_name="sp attack", stat_value=45),
        PokemonStat(stat_name="sp defense", stat_value=55),
        PokemonStat(stat_name="speed", stat_value=65)
    ]
    nidoran_f.stats = [
        PokemonStat(stat_name="hp", stat_value=55),
        PokemonStat(stat_name="attack", stat_value=47),
        PokemonStat(stat_name="defense", stat_value=52),
        PokemonStat(stat_name="sp attack", stat_value=40),
        PokemonStat(stat_name="sp defense", stat_value=40),
        PokemonStat(stat_name="speed", stat_value=41)
    ]
    nidorina.stats = [
        PokemonStat(stat_name="hp", stat_value=70),
        PokemonStat(stat_name="attack", stat_value=62),
        PokemonStat(stat_name="defense", stat_value=67),
        PokemonStat(stat_name="sp attack", stat_value=55),
        PokemonStat(stat_name="sp defense", stat_value=55),
        PokemonStat(stat_name="speed", stat_value=56)
    ]
    nidoqueen.stats = [
        PokemonStat(stat_name="hp", stat_value=90),
        PokemonStat(stat_name="attack", stat_value=92),
        PokemonStat(stat_name="defense", stat_value=87),
        PokemonStat(stat_name="sp attack", stat_value=75),
        PokemonStat(stat_name="sp defense", stat_value=85),
        PokemonStat(stat_name="speed", stat_value=76)
    ]
    nidoran_m.stats = [
        PokemonStat(stat_name="hp", stat_value=46),
        PokemonStat(stat_name="attack", stat_value=57),
        PokemonStat(stat_name="defense", stat_value=40),
        PokemonStat(stat_name="sp attack", stat_value=40),
        PokemonStat(stat_name="sp defense", stat_value=40),
        PokemonStat(stat_name="speed", stat_value=50)
    ]
    nidorino.stats = [
        PokemonStat(stat_name="hp", stat_value=61),
        PokemonStat(stat_name="attack", stat_value=72),
        PokemonStat(stat_name="defense", stat_value=57),
        PokemonStat(stat_name="sp attack", stat_value=55),
        PokemonStat(stat_name="sp defense", stat_value=55),
        PokemonStat(stat_name="speed", stat_value=65)
    ]
    nidoking.stats = [
        PokemonStat(stat_name="hp", stat_value=81),
        PokemonStat(stat_name="attack", stat_value=102),
        PokemonStat(stat_name="defense", stat_value=77),
        PokemonStat(stat_name="sp attack", stat_value=85),
        PokemonStat(stat_name="sp defense", stat_value=75),
        PokemonStat(stat_name="speed", stat_value=85)
    ]
    clefairy.stats = [
        PokemonStat(stat_name="hp", stat_value=70),
        PokemonStat(stat_name="attack", stat_value=45),
        PokemonStat(stat_name="defense", stat_value=48),
        PokemonStat(stat_name="sp attack", stat_value=60),
        PokemonStat(stat_name="sp defense", stat_value=65),
        PokemonStat(stat_name="speed", stat_value=35)
    ]
    clefable.stats = [
        PokemonStat(stat_name="hp", stat_value=95),
        PokemonStat(stat_name="attack", stat_value=70),
        PokemonStat(stat_name="defense", stat_value=73),
        PokemonStat(stat_name="sp attack", stat_value=95),
        PokemonStat(stat_name="sp defense", stat_value=90),
        PokemonStat(stat_name="speed", stat_value=60)
    ]
    vulpix.stats = [
        PokemonStat(stat_name="hp", stat_value=38),
        PokemonStat(stat_name="attack", stat_value=41),
        PokemonStat(stat_name="defense", stat_value=40),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=65),
        PokemonStat(stat_name="speed", stat_value=65)
    ]
    ninetales.stats = [
        PokemonStat(stat_name="hp", stat_value=73),
        PokemonStat(stat_name="attack", stat_value=76),
        PokemonStat(stat_name="defense", stat_value=75),
        PokemonStat(stat_name="sp attack", stat_value=81),
        PokemonStat(stat_name="sp defense", stat_value=100),
        PokemonStat(stat_name="speed", stat_value=100)
    ]
    jigglypuff.stats = [
        PokemonStat(stat_name="hp", stat_value=115),
        PokemonStat(stat_name="attack", stat_value=45),
        PokemonStat(stat_name="defense", stat_value=20),
        PokemonStat(stat_name="sp attack", stat_value=45),
        PokemonStat(stat_name="sp defense", stat_value=25),
        PokemonStat(stat_name="speed", stat_value=20)
    ]
    wigglytuff.stats = [
        PokemonStat(stat_name="hp", stat_value=140),
        PokemonStat(stat_name="attack", stat_value=70),
        PokemonStat(stat_name="defense", stat_value=45),
        PokemonStat(stat_name="sp attack", stat_value=85),
        PokemonStat(stat_name="sp defense", stat_value=50),
        PokemonStat(stat_name="speed", stat_value=45)
    ]
    zubat.stats = [
        PokemonStat(stat_name="hp", stat_value=40),
        PokemonStat(stat_name="attack", stat_value=45),
        PokemonStat(stat_name="defense", stat_value=35),
        PokemonStat(stat_name="sp attack", stat_value=30),
        PokemonStat(stat_name="sp defense", stat_value=40),
        PokemonStat(stat_name="speed", stat_value=55)
    ]
    golbat.stats = [
        PokemonStat(stat_name="hp", stat_value=75),
        PokemonStat(stat_name="attack", stat_value=80),
        PokemonStat(stat_name="defense", stat_value=70),
        PokemonStat(stat_name="sp attack", stat_value=65),
        PokemonStat(stat_name="sp defense", stat_value=75),
        PokemonStat(stat_name="speed", stat_value=90)
    ]
    oddish.stats = [
        PokemonStat(stat_name="hp", stat_value=45),
        PokemonStat(stat_name="attack", stat_value=50),
        PokemonStat(stat_name="defense", stat_value=55),
        PokemonStat(stat_name="sp attack", stat_value=75),
        PokemonStat(stat_name="sp defense", stat_value=65),
        PokemonStat(stat_name="speed", stat_value=30)
    ]
    gloom.stats = [
        PokemonStat(stat_name="hp", stat_value=60),
        PokemonStat(stat_name="attack", stat_value=65),
        PokemonStat(stat_name="defense", stat_value=70),
        PokemonStat(stat_name="sp attack", stat_value=85),
        PokemonStat(stat_name="sp defense", stat_value=75),
        PokemonStat(stat_name="speed", stat_value=40)
    ]
    vileplume.stats = [
        PokemonStat(stat_name="hp", stat_value=75),
        PokemonStat(stat_name="attack", stat_value=80),
        PokemonStat(stat_name="defense", stat_value=85),
        PokemonStat(stat_name="sp attack", stat_value=110),
        PokemonStat(stat_name="sp defense", stat_value=90),
        PokemonStat(stat_name="speed", stat_value=50)
    ]
    paras.stats = [
        PokemonStat(stat_name="hp", stat_value=35),
        PokemonStat(stat_name="attack", stat_value=70),
        PokemonStat(stat_name="defense", stat_value=55),
        PokemonStat(stat_name="sp attack", stat_value=45),
        PokemonStat(stat_name="sp defense", stat_value=55),
        PokemonStat(stat_name="speed", stat_value=25)
    ]
    parasect.stats = [
        PokemonStat(stat_name="hp", stat_value=60),
        PokemonStat(stat_name="attack", stat_value=95),
        PokemonStat(stat_name="defense", stat_value=80),
        PokemonStat(stat_name="sp attack", stat_value=60),
        PokemonStat(stat_name="sp defense", stat_value=80),
        PokemonStat(stat_name="speed", stat_value=30)
    ]
    venonat.stats = [
        PokemonStat(stat_name="hp", stat_value=60),
        PokemonStat(stat_name="attack", stat_value=55),
        PokemonStat(stat_name="defense", stat_value=50),
        PokemonStat(stat_name="sp attack", stat_value=40),
        PokemonStat(stat_name="sp defense", stat_value=55),
        PokemonStat(stat_name="speed", stat_value=45)
    ]
    venomoth.stats = [
        PokemonStat(stat_name="hp", stat_value=70),
        PokemonStat(stat_name="attack", stat_value=65),
        PokemonStat(stat_name="defense", stat_value=60),
        PokemonStat(stat_name="sp attack", stat_value=90),
        PokemonStat(stat_name="sp defense", stat_value=75),
        PokemonStat(stat_name="speed", stat_value=90)
    ]
    diglett.stats = [
        PokemonStat(stat_name="hp", stat_value=10),
        PokemonStat(stat_name="attack", stat_value=55),
        PokemonStat(stat_name="defense", stat_value=25),
        PokemonStat(stat_name="sp attack", stat_value=35),
        PokemonStat(stat_name="sp defense", stat_value=45),
        PokemonStat(stat_name="speed", stat_value=95)
    ]
    dugtrio.stats = [
        PokemonStat(stat_name="hp", stat_value=35),
        PokemonStat(stat_name="attack", stat_value=100),
        PokemonStat(stat_name="defense", stat_value=50),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=70),
        PokemonStat(stat_name="speed", stat_value=120)
    ]
    ########################################################
    meowth.stats = [
        PokemonStat(stat_name="hp", stat_value=50),
        PokemonStat(stat_name="attack", stat_value=65),
        PokemonStat(stat_name="defense", stat_value=55),
        PokemonStat(stat_name="sp attack", stat_value=40),
        PokemonStat(stat_name="sp defense", stat_value=40),
        PokemonStat(stat_name="speed", stat_value=40)
    ]
    persian.stats = [
        PokemonStat(stat_name="hp", stat_value=65),
        PokemonStat(stat_name="attack", stat_value=70),
        PokemonStat(stat_name="defense", stat_value=60),
        PokemonStat(stat_name="sp attack", stat_value=65),
        PokemonStat(stat_name="sp defense", stat_value=65),
        PokemonStat(stat_name="speed", stat_value=115)
    ]
    psyduck.stats = [
        PokemonStat(stat_name="hp", stat_value=50),
        PokemonStat(stat_name="attack", stat_value=52),
        PokemonStat(stat_name="defense", stat_value=48),
        PokemonStat(stat_name="sp attack", stat_value=65),
        PokemonStat(stat_name="sp defense", stat_value=50),
        PokemonStat(stat_name="speed", stat_value=55)
    ]
    golduck.stats = [
        PokemonStat(stat_name="hp", stat_value=80),
        PokemonStat(stat_name="attack", stat_value=82),
        PokemonStat(stat_name="defense", stat_value=78),
        PokemonStat(stat_name="sp attack", stat_value=95),
        PokemonStat(stat_name="sp defense", stat_value=80),
        PokemonStat(stat_name="speed", stat_value=85)
    ]
    mankey.stats = [
        PokemonStat(stat_name="hp", stat_value=40),
        PokemonStat(stat_name="attack", stat_value=80),
        PokemonStat(stat_name="defense", stat_value=35),
        PokemonStat(stat_name="sp attack", stat_value=35),
        PokemonStat(stat_name="sp defense", stat_value=45),
        PokemonStat(stat_name="speed", stat_value=70)
    ]
    primeape.stats = [
        PokemonStat(stat_name="hp", stat_value=65),
        PokemonStat(stat_name="attack", stat_value=105),
        PokemonStat(stat_name="defense", stat_value=60),
        PokemonStat(stat_name="sp attack", stat_value=60),
        PokemonStat(stat_name="sp defense", stat_value=70),
        PokemonStat(stat_name="speed", stat_value=95)
    ]
    growlithe.stats = [
        PokemonStat(stat_name="hp", stat_value=55),
        PokemonStat(stat_name="attack", stat_value=70),
        PokemonStat(stat_name="defense", stat_value=45),
        PokemonStat(stat_name="sp attack", stat_value=70),
        PokemonStat(stat_name="sp defense", stat_value=50),
        PokemonStat(stat_name="speed", stat_value=60)
    ]
    arcanine.stats = [
        PokemonStat(stat_name="hp", stat_value=90),
        PokemonStat(stat_name="attack", stat_value=110),
        PokemonStat(stat_name="defense", stat_value=80),
        PokemonStat(stat_name="sp attack", stat_value=100),
        PokemonStat(stat_name="sp defense", stat_value=80),
        PokemonStat(stat_name="speed", stat_value=95)
    ]
    poliwag.stats = [
        PokemonStat(stat_name="hp", stat_value=40),
        PokemonStat(stat_name="attack", stat_value=50),
        PokemonStat(stat_name="defense", stat_value=40),
        PokemonStat(stat_name="sp attack", stat_value=40),
        PokemonStat(stat_name="sp defense", stat_value=40),
        PokemonStat(stat_name="speed", stat_value=90)
    ]
    poliwhirl.stats = [
        PokemonStat(stat_name="hp", stat_value=65),
        PokemonStat(stat_name="attack", stat_value=65),
        PokemonStat(stat_name="defense", stat_value=65),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=50),
        PokemonStat(stat_name="speed", stat_value=90)
    ]
    poliwrath.stats = [
        PokemonStat(stat_name="hp", stat_value=90),
        PokemonStat(stat_name="attack", stat_value=95),
        PokemonStat(stat_name="defense", stat_value=95),
        PokemonStat(stat_name="sp attack", stat_value=70),
        PokemonStat(stat_name="sp defense", stat_value=90),
        PokemonStat(stat_name="speed", stat_value=70)
    ]
    abra.stats = [
        PokemonStat(stat_name="hp", stat_value=25),
        PokemonStat(stat_name="attack", stat_value=20),
        PokemonStat(stat_name="defense", stat_value=15),
        PokemonStat(stat_name="sp attack", stat_value=105),
        PokemonStat(stat_name="sp defense", stat_value=55),
        PokemonStat(stat_name="speed", stat_value=90)
    ]
    kadabra.stats = [
        PokemonStat(stat_name="hp", stat_value=40),
        PokemonStat(stat_name="attack", stat_value=35),
        PokemonStat(stat_name="defense", stat_value=30),
        PokemonStat(stat_name="sp attack", stat_value=120),
        PokemonStat(stat_name="sp defense", stat_value=70),
        PokemonStat(stat_name="speed", stat_value=105)
    ]
    alakazam.stats = [
        PokemonStat(stat_name="hp", stat_value=55),
        PokemonStat(stat_name="attack", stat_value=50),
        PokemonStat(stat_name="defense", stat_value=65),
        PokemonStat(stat_name="sp attack", stat_value=175),
        PokemonStat(stat_name="sp defense", stat_value=105),
        PokemonStat(stat_name="speed", stat_value=150)
    ]
    machop.stats = [
        PokemonStat(stat_name="hp", stat_value=70),
        PokemonStat(stat_name="attack", stat_value=80),
        PokemonStat(stat_name="defense", stat_value=50),
        PokemonStat(stat_name="sp attack", stat_value=35),
        PokemonStat(stat_name="sp defense", stat_value=35),
        PokemonStat(stat_name="speed", stat_value=35)
    ]
    machoke.stats = [
        PokemonStat(stat_name="hp", stat_value=80),
        PokemonStat(stat_name="attack", stat_value=100),
        PokemonStat(stat_name="defense", stat_value=70),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=60),
        PokemonStat(stat_name="speed", stat_value=45)
    ]
    machamp.stats = [
        PokemonStat(stat_name="hp", stat_value=90),
        PokemonStat(stat_name="attack", stat_value=130),
        PokemonStat(stat_name="defense", stat_value=80),
        PokemonStat(stat_name="sp attack", stat_value=65),
        PokemonStat(stat_name="sp defense", stat_value=85),
        PokemonStat(stat_name="speed", stat_value=55)
    ]
    bellsprout.stats = [
        PokemonStat(stat_name="hp", stat_value=50),
        PokemonStat(stat_name="attack", stat_value=75),
        PokemonStat(stat_name="defense", stat_value=35),
        PokemonStat(stat_name="sp attack", stat_value=70),
        PokemonStat(stat_name="sp defense", stat_value=30),
        PokemonStat(stat_name="speed", stat_value=40)
    ]
    weepinbell.stats = [
        PokemonStat(stat_name="hp", stat_value=65),
        PokemonStat(stat_name="attack", stat_value=90),
        PokemonStat(stat_name="defense", stat_value=50),
        PokemonStat(stat_name="sp attack", stat_value=85),
        PokemonStat(stat_name="sp defense", stat_value=45),
        PokemonStat(stat_name="speed", stat_value=55)
    ]
    victreebel.stats = [
        PokemonStat(stat_name="hp", stat_value=80),
        PokemonStat(stat_name="attack", stat_value=105),
        PokemonStat(stat_name="defense", stat_value=65),
        PokemonStat(stat_name="sp attack", stat_value=100),
        PokemonStat(stat_name="sp defense", stat_value=70),
        PokemonStat(stat_name="speed", stat_value=70)
    ]
    tentacool.stats = [
        PokemonStat(stat_name="hp", stat_value=40),
        PokemonStat(stat_name="attack", stat_value=40),
        PokemonStat(stat_name="defense", stat_value=35),
        PokemonStat(stat_name="sp attack", stat_value=50),
        PokemonStat(stat_name="sp defense", stat_value=100),
        PokemonStat(stat_name="speed", stat_value=70)
    ]

    db.session.add(bulbasaur)
    db.session.add(ivysaur)
    db.session.add(venusaur)
    db.session.add(charmander)
    db.session.add(charmeleon)
    db.session.add(charizard)
    db.session.add(squirtle)
    db.session.add(wartortle)
    db.session.add(blastoise)
    db.session.add(caterpie)
    db.session.add(metapod)
    db.session.add(butterfree)
    db.session.add(weedle)
    db.session.add(kakuna)
    db.session.add(beedrill)
    db.session.add(pidgey)
    db.session.add(pidgeotto)
    db.session.add(pidgeot)
    db.session.add(rattata)
    db.session.add(raticate)
    db.session.add(spearow)
    db.session.add(fearow)
    db.session.add(ekans)
    db.session.add(arbok)
    db.session.add(pikachu)
    db.session.add(raichu)
    db.session.add(sandshrew)
    db.session.add(sandslash)
    db.session.add(nidoran_f)
    db.session.add(nidorina)
    db.session.add(nidoqueen)
    db.session.add(nidoran_m)
    db.session.add(nidorino)
    db.session.add(nidoking)
    db.session.add(clefairy)
    db.session.add(clefable)
    db.session.add(vulpix)
    db.session.add(ninetales)
    db.session.add(jigglypuff)
    db.session.add(wigglytuff)
    db.session.add(zubat)
    db.session.add(golbat)
    db.session.add(oddish)
    db.session.add(gloom)
    db.session.add(vileplume)
    db.session.add(paras)
    db.session.add(parasect)
    db.session.add(venonat)
    db.session.add(venomoth)
    db.session.add(diglett)
    db.session.add(dugtrio)
    db.session.add(meowth)
    db.session.add(persian)
    db.session.add(psyduck)
    db.session.add(golduck)
    db.session.add(mankey)
    db.session.add(primeape)
    db.session.add(growlithe)
    db.session.add(arcanine)
    db.session.add(poliwag)
    db.session.add(poliwhirl)
    db.session.add(poliwrath)
    db.session.add(abra)
    db.session.add(kadabra)
    db.session.add(alakazam)
    db.session.add(machop)
    db.session.add(machoke)
    db.session.add(machamp)
    db.session.add(bellsprout)
    db.session.add(weepinbell)
    db.session.add(victreebel)
    db.session.add(tentacool)

    db.session.commit()

def undo_pokemon():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.pokemon_stats RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.pokemons RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM pokemon_stats"))
        db.session.execute(text("DELETE FROM pokemons"))

    db.session.commit()

