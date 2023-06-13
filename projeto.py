from funcoes import *

while True:
    menu_prin = menu_principal()
    if(menu_prin == 0): #FECHANDO O PROGRAMA
        print("Obrigada pela preferência!")
        break
    elif(menu_prin == 1): #CADASTRANDO NOVO USUARIO
        print("=-" * 17)
        cadastrar_vendedor(0)
    elif(menu_prin == 2): #FAZENDO LOGIN
        print("=-" * 17)
        confere_login()
        while True:
            opcao = menu_vendedor()
            if(opcao == 0): #SAIR
                print("Estamos desconectando você. Obrigada pela preferência!")
                break
            elif(opcao == 1): #CADASTRAR PRODUTO
                print("=-" * 17)
                cadastrar_produto()
            elif(opcao == 2): #REMOVER PRODUTO
                print("=-" * 17)
                remover_produto()
            elif(opcao == 3): #BUSCAR PRODUTO
                print("=-" * 17)
                buscar_produto_vendedor(1, "")
            elif(opcao == 4): #ATUALIZAR PRODUTO
                print("=-" * 17)
                atualizar_produto()
            elif(opcao == 5): #ATUALIZAR SENHA
                print("=-" * 17)
                atualizar_senha()
    elif(menu_prin == 3):
        while True:
            escolha = menu_cliente()
            if(escolha == 0):
                print("Obrigada pela preferência!")
                break
            elif(escolha == 1):
                busca_cliente()
            elif(escolha == 2):
                compras = mostrar_carrinho()
                if(compras == 1):
                    print("Obrigada pela preferência!")
                    break
                else:
                    continue
            elif(escolha == 3):
                consultarchatgpt()