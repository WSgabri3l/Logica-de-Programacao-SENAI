email = input("Insira seu email: ")

validacao_1 = email[0].isalpha()

if email == "":
    print ("O email informado não passou pelos critérios de validação, tente novamente.")

elif not validacao_1:

    print ("O email informado não passou pelos critérios de validação, tente novamente.")

elif len(email) < 11:
    
    print ("O email informado não passou pelos critérios de validação, tente novamente.")

elif email.find("@") < 0:

    print ("O email informado não passou pelos critérios de validação, tente novamente.")

else:

    print (f"Email {email} está válido.")

    