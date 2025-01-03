class AlunoClass:
    def __init__(self, nome, sobrenome, nota):
        self.nome = nome;
        self.sobrenome = sobrenome;
        self.nota = nota;

    def mostrarAluno(self):
        return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);

    def salvar(self, conexao, colecao):
        mydict = self.__dict__
        mydict['nome'] = self.nome
        mydict['sobrenome'] = self.sobrenome
        mydict['nota'] = self.nota
        x = conexao[colecao].insert_one(mydict)
        return x.acknowledged