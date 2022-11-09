# Instalando o Docker
0) Será necessário instalar o Docker.<p>
   Caso Seja Windows: [Docker](https://www.docker.com/) <p>
   Caso Seja Linux: [Docker](https://docs.docker.com/engine/install/ubuntu/)

1) APOS INSTALAR O DOCKER IREMOS RODAR O COMANDO PARA BAIXAR A IMAGEM DO MONGODB
   > docker pull mongo

## INICIANDO
2) Após configurar tudo iremos rodar o comando 
   > docker-compose up -d

3) Uri de conexão com o banco de dados mongo, sendo necessário algum client noSql, seja ele DBEAVER ou MONGODB Compass <p>
   > mongodb://APSUNIP:APSUNIP@localhost:27017/?authMechanism=DEFAULT 
    
4) Será necessário instalar a biblioteca do opencv  <p>
   > pip install opencv-python

5) Após isso será necessário cadastrar um usuário direto no banco no database admin sera necessario criar uma collection <strong>users</strong> <p>

  > <img src="https://github.com/jvrs2812/autenticacao-com-biometria-python/blob/main/imagens_readme/collections.png" width="350" title="hover text">
   
6) Após isso sera necessario jogar a biometria para a pasta biometrias dentro do projeto e passar o caminho para o banco <p>
   > 📂 biometrias

7) Exemplo de insert de usuario <p>
   > {  "_id": {    "$oid": "63687808428d1c94ebf9ccba"  },  "nome": "leo",  "nivel_usuario": 10,  "url_biometria": "C:/Users/jvrs_/Desktop/Projeto python/biometrias/biometrialeo.tif"}

# E pronto !!!

# Como usar

### Tela inicial
  Ao clickar em autenticar ele irá pedir para que você selecione a imagem da digital na extensão .tif 
  > <img src="https://github.com/jvrs2812/autenticacao-com-biometria-python/blob/main/imagens_readme/telainicial.png" width="350" title="hover text">
  
  Caso a biometria informada seja encontrado no banco, o login será feito, caso não irá aparecer uma mensagem assim
  > <img src="https://github.com/jvrs2812/autenticacao-com-biometria-python/blob/main/imagens_readme/Error.png" width="350" title="hover text"> 

  ## Caso precise de Biometrias .tif para testa segue o link com varias para download.
   > [Biometrias](http://bias.csr.unibo.it/fvc2000/download.asp)

 # APS UNIP 2022<p>


| Participantes               | Github                       |
| ----------------------------|------------------------------|
| João Victor Ramos de Sousa  | [João](https://github.com/jvrs2812)|
| Ellen Fernanda Romano       | [Ellen]() |
| Abner Alexandre Bonini      | [Abner](https://github.com/AbnerBonini22) |
| Marcos Bianchi              | [Marcos]() |
| Jheny Santos                | [Jheny]() |
     
Sistema desenvolvido para fins didáticos.<p>
