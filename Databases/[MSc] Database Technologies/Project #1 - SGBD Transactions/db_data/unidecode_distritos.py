import os
from unidecode import unidecode

handler = open( "dados_processados/distritos.csv", "r" )
handler2 = open( "dados_processados/distritos_tmp.csv", "w" )

first = True
for line in handler :
    if first :
        handler2.write( unidecode( line ) )
        first = False
    else :
        handler2.write( unidecode( line.lower() ) )

handler.close()
handler2.close()

os.remove( "dados_processados/distritos.csv" )
os.rename( 
    "dados_processados/distritos_tmp.csv",
    "dados_processados/distritos.csv"
)