from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign("ps_main", metadata(3, 8, "test\Main.purs", 0))
           , assign("exports", record(("main", var("ps_main")))) )
res = module_code(res)
