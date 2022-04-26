# line.decode('latin1')
# distritos já estão processados

import csv
import os
from unidecode import unidecode

def load_distritos() :
    with open( 'dados_processados/distritos.csv' ) as csv_file :
        reader = csv.reader( csv_file, delimiter="$" )
        first = True
        for row in reader :
            if first :
                first = False
            else :
                distritos[ row[1].lower().replace(' ', '') ] = row[0]

def calculate_concelhos() :
    file_list = os.listdir( os.getcwd() + "/dados" )

    for f in file_list :
        distrito_name = unidecode(f.split("_")[0]).lower()

        hdl = open( 'dados/' + f, "rb" )
        first = True
        for line in hdl.readlines() :
            if first : first = False
            else :
                rows = line.decode('latin1').split(',')
                no_garbage = rows[0].replace('"', '').replace('\r','')
                concelhos[ no_garbage ] = distrito_name

    #---- Save data from concelhos to the concelhos.csv ----
    concelhos_lst = list( concelhos.items() )
    concelhos_lst = [
        ( int( distritos[ y ] ), x ) for (x,y) in concelhos_lst
    ]
    concelhos_lst.sort()

    hdl_concelhos = open( 'dados_processados/concelhos.csv', "w" )
    hdl_concelhos.write( 'IdConcelho$Nome$IdDistrito' )
    index = 1
    for c in concelhos_lst :
        hdl_concelhos.write(
            "\n" + str( index ) + "$" +
            c[1] + "$" +
            str( c[0] ) 
        )
        index += 1
    hdl_concelhos.close()

def calculate_vias() :

    concelhos.clear()

    with open( 'dados_processados/concelhos.csv' ) as csv_file :
        reader = csv.reader( csv_file, delimiter="$" )
        first = True
        for row in reader :
            if first :
                first = False
            else :
                concelhos[ row[1] ] = row[0]

    file_list = os.listdir( os.getcwd() + "/dados" )

    for f in file_list :

        hdl = open( 'dados/' + f, "rb" )
        first = True
        for line in hdl.readlines() :
            if first : first = False
            else :
                rows = line.decode('latin1').split(',')
                no_garbage_via = rows[4].replace('"', '').replace('\r','')
                no_garbage_conce = rows[0].replace('"', '').replace('\r','')
        
                #---- O processamento dos campos do tuplo são processados ----
                #---- aquando a insercao da data nos ficheiros ----
                vias[ no_garbage_via ] = ( no_garbage_conce, "unknown" )

    #---- Save data from concelhos to the concelhos.csv ----
    vias_lst = list( vias.items() )
    vias_lst = [
        ( int( concelhos[y] ), x, z ) for (x, (y,z)) in vias_lst
    ]
    vias_lst.sort()

    hdl_vias = open( 'dados_processados/vias.csv', 'w' )
    hdl_vias.write( 'IdVia$Nome$IdConcelho$Tipo' )
    index = 1
    for v in vias_lst :
        hdl_vias.write(
            "\n" + str( index ) + "$" +
            v[1] + "$" +
            str( v[0] ) + "$" +
            v[2]
        )
        index += 1
    hdl_vias.close()

def calculate_acidentes() :

    vias.clear()

    with open( 'dados_processados/vias.csv' ) as csv_file :
        reader = csv.reader( csv_file, delimiter="$" )
        first = True
        for row in reader :
            if first :
                first = False
            else :
                vias[ row[1] ] = row[0]    

    file_list = os.listdir( os.getcwd() + "/dados" )

    '''
    vias_set = set()
    for (x, y) in list( vias.items() ) :
        vias_set.add(y)
    '''

    for f in file_list :

        hdl = open( 'dados/' + f, "rb" )
        first = True
        for line in hdl.readlines() :
            if first : first = False
            else :
                ####---- Treat Bad Line Formating ----
                pline = line.decode( 'latin1' ).replace('\r','').replace('\n','').replace('"','')

                rows = pline.split( ',' )

                km, natureza = '', ''

                #---- Verificacao da via na base de dados ----
                try :
                    g = vias[ rows[ 4 ] ]
                except :
                    pass

                try :
                    if len(rows) == 8 :
                        km = str(int(( (rows[5] + rows[6]).replace('\'', '') )))
                        natureza = rows[7]
                    if len(rows) == 7 :
                        if rows[5] == '-' :\
                            km = ''
                        else : km.replace('\'','')
                        natureza = rows[6]
                except :
                    continue

                acidentes.append((
                    rows[1], #data_hora
                    rows[2], #mortos
                    rows[3], #feridos graves
                    rows[4].replace('"', '').replace('\r','').replace('\n',''), #via
                    km, #km
                    natureza  #natureza
                ))
                ####---- [END] Treat Bad Line Formating ----

        acidentes.sort()

        hdl_acidentes = open( 'dados_processados/acidentes.csv', 'w' )
        hdl_acidentes.write( "IdAcidente$DataHora$IdVia$Natureza$Km$Mortos$FeridosGraves" )
        index = 1
        for a in acidentes :

            aux = a[4]

            hdl_acidentes.write(
                "\n" + str( index ) + "$" + # id
                a[0] + "$" + # data
                str( vias[ a[3] ] ) + "$" + # id vias
                a[5] + "$" + # natureza
                aux + "$" + # caso o km n seja especificado
                a[1] + "$" + # mortos
                a[2] # feridos
            )
            index += 1
        hdl_acidentes.close()


distritos = {}
concelhos = {}
vias = {}
acidentes = []

load_distritos()
calculate_concelhos()
calculate_vias()
calculate_acidentes()

def wtf_clean() :
    os.rename(
        "dados_processados/acidentes.csv",
        "dados_processados/acidentes_tmp.csv"
    )

    hdl_in = open( "dados_processados/acidentes_tmp.csv", 'r' )
    hdl_out = open( "dados_processados/acidentes.csv", 'w' )

    for line in hdl_in :
        if line.count('$') != 6 or "$-$" in line : pass #print(line)
        else : hdl_out.write( line )


    hdl_in.close()
    hdl_out.close()
    os.remove( 'dados_processados/acidentes_tmp.csv' )

wtf_clean()