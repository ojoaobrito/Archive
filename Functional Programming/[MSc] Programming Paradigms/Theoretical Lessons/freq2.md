**Paradigmas de Programação - Frequência 2**

# **Type Classes**

Em Haskell, as **classes agrupam tipos**, em vez de objetos como tradicionalmente se faz em Java ou outras linguagens.

Define-se um tipo do seguinte modo: 

```haskell
-- exemplo com o tipo de dados Maybe
data Maybe a = Nothing | Just a
```

Se, por exemplo, quisermos declarar um tipo de dados como instância de uma classe:

```haskell
-- EXEMPLO 1
-- definição da classe Eq
class Eq a where
(==) :: a -> a -> Bool

-- NOTA: "==" é um método da classe Eq
(==) :: Eq a => a -> a -> Bool

-- definição de uma instância de Eq para o tipo de dados Maybe
instance (Eq a) => Eq (Maybe a) where
    Nothing == Nothing = True
    Just a1 == Just a2 = a1 == a2


-- EXEMPLO 2
-- definição da classe Listable
class Listable a where 
    toList :: a -> [Int]

-- definição de uma instância de Listable para o tipo de dados Bool
instance Listable Bool where 
    toList True = [1]
    toList False = [0]


-- EXEMPLO 3
class Show a where 
    show :: a -> String

instance (Show a) => Show (Maybe a) where
    show (Nothing) = show "Nothing Much"
    show (Just a) = show ("Just ")++ show a ++("!")


-- EXEMPLO 4
class Num a where
(+), (-), (*) :: a -> a -> a 
negate :: a -> a
abs, signum :: a -> a 
fromInteger :: Integer -> a
```

# **Monads**
Uma monad é uma classe que permite encadear operações. 

```haskell
-- definição da classe Monad
class Monad where
   (>>=) :: Monad m => m a -> (a -> m b) -> m b
   return :: a -> m a

-- definição de uma instância de Monad para o tipo de dados Maybe
instance Monad Maybe where 
    Nothing >>= f   = Nothing 
    (Just x) >>= f  = f x 
    return          = Just
```


# **Functors and Applicative Functors**







## Operações *eval*, *exec* e *comp*



## Provas por indução