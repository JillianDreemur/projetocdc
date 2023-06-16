#FUNÇÕES DO PROJETO
import openai

lista = []
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
carrinho = []

def menu_principal():
    try:
        while True:
            print("________________________________________________"
                  "\n|=-=|-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-|=-=|"
                  "\n|=-=|-=-=-=-=-=-=|  - MENU -  |=-=-=-=-=-=-|=-=|"
                  "\n|=-=| 0 - Fechar programa                  |=-=|"
                  "\n|=-=| 1 - Cadastrar novo vendedor          |=-=|"
                  "\n|=-=| 2 - Realizar login do vendedor       |=-=|"
                  "\n|=-=| 3 - Acessar área do cliente          |=-=|"
                  "\n------------------------------------------------")
            opcao = int(input("Selecione a opção desejada: "))
            if(opcao > 3 or opcao < 0):
                print("A opção que você selecionou não existe, por favor selecione uma opção valida")
                print("=-" * 17)
            else:
                return opcao
    except:
        print("Um erro inesperado aconteceu, por favor, tente novamente.")

#===========================================================================================
#CADASTRO DE VENDEDOR

def recebe_nome():
    try:
        while True:
            nome = input("Digite seu nome completo: ").strip().lower()
            print("=-" * 17)
            for i in range(len(nome)):
                if(nome[i] in numeros):
                    return print("Seu nome não pode conter números.\n", "=-" * 17)
            return nome
    except:
        print("Um erro inesperado aconteceu, por favor, tente novamente.")

def recebe_idade():
    try:
        idade = int(input("Digite sua idade: "))
        while idade < 18 or idade > 100:
            print("Idade inválida, por favor insira uma idade válida.")
            idade = int(input("Digite sua idade: "))
        return idade
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def recebe_cpf(opcao):
    try:
        if(opcao == 0):
            while True:
                cadastrado = 0
                print("=-" * 17)
                cpf = input("Digite seu CPF: ").replace('.', '').replace('-', '').strip()
                for dado in lista:
                    if(dado["cpf"] == cpf):
                        print("=-" * 17)
                        print("Este CPF ja foi cadastrado, por favor, tente novamente.")
                        cadastrado = 1
                if(len(cpf) != 11):
                    print("=-" * 17)
                    print("CPF inválido \nPor favor insira um CPF com formato válido \n"
                          "Exemplo: 111.111.111-11")
                elif(cadastrado == 1):
                    continue
                else:
                    break
            return cpf
        elif(opcao == 1):
            while True:
                print("=-" * 17)
                cpf = input("Confirme seu CPF: ").replace('.', '').replace('-', '').strip()
                if(len(cpf) != 11):
                    print("=-" * 17)
                    print("CPF inválido \nPor favor insira um CPF com formato válido \n"
                          "Exemplo: 111.111.111-11")
                elif(len(cpf) == 11):
                    for item in lista:
                        if(item["cpf"] == cpf):
                            return cpf
                        else:
                            continue
                    return 0
        elif(opcao == 2):
            while True:
                print("=-" * 17)
                cpf = input("Confirme seu CPF: ").replace('.', '').replace('-', '').strip()
                if(len(cpf) != 11):
                    print("=-" * 17)
                    print("CPF inválido \nPor favor insira um CPF com formato válido \n"
                          "Exemplo: 111.111.111-11")
                elif(len(cpf) == 11):
                    for item in lista:
                        if(item["cpf"] == cpf):
                            return cpf
                        else:
                            continue
                    return 0
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def recebe_loja():
    try:
        while True:
            cadastrado = 0
            loja = input("Digite o nome da sua loja: ").strip().lower()
            for i in range(len(loja)):
                if(loja[i] in numeros):
                    print("Desculpe, mas este campo não pode conter números.")
            for item in lista:
                if(item["loja"] == loja):
                    print("Esta loja já foi cadastrada")
                    cadastrado = 1
                else:
                    continue
            if(cadastrado == 1):
                continue
            else:
                break
        return loja
    except:
        print("Um erro inesperado aconteceu, por favor, tente novamente.")

def recebe_cnpj():
    try:
        while True:
            cnpj = input("Digite o CNPJ: ").replace('.', '').\
                replace('-', '').replace("/", "").strip()
            entrou = False
            for dado in lista:
                if(dado["cnpj"] == cnpj):
                    print("Este CNPJ ja foi cadastrado")
                    entrou = True
                else:
                    continue
            if(entrou == False):
                if(len(cnpj) == 14):
                    break
                elif(len(cnpj) != 14):
                    print("CNPJ inválido \nPor favor insira um CNPJ com formato válido "
                          "\nExemplo: 11.111.111/0001-11")
            else:
                continue
        return cnpj
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def recebe_senha(opcao, dado_cpf):
    try:
        if(opcao == 0):
            while True:
                senha = input("Crie uma senha: ").strip()
                if(len(senha) < 5):
                    print("Por favor insira uma senha com 5 ou mais caracteres")
                else:
                    confirma_senha = input("Confirme sua senha: ")
                    if(confirma_senha != senha):
                        print("As senhas são diferentes, tente novamente")
                    else:
                        return senha
        elif(opcao == 1):
            while True:
                senha = input("Confirme a senha: ").strip()
                if(len(senha) < 5):
                    print("Por favor insira uma senha com 5 ou mais caracteres")
                else:
                    for item in lista:
                        if(item['cpf'] == dado_cpf):
                            if(item['senha'] == senha):
                                return 1
                        else:
                            continue
                    return 0
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def cadastrar_vendedor():
    try:
        while True:
            nome = recebe_nome()
            idade = recebe_idade()
            cpf = recebe_cpf(0)
            loja = recebe_loja()
            cnpj = recebe_cnpj()
            senha = recebe_senha(0, '')
            produtos = {}
            dados = {"nome": nome, "idade": idade, "cpf": cpf, "loja": loja, "cnpj": cnpj,
                     "senha": senha, "produtos": produtos}
            lista.append(dados)
            if(dados in lista):
                return print("cadastro realizado com sucesso")
            else:
                print("Erro ao cadastrar.")
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def confere_login(opcao, cpf):
    try:
        if(opcao == 0):
            if(len(lista) <= 0):
                print("Não existe nenhum vendedor cadastrado ainda, por favor, cadastre-se primeiro.")
                return False
            else:
                busca_cpf = recebe_cpf(1)
                if(busca_cpf == 0):
                    print("CPF não cadastrado, redirecionaremos você para o menu.")
                    return False
                else:
                    busca_senha = recebe_senha(1, busca_cpf)
                    if(busca_senha == 1):
                        print("=-" * 17)
                        print("Identidade confirmada, por favor, prossiga.")
                        print("=-" * 17)
                        return busca_cpf
                    else:
                        print('Senha incorreta, redirecionaremos você para o menu.')
                        return False
        elif(opcao == 1):
            while True:
                busca_cpf = cpf
                busca_senha = recebe_senha(1, busca_cpf)
                if(busca_senha == 1):
                    print("=-" * 17)
                    print("Identidade confirmada, por favor, prossiga.")
                    print("=-" * 17)
                    return busca_cpf
                else:
                    print('Senha incorreta, por favor, tente novamente.')
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

#===========================================================================================
#AREA DO VENDEDOR

def menu_vendedor():
    try:
        while True:
            print("________________________________________________"
                  "\n|=-=|-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-|=-=|"
                  "\n|=-=|-=-=-=-=-=-=|  - LOJA -  |=-=-=-=-=-=-|=-=|"
                  "\n|=-=| 0 - Deslogar                         |=-=|"
                  "\n|=-=| 1 - Cadastrar novo produto           |=-=|"
                  "\n|=-=| 2 - Remover produto                  |=-=|"
                  "\n|=-=| 3 - Buscar produto                   |=-=|"
                  "\n|=-=| 4 - Atualizar produto                |=-=|"
                  "\n|=-=| 5 - Atualizar senha                  |=-=|"
                  "\n------------------------------------------------")
            opcao = int(input("Digite sua escolha: "))
            if(opcao < 0 or opcao > 5):
                print("Por favor digite um número valido.")
            else:
                return opcao
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def cadastrar_preco():
    try:
        preco = float(input("Digite o preco do produto: "))
        while preco <= 0:
            preco = float(input("Por favor, digite um valor válido: "))
        return preco
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def cadastrar_estoque():
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
        while quantidade <= 0:
            quantidade = int(input("Por favor, digite uma quantidade válida: "))
        return quantidade
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def buscar_produto_vendedor(onde_vai, rem_prod, cpf):
    try:
        while True:
            busca_prod = input("Digite o nome do produto: ")
            if(onde_vai == 0):
                for dados in lista:
                    if(dados['cpf'] == cpf):
                        for item in dados['produtos']:
                            for produto in item:
                                if(produto['nome'] == busca_prod):
                                    print("Desculpe, mas já existe um produto cadastrado com esse nome.")
                                    return "1" + busca_prod
                return "0" + busca_prod
            elif(onde_vai == 1):
                for dados in lista:
                    if(dados['cpf'] == cpf):
                        for item in dados['produtos']:
                            for produto in item:
                                if(produto['nome'] == busca_prod):
                                    resultado = print("O produto está cadastrado no sistema.\n",
                                      ("=-" * 17), "\n",
                                      "Nome do produto: {}\n"
                                      "Preço: {}\n"
                                      "Estoque disponível: {}\n"
                                      "ID do produto: {}\n",
                                      ("=-" * 17).format(produto["nome"],produto["preco"],
                                        produto["estoque"], produto["id"]))
                                    return resultado
                return print("Desculpe, mas o produto não está cadastrado no sistema.")
            elif(onde_vai == 2):
                for dados in lista:
                    if(dados['cpf'] == cpf):
                        for item in dados['produtos']:
                            for produto in item:
                                if(produto['nome'] == remover_produto): #esta cadastrado
                                    return "1" + rem_prod
                                else:
                                    continue
                return "0" + rem_prod # nao esta cadastrado
            elif(onde_vai == 3):
                for dados in lista:
                    for item in dados['produtos']:
                        for produto in item:
                            if(produto['nome'] == busca_prod):
                                print("O produto está cadastrado no sistema.\n", ("=-" * 17))
                                print("Nome da Loja: {}\n",
                                      ("=-" * 17), "\n"
                                      "Nome do produto: {}\n"
                                      "Preço: {}\n"
                                      "Estoque disponível: {}\n",
                                      ("=-" * 17).format(dados['loja'], produto["nome"],
                                        produto["preco"], produto["estoque"]))
                                return produto['nome'], produto['preco'], produto['estoque'], dados['cpf']
                return print("Desculpe, mas o produto não está cadastrado no sistema.")
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def cadastrar_produto(cpf):
    try:
        confere_login(1, cpf)
        while True:
            novo_produto = buscar_produto_vendedor(0, '', cpf)
            if(novo_produto[0] == "1"):
                return print("=-" * 17, "\nO produto já está cadastrado.", "\n=-" * 17)
            else:
                novo_produto = novo_produto.replace("0", "")
            preco = cadastrar_preco()
            quantidade = cadastrar_estoque()
            id = 0
            for dados in lista:
                if(dados['cpf'] == cpf):
                    if(len(dados['produtos']) <= 0):
                        id = 0
                    else:
                        id = len(dados['produtos'])
            produto = {"nome": novo_produto, "preco": preco, "estoque": quantidade, "id": id}
            prod = 'produto' + str(id)
            if(id == 0):
                for dados in lista:
                    if(dados['cpf'] == cpf):
                        dados['produtos'] = {prod: produto}
                for dados in lista:
                    if(dados['cpf'] == cpf):
                        for produtos in dados['produtos']:
                            for produto in item['produtos']:
                                if produto['nome'] == novo_produto:
                                    return print("Produto cadastrado com sucesso!" + ("\n=-" * 17))
                print("Erro no cadastro, por favor, tente novamente")
            else:
                for dados in lista:
                    if(dados['cpf'] == cpf):
                        for item in dados['produtos']:
                            item[prod] = produto
                for dados in lista:
                    if(dados['cpf'] == cpf):
                        for item in dados['produtos']:
                            if(item['nome'] == novo_produto):
                                return print("Produto cadastrado com sucesso!" + ("\n=-" * 17))
                print("Erro no cadastro, por favor, tente novamente")
            continue
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def remover_produto(cpf):
    try:
        confere_login(1, cpf)
        while True:
            remove_prod = buscar_produto_vendedor(2, '', cpf)
            if(remove_prod[0] == "0"):
                return print("Sinto muito, mas o produto não está cadastrado.")
            else:
                remove_prod.replace("1", "")
                for dados in lista:
                    if(dados['cpf'] == cpf):
                        for item in dados['produtos']:
                            for produto in item:
                                if(produto['nome'] == remove_prod):
                                    item.pop(produto)
                confirma_remocao = buscar_produto_vendedor(2, remove_prod, cpf)
                if(confirma_remocao[0] == "1"):
                    print("Erro na remoção do produto, por favor, tente novamente.")
                else:
                    return print("Produto removido com sucesso.")
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def atualizar_produto(opcao, cpf, nome_produto, tira_estoque):
    try:
        if(opcao == 0):
            while True:
                confere_login(1, cpf)
                antigo_nome = buscar_produto_vendedor(0, "", cpf)
                if(antigo_nome[0] == "0"):
                    print("=-" * 17)
                    print("Desculpe, mas o produto não está cadastrado no sistema.")
                    print("=-" * 17)
                else:
                    antigo_nome.replace("1", "")
                    while True:
                        print("=-" * 17)
                        novo_nome = input("Digite o novo nome do produto: ")
                        if(novo_nome == antigo_nome):
                            print("O novo nome deve ser diferente do anterior,"
                                  " por favor, tente novamente.")
                            continue
                        else:
                            confirmacao = buscar_produto_vendedor(2, novo_nome, cpf)
                            if(confirmacao[0] == "1"):
                                print("Esse nome já está cadastrado em outro produto, "
                                      "por favor tente novamente.")
                            else:
                                novo_preco = cadastrar_preco()
                                novo_estoque = cadastrar_estoque()
                                for dados in lista:
                                    if(dados['cpf'] == cpf):
                                        for item in dados['produtos']:
                                            for produto in item:
                                                if(produto['nome'] == antigo_nome):
                                                    produto["nome"] = novo_nome
                                                    produto["preco"] = novo_preco
                                                    produto["estoque"] = novo_estoque
                                confirmo = buscar_produto_vendedor(2, novo_nome, cpf)
                                if(confirmo[0] == '0'):
                                    print("Erro na atualização do produto, "
                                          "por favor, tente novamente.")
                                else:
                                    return print("Produto atualizado com sucesso!")
        elif(opcao == 1):
            estoque_antigo = 0
            for dados in lista:
                if(dados['cpf'] == cpf):
                    for item in dados['produtos']:
                        for produto in item:
                            if(produto['nome'] == nome_produto):
                                estoque_antigo = produto['estoque']
                                produto['estoque'] -= tira_estoque
            for dados in lista:
                if(dados['cpf'] == cpf):
                    for item in dados['produtos']:
                        for produto in item:
                            if(produto['nome'] == nome_produto):
                                if(produto['estoque'] == estoque_antigo):
                                    return False
            return True
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def atualizar_senha(cpf):
    try:
        while True:
            nova_senha = input("Digite a nova senha: ").strip()  # recebe a nova senha
            if(len(nova_senha) < 5):
                print("Por favor insira uma senha com 5 ou mais caracteres")
            else:
                senha_antiga = 0
                for dado in lista:
                    if(dado['cpf'] == cpf):
                        senha_antiga = dado['senha']
                        break
                if(nova_senha == senha_antiga):
                    print("Desculpe, mas a nova senha não pode ser igual à anterior.")
                else:
                    for dado in lista:
                        if(dado['cpf'] == cpf):
                            if(dado['senha'] == senha_antiga):
                                dado["senha"] = nova_senha
                    for dado in lista:
                        if(dado['cpf'] == cpf):
                            if(dado['senha'] == nova_senha):
                                return print("Senha atualizada com sucesso!")
                    print("Erro na atualização da senha, por favor, tente novamente.")
                    continue
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

#===========================================================================================
#ÁREA DO CLIENTE

'''
def carrinho_cliente():
    opcao = int(input("0 - Pagar compras armazenadas e sair da área do cliente\n"
          "1 - Voltar à seção de compras\n"
          "2 - Pagar compras armazenadas e continuar comprando\n"
          "3 - Remover produto do carrinho\n"
          "4 - Atualizar quantidade da compra\n"
          "----------------------------------------------------------\n"
          "Por favor, digite a opção desejada: "))
'''

def menu_cliente():
    try:
        while True:
            print("_________________________________________________"
                  "\n|=-=|-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=|=-=|"
                  "\n|=-=|=-=-=-=-=-=|  - CLIENTE -  |=-=-=-=-=-=|=-=|"
                  "\n|=-=| 0 - Voltar                            |=-=|"
                  "\n|=-=| 1 - Buscar produto                    |=-=|"
                  "\n|=-=| 2 - Ver meu carrinho                  |=-=|"
                  "\n|=-=| 3 - Descrição do produto              |=-=|"
                  "\n-------------------------------------------------")
            escolha = int(input("Digite sua opção: "))
            if(escolha < 0 or escolha > 3):
                print("Por favor, escolha uma opção válida.")
            else:
                return escolha
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def busca_cliente():
    try:
        lojas_cadas = 0
        for dados in lista:
            for produtos in dados['produtos']:
                if(len(produtos) > 0):
                    lojas_cadas = 1
                else:
                    continue
        if(lojas_cadas == 0):
            return print("Desculpe, mas as lojas cadastradas ainda estão sem produtos pra vender!")
        else:
            while True:
                busca_produto, estoque, preco, dado_cpf = buscar_produto_vendedor(3, "", '')
                while True:
                    escolha = int(input("Deseja comprar este produto?"
                                        "\nPara 'Sim' digite 1, e para 'Não' digite 2.\n> "))
                    if(escolha < 1 or escolha > 2):
                        print("Por favor, digite uma opção válida.")
                    elif(escolha == 1):
                        while True:
                            qtd = int(input("Digite quantos items deseja comprar: "))
                            if(qtd < 0 or qtd > estoque):
                                print("Por favor, digite uma quantidade válida")
                            else:
                                break
                        preco_compra = preco * qtd
                        compra = {"nome": busca_produto, "quantidade": qtd, "preco": preco_compra}
                        carrinho.append(compra)
                        if(compra in carrinho):
                            if(atualizar_produto(1, dado_cpf, busca_produto, qtd) == False):
                                print("Erro ao adicionar o produto no carrinho, "
                                      "por favor, tente novamente.")
                            else:
                                return print("Produto adicionado ao carrinho com sucesso!")
                        else:
                            print("Erro ao adicionar o produto ao carrinho, por favor, "
                                  "tente novamente.")
                    elif(escolha == 2):
                        return print("Agradecemos pela sua escolha. Fique à "
                                     "vontade para olhar outros itens.")
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def mostrar_carrinho():
    try:
        while True:
            if(len(carrinho) <= 0):
                print("Seu carrinho está vazio! Que tal preenchê-lo com alguns produtos?")
                break
            else:
                preco_total = 0
                quantidade_total = 0
                for item in carrinho:
                    print("Nome: {}\n"
                          "Quantidade: {}\n"
                          "Preço: {}\n"
                          "------------------------------------------".
                          format(item["nome"], item["quantidade"], item["preco"]))
                    preco_total += item["preco"]
                    quantidade_total += item["quantidade"]
                print("Preço total das compras armazenadas no carrinho: {}"
                      "Quantidade total de compras armazenadas no carrinho: {}"
                      "------------------------------------------".
                      format(preco_total, quantidade_total))
                while True:
                    fechar_compra = int(input("Gostaria de pagar e fechar o carrinho?\n"
                                              "Digite 1 para 'Sim' ou 2 para 'Não'.\n> "))
                    if(fechar_compra < 1 or fechar_compra > 2):
                        print("Por favor, digite uma opção válida.")
                    elif(fechar_compra == 1):
                        print("Obrigada pela preferência e tenha um bom dia!")
                        return 1
                    elif(fechar_compra == 2):
                        print("Sinta-se à vontade e tenha boas compras!")
                        return 0
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")

def consultarchatgpt():
    try:
        produto = input("Digite o nome do produto pelo qual deseja pesquisar: ")
        openai.api_key = 'cole sua chave aqui'

        # Set the model and prompt
        model_engine = "text-davinci-003"
        prompt = 'me diga resumidamente, o que você acha do ' + produto + ' ?'
        # Set the maximum number of tokens to generate in the response
        max_tokens = 1024

        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)

        # Print the response
        return completion.choices[0].text
    except:
        print("Um erro inesperado ocorreu, por favor, tente novamente.")