"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Simplified 8-room map dictionary tracking directional connectivity paths
rooms = {
    'Cryo Chamber': {  # 1. Start Room
        'North': 'Research Lab',
        'East': 'Crew Quarters'
    },
    'Research Lab': {  # 2. Room
        'South': 'Cryo Chamber',
        'East': 'Storage Bay'
    },
    'Storage Bay': {  # 3. Room
        'West': 'Research Lab',
        'East': 'Engine Room'
    },
    'Engine Room': {  # 4. Room
        'West': 'Storage Bay',
        'South': 'Reactor Core'
    },
    'Reactor Core': {  # 5. Room
        'North': 'Engine Room',
        'West': 'Greenhouse'
    },
    'Greenhouse': {  # 6. Room
        'East': 'Reactor Core',
        'West': 'Crew Quarters'
    },
    'Crew Quarters': {  # 7. Room
        'West': 'Cryo Chamber',
        'East': 'Greenhouse',
        'North': 'Control Room'  # Path leading to the ending area
    },
    'Control Room': {  # 8. Ending / Villain Room
        'South': 'Crew Quarters'
    }
}
