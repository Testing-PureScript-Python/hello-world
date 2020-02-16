# **Hello World** of PureScript-Python

## Requisite

- Installation of [PureScript Python](https://github.com/thautwarm/purescript-python/), currently you have to install it from source with command `stack install .`.

- Python version `>=3.5`, and the installation of following Python packages:
  - purescripto
  - pysexpr

## Notes

Currently, we cannot use `Prelude` and many other libraries.

Hence we use this `src/Main.purs`:

```purescript
module Main where
data IO a
foreign import println :: forall a. a -> IO {}

main :: IO {}
main = println "hello world"
```

`Main.js` in `src` is only for IDE use. PureScript has an awesome IDE support within VSCode, and I bet you will be a fan of this IDE functions if you're also a Haskeller(you know why)..

You can remove `Main.js` if you don't want to enjoy the IDE.

`Main.py` is the Python FFI file.

Just use the purescript build tool `spago`(bundled in purescript releases), type `spago run` in the root of this project, you got

```
hello world
```

See Python package  `hello_world/hello_world` to check the effect.

See configurations in `spago.dhall`, there're 2 crucial points:

1. remove `dependencies = [ "console", "effect", ...]`, use `dependencies = [] : List Text`
2. add `backend = "pspy"`

Finally, we will give examples of customizing the name of generated Python package, and the search path of foreign files.
