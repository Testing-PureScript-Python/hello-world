module Main where
data IO a
foreign import println :: forall a. a -> IO {}

main :: IO {}
main = println "hello world"
