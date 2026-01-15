# StudyBuddy

Projeto de um site simples de criação de salas de estudo, com troca de mensagens dentro das salas, feito em Django, para fins educacionais. O HTML, CSS e os Scripts em JavaScript não foram feitos por mim, apenas modificados para renderizar corretamente as variáveis e objetos. O projeto foi feito seguindo o tutorial [Python Django 7 Hour Course](https://www.youtube.com/watch?v=PtQiiknWUcI).

---

## Requisitos

- Python 3.10+
- pip
- (Opcional) PostgreSQL  
  > Caso queira usar SQLite, não é necessário PostgreSQL

---

## Clonando o repositório

```bash
git clone https://github.com/jeovasb00/StudyBud.git
cd StudyBud
```

---
## Criando e ativando ambiente virtual

```bash
python -m venv .venv 
```

#### Ativando no Linux/Mac:
```bash
source .venv/bin/activate
```
#### Ativando no Windows:
```bash
.venv\Scripts\activate
```
---
## Instalando dependências 

```bash
pip install -r requirements.txt
```
---

## Configurando variáveis de ambiente

Crie um arquivo .env na pasta raiz do projeto baseado no arquivo .env.example

```env
cp .env.example .env
```

## Exemplo usando SQLite 
#### (SECRET_KEY pode ser qualquer uma, desde que o projeto esteja rodando localmente)


```env
USE_SQLITE=True
SECRET_KEY=change-me
DEBUG=True
```

#### Opcionalmente, você pode gerar uma chave segura com:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```


## Exemplo usando PostgreSQL (opcional)

```env
USE_SQLITE=False
SECRET_KEY=change-me
DEBUG=True

DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432
```

---

## Aplicando migrações

```bash
python manage.py migrate
```

## Criando superusuário (opcional, mas necessário para acessar o Admin)

```bash
python manage.py createsuperuser
```

## Executando o projeto

```bash
python manage.py runserver
```