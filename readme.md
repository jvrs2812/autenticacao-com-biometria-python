# Instalando o Docker
0) Será necessário ter o docker instalado para subir toda configuração de banco do projeto. Para isso basta acessar o link e baixar. <p>
[Docker](https://www.docker.com/)


1) APOS INSTALAR O DOCKER IREMOS RODAR O COMANDO PARA BAIXAR A IMAGEM DO MONGODB
> docker pull mongo

## INICIANDO
2) Após configurar tudo iremos rodar o comando 
> docker-compose up -d

3) Uri de conexão com o banco de dados mongo, sendo necessário algum client noSql, seja ele DBEAVER ou MONGODB Compass
> mongodb://APSUNIP:APSUNIP@localhost:27017/?authMechanism=DEFAULT 
    
4) Será necessário instalar a biblioteca do opencv  
> pip install opencv-python

5) Após isso será necessário cadastrar um usuário direto no banco no database admin sera necessario criar uma collection users

5.1) Após isso sera necessario jogar a biometria para a pasta biometrias dentro do projeto e passar o caminho para o banco
> 📂 biometrias

5.2) Exemplo de insert de usuario
> {  "_id": {    "$oid": "63687808428d1c94ebf9ccba"  },  "nome": "leo",  "nivel_usuario": 10,  "url_biometria": "C:/Users/jvrs_/Desktop/Projeto python/biometrias/biometrialeo.tif"}

# E pronto !!!
