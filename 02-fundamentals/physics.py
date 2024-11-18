'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458  #? rychlost světla ve vakuu
SPEED_OF_SOUND = 1234 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant. #
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

# How long it takes sound to travel a distance
def sound_travel_time(distance_km: float) -> float:
    # Result is in seconds
    return distance_km / SPEED_OF_SOUND * 60 * 60

# How long it takes light to travel a distance
def light_travel_time(distance_km: float) -> float:
    return distance_km / (SPEED_OF_LIGHT / 1000)

# How long it takes to fall from a height on Earth
def fall_time(height_m: float) -> float:
    return (2 * height_m / EARTH_GRAVITY) ** 0.5

# How long it takes to fall from a height on the Moon
def fall_time_moon(height_m: float) -> float:
    return (2 * height_m / MOON_GRAVITY) ** 0.5

# How much do I weigh on the Moon
def weight_on_moon(weight_kg: float) -> float:
    return (weight_kg * MOON_GRAVITY) / EARTH_GRAVITY