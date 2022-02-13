{-# LANGUAGE FlexibleContexts #-}
import Control.Monad.State;
{-- 
Nome:
Numero:
--}


{-Questao 1
a) 
b)
c) 
-}

{- Questao 2
Hipotese de Inducao: compL (replica n x) = n

--}

{--Questao 3 --}
--a) 

--b)

--c) 

--d) 

--e) 

{-- Fim da Questao 3--}

{-- Questao 4 --}
--a)
data Expr = Val Int | Add Expr Expr 
type Stack = [Int]
type Code = [Op]
data Op = PUSH Int | ADD deriving Show 

eval :: Expr -> Int       
eval (Val n) = n
eval (Add n m) = eval n + eval m

exec :: Code -> Stack -> Stack
exec [] s = s
exec (PUSH n:rc) s = exec rc (n:s)
exec (ADD: c) (m:n:s) = exec c (n+m:s) 

comp :: Expr -> Code
comp (Val n) = [PUSH n]
comp (Add n m) = comp n ++ comp m ++ [ADD]

--b) 
{-- Assumir a propriedade da distributividade:
        exec (c ++ d) s = exec d (exec c s)
 
 Prova para Mult:
 --}

{-- Questao 5 --}
--Possivel solucao
data EstadoJogo = EJ {j1::Int,j2::Int,jogador::Bool} deriving Show


{-- Fim Questao 5 --}

{--Questao 6--}
data Arv a = Folha a | Nodo (Arv a) (Arv a) 

--Exemplos de arvores
arv1 = Nodo (Nodo (Folha 1) (Folha 2)) (Folha 3)
arv2 = Nodo (Nodo (Folha 4) (Nodo (Folha 1) (Folha 3))) (Nodo (Folha 2) (Folha 5))

--folhas :: Arv a -> [a]
--tamanho :: Arv a -> Int

--b)
--espelhar :: Arv a -> Arv a

--c)
{--Provar que 
    tamanho (espelhar t) = tamanho t 
   


--}

--d) 

--e)
instance Functor Arv where
  fmap f (Folha a)       = Folha $ f a
  fmap f (Nodo t1 t2) = Nodo (fmap f t1) (fmap f t2)

instance Applicative Arv where
  pure = Folha
  Folha f       <*> t            = f <$> t
  Nodo t1 t2 <*> Folha a       = Nodo (fmap ($ a) t1) (fmap ($ a) t2)
  Nodo t1 t2 <*> Nodo t3 t4 = Nodo (t1 <*> t3) (t2 <*> t4)

--instance Monad Arv where

--Exemplo