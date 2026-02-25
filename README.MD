# Looqbox Challenge – Data Analysis & SQL

## 📌 Sobre o Projeto
Este é o meu desafio técnico para a Looqbox, onde precisei trabalhar com duas frentes principais:
✏️ SQL – Consultas analíticas no banco MySQL

🐍 Python – Funções dinâmicas e análises usando pandas
O objetivo era mostrar como eu consigo:
Analisar dados e tirar insights
Escrever queries SQL eficientes
Manipular e agregar dados em Python
Organizar e estruturar código de forma clara
Também deixei tudo documentado pra que qualquer pessoa consiga entender e reproduzir o que fiz.

---
```text
## 🗂 Estrutura do Projeto
looqbox/
│
├── src/
│ ├── database.py
│ ├── data_access.py
│ ├── cases/
│ │ ├── case1.py
│ │ ├── case2.py
│ │ ├── case3.py
│ │ └── retrieve_data.py
│ │
│ └── questions/
│ ├── question1.py
│ ├── question2.py
│ └── question3.py
│
├── .gitignore
├── README.md
├── requirements.txt

```

---

## 🛠 Tecnologias Utilizadas
- Python 3.x  
- MySQL  
- Pandas  
- PyMySQL  
- Matplotlib  
- SQL  

---

## 🗄 Conexão com Banco de Dados
Criei o database.py para centralizar a conexão com o MySQL usando pymysql.
Separei a conexão em database.py pra não precisar ficar repetindo o mesmo código toda hora, e isso deixou tudo mais organizado.

---

## ▶️ Como Executar o Projeto
1️⃣ Puxando o projeto pra sua máquina
```text
git clone https://github.com/RuyLuques/looqbox-desafio-2026
```
```text
cd looqbox-desafio-2026
```

2️⃣ Instalando as dependências
```text
pip install -r requirements.txt
```
3️⃣ Rodando os scripts
Os scripts estão todos na pasta src. Pra rodar qualquer um, eu uso o caminho completo a partir dela.
Por exemplo:
Cases (Python + análises com pandas)
```text
python -m src.cases.case1
```
```text
python -m src.cases.case2
```
```text
python -m src.cases.case3
```
```text
python -m src.cases.retrieve_data
```

Questions (consultas SQL)
```text
python -m src.questions.question1
```
```text
python -m src.questions.question2
```
```text
python -m src.questions.question3
```

💡 Dica:
Todos os scripts usam a função get_connection() que tá em src/database.py pra se conectar ao banco MySQL do desafio. Então, fique na pasta raiz do projeto (looqbox) quando for rodar os comandos.

4️⃣ Vendo os resultados
Nos cases, você vai ver os dados aparecendo no terminal e, quando tiver gráfico, ele vai abrir pra você (matplotlib).
Nas questions, os resultados das queries aparecem direto no terminal.

---

Documentação: https://drive.google.com/file/d/1BjaJD2YaBom-sNdKk_9caNSaZczWSBkL/view?usp=sharing
