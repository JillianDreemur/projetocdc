from funcoes import *

while True:
    menu_prin = menu_principal()
    if(menu_prin == 0): #FECHANDO O PROGRAMA
        print("Obrigada pela preferência!")
        break
    elif(menu_prin == 1): #CADASTRANDO NOVO USUARIO
        print("=-" * 17)
        cadastrar_vendedor()
    elif(menu_prin == 2): #FAZENDO LOGIN
        print("=-" * 17)
        login = confere_login(0, '')
        if(login == False):
            continue
        else:
            cpf_logado = login
            while True:
                opcao = menu_vendedor()
                if(opcao == 0): #SAIR
                    print("Estamos desconectando você. Obrigada pela preferência!")
                    break
                elif(opcao == 1): #CADASTRAR PRODUTO
                    print("=-" * 17)
                    cadastrar_produto(cpf_logado)
                elif(opcao == 2): #REMOVER PRODUTO
                    print("=-" * 17)
                    remover_produto(cpf_logado)
                elif(opcao == 3): #BUSCAR PRODUTO
                    print("=-" * 17)
                    buscar_produto_vendedor(1, "", cpf_logado)
                elif(opcao == 4): #ATUALIZAR PRODUTO
                    print("=-" * 17)
                    atualizar_produto(0, cpf_logado, '', '')
                elif(opcao == 5): #ATUALIZAR SENHA
                    print("=-" * 17)
                    atualizar_senha(cpf_logado)
    elif(menu_prin == 3):
        if(len(lista) <= 0):
            print("Pedimos perdão pelo inconveniente, mas nenhuma loja foi cadastrada ainda. "
                  "Por favor, volte em outro momento.")
        else:
            while True:
                escolha = menu_cliente()
                if(escolha == 0):
                    print("Obrigada pela preferência!")
                    break
                elif(escolha == 1):
                    busca_cliente()
                elif(escolha == 2):
                    if(mostrar_carrinho() == 1):
                        print("Obrigada pela preferência!")
                        break
                    else:
                        continue
                elif(escolha == 3):
                    consultarchatgpt()