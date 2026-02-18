<div align="center">
  <img src="./escola/static/escola/IF.png" width="35" alt="Logo IFRO" />
  <br>
  <h1>Sistema de Gestão Escolar - Matrículas</h1>
  <p>
    <strong>IFRO - Campus Ariquemes | Programação IV</strong>
  </p>
</div>

<div align="center">
  
[![Django](https://img.shields.io/badge/Django-6.0-darkgreen?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-purple?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

</div>

<br>

## 1. Descrição do Projeto

Este projeto é uma aplicação web desenvolvida como atividade da disciplina de **Programação IV**, focada na revisão de conceitos do framework Django. O objetivo principal é gerenciar o processo de matrícula de alunos, implementando fielmente um **Diagrama de Entidade-Relacionamento (DER)** pré-definido.

O sistema utiliza a arquitetura **MVT (Model-View-Template)** para separar a lógica de negócios da interface do usuário, garantindo uma estrutura organizada e escalável. O foco da implementação está na correta modelagem de dados, uso de relacionamentos complexos (1:N e N:N) e personalização do fluxo de trabalho fora do painel administrativo padrão.

---

## 2. Requisitos Atendidos

O desenvolvimento seguiu as diretrizes da atividade:

* ✅ **Modelagem de Dados:** Criação de Models para todas as entidades (`Aluno`, `Professor`, `Curso`, `Disciplina`, `Matricula`), respeitando as cardinalidades.
* ✅ **Gestão Administrativa:** Registro dos models no `Django Admin` para cadastro, **exceto** a tabela de Matrículas, conforme solicitado.
* ✅ **Fluxo de Matrícula:** Criação de Views (`ListView`, `CreateView`), Forms e Rotas específicas para gerenciar matrículas via interface pública.
* ✅ **Front-end Modular:** Utilização de **Herança de Templates** para reaproveitamento de código HTML (`base.html`).

---

## 3. Arquitetura e Modelagem

O projeto foi estruturado para refletir os relacionamentos do modelo escolar:

### Entidades e Relacionamentos
* **Aluno:** Entidade principal com RA (Chave Primária). Relaciona-se 1:N com *Matricula*.
* **Curso:** Possui carga horária e nome. Relaciona-se 1:N com *Disciplina* e 1:N com *Matricula*.
* **Professor:** Possui titulação. Relaciona-se N:N com *Disciplina* (Um professor ministra várias disciplinas, uma disciplina tem vários professores).
* **Disciplina:** Vinculada a um único Curso.
* **Matricula (Entidade Associativa):** O núcleo da atividade. Conecta um *Aluno* a um *Curso*.

### Estrutura de Diretórios
A organização segue o padrão de *Apps* do Django:

* **`setup/`**: Configurações globais do projeto (Settings, URLs principais, WSGI/ASGI).
* **`escola/`**: App principal contendo a lógica de negócio.
    * **`models.py`**: Definição do ORM e relacionamentos.
    * **`views.py`**: Lógica das páginas de listagem e criação de matrículas.
    * **`forms.py`**: Formulário personalizado para o processo de matrícula.
    * **`admin.py`**: Configuração do painel administrativo (com restrições).
    * **`templates/`**: Arquivos HTML utilizando Bootstrap 5 e herança.

---

## 4. Funcionalidades

### Módulo Público (Fluxo de Matrícula)
* **Listagem de Matrículas:** Visualização de todas as matrículas realizadas, exibindo aluno, curso e data.
* **Nova Matrícula:** Formulário para vincular um aluno existente a um curso disponível.

### Módulo Administrativo (Restrito)
* **Gestão de Cadastros Base:** Interface completa (CRUD) para gerenciar:
    * Alunos
    * Professores
    * Cursos
    * Disciplinas (com interface para selecionar múltiplos professores)

---

## 5. Instruções de Execução

Para executar o projeto localmente em sua máquina:

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Git instalado.

### Passo a Passo

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/ArmandoGT/prog4-django-gestao-escolar.git](https://github.com/ArmandoGT/prog4-django-gestao-escolar.git)
    cd prog4-django-gestao-escolar
    ```

2.  **Criar e ativar o ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar o Banco de Dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Criar Superusuário (Para acessar o Admin):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Executar o servidor:**
    ```bash
    python manage.py runserver
    ```

Acesse a aplicação em:
* **Área Pública:** `http://127.0.0.1:8000/`
* **Área Administrativa:** `http://127.0.0.1:8000/admin/`

---

## 6. Tecnologias Utilizadas

| Tecnologia | Propósito |
|-----------|----------|
| **Django 6.0** | Framework web backend principal |
| **Python** | Linguagem de programação |
| **SQLite** | Banco de dados relacional (Padrão Django) |
| **Bootstrap 5** | Estilização e responsividade das interfaces |
| **Django Templates** | Renderização do Front-end |

---

<div align="center">
  <p>Desenvolvido por <strong>ArmandoGT</strong></p>
  <p><img src="./escola/static/escola/IF.png" width="8" alt="Logo IFRO"/> 
  IFRO - Instituto Federal de Rondônia</p>
</div>