from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
from os.path import join as joinpath
project_path = "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\hello-world"
res = block( "No document"
           , assign( "$foreign"
                   , call( var('import_module')
                         , "hello_world.Main.purescript_foreign" ) )
           , assign( "ps_main"
                   , call( get_attr(var("$foreign"), "println")
                         , metadata( 6
                                   , 16
                                   , joinpath(project_path, "src\\Main.purs")
                                   , "hello world" ) ) )
           , assign( "exports"
                   , record( ("main", var("ps_main"))
                           , ( "println"
                             , get_attr(var("$foreign"), "println") ) ) ) )
res = module_code(res)
