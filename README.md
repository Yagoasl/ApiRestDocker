# ApiRestDocker

## Descrição

O objetivo desse desafio é construir uma interface REST que permita a gestão (start, stop, remove) de contêineres, imagens, volumes e redes Docker remotamente utilizando uma API para tal.

- Seguir as boas práticas para o desenvolvimento de APIs REST;
- Utilizar os métodos HTTP para a gestão dos contêineres;
  - Ela deve permitir a criação de contêineres;
  - Ela deve permitir a inicialização de contêineres;
  - Ela deve permitir a parada de contêineres;
  - Ela deve permitir a deleção de contêineres;
  - Ela deve listar todos os contêineres, com e sem filtros por estados;
  - Ela deve permitir a criação de redes Docker;
  - Ela deve permitir a deleção de redes Docker;
  - Ela deve listar todas as redes criadas, com e sem filtros por estados;
  - Ela deve permitir o pull de imagens;
  - Ela deve permitir a remoção de imagens baixadas;
  - Ela deve listar as imagens baixadas;
  - Ela deve permitir a criação de volumes;
  - Ela deve permitir a listagem de volumes;
  - Ela deve permitir a deleção de volumes;
- A gestão dos contêineres deve permitir a associação um ou mais volumes, uma ou
mais redes, exposição de uma ou mais portas, nomeação de contêineres.
- Todos os artefatos (código, arquivos de configuração, desenho da arquitetura...)
desenvolvidos precisam estar disponíveis em um repositório de versionamento de
código acessível pelo time de avaliadores;
- O desafio deve ser executável em ambientes Linux x86_64.

## Linha de pensamento

1. Usar o Django Rest Framework para criar a interface. (desenvolvido)
2. Coletar os dados desejados de imagem, volume, portas, comandos. E salvar em um arquivo json. (Em desenvolvimento)
3. Transformar arquivos Json em um possivel dockerfile ou docker-compose. (Não desenvolvido)
4. Start, stop, remove de containers. (Não desenvolvido)

## Ferramentas usadas

1. [Python 3.10](https://docs.python.org/3/)
2. [Django 4](https://docs.djangoproject.com/pt-br/4.0/)
3. [Django Rest Framework](https://www.django-rest-framework.org/)

## Como rodar

Para testar, execute o virtualenv com às dependências do projeto. Execute o servidor django, executando na pasta onde se encontra o arquivo `manage.py` o comando `python manage.py runserver`.

Acesse `http://localhost:8000/`. Ao fim, você será direcionado a página inicial. 

No link `http://localhost:8000/dockerfile/` poderemos encontrar um rascunho de como salvar as informações desejadas no banco de dados e no arquivo Json.

A url `http://localhost:8000/dockerCompose/` não é exibida na pagina inicial, no entanto, ela existe. Nele poderemos encontrar um rascunho de como salvar as informações desejadas no banco de dados e no arquivo Json.
