Nome_Herói = str(input("Informe o nome do Héroi: ")) # é o nome do herói
XP = int(input("Digite um número entre 0 e 20000 jair")) # é a quantidade de Experiencia do  herói

Lista_dados_Hero = [Nome_Herói, XP]
if XP <= 1000:
    print("O Herói de " + Nome_Herói +" está no nível Ferro")
elif XP > 1000 and XP <= 2000:
    print("O Herói de " + Nome_Herói +" está no nível Bronze")
elif XP > 2000 and XP <= 5000:
    print("O Herói de " + Nome_Herói +" está no nível Prata")   
elif XP > 5000 and XP <= 7000:
    print("O Herói de " + Nome_Herói +" está no nível Ouro")
elif XP > 7000 and XP <= 8000:
    print("O Herói de " + Nome_Herói +" está no nível Platina")
elif XP > 8000 and XP <= 9000:
    print("O Herói de " + Nome_Herói +" está no nível Ascendente")
elif XP > 9000 and XP <= 10000:
    print("O Herói de " + Nome_Herói +" está no nível Imortal") 
else:
    print("O Herói de " + Nome_Herói +" está no nível Radiante")
