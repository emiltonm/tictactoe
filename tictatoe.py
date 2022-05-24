DOUBLE_LEFT_TOP = u'\u2554'
DOUBLE_VERTI_PIPE = u'\u2551'
DOUBLE_LEFT_BOTTOM = u'\u255a'
DOUBLE_RIGHT_TOP = u'\u2557'
DOUBLE_RIGHT_BOTTOM = u'\u255d'
DOUBLE_HORIZ_PIPE = u'\u2550'

DOUBLE_RIGHT_MIDDLE = u'\u2560'
DOUBLE_LEFT_MIDDLE = u'\u2563'
DOUBLE_BOTTOM_MIDDLE = u'\u2566'
DOUBLE_TOP_MIDDLE = u'\u2569'

DOUBLE_CROSS = u'\u256c'

SINGLE_LEFT_TOP = u'\u250c'
SINGLE_VERTI_PIPE = u'\u2502'
SINGLE_LEFT_BOTTOM = u'\u2514'
SINGLE_RIGHT_TOP = u'\u2510'
SINGLE_RIGHT_BOTTOM = u'\u2518'
SINGLE_HORIZ_PIPE = u'\u2500'

#NROWS,NCOLUMNS,ANCHO,ALTO,SIMPLE O DOBLE,HEADER,FOOTER,LISTA_VALORES
def draw_grid(nrows,ncolumns,valores):
    left_top=DOUBLE_LEFT_TOP
    horizontal=DOUBLE_HORIZ_PIPE
    right_top=DOUBLE_RIGHT_TOP
    vertical=DOUBLE_VERTI_PIPE
    left_bottom=DOUBLE_LEFT_BOTTOM
    right_bottom=DOUBLE_RIGHT_BOTTOM
    bottom_middle=DOUBLE_BOTTOM_MIDDLE
    top_middle=DOUBLE_TOP_MIDDLE
    cross=DOUBLE_CROSS
    right_middle=DOUBLE_RIGHT_MIDDLE
    left_middle=DOUBLE_LEFT_MIDDLE

    if nrows < 1 or ncolumns < 1:
        print("los valores de numero de renglones, columnas, ancho y alto deben ser mayores a 0")
        return("los valores de numero de renglones, columnas, ancho y alto deben ser mayores a 0")
    #nrows=nrows+2
    print(left_top+(horizontal+bottom_middle)*(ncolumns-1)+horizontal+right_top)
    for contador_rows in range(nrows):
        renglon=""        
        for contador_columns in range(ncolumns):
            renglon=renglon+str(valores[contador_columns+contador_rows*ncolumns])+vertical
        print(vertical+renglon)
        if contador_rows < nrows-1:
            print(right_middle+(horizontal+cross)*(ncolumns-1)+horizontal+left_middle)
    print(left_bottom+(horizontal+top_middle)*(ncolumns-1)+horizontal+right_bottom)
    


draw_grid(3,8,["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
