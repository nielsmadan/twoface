import vim
import venom
import os.path

MAP_FILE_EXTENSION = {
    'h': ['c', 'cpp'],
    'hpp': ['cpp'],
    'cpp': ['hpp', 'h'],
    'c': ['h'],
}

def toggle_file():
    fpath = venom.get_current_file_path()

    possible_files = find_possible_files(fpath)

    if len(possible_files) != 0:
        venom.open_file(possible_files[0])

def open_horizontal():
    pass

def open_vertical():
    pass

def open_tab():
    pass

def find_possible_files(fpath):
    (path, extension) = os.path.splitext(fpath)

    return [path + '.' + ext for ext in MAP_FILE_EXTENSION[extension[1:]]]
