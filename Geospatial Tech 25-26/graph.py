import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = [
    ("QN51","Murray Hill",2.8),
    ("QN27","East Elmhurst",3.8),
    ("BK81","Brownsville",3.2),
    ("BK85","East New York (Pennsylvania Ave)",3.4),
    ("BK41","Kensington-Ocean Parkway",3),
    ("BX46","Parkchester",2.2),
    ("BK95","Erasmus",3.6),
    ("QN33","Cambria Heights",3.6),
    ("BK91","East Flatbush-Farragut",3.6),
    ("BK46","Ocean Parkway South",3.4),
    ("BK93","Starrett City",2),
    ("BX35","Morrisania-Melrose",3),
    ("QN29","Elmhurst",3.8),
    ("MN22","East Village",2.8),
    ("QN44","Glen Oaks-Floral Park-New Hyde Park",2.6),
    ("BX33","Longwood",3.8),
    ("MN32","Yorkville",2.6),
    ("MN40","Upper East Side-Carnegie Hill",3.4),
    ("BK40","Windsor Terrace",2),
    ("QN12","Hammels-Arverne-Edgemere",3.2),
    ("BX98","Rikers Island",3.2),
    ("BX27","Hunts Point",4),
    ("QN28","Jackson Heights",2.6),
    ("BK27","Bath Beach",3.2),
    ("SI36","Old Town-Dongan Hills-South Beach",3),
    ("BK42","Flatbush",2),
    ("BX34","Melrose South-Mott Haven North",3.4),
    ("BK79","Ocean Hill",3.4),
    ("MN09","Morningside Heights",1.8),
    ("BX55","Soundview-Bruckner",2.6),
    ("BX31","Allerton-Pelham Gardens",3.2),
    ("QN06","Jamaica Estates-Holliswood",2.2),
    ("QN07","Hollis",3.8),
    ("BK58","Flatlands",3.4),
    ("BK82","East New York",3.4),
    ("BX30","Kingsbridge Heights",3),
    ("QN02","Springfield Gardens North",3.4),
    ("BK50","Canarsie",2.4),
    ("BX43","Norwood",2),
    ("MN06","Manhattanville",2.4),
    ("MN23","West Village",3.4),
    ("SI14","Grasmere-Arrochar-Ft. Wadsworth",3),
    ("QN34","Queens Village",3.8),
    ("MN27","Chinatown",3.2),
    ("BX10","Pelham Bay-Country Club-City Island",2.6),
    ("BX62","Woodlawn-Wakefield",3.2),
    ("QN71","Old Astoria",3),
    ("QN70","Astoria",3),
    ("MN50","Stuyvesant Town-Cooper Village",1.6),
    ("BK30","Dyker Heights",3.2),
    ("BK28","Bensonhurst West",3.8),
    ("SI22","West New Brighton-New Brighton-St. George",2),
    ("SI35","New Brighton-Silver Lake",2),
    ("SI07","Westerleigh",2.4),
    ("BX36","University Heights-Morris Heights",2.6),
    ("QN46","Bayside-Bayside Hills",2.6),
    ("BK61","Crown Heights North",2.2),
    ("BX14","East Concourse-Concourse Village",4.2),
    ("QN26","North Corona",4),
    ("BK83","Cypress Hills-City Line",2.8),
    ("QN37","Kew Gardens Hills",2.6),
    ("QN38","Pomonok-Flushing Heights-Hillcrest",2.8),
    ("BK73","North Side-South Side",3.8),
    ("MN28","Lower East Side",2.2),
    ("BK76","Greenpoint",4),
    ("BX29","Spuyten Duyvil-Kingsbridge",1.8),
    ("BK34","Sunset Park East",3),
    ("MN01","Marble Hill-Inwood",3.4),
    ("BK25","Homecrest",3.6),
    ("MN35","Washington Heights North",1.6),
    ("QN72","Steinway",3.4),
    ("BX39","Mott Haven-Port Morris",3.8),
    ("BK23","West Brighton",3.4),
    ("MN03","Central Harlem North-Polo Grounds",2.6),
    ("QN68","Queensbridge-Ravenswood-Long Island City",3.6),
    ("SI45","New Dorp-Midland Beach",3.6),
    ("BX28","Van Cortlandt Village",2.2),
    ("BX13","Co-op City",3.2),
    ("BK31","Bay Ridge",1.6),
    ("BK32","Sunset Park West",3.8),
    ("BK68","Fort Greene",1.8),
    ("MN24","SoHo-TriBeCa-Civic Center-Little Italy",3.8),
    ("MN25","Battery Park City-Lower Manhattan",3.4),
    ("MN15","Clinton",3.8),
    ("BK64","Prospect Heights",2),
]



df = pd.DataFrame(data, columns=["Code","Neighborhood","HeatIndex"])
df = df.sort_values("HeatIndex", ascending=False)
colors = ["red" if val >= 4 else "steelblue" for val in df["HeatIndex"]]



x = np.arange(len(df)) * 2.5   
plt.figure(figsize=(14,6))
plt.bar(x, df["HeatIndex"], color=colors, width=0.5)
plt.xticks(x, df["Neighborhood"], rotation=90, fontsize=8)
plt.xticks(rotation=90, fontsize=8)
plt.tick_params(axis="x", pad=10)
plt.ylabel("Urban Heat Index Value")
plt.xlabel("New York City Areas")
plt.title("NYC Neighborhood Urban Heat Index Values")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()