# Cartola FC - Chatbot

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/wladneto/cartola-bot)

Projeto de chatbot utilizando opensource [Rasa](https://rasa.com/) para auxiliar jogadores do fantasy game [Cartola FC](https://ge.globo.com/cartola/).

## Como executar o chatbot localmente?
 
1 - Crie um ambiente virtual Python 3.8 com o comando abaixo. Assim uma pasta `./venv` será criada na raiz do projeto.
  ```bash
  python3 -m venv ./venv
  ```
2 - Ative o ambiente virtual.
  ```bash
  source ./venv/bin/activate
  ```
3 - Verifique versão do python. (Deverá ser a 3.8.XX)
  ```bash
  source ./venv/bin/activate
  ```
4 - Instale o rasa
  ```bash
  pip3 install rasa
  ```
5 - Execute o treinamento do chatbot
  ```bash
  rasa train
  ```
6 - Execute o rasa localmente
  ```bash
  rasa run --cors "*"
  ```
7 - Em um novo terminal execute as actions
  ```bash
  rasa run actions
  ```
8 - Abra no browser o arquivo /local/testPage.html

9 - Converse com o chatbot :)

## Canais
- Telegram (TO:DO)
- Web (local)
## Funções
- Informações sobre a rodada
- Lista de mais escalados para rodada

