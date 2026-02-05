mensaje="hay un error"

while mensaje=="hay un error":
    try:
        entrada=int(input("Digite la entrada: "))
        print("-------------------------")
        print(str(entrada))
        print("FIN DE LA EJECUCION")
    except:
        mensaje="hay un error"
