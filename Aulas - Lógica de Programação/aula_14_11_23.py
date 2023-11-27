email = input("Insira seu email: ")

validacao_1 = email[0].isalpha()

nome_email = email.split("@")

validacao_2 = len(nome_email)
print(validacao_2)

validacao_3 = email.count("@")


if validacao_1 == True:
    print("AAA")

elif validacao_2 == True:
    print ("BBB")

elif validacao_3 == True:
    print ("CCC")

else:
    print ("SIM")

# if email == "":
#     print ("O email informado não passou pelos critérios de validação, tente novamente.")

# elif validacao_1 == False:

#     print ("O email informado não passou pelos critérios de validação, tente novamente.")

# elif validacao_2 < 11:
    
#     print ("O email informado não passou pelos critérios de validação, tente novamente.")

# elif validacao_3 < 1:

#     print ("O email informado não passou pelos critérios de validação, tente novamente.")

# else:

#     print (f"Email {email} está válido.")

