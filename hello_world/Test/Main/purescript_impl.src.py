from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
from os.path import join as joinpath
project_path = "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\hello-world"
res = block( "No document"
           , assign( "ps_main"
                   , metadata( 3
                             , 8
                             , joinpath(project_path, "test\\Main.purs")
                             , 0 ) )
           , assign("exports", record(("main", var("ps_main")))) )
res = module_code(res)
