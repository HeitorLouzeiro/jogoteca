# Jogoteca

Repositório para estudo relacionado ao framework Flask em Python e criação de APIs.

## Descrição

O Jogoteca é uma aplicação web simples desenvolvida como parte de estudos do curso da Alura. Esta aplicação demonstra os conceitos básicos de desenvolvimento web utilizando Flask, um microframework para Python.

## Funcionalidades Atuais

- Rota inicial `/inicio` que exibe uma mensagem "Olá Mundo!"

## Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/HeitorLouzeiro/jogoteca
   cd jogoteca
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

Execute o seguinte comando para iniciar a aplicação:

```bash
python jogoteca.py
```

A aplicação estará disponível em: http://localhost:5000/inicio

## Dependências

O projeto utiliza as seguintes bibliotecas:
- Flask 3.1.1
- Werkzeug 3.1.3
- Jinja2 3.1.6
- MarkupSafe 3.0.2
- itsdangerous 2.2.0
- click 8.2.1
- colorama 0.4.6
- blinker 1.9.0

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE) - veja o arquivo LICENSE para mais detalhes.
