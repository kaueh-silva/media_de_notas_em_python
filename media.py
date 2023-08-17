nota = float(input("Digite sua nota,entre 0 e 10 \n"))

if nota >=9.0:
    conceito = "A"
    print("Seu conceito foi '{}', e esta aprovado".format(conceito))
elif nota >=7.5 and nota <=8.0:
    conceito = "B"
    print("Seu conceito foi '{}', e esta aprovado".format(conceito))

elif nota >=6.0 and nota <=7.4:
    conceito = "C"
    print("Seu conceito foi '{}', e esta aprovado".format(conceito))

elif nota >=4.0 and nota <=5.9:
    conceito = "D"
    print("Seu conceito foi '{}', e esta reprovado".format(conceito))

else:
    conceito = "E"
    print("Seu conceito foi '{}', e esta reprovado".format(conceito))