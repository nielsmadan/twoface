import vim
import venom
import os.path


def toggle_file():
    fpath = venom.get_current_file_path()

    path_ext = os.path.splitext(fpath)

    newpath = ""

    if path_ext[1] == ".h":
        newpath = path_ext[0] + ".cpp"
    elif path_ext[1] == ".cpp":
        newpath = path_ext[0] + ".h"

    venom.open_file(newpath)

def open_horizontal():
    pass

def open_vertical():
    pass

def open_buffer():
    pass
