import Prelude hiding (Monad,Maybe,Nothing,Just,Eq)

data Maybe a = Nothing | Just a

{--class Monad m where
    (>>=) :: m a -> (a -> m b) -> m b 
    return :: a -> m a

instance Monad (Maybe a) where
    Nothing >>= f = Nothing 
    (Just x) >>= f = f x 
    return = Just--}

class Eq a where
    (==) :: a -> a -> Bool

instance (Eq a) => Eq (Maybe a) where
    Nothing == Nothing      = True
    Just a1 == Just a2      = a1 Main.== a2