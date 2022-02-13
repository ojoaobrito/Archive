j :: Int -> Maybe Int
j s = return s

g :: Int -> Maybe Int
g s = return (s+1)

h :: Int -> Maybe Int
h s = return (s+2)

f :: Int -> Maybe Int
f s = do 
      m <- g s >>= h
      n <- h m 
      j n
