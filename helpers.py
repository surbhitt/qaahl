# set of helper functions

def is_cursor_on_node(curx, cury, cx, cy, rad):
    # for a node that is circular
    # curx, cury = cursor(x, y);  cx, cy = center(x, y)
    if (curx-cx)**2 + (cury-cy)**2 <= rad**2:
        return False
    return True

