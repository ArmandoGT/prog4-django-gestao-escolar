from django.db import models


class Aluno(models.Model):
    # RA como chave primária manual ou IntegerField com unique=True
    ra = models.CharField(max_length=20, primary_key=True, verbose_name="RA")
    nome_aluno = models.CharField(max_length=100, verbose_name="Nome do Aluno")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")

    GENERO_CHOICES = [('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, verbose_name="Gênero")

    def __str__(self):
        return f"{self.ra} - {self.nome_aluno}"


class Professor(models.Model):
    rp = models.CharField(max_length=20, primary_key=True, verbose_name="RP")
    nome_prof = models.CharField(max_length=100, verbose_name="Nome do Professor")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    genero = models.CharField(max_length=1, choices=Aluno.GENERO_CHOICES, verbose_name="Gênero")
    titulacao = models.CharField(max_length=50, verbose_name="Titulação")

    def __str__(self):
        return self.nome_prof


class Curso(models.Model):
    cod_cur = models.AutoField(primary_key=True)
    nome_cur = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_cur = models.IntegerField(verbose_name="Carga Horária")

    def __str__(self):
        return self.nome_cur


class Disciplina(models.Model):
    cod_disc = models.AutoField(primary_key=True)
    nome_disc = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    carga_horaria_disc = models.IntegerField(verbose_name="Carga Horária")

    # Relacionamento: Pertence a UM Curso (1,1)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')

    # Relacionamento: Ministrada por Professores (N,N)
    professores = models.ManyToManyField(Professor, related_name='disciplinas')

    def __str__(self):
        return self.nome_disc


class Matricula(models.Model):
    cod_mat = models.AutoField(primary_key=True)
    data_mat = models.DateField(auto_now_add=True, verbose_name="Data da Matrícula")

    # Relacionamento: Aluno faz Matrícula (1,n)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')

    # Relacionamento: Matrícula pertence a Curso (1,1)
    # Nota: No DER, a matrícula liga Aluno e Curso.
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')

    def __str__(self):
        return f"Matrícula {self.cod_mat} - {self.aluno}"