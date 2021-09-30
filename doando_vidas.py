print("Vamos doar vidas???")
print("Vamos lhe fazer algumas perguntas para saber se vc está pronto para essa atitude muito importante!!!")

idade = int(input("Digite sua idade em anos: "))
if idade > 18 and idade < 70:
    if int(input("Digite seu peso em kg: "))> 49:
        if input("Você fez tatuagem no ultimo ano: s ou n ? ") == "n":
            if input("Você ingeriu alguma bebida alcoólica nas ultimas 12h: s ou n ? ") == "n":
                print("Você será um doador de vida :-p")
            else:
                print("Você NÃO poderá ser um doador devido a sua ingestão de bebidas alcoolicas!")
        else:
            print("Você NÃO poderá ser um doador devido o periodo que vc fez a sua ultima tatuagem!")
    else:
        print("Você NÃO poderá ser um doador devido ao seu baixo peso!")
else:
    print("Você NÃO poderá ser um doador devido a sua idade!")


