# Project One Storyboard | Text-Based Adventure Game

> Complete the `TODO:` prompts using your own game idea. This file is a graded
> Project One deliverable and later becomes a reference for Project Two.

## Theme and Storyline
# IT-140: Text Adventure Game.storyboard

# Theme: Space Station Escape 
# Storyline: You wake up on an abandoned space station. You must collect 6 ship parts 
# to repair the escape pod before the station's malfunctioning AI shuts down life support.

def show_instructions():
    """Prints the game instructions and commands to the player."""
    print("==================================================")
    print("               SPACE STATION ESCAPE               ")
    print("==================================================")
    print("Collect 6 items to repair the pod before facing the AI!")
    print("Move commands: Go North, Go South, Go East, Go West")
    print("Get command: Get 'item_name'")
    print("Type 'Exit' to quit the game.")
    print("==================================================")

def main():
    # Define the 8-room dictionary layout with connections and items
    # Every room except the Start room ('Cryo Chamber') and Villain room ('Control Room') has 1 item
    rooms = {
        'Cryo Chamber': {  # 1. Start Room
            'North': 'Research Lab',
            'East': 'Crew Quarters'
        },
        'Research Lab': {  # 2. Room with Item
            'South': 'Cryo Chamber',
            'East': 'Storage Bay',
            'item': 'Keycard'
        },
        'Storage Bay': {  # 3. Room with Item
            'West': 'Research Lab',
            'East': 'Engine Room',
            'item': 'Spacesuit'
        },
        'Engine Room': {  # 4. Room with Item
            'West': 'Storage Bay',
            'South': 'Reactor Core',
            'item': 'Plasma Torch'
        },
        'Reactor Core': {  # 5. Room with Item
            'North': 'Engine Room',
            'West': 'Greenhouse',
            'item': 'Fuel Cell'
        },
        'Greenhouse': {  # 6. Room with Item
            'East': 'Reactor Core',
            'West': 'Crew Quarters',
            'item': 'Oxygen Tank'
        },
        'Crew Quarters': {  # 7. Room with Item
            'West': 'Cryo Chamber',
            'East': 'Greenhouse',
            'North': 'Control Room', # Leads to Villain Room
            'item': 'Navigation Chip'
        },
        'Control Room': {  # 8. Villain Room
            'South': 'Crew Quarters',
            'item': 'Malfunctioning AI'  # The threat
        }
    }

    # Track player's current state
    current_room = 'Cryo Chamber'
    inventory = []
    required_items_count = 6

    # Display instructions at start
    show_instructions()

    # Main gameplay loop
    while True:
        print(f"\nYou are in the {current_room}")
        print(f"Inventory: {inventory}")
        
        # Check if the current room contains an item
        if 'item' in rooms[current_room] and current_room != 'Control Room':
            print(f"You see a {rooms[current_room]['item']}")
        print("--------------------------------------------------")

        # Win/Loss condition check when entering the Villain Room
        if current_room == 'Control Room':
            if len(inventory) == required_items_count:
                print("Congratulations! You collected all 6 items, bypassed the Malfunctioning AI, and escaped!")
                print("You win!")
            else:
                print("Oh no! You entered the Control Room without all 6 required items.")
                print("The Malfunctioning AI locked you out of the escape pod forever.")
                print("Game Over!")
            break

        # Get player input
        player_input = input("Enter your move: ").strip().split(maxsplit=1)
        
        # Handle empty input
        if not player_input:
            continue
            
        action = player_input[0].title()
        
        # Handle game exit
        if action == 'Exit':
            print("Thanks for playing!")
            break

        # Handle movement command (e.g., "Go North")
        if action == 'Go' and len(player_input) > 1:
            direction = player_input[1].title()
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")
                
        # Handle item collection command (e.g., "Get Keycard")
        elif action == 'Get' and len(player_input) > 1:
            target_item = player_input[1].title()
            if 'item' in rooms[current_room] and rooms[current_room]['item'].title() == target_item:
                inventory.append(rooms[current_room]['item'])
                print(f"You picked up the {rooms[current_room]['item']}!")
                del rooms[current_room]['item']  # Remove item from the room once picked up
            else:
                print(f"Can't find '{target_item}' here!")
                

Before submitting, compare this storyboard with `game_map.drawio`.

* [ ] I included eight (8) rooms.
* [ ] I included six (6) collectable items.
* [ ] The start room has no item.
* [ ] The villain room has no item.
* [ ] Every room except the start room and villain room contains one item.
* [ ] Room, item, and villain names match my map.
* [ ] The map allows the player to collect all required items before the
  villain is encountered.

## Project Two Handoff

Keep this file after Project One. In Module Seven, use these names and design
choices when building the final room/item dictionary and player-facing output.
