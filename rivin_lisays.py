'''
file.read(): 
    - lukee koko tiedoston tai määritetyn määrän tavuja YHDEKSI STRINGIKSI
    - palauttaa stringiä koko tiedoston sisältön 
    - print(content[:50]) # lukisi 50 ensimäistä merkkiä
    - hyvä suhteelisen pieniin tiedostoihin <----- 
lines = file.readlines()
    - lukee tiedoston sisällön listan rivejä
    - palautta listan string-muotoisena, jokainen alkio listassa on yksi rivi
    - hyvä käyttää, jos haluaa yksittäisiä rivejä manipuloida
    - jos on iso tiedosto, on parempi käydä rivi riviltä läpi:
        for line in f:
            ... mitä haluaakaan tehdä # muistille kevyempi
f.write('HELLO WORLD')
    - ei automaattisesti lisä newline \n 
    - hyvä jos haluaa kirjoittaa yhden pitkän stringin tai rivi riviltä tiedostoa 

lines = ["Rivi 1\n", "Rivi 2\n", "Rivi 3\n", "Rivi 4\n"]
f.writelines(lines)
    - ei automaattisesti lisä newlinea \n
    - hyvä, jos haluaa kirjoittaa useita rivejä kerralla tai muokattuaan tiedoston sisältöä
'''

# luetaan tiedoston sisältö muuttujaan
with open('tekstia.txt', 'r') as file: 
    vanha_teksti = file.read() # löytyy read(), readlines(), write(), writelines()

# kirjoitetaan uusi teksti ennen vanhaan sisältöä
with open('tekstia.txt', 'w') as f:
    f.write('Hello world\n' + vanha_teksti)

with open('tekstia.txt', 'a') as f:
    f.write('\nViimeinen rivi\n')

""" 
from pathlib import Path
file_path = Path("abc.txt")
if file_path.exists(): # jost tiedosto löytyi """