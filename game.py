import field
from item_factory import *
from item_manager import *
from helpers import *
from position import *
import physics
import sys
import os
import copy
from input_mode import raw_mode

levels_path = "./levels/"
game_keys   = ["w", "a", "s", "d"]
system_keys = ["q", "r"]

def upp_1(): 
    obj = create_item("#", create_position(1,0))
    _field = field.add_to_field(obj)
    _field = field.add_to_field(create_item("#", create_position(0,1)), _field)
    _field = field.add_to_field(create_item("#", create_position(2,1)), _field)
    _field = field.add_to_field(create_item("#", create_position(1,2)), _field)
    _field = field.add_to_field(create_item("@", create_position(1,1)), _field)
    field.draw(_field)

def clear():
    print("\033c")

def generate(map_name):
    symbol_field = []
    with open(levels_path+map_name, 'r') as f:
        for line in f:
            array = list(line)
            slice_unwanted(array)
            symbol_field.append(array)

    object_field = field.symbolfield_to_objectfield(symbol_field)
    return object_field

def move(position, ch):
    switcher = {
        "w": moveUp(position),
        "a": moveLeft(position),
        "s": moveDown(position),
        "d": moveRight(position)
    }
    try:
        return switcher[ch]
    except:
        print("Det finns bara w a s d att använda")
        return position


def is_game_action_key(ch):
   return True if ch in game_keys else False 

def is_system_action_key(ch):
    return True if ch in system_keys else False
        
def game_won(game_field):
    return field.number_of("box", game_field) == field.number_of_in_store("box", game_field)

def main(game_field):
    clear()
    original_field = copy.deepcopy(game_field)
    field.draw(game_field)
    ch = None
    print("Använd w a s d för att röra på dig")
    with raw_mode(sys.stdin):
        try:
            while not game_won(game_field):
                ch = sys.stdin.read(1)
                player         = field.player(game_field)
                if is_system_action_key(ch): break
                next_position  = move(position_of(player), ch)
                next_obj       = field.item_at(next_position, game_field)
                last_position  = move(next_position, ch)
                last_position  = next_position if last_position == None else last_position
                last_obj       = field.item_at(last_position, game_field)
                if physics.evaluate(player, next_obj, last_obj):
                    game_field = field.move_in_field(next_obj, last_position, game_field)
                    game_field = field.move_in_field(player,   next_position, game_field)
                    clear()
                    field.draw(game_field)
            if game_won(game_field):
                print("Du vann!")
            if is_system_action_key(ch) and ch == "r":
                main(original_field)
        except (KeyboardInterrupt, EOFError):
            pass


def choose_map():
    all_levels = os.listdir("./levels")
    print("Banor: ")
    for i in range(len(all_levels)):
        print(i+1, all_levels[i])
    print()
    level_index = int(input("Skriv numret på banan: "))
    if level_index <= len(all_levels) and level_index > 0:
        return all_levels[level_index-1]
    else:
        return choose_map()

def menu():
    clear()
    print("Welcome to 倉庫番")
    print()
    chosen_map = choose_map()    
    main(generate(map_name = chosen_map))

while True:
    menu()
    







