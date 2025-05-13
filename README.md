# 💰 Controle Financeiro Pessoal (Python CLI)

Aplicativo de linha de comando desenvolvido em Python para gerenciar finanças pessoais. Permite registrar receitas e despesas, categorizar transações, consultar saldo e exportar relatórios.

---

## 🚀 Funcionalidades

- Registro de receitas e despesas
- Categorização por tipo (ex: Alimentação, Lazer, Salário)
- Listagem de transações por período
- Cálculo automático de saldo
- Exportação de relatórios em CSV
- Armazenamento local em JSON
- Log de ações do usuário

---

## 🛠 Tecnologias e Conceitos

- Python 3.10+
- Programação Orientada a Objetos
- Manipulação de arquivos: JSON, CSV
- Manipulação de datas (`datetime`)
- Geradores, decoradores, exceções
- `pip-tools` para gestão de dependências

---

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seuusuario/controle-financeiro.git
cd controle-financeiro
```
### 2. Crie o ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate     # Linux/Mac
.venv\Scripts\activate        # Windows
```
### 3. Instale o pip-tools e compile os requisitos
```bash
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```
### 4. Executar
```bash
python src/main.py
```