# Sistema de Gerenciamento de Biblioteca

## Sobre o Projeto

Este é um projeto de um Sistema de Gerenciamento de Biblioteca desenvolvido com Django. A plataforma permite gerenciar de forma completa o acervo de livros, autores, categorias, leitores e o controle de empréstimos, tudo isso com um sistema de autenticação e permissões robusto.

O objetivo foi construir uma aplicação web completa e funcional, aplicando os conceitos que aprendi em minha jornada com Python e Django, e ao mesmo tempo, explorar ferramentas modernas para otimizar o ciclo de desenvolvimento.

## Principais Funcionalidades

* **Gestão de Catálogo:** CRUD completo para Livros, Autores e Categorias.
* **Controle de Leitores:** Cadastro e gerenciamento de informações dos leitores (patrons).
* **Sistema de Empréstimos:**
    * Registro de novos empréstimos, com atualização automática do estoque de livros.
    * Registro de devoluções.
    * Listagem separada de empréstimos ativos e já devolvidos.
    * Busca inteligente por livro, leitor ou CPF.
* **Autenticação e Permissões:** O sistema utiliza o sistema de autenticação e permissões do Django para controlar o acesso a diferentes funcionalidades, garantindo que apenas usuários autorizados possam realizar determinadas ações.

## Tecnologias Utilizadas

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap 5
* **Banco de Dados:** PostgreSQL (configurado para rodar com Docker)
* **Testes:** Pytest, Pytest-Django
* **Containerização:** Docker, Docker Compose
  
[▶️ Clique aqui para ver a demonstração em vídeo](https://youtu.be/Tbng-8h86uc)

## Como Executar o Projeto Localmente

O projeto é containerizado com Docker, facilitando a configuração do ambiente.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/CFBruna/library_management.git](https://github.com/CFBruna/library_management.git)
    cd library_management
    ```

2.  **Configure as variáveis de ambiente:**
    * Renomeie o arquivo `.env.example` para `.env`.
    * Se desejar, altere os valores dentro do arquivo `.env` (não é estritamente necessário para rodar localmente, mas é uma boa prática).

3.  **Suba os containers com Docker Compose:**
    ```bash
    docker-compose up --build
    ```

4.  **Acesse a aplicação:**
    * Abra seu navegador e acesse `http://localhost:8000`.

## Meu Processo de Desenvolvimento e o Papel da IA

Desde o início, minha meta era não apenas construir um projeto, mas também otimizar o processo. Eu fui responsável por toda a arquitetura da aplicação: desenhei os `models`, estruturei as `views` com a lógica de negócio e defini as regras de permissão.

Nesse processo, utilizei ferramentas de Inteligência Artificial como uma assistente de desenvolvimento. Em vez de gastar tempo com tarefas repetitivas, eu direcionei a IA para:

* **Gerar os testes automatizados:** Com meu conhecimento sobre o que precisava ser testado, guiei a IA para criar os testes unitários e de integração com Pytest, o que acelerou a garantia de qualidade do código.
* **Estruturar o frontend:** O template `base.html` e outros templates foram gerados com o auxílio da IA, seguindo as diretrizes de design que eu estabeleci.
* **Configurar o ambiente de deploy:** Utilizei a IA para me ajudar a escrever o `Dockerfile` e o `docker-compose.yml`, com base nos requisitos do meu projeto.

Acredito que a habilidade mais importante de um desenvolvedor moderno é saber traduzir uma necessidade de negócio em uma solução técnica funcional, utilizando as melhores e mais eficientes ferramentas disponíveis. Este projeto é um reflexo dessa filosofia.
