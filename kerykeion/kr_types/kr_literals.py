"""
    This is part of Kerykeion (C) 2023 Giacomo Battaglia
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Literal

# Zodiac Types:
ZodiacType = Literal["Tropic", "Sidereal"]

# Sings:
Sign = Literal[
    "Ari", "Tau", "Gem", "Can", "Leo", "Vir", "Lib", "Sco", "Sag", "Cap", "Aqu", "Pis"
]

Houses = Literal[
    "First_House",
    "Second_House",
    "Third_House",
    "Fourth_House",
    "Fifth_House",
    "Sixth_House",
    "Seventh_House",
    "Eighth_House",
    "Ninth_House",
    "Tenth_House",
    "Eleventh_House",
    "Twelfth_House",
]

Planet = Literal[
    "Sun",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
    "Mean_Node",
    "True_Node",
]

Element = Literal["Air", "Fire", "Earth", "Water"]

Quality = Literal[
    "Cardinal",
    "Fixed",
    "Mutable",
]


ChartType = Literal["Natal", "Composite", "Transit"]

LunarPhaseEmoji = Literal["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]