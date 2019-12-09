from item_manager import *

def evaluate(player, next_obj, last_obj):
    if is_movable(next_obj):
        if is_stepable(last_obj):
            return True
    elif is_stepable(next_obj):
        return True
    return False
