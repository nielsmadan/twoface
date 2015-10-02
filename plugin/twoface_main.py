import venom
import vim

from twoface import toggle_file, open_horizontal, open_vertical, open_buffer

venom.py_fn_to_vim_command("TwofaceToggleFile", toggle_file)
venom.py_fn_to_vim_command("TwofaceOpenHorizontal", open_horizontal)
venom.py_fn_to_vim_command("TwofaceOpenVertical", open_vertical)
venom.py_fn_to_vim_command("TwofaceOpenBuffer", open_buffer)

vim.map.nnoremap("<leader>tt", ":TwofaceToggleFile<CR>")
vim.map.nnoremap("<leader>th", ":TwofaceOpenHorizontal<CR>")
vim.map.nnoremap("<leader>tv", ":TwofaceOpenVertical<CR>")
vim.map.nnoremap("<leader>tb", ":TwofaceOpenBuffer<CR>")
