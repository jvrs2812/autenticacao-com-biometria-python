## INSTALE ANTES DE TUDO O DOCKER
# APOS INSTALAR O DOCKER IREMOS RODAR O COMANDO PARA BAIXAR A IMAGEM DO MONGODB
# docker pull mongo

## INICIANDO
# apos configurar tudo iremos rodar o comando 
# docker-compose up -d

# URI PARA CONEXAO mongodb://APSUNIP:APSUNIP@localhost:27017/?authMechanism=DEFAULT
# SERA NECESSARIO INSTALAR BIBLIOTECA COMO O OPENCV 
# pip install opencv-python

# apos isso sera necessario cadastrar um usuario direto no banco 
# no database admin sera necessario criar uma collection users
# apos isso sera necessario jogar a biometria para a pasta biometrias dentro do projeto e passar o caminho para o banco

# exemplo de insert de usuario
# {  "_id": {    "$oid": "63687808428d1c94ebf9ccba"  },  "nome": "leo",  "nivel_usuario": 10,  "url_biometria": "C:/Users/jvrs_/Desktop/Projeto python/biometrias/biometrialeo.tif"}

# apos isso o sistema esta pronto para ser usado