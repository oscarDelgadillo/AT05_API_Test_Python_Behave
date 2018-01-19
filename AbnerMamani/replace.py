#The function replaces all occurrences of old with new in a string
def replace(song, origen, after):
   varArr= song.split(origen)
   strfinal=after.join(varArr)
   print(strfinal)

replace("Mississippi", "i", "I")