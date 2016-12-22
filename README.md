# MountRUSHmore

Fien Lute - 10752862
Barbara Boeters - 10774513
Mirja Lagerwaard - 10363149

* main.py
In dit bestand staan de command line arguments geprogrammeerd. Je kunt de code
op de volgende manier runnen:

python main.py <6_1/6_2/6_3/9_1/9_2/9_3/12> <breadth/depth/random>

Je kunt dus als command line meegeven welk bord je met welk algoritme wilt laten
runnen.

* board.py
In dit bestand staat alles geprogrammeerd wat met het Rush hour bord heeft te
maken. Het bord kan worden geinitialiseerd, geprint, gemaakt, geupdated, alle
mogelijk bewegingen op het bord kunnen worden teruggegeven en er kan gekeken
worden of het bord de oplossing is.

* vehicles.py
In dit bestand staat de initialisatie van de auto's op het Rush Hour bord
geprogrammeerd.

* algorithms.py
In dit bestand staan alle algoritmes geprogrammeerd. Daarnaast staan hier ook
een aantal functies in die gebruikt worden bij de algoritmes, zoals iets omzetten
naar een string of het updaten van de vehicles array.

Bij Random Search kun je zelf nog aanpassen hoeveel iteraties (iterations) je
wilt runnen. Bij Reversed Iterative Deepening Depth First Search kun je zelf nog
aanpassen wat de maximum depth is. Als je een maximum depth van 1000 invult, dan
is de maximum depth (eigenlijk 1002, maar het is tot 1002 dus hij zal niet verder
zoeken dan in laag 1001). Dit komt omdat in de maximum depth niet wordt meegenomen
dat de eerste stap en het eruit rijden van de rode auto ook zetten zijn.

* CSV files
In de CSV files staan alle borden die bij deze case horen beschreven. Het eerste
element bepaald of de auto een horizontale of verticale auto is. Het tweede
element is de ID van de auto, waar de rode auto wordt aangegeven met een #. bij
het runnen van main.py kun je meegeven welk van deze borden je wilt runnen.
