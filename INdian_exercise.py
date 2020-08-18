import csv
import re
main_path='/home/d3uslinux/Escritorio'
output_pat = '/home/d3uslinux/Escritorio/output.txt'
lista=[]
with open(main_path+'/'+'EXTukau.txt', encoding='latin1') as fich:
    with open(output_pat,'w',encoding='latin1' ) as fich_w:
        lector= csv.reader(fich)
        for index,linea in enumerate(lector):
            for val in linea:
                for val, unit in re.findall('([0-9\.]+)([A-Za-z]+)', val):
                    lista.append(val)
                    lista.append(unit)
            s = '\t'
            s = s.join(lista)

            fich_w.write(s)
            fich_w.write('\n')
            lista=[]



