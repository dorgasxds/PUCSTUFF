import json

# Função para exibir o menu principal
def menu_principal():
    print("--- MENU PRINCIPAL ---")
    print("(1) Gerenciar Estudantes.")
    print("(2) Gerenciar Disciplinas.")
    print("(3) Gerenciar Professores.")
    print("(4) Gerenciar Turmas.")
    print("(5) Gerenciar Matrículas.")
    print("(6) SAIR.")
    
    return input("Selecione uma opção principal: ")

# Função para exibir o menu de operações
def menu_operacao():
    print("--- MENU DE OPERAÇÕES ---")
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(5) Voltar para o menu principal.")

    return input("Selecione uma operação válida: ")

# Função para cadastrar uma pessoa (pode ser aluno ou professor)
def cadastrar_pessoa(lista_geral, bloco, houver_cpf):
    codigo = int(input("Entre com o código do indivíduo: ")) 
    for pessoa in lista_geral:
        if pessoa["codigo"] == codigo:
            print("Código já cadastrado. Por favor, insira um código diferente.")
            return
        
    nome = input("Digite o nome: ")
    cpf = input("Insira o CPF: ") if houver_cpf else None
    lista_cadastral = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
    }

    lista_geral.append(lista_cadastral)
    salvar_arquivo(lista_geral, bloco)

# Função para cadastrar disciplinas
def cadastrar_disciplinas(lista_geral, bloco, cod_disciplina):
    codigo = int(input("Entre com o código: ")) if cod_disciplina else None
    for disciplina in lista_geral:
        if "codigo" in disciplina and disciplina["codigo"] == codigo:
            print("Código já cadastrado. Por favor, insira um código diferente.")
            return
        
    nome_disciplina = input("Digite o nome: ") 
    lista_cadastral = {
        "codigo": codigo,
        "nome da disciplina": nome_disciplina 
    }

    lista_geral.append(lista_cadastral)
    salvar_arquivo(lista_geral, bloco)

# Função para cadastrar turmas
def cadastrar_turmas(lista_geral, bloco, cod_turmas):
    codigo = int(input("Entre com o código da turma: ")) if cod_turmas else None
    turmas = ler_arquivo(arquivo_turmas)
    if codigo not in [turma["codigo"] for turma in turmas]:
        codigo_professor = input("Digite o código do professor: ")
        codigo_disciplina = input("Digite o código da disciplina: ")
        lista_cadastral = {
            "codigo": codigo,
            "codigo do professor": codigo_professor,
            "codigo da disciplina": codigo_disciplina
        }
        print(f"Turma {codigo} cadastrada com sucesso!")
        lista_geral.append(lista_cadastral)
        salvar_arquivo(lista_geral, bloco)
    else:
        print(f"Código {codigo} já cadastrado.")

# Função para cadastrar matrículas de alunos em turmas
def cadastrar_matriculas(lista_geral, bloco, alunos_professores, arquivo_turmas):
    aluno_encontrado = None
    while aluno_encontrado is None:
        codigo_aluno = int(input("Entre com o código do aluno: "))
        alunos_professores_data = ler_arquivo(alunos_professores)
        if alunos_professores_data is None:
            print(f"O arquivo {alunos_professores} não contém dados válidos ou não existe.")
        else:
            for aluno in alunos_professores_data:
                if aluno["codigo"] == codigo_aluno:
                    aluno_encontrado = aluno
                    break
            if aluno_encontrado is None:
                print(f"Aluno com código {codigo_aluno} não encontrado em {alunos_professores}.")

    turma_encontrada = None
    while turma_encontrada is None:
        codigo_turma = int(input("Entre com o código da turma: "))
        turmas_data = ler_arquivo(arquivo_turmas)
        if turmas_data is None:
            print(f"O arquivo {arquivo_turmas} não contém dados válidos ou não existe.")
        else:
            for turma in turmas_data:
                if turma["codigo"] == codigo_turma:
                    turma_encontrada = turma
                    break
            if turma_encontrada is None:
                print(f"Turma com código {codigo_turma} não encontrada em {arquivo_turmas}.")

    if aluno_encontrado is not None and turma_encontrada is not None:
        lista_cadastral = {
            "codigo": codigo_aluno,
            "turma": codigo_turma
        }
        lista_geral.append(lista_cadastral)
        salvar_arquivo(lista_geral, bloco)
        print(f"Matrícula do aluno {codigo_aluno} na turma {codigo_turma} realizada com sucesso!")

# Função para listar itens (alunos, disciplinas, professores, turmas)
def listar(lista_geral, bloco):
    print("Você selecionou a opção: " + operacao )
    lista_geral = ler_arquivo(bloco)
    if len(lista_geral) == 0:
        print("Não cadastrado")
    else:
        for x in lista_geral:
            print(x)

# Função para atualizar uma matrícula
def atualizar_matricula(codigo_editar, bloco, edit_matricula):
    lista_geral = ler_arquivo(bloco)
    editar_matricula = None
    for dados_matricula in lista_geral:
        if dados_matricula["codigo"] == codigo_editar:
            editar_matricula = dados_matricula
            break
    if editar_matricula is None:
                return False
    else:
        editar_matricula["codigo"] = int(input("Digite novo código: "))
        editar_matricula["codigo do estudante"] = input("Código do estudante: ") if edit_matricula else None
        salvar_arquivo(lista_geral, bloco)
        return True
    
# Função para atualizar uma turma
def atualizar_turma(codigo_editar, bloco, edit_turma):
    lista_geral = ler_arquivo(bloco)
    editar_turma = None
    for dados_turma in lista_geral:
        if dados_turma["codigo"] == codigo_editar:
            editar_turma = dados_turma
            break
    if editar_turma is None:
                return False
    else:
        editar_turma["codigo"] = int(input("Digite novo código: "))
        editar_turma["codigo do professor"] = input("Digite novo código do professor: ") if edit_turma else None
        editar_turma["codigo da disciplina"] = input("Digite novo código da disciplina: ")
        salvar_arquivo(lista_geral, bloco)
        return True
    
# Função para atualizar uma disciplina
def atualizar_disciplina(codigo_editar, bloco, edit_disc):
    lista_geral = ler_arquivo(bloco)
    editar_disciplina = None
    for dados_disciplina in lista_geral:
        if dados_disciplina["codigo"] == codigo_editar:
            editar_disciplina = dados_disciplina
            break
    if editar_disciplina is None:
                return False
    else:
        editar_disciplina["codigo"] = int(input("Digite novo código: "))
        editar_disciplina["nome da disciplina"] = input("Digite novo nome: ") if edit_disc else None
        salvar_arquivo(lista_geral, bloco)
        return True

# Função para atualizar uma pessoa (aluno ou professor)
def atualizar_pessoa(codigo_editar, bloco, houver_cpf):
    lista_geral = ler_arquivo(bloco)
    pessoa_alterada = None
    for dados_pessoa in lista_geral:
        if dados_pessoa["codigo"] == codigo_editar:
            pessoa_alterada = dados_pessoa
            break
    if pessoa_alterada is None:
                return False
    else:
        pessoa_alterada["codigo"] = int(input("Digite novo código: "))
        pessoa_alterada["nome"] = input("Digite novo nome: ")
        pessoa_alterada["cpf"] = input("Digite novo CPF: ") if houver_cpf else None
        salvar_arquivo(lista_geral, bloco)
        return True

# Função para excluir um item (aluno, disciplina, professor, turma)
def excluir_codigo(codigo_excluir, bloco):
    lista_geral = ler_arquivo(bloco)  
    codigo_removido = None       
    for dados in lista_geral:
        if dados["codigo"] == codigo_excluir:
            codigo_removido = dados
            break
                             
    if codigo_removido is not None:
        lista_geral.remove(codigo_removido)
        salvar_arquivo(lista_geral, bloco)
    else:
        print(f"Não encontramos o código {codigo_excluir} na lista")

# Função para salvar dados em um arquivo JSON
def salvar_arquivo(lista_geral, bloco):
    with open(bloco, 'w') as f:
        json.dump(lista_geral, f)

# Função para ler dados de um arquivo JSON
def ler_arquivo(bloco):
   try:
    with open(bloco, 'r') as f:
        lista_geral = json.load(f)
        return lista_geral
   except:
       return []

# Função que gerencia as opções de operação com base na escolha do usuário
def menu_operacao_opcoes(operacao, bloco, houver_cpf, cod_disciplina, cod_turmas, cod_matriculas, edit_disc, edit_turma, edit_matricula):
    lista_geral = ler_arquivo(bloco)
    while True:
        if operacao == "1":
            if houver_cpf:
                cadastrar_pessoa(lista_geral, bloco, houver_cpf)
            if cod_disciplina:
                cadastrar_disciplinas(lista_geral, bloco, cod_disciplina)
            if cod_turmas:
                cadastrar_turmas(lista_geral, bloco, cod_turmas)
            if cod_matriculas:
                cadastrar_matriculas(lista_geral, arquivo_matriculas, alunos_professores, arquivo_turmas)
        elif operacao == "2":
            listar(lista_geral, bloco)
        elif operacao == "3":
            codigo_editar = int(input("Qual código deseja editar: "))
            if edit_turma: 
                atualizar_turma(codigo_editar, bloco, edit_turma)
            if edit_disc:
                atualizar_disciplina(codigo_editar, bloco, edit_disc)
            if edit_matricula:
                atualizar_matricula(codigo_editar, bloco, edit_matricula)
            if houver_cpf:
                atualizar_pessoa(codigo_editar, bloco, houver_cpf)
        elif operacao == "4":
            codigo_excluir = int(input("Qual código deseja excluir: "))
            excluir_codigo(codigo_excluir, bloco)
        elif operacao == "5":
            print("Voltando ao Menu Principal")
            return False
        else:
            print("Opção inválida. Tente novamente.")
        return True

# Nomes de arquivos para armazenar os dados
alunos_professores = "cadastros.json"
arquivo_disciplina = "disciplinas.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"
 
while True:
    selecionar = menu_principal()

    if selecionar == "1":
        houver_cpf = True
        cod_disciplina = False
        cod_turmas = False
        cod_matriculas = False
        edit_disc = False 
        edit_turma = False 
        edit_matricula = False
        while True:
            operacao = menu_operacao()
            if not menu_operacao_opcoes(operacao, alunos_professores, houver_cpf, cod_disciplina, cod_turmas, cod_matriculas, edit_disc, edit_turma, edit_matricula):
                break

    elif selecionar == "2":        
        houver_cpf = False
        cod_disciplina = True  
        cod_turmas = False
        cod_matriculas = False
        edit_disc = True 
        edit_turma = False 
        edit_matricula = False 
        while True:
            operacao = menu_operacao()
            if not menu_operacao_opcoes(operacao, arquivo_disciplina, houver_cpf, cod_disciplina, cod_turmas, cod_matriculas, edit_disc, edit_turma, edit_matricula):
                break
    
    elif selecionar == "3":
        houver_cpf = True
        cod_disciplina = False
        cod_turmas = False
        cod_matriculas = False
        edit_disc = False 
        edit_turma = False
        edit_matricula = False
        while True:
            operacao = menu_operacao()
            if not menu_operacao_opcoes(operacao, alunos_professores, houver_cpf, cod_disciplina, cod_turmas, cod_matriculas, edit_disc, edit_turma, edit_matricula):
                break
            
    elif selecionar == "4":
        houver_cpf = False
        cod_disciplina = False
        cod_turmas = True
        cod_matriculas = False
        edit_disc = False 
        edit_turma = True
        edit_matricula = False
        while True:    
            operacao = menu_operacao()
            if not menu_operacao_opcoes(operacao, arquivo_turmas, houver_cpf, cod_disciplina, cod_turmas, cod_matriculas, edit_disc, edit_turma, edit_matricula):
                break
    
    elif selecionar == "5":
        houver_cpf = False
        cod_disciplina = False
        cod_turmas = False
        cod_matriculas = True
        edit_disc = False 
        edit_turma = False
        edit_matricula = True
        while True:    
            operacao = menu_operacao()
            if not menu_operacao_opcoes(operacao, arquivo_matriculas, houver_cpf, cod_disciplina, cod_turmas, cod_matriculas, edit_disc, edit_turma,edit_matricula):
                break
    
    elif selecionar == "6":
        print("Você está saindo do Sistema!")
        break
    else:
        print("Opção inválida.")
