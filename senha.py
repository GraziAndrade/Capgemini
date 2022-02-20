#Validar campo senha
while True:
    senha = str(input("Digite sua senha : "))
    if len(senha) < 6 :
        print("A senha deve conter pelo menos 6 caracteres: ")
    elif senha.isalpha():
        print("A senha deve conter pelo menos 1 número: ")
    elif senha.isupper():
        print("A senha deve conter pelo menos 1 caractere minúsculo: ")
    elif senha.islower():
        print("A senha deve conter pelo menos 1 caractere MAIUSCULO: ")
    elif senha.isalnum() :
        print("A senha deve conter pelo menos 1 caractere especial: ")
    else:
        break