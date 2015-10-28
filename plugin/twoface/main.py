import vim
import venom
import os.path

MAP_FILE_EXTENSION = {
    'h': ['c', 'cpp'],
    'hpp': ['cpp'],
    'cpp': ['hpp', 'h'],
    'c': ['h'],
}

def __gen_foo(open_file_fn):
    def foo():
        fpath = venom.get_current_file_path()

        possible_files = find_possible_files(fpath)

        existing_files = [f for f in possible_files if os.path.isfile(f)]

        if len(existing_files) != 0:
            open_file_fn(existing_files[0])

    return foo

def find_possible_files(fpath):
    (path, extension) = os.path.splitext(fpath)

    return [path + '.' + ext for ext in MAP_FILE_EXTENSION[extension[1:]]]

toggle_file = __gen_foo(venom.open_file)
open_horizontal = __gen_foo(venom.open_file_hsplit)
open_vertical = __gen_foo(venom.open_file_vsplit)
open_tab = __gen_foo(venom.open_file_tab)
