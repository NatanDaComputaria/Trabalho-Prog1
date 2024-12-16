class Aluno:
    def __init__(self, primeiro_nome, sobrenome, endereco, filiacao, email_responsavel, ra, segmento, cursos, nome_usuario, email, senha):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.filiacao = filiacao
        self.email_responsavel = email_responsavel
        self.ra = ra
        self.segmento = segmento  # EM ou Superior
        self.cursos = cursos  # Mecatrônica, Eletromecânica, Informática, Ciências da Computação, Pedagogia
        self.nome_usuario = nome_usuario
        self.email = email
        self.senha = senha
        self.turmas = []  # A turma do aluno

    @property 
    def nome_completo(self):
        return f"{self.primeiro_nome} {self.sobrenome}"

    @property
    def dados_contato(self):
        return f"Email responsável: {self.email_responsavel}, Filiação: {self.filiacao}"

    #def transferir_de_curso(self, novo_curso):
        #Mostrar ao usuário as turmas disponiveis para a troca
        #Pedir que escolha uma
        #trocar o usuário para a turma
        
        #self.curso = novo_curso
        #print(f"Aluno {self.primeiro_nome} transferido para o curso {novo_curso}.")

class Professor:
    def __init__(self, primeiro_nome, sobrenome, cpf, endereco, formacao, disciplinas, segmentos, turmas, nome_usuario, email, senha):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.endereco = endereco
        self.formacao = formacao
        self.disciplinas = disciplinas  # Lista de disciplinas que o professor leciona
        self.segmentos = segmentos  # EM ou Superior
        self.turmas = turmas  # Lista de turmas que o professor leciona
        self.nome_usuario = nome_usuario
        self.email = email
        self.senha = senha

    @property
    def nome_professor(self):
        return f"{self.primeiro_nome} {self.sobrenome}"

    @property
    def disciplinas_lecionadas(self):
        return ", ".join(self.disciplinas)

class Disciplina:
    def __init__(self, id_disciplina, descricao, segmento, professor_titular):
        self.id_disciplina = id_disciplina
        self.descricao = descricao
        self.segmento = segmento  # EM ou Superior 0=EM 1=Superior 2=Ambos
        self.professor_titular = professor_titular  # Professor responsável pela disciplina

    @property
    def tipo_segmento(self):
        if self.segmento == 0:
            return "Ensino Médio"
        elif self.segmento == 1:
            return "Superior"
        elif self.segmento == 2:
            return "Ambos"
        else:
            return "Segmento inválido"

    @property
    def nome_professor_titular(self):
        return f"{self.professor_titular.primeiro_nome} {self.professor_titular.sobrenome}"

class Turma:
    def __init__(self, nome, segmento, curso, ano, maximo, alunos=None, professores=None, disciplinas=None):
        self.nome = nome
        self.segmento = segmento  # EM ou Superior
        self.curso = curso  # Mecatrônica, Eletromecânica, Informática, Ciências da Computação, Pedagogia
        self.ano = ano
        self.alunos = alunos if alunos else []
        self.professores = professores if professores else []
        self.disciplinas = disciplinas if disciplinas else []
        self.maximo=maximo

    @property
    def vagas_disponiveis(self):
        return self.maximo - len(self.alunos)

    @property
    def alunos_matriculados(self):
        return ", ".join([aluno.nome_completo for aluno in self.alunos])

    def adicionar_aluno(self, aluno, remove):
        if not aluno in self.alunos:
            if len(self.alunos) < self.maximo:
                if self.curso in aluno.cursos:
                    self.alunos.append(aluno)
                    if remove:
                        aluno.turmas = [self]
                    else:
                        aluno.turmas.append(self)
                    print(f"Aluno {aluno.primeiro_nome} {aluno.sobrenome} adicionado à turma {self.nome}.")
                else: 
                    print(f"Aluno não é do mesmo curso que a turma(curso do aluno:{aluno.cursos},curso da turma: {self.curso})")
            else:
                print(f"Turma {self.nome} já possui o número máximo de alunos.")
        else:
            print(f"Aluno {aluno.primeiro_nome} já está na turma.")

    def adicionar_professor(self, professor):
        self.professores.append(professor)
        print(f"Professor {professor.primeiro_nome} {professor.sobrenome} adicionado à turma {self.nome}.")

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        print(f"Disciplina {disciplina.descricao} adicionada à turma {self.nome}.")

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            aluno.turmas.remove(self)
            print(f"Aluno {aluno.primeiro_nome} {aluno.sobrenome} removido da turma {self.nome}.")
        else:
            print(f"Aluno não encontrado na turma {self.nome}.")

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
            print(f"Professor {professor.primeiro_nome} {professor.sobrenome} removido da turma {self.nome}.")
        else:
            print(f"Professor não encontrado na turma {self.nome}.")

    def remover_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            print(f"Disciplina {disciplina.descricao} removida da turma {self.nome}.")
        else:
            print(f"Disciplina não encontrada na turma {self.nome}.")

class SistemaAcademico:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.turmas = []
        self.disciplinas = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.primeiro_nome} {aluno.sobrenome} cadastrado com sucesso.")

    def adicionar_professor(self, professor):
        self.professores.append(professor)
        print(f"Professor {professor.primeiro_nome} {professor.sobrenome} cadastrado com sucesso.")

    def adicionar_turma(self, turma):
        self.turmas.append(turma)
        print(f"Turma {turma.nome} cadastrada com sucesso.")

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        print(f"Disciplina {disciplina.descricao} cadastrada com sucesso.")


    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            #aluno.turma.remover_aluno(aluno)
            print(f"Aluno {aluno.primeiro_nome} {aluno.sobrenome} removido.")
        else:
            print(f"Aluno não encontrado.")

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
            print(f"Professor {professor.primeiro_nome} {professor.sobrenome} removido.")
        else:
            print(f"Professor não encontrado.")

    def remover_turma(self, turma):
        if turma in self.turmas:
            self.turmas.remove(turma)
            print(f"Disciplina {turma.nome} removida.")
        else:
            print(f"Turma não encontrada")

    def remover_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            print(f"Disciplina {disciplina.descricao} removida")
        else:
            print(f"Disciplina não encontrada")

    def exibir_turmas(self):
        for turma in self.turmas:
            print(f"Turma: {turma.nome}, Segmento: {turma.segmento}, Curso: {turma.curso}, Ano: {turma.ano}, Alunos: {len(turma.alunos)}, Máximo: {turma.maximo}")

    def transferir_de_curso(self, aluno, novo_curso):
        #Mostrar ao usuário as turmas disponiveis para a troca
        #Pedir que escolha uma
        #trocar o usuário para a turma
        print("Turmas Disponiveis no curso selecionado:")
        i=0
        for turma in self.turmas:
            if turma.curso == novo_curso and len(turma.alunos)<turma.maximo:
                print(f"Turma: {turma.nome}, Segmento: {turma.segmento}, Curso: {turma.curso}, Ano: {turma.ano}, Alunos: {len(turma.alunos)}, Máximo: {turma.maximo}")
                i+=1
        if i==0:
            print("Não há turmas disponiveis")
        else:
            selecionou=False
            while True:
                if not selecionou:
                    turmaselecionada=input("Qual turma transferir o aluno: ")
                    selecionou=True
                    i=0
                novaturma=self.turmas[i]
                #print(novaturma.nome,turmaselecionada)
                #print(turma.curso,novo_curso)
                #print(len(turma.alunos),turma.maximo)
                if novaturma.nome==turmaselecionada and novaturma.curso == novo_curso and len(novaturma.alunos)<novaturma.maximo:
                    break
                i+=1
                if i >= len(self.turmas):
                    print("Não selecionou uma turma disponivel.")
                    selecionou=False
            for i in aluno.turmas:
                i.remover_aluno(aluno)
            aluno.cursos = [novo_curso]
            novaturma.adicionar_aluno(aluno,True)
            print(f"Aluno {aluno.primeiro_nome} transferido para o curso {novo_curso} na turma {turmaselecionada}.")

    @property
    def numero_de_alunos(self):
        return len(self.alunos)

    @property
    def numero_de_turmas(self):
        return len(self.turmas)

# Exemplo de uso

# Criando alunos
alunos1 = [
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0001", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0002", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0003", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0004", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0005", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0006", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0007", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0008", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0009", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0010", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0011", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0012", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0013", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0014", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0015", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0016", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0017", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0018", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0019", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0020", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0021", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0022", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0023", "EM", ["Mecatrônica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0024", "EM", ["Mecatrônica"], "maria.oliveira", "maria@email.com", "senha123")]
alunos2 = [
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0025", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0026", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0027", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0028", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0029", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0030", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0031", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0032", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0033", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0034", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0035", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0036", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0037", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0038", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0039", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0040", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0041", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0042", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0043", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0044", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0045", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0046", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0047", "EM", ["Informática"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0048", "EM", ["Informática"], "maria.oliveira", "maria@email.com", "senha123")]
alunos3 = [
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0049", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0050", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0051", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0052", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0053", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0054", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0055", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0056", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0057", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0058", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0059", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0060", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0061", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0062", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0063", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0064", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0065", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0066", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0067", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0068", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0069", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0070", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0071", "EM", ["Eletromecânica"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0072", "EM", ["Eletromecânica"], "maria.oliveira", "maria@email.com", "senha123")]
alunoambos1=Aluno("Felipe", "Domingos", "Rua C", "Mãe: Maria Domingos", "maria.domingos@email.com", "RA0073", "EM", ["Ciências da Computação","Pedagogia"], "joao.silva", "joao@email.com", "senha123")
alunoambos2=Aluno("Pedro", "Silva", "Rua D", "Pai: João Josefino", "joao.jsfino@email.com", "RA0074", "EM", ["Ciências da Computação","Pedagogia"], "joao.silva", "joao@email.com", "senha123")
alunos4 = [
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0075", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0076", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0077", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0078", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0079", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0080", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0081", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0082", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0083", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0084", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0085", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0086", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0087", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0088", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0089", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0090", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0091", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0092", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0093", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0094", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0095", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0096", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0097", "EM", ["Ciências da Computação"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0098", "EM", ["Ciências da Computação"], "maria.oliveira", "maria@email.com", "senha123")]
alunos5 = [
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0099", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0100", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0101", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0102", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0103", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0104", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0105", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0106", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0107", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0108", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0109", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0110", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0111", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0112", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0113", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0114", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0115", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0116", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("João", "Silva", "Rua A", "Mãe: Maria Silva", "maria.silva@email.com", "RA0117", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Maria", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0118", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Josevildo", "Lorenha", "Rua A", "Mãe: Luana Lorenha", "luana.lorenha@email.com", "RA0119", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Isabela", "Otero", "Rua C", "Pai: José Otero", "jose.otero@email.com", "RA0120", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123"),
    Aluno("Gustavo", "José", "Rua D", "Mãe: Maria Silva", "maria.silva@email.com", "RA0121", "EM", ["Pedagogia"], "joao.silva", "joao@email.com", "senha123"),
    Aluno("Natan", "Oliveira", "Rua B", "Pai: João Oliveira", "joao.oliveira@email.com", "RA0122", "EM", ["Pedagogia"], "maria.oliveira", "maria@email.com", "senha123")]
# Criando professores
professor1 = Professor("Carlos", "Pereira", "123.456.789-00", "Rua C", "Mestre em Mecatrônica", ["Mecatrônica"], ["EM"], [], "carlos.pereira", "carlos@email.com", "senha123")
professor2 = Professor("Gustavo", "Silva", "123.456.789-00", "Rua D", "Mestre em Informática", ["Informática"], ["EM"], [], "carlos.pereira", "carlos@email.com", "senha123")
professor3 = Professor("Gustavo", "Silva", "123.456.789-00", "Rua D", "Mestre em Eletromecânica", ["Eletromecânica"], ["EM"], [], "carlos.pereira", "carlos@email.com", "senha123")
professor4 = Professor("Gustavo", "Silva", "123.456.789-00", "Rua D", "Mestre em Ciências da Computação", ["Ciências da Computação"], ["S"], [], "carlos.pereira", "carlos@email.com", "senha123")
professor5 = Professor("Gustavo", "Silva", "123.456.789-00", "Rua D", "Mestre em Pedagogia", ["Pedagogia"], ["S"], [], "carlos.pereira", "carlos@email.com", "senha123")

# Criando disciplinas
disciplina1 = Disciplina("D001", "Introdução à Mecatrônica", "0", professor1)
disciplina2 = Disciplina("D002", "Introdução à Informática", "0", professor2)
disciplina3 = Disciplina("D003", "Introdução à Eletromecânica", "0", professor3)
disciplina4 = Disciplina("D004", "Introdução às Ciências da Computação", "1", professor4)
disciplina5 = Disciplina("D005", "Introdução à Pedagogia", "1", professor5)

# Criando turmas
turma1 = Turma("Turma A", "EM", "Mecatrônica", 2024 ,40)
turma2 = Turma("Turma B", "EM", "Informática", 2024 ,40)
turma3 = Turma("Turma C", "EM", "Eletromecânica", 2024 ,40)

turma4 = Turma("Turma D", "S", "Ciências da Computação", 2024 ,40)
turma5 = Turma("Turma E", "S", "Pedagogia", 2024 ,40)

# Criando o sistema acadêmico
sistema = SistemaAcademico()

# Adicionando dados ao sistema
#sistema.adicionar_aluno(aluno1);sistema.adicionar_aluno(aluno2);sistema.adicionar_aluno(aluno3)
#sistema.adicionar_aluno(aluno4);sistema.adicionar_aluno(aluno5);sistema.adicionar_aluno(aluno6)
for i in alunos1:
    sistema.adicionar_aluno(i)
for i in alunos2:
    sistema.adicionar_aluno(i)
for i in alunos3:
    sistema.adicionar_aluno(i)
for i in alunos4:
    sistema.adicionar_aluno(i)
for i in alunos5:
    sistema.adicionar_aluno(i)
sistema.adicionar_aluno(alunoambos1)
sistema.adicionar_aluno(alunoambos2)
sistema.adicionar_professor(professor1)
sistema.adicionar_disciplina(disciplina1)
sistema.adicionar_disciplina(disciplina2)
sistema.adicionar_disciplina(disciplina3)
sistema.adicionar_disciplina(disciplina4)
sistema.adicionar_disciplina(disciplina5)
sistema.adicionar_turma(turma1)
sistema.adicionar_turma(turma2)
sistema.adicionar_turma(turma3)
sistema.adicionar_turma(turma4)
sistema.adicionar_turma(turma5)
turma1.adicionar_disciplina(disciplina1)
turma2.adicionar_disciplina(disciplina2)
turma3.adicionar_disciplina(disciplina3)
turma4.adicionar_disciplina(disciplina4)
turma5.adicionar_disciplina(disciplina5)

# Adicionando alunos à turma
for i in alunos1:
    turma1.adicionar_aluno(i,False)
for i in alunos2:
    turma2.adicionar_aluno(i,False)
for i in alunos3:
    turma3.adicionar_aluno(i,False)
for i in alunos4:
    turma4.adicionar_aluno(i,False)
turma4.adicionar_aluno(alunoambos1,False)
turma4.adicionar_aluno(alunoambos2,False)
for i in alunos5:
    turma5.adicionar_aluno(i,False)
turma5.adicionar_aluno(alunoambos1,False)
turma5.adicionar_aluno(alunoambos2,False)
#turma1.adicionar_aluno(aluno1)
#turma1.adicionar_aluno(aluno2)

#turma2.adicionar_aluno(aluno3)
#turma2.adicionar_aluno(aluno4)

#turma3.adicionar_aluno(aluno5)
#turma3.adicionar_aluno(aluno6)
print("\n--------\n")
# Exibindo as turmas cadastradas
sistema.exibir_turmas()

# Transferindo aluno de curso
sistema.transferir_de_curso(alunos1[0],"Eletromecânica")
sistema.exibir_turmas()