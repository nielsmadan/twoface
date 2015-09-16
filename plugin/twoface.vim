call venom#Load()

let s:sfile = expand("<sfile>")

py << END_PY
import venom

venom.import_py(vim.eval("s:sfile"), "twoface_main")
END_PY
