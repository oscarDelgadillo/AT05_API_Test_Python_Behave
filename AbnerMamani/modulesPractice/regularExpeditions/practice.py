import re
#
# idPatron=re.compile('[a,z]]')
# idUser="12132"
# if re.match(idPatron, idUser):
#     print('true')
# else:
#     print('false')
#




patron = re.compile('^[a-z0-9]*$') # coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
cadena = 'baTa'
print (patron.match(cadena))

print (patron.search(cadena))

patron.match(cadena)  # <_sre.SRE_Match object at 0x02303BF0>
patron.search(cadena) # <_sre.SRE_Match object at 0x02303C28>
cadena = 'ba3455' # la coincidencia no está al principio!
patron.search(cadena)  #  <_sre.SRE_Match object at 0x02303BF0>
# print (patron.match(cadena)) # None
