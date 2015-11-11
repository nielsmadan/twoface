import vim
import venom
import os.path

MAP_FILE_EXTENSION = {
    'h': ['c', 'cpp'],
    'hpp': ['cpp'],
    'cpp': ['hpp', 'h'],
    'c': ['h'],
}

def __gen_open_fn(open_file_fn):
    def open_fn():
        fpath = venom.get_current_file_path()

        possible_files = find_possible_files(fpath)

        existing_files = filter_existing_files(possible_files)

        if len(existing_files) != 0:
            open_file_fn(existing_files[0])

    return open_fn

def filter_existing_files(file_list):
    return [f for f in file_list if os.path.isfile(f)]

def find_possible_files(fpath):
    (path, extension) = os.path.splitext(fpath)

    return [path + '.' + ext for ext in MAP_FILE_EXTENSION[extension[1:]]]

toggle_file = __gen_open_fn(venom.open_file)
open_horizontal = __gen_open_fn(venom.open_file_hsplit)
open_vertical = __gen_open_fn(venom.open_file_vsplit)
open_tab = __gen_open_fn(venom.open_file_tab)
