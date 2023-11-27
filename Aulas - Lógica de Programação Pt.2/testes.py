#Arquivo
#Ação

def escrever():

    f = open("texto.txt", "w")
    f.write("Hello world!")
    f.close()

f = open("texto.txt", "r")
print(f.read())
f.close()