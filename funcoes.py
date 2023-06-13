#FUNÇÕES DO PROJETO
import openai

lista = []
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
produtos = []
carrinho = []

def menu_principal():
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
#===========================================================================================
#CADASTRO DE VENDEDOR

def recebe_nome():
    while True:
        nome = input("Digite seu nome completo: ").strip().lower()
        if(nome == ""):
            print("Este campo não pode estar vazio")
        else:
            continua = False
            for i in range(len(nome)):
                if(nome[i] in numeros):
                    print("Seu nome não pode conter números.")
                    continua = True
                else:
                    continue
            if(continua == True):
                pass
            else:
                break
    return nome

def recebe_idade():
    while True:
        idade = int(input("Digite sua idade: "))
        if(idade == ""):
            print("Este campo não pode estar vazio")
        elif(idade < 18 or idade > 100):
            print("Idade inválida, por favor insira uma idade válida.")
        else:
            break
    return idade

def recebe_cpf(opcao):
    if(opcao == 0):
        while True:
            cpf = input("Digite seu CPF: ").replace('.', '').replace('-', '').strip()
            for item in lista:
                if(item["cpf"] == cpf):
                    print("Este CPF ja foi cadastrado, por favor, tente novamente.")
                else:
                    continue
            if(len(cpf) == 11):
                break
            elif(len(cpf) != 11):
                print("CPF inválido \nPor favor insira um CPF com formato válido \n"
                        "Exemplo: 111.111.111-11")
        return cpf
    elif(opcao == 1):
        while True:
            cpf = input("Confirme seu CPF: ").replace('.', '').replace('-', '').strip()
            if(len(cpf) != 11):
                print("CPF inválido \nPor favor insira um CPF com formato válido \n"
                      "Exemplo: 111.111.111-11")
            elif(len(cpf) != 11):
                for item in lista:
                    if(item["cpf"] == cpf):
                        confirma = "1" + cpf
                        return confirma
                    else:
                        continue
            confirma = "0" + cpf
            return confirma

def recebe_loja():
    while True:
        loja = input("Digite o nome da sua loja: ").strip().lower()
        for item in lista:
            if(item["loja"] == loja):
                print("Esta loja já foi cadastrada")
            else:
                continue
        break
    return loja

def recebe_cnpj():
    while True:
        cnpj = input("Digite o CNPJ ").replace('.', '').\
            replace('-', '').replace("/", "").strip()
        entrou = False
        for c in lista:
            if(c["cnpj"] == cnpj):
                print("Este CNPJ ja foi cadastrado")
                entrou = True
            else:
                continue
        if(entrou == False):
            if len(cnpj) == 14:
                break
            elif(len(cnpj) != 14):
                print("CNPJ inválido \nPor favor insira um CNPJ com formato válido "
                      "\nExemplo: 11.111.111/0001-11")
        else:
            continue
    return cnpj

def recebe_senha():
    while True:
        senha = input("Crie uma senha: ").strip()
        if(len(senha) >= 5):
            break
        elif(len(senha) < 5):
            print("Por favor insira uma senha com 5 ou mais caracteres")
        confirma_senha = input("Confirme sua senha: ")
        if(confirma_senha != senha):
            print("As senhas são diferentes, tente novamente")
        else:
            break
    return senha

def cadastrar_vendedor(opcao):
    nome = recebe_nome()
    idade = recebe_idade()
    cpf = recebe_cpf(0)
    loja = recebe_loja()
    cnpj = recebe_cnpj()
    senha = recebe_senha()
    dados = {"nome": nome, "idade": idade, "cpf": cpf, "loja": loja, "cnpj": cnpj,
             "senha": senha}
    lista.append(dados)
    if(dados in lista):
        print("cadastro realizado com sucesso")
        if(opcao == 1):
            return dados["senha"]
        else:
            pass
    else:
        print("Erro ao cadastrar.")

#===========================================================================================
#LOGIN DO VENDEDOR

def confere_login():
    while True:
        busca_cpf = input("Confirme seu CPF:").replace('.', '').replace('-', '').strip()
        busca_senha = input("Confirme sua senha: ").strip()
        for c in lista:
            if c["cpf"] == busca_cpf and c["senha"] == busca_senha:
                print("=-" * 17)
                print("Identidade confirmada, por favor, prossiga.")
                print("=-" * 17)
                break
            else:
                print('CPF ou senha incorretos')
                continue

def menu_vendedor():
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

def buscar_produto_vendedor(onde_vai, produto):
    #onde_vai é a variavel que diz onde a função vai ser chamada
    #se for 0, ela está sendo chamada dentro de outra função, então nao precisa print
    #se for 1, ela está sendo chamada pelo vendedor, aí vai printar os dados do produto
    #se for 2, ela está sendo chamada pela função de remover, que não quer o nome do produto
    #mas quer saber se o produto foi removido ou não
    #se for 3, ela está sendo chamada pelo cliente, e ele não precisa saber o id
    esta = 0
    para = False
    while True:
        busca_prod = input("Digite o nome do produto: ")
        if(onde_vai == 0):
            for item in produtos:
                if(item["nome"] == busca_prod):
                    esta = "1" + busca_prod
                    para = True
                    return esta
                else:
                    esta = "0" + busca_prod
                    para = True
                    return esta
        elif(onde_vai == 1):
            for item in produtos:
                if(item["nome"] == busca_prod):
                    print("O produto está cadastrado no sistema.")
                    print("=-" * 17)
                    print("Nome do produto: {}"
                          "Preço: {}"
                          "Estoque disponível: {}"
                          "ID do produto: {}".format(item["nome"], item["preco"],
                                                     item["estoque"], item["id"]))
                    print("=-" * 17)
                    para = True
                else:
                    print("Desculpe, mas o produto não está cadastrado no sistema.")
        elif(onde_vai == 2):
            for item in produtos:
                if(item["nome"] == produto):
                    esta = "1" #esta cadastrado
                    para = True
                    return esta
                else:
                    esta = "0" #nao esta cadastrado
                    para = True
                    return esta
        elif(onde_vai == 3):
            for item in produtos:
                if(item["nome"] == busca_prod):
                    print("O produto está cadastrado no sistema.")
                    print("=-" * 17)
                    print("Nome do produto: {}"
                          "Preço: {}"
                          "Estoque disponível: {}".format(item["nome"], item["preco"],
                                                          item["estoque"]))
                    print("=-" * 17)
                    return busca_prod, item["estoque"], item["preco"]
        if(para == True):
            break
        else:
            continue

def cadastrar_preco():
    while True:
        preco = float(input("Digite o preco do produto: "))
        if(preco <= 0):
            print("Por favor digite um preco válido.")
        else:
            break
    return preco

def cadastrar_estoque():
    while True:
        quantidade = int(input("Digite a quantidade do produto: "))
        if(quantidade <= 0):
            print("Por favor, digite uma quantidade válida.")
        else:
            break
    return quantidade

def cadastrar_produto():
    while True:
        produto = buscar_produto_vendedor(0, "")
        if(produto[0] == "1"):
            print("O produto já está cadastrado.")
        else:
            produto -= produto[0]
            break
    preco = cadastrar_preco()
    quantidade = cadastrar_estoque()
    id = len(produtos)
    if(len(produtos) == None):
        id = 0
    else:
        pass
    produto = {"Nome": produto, "Preço": preco, "Estoque": quantidade, "ID": id}
    produtos.append(produto)
    if(produto in produtos):
        print("Produto cadastrado com sucesso")
        for item in lista:
            item["produtos"] = produtos
    else:
        print("Erro no cadastro, por favor, tente novamente")

def remover_produto():
    id_item = 0
    while True:
        remove_prod = buscar_produto_vendedor(0, "")
        if(remove_prod[0] == "0"):
            print("Sinto muito, mas o produto não está cadastrado.")
            break
        else:
            remove_prod -= remove_prod[0]
            confere_login()
            for id in produtos:
                if(id["nome"] == remove_prod):
                    id_item = id["id"]
                else:
                    continue
            produtos.pop(id_item)
            confirma_remocao = buscar_produto_vendedor(2, remove_prod)
            if(confirma_remocao == 1):
                print("Erro na remoção do produto, por favor, tente novamente.")
            else:
                print("Produto removido com sucesso.")
                break

def atualizar_produto():
    while True:
        para = False
        produto = buscar_produto_vendedor(0, "")
        if(produto[0] == 0):
            print("Desculpe, mas o produto não está cadastrado no sistema.")
        else:
            produto -= produto[0]
            while True:
                novo_nome = input("Digite o novo nome do produto: ")
                if(novo_nome == produto):
                    print("O novo nome deve ser diferente do anterior,"
                          " por favor, tente novamente.")
                    continue
                else:
                    confirmacao = buscar_produto_vendedor(2, novo_nome)
                    if(confirmacao == 1):
                        print("Esse nome já está cadastrado em outro produto, "
                              "por favor tente novamente.")
                    else:
                        novo_preco = cadastrar_preco()
                        novo_estoque = cadastrar_estoque()
                        confere_login()
                        for id in produtos:
                            if(id["nome"] == produto):
                                id["nome"] = novo_nome
                                id["preco"] = novo_preco
                                id["estoque"] = novo_estoque
                            else:
                                continue
                        confir = buscar_produto_vendedor(2, novo_nome)
                        if(confir[0] == 0):
                            print("Erro na atualização do produto, "
                                  "por favor, tente novamente.")
                        else:
                            print("Produto atualizado com sucesso!")
                            para = True
                            break
        if(para == True):
            break
        else:
            continue

def atualizar_senha():
    while True:
        cpf = recebe_cpf(1)
        if(cpf[0] == 0):
            print("O CPF recebido não está cadastrado no sistema, por favor tente novamente.")
        elif(cpf[0] == 1):
            cpf -= cpf[0]
            nova_senha = input("Digite a nova senha: ").strip()  # recebe a nova senha
            if(len(nova_senha) < 5):
                print("Por favor insira uma senha com 5 ou mais caracteres")
            elif(len(nova_senha) > 5):
                senha_antiga = cadastrar_vendedor(1)
                if(nova_senha == senha_antiga):
                    print("Desculpe, mas a nova senha não pode ser igual à anterior.")
                else:
                    for item in lista:
                        if(item["senha"] == senha_antiga):
                            item["senha"] = nova_senha
                    for item in lista:
                        if(item["senha"] == nova_senha):
                            print("Senha atualizada com sucesso!")
                            break
                    print("Erro na atualização da senha, por favor, tente novamente.")

#===========================================================================================
#ÁREA DO CLIENTE
def menu_cliente():
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

def busca_cliente():
    busca_produto, estoque, preco = buscar_produto_vendedor(3, "")
    while True:
        escolha = int(input("Deseja comprar este produto?"
                            "\nPara 'Sim' digite 1, e para 'Não' digite 2."
                            "\n> "))
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
                print("Produto adicionado ao carrinho!")
                break
            else:
                print("Erro ao adicionar o produto ao carrinho, por favor, tente novamente.")
        elif(escolha == 2):
            print("Agradecemos pela sua escolha. Fique à vontade para olhar outros itens.")
            break

def mostrar_carrinho():
    while True:
        if(len(carrinho) == None):
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
                  "Quantidade total de compras armazenadas no carrinho: {}".
                  format(preco_total, quantidade_total))
            while True:
                fechar_compra = int(input("Gostaria de pagar e fechar o carrinho?\n"
                                          "Digite 1 para 'Sim' ou 2 para 'Não'.\n"
                                          "> "))
                if(fechar_compra < 1 or fechar_compra > 2):
                    print("Por favor, digite uma opção válida.")
                elif(fechar_compra == 1):
                    print("Obrigada pela preferência e tenha um bom dia!")
                    sair = 1
                    return sair
                elif(fechar_compra == 2):
                    print("Sinta-se à vontade e tenha boas compras!")
                    sair = 0
                    break
            if(sair == 0):
                break

def consultarchatgpt():
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
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text