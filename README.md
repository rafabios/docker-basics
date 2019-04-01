# Lab0 - Opcional

1. Instalar o Ubuntu 16.04 (VirtualBox);
2. Instalar o docker-ce 19.03
3. Baixar as imagens:
	* rancher/server:latest
	* rancher/agent
	* rancher/metadata
	* rancher/net
	* rancher/dns
	* rancher/healthcheck
	* rancher/metadata
	* rancher/network-manager
	* rancher/net:holder
	* alpine
	* debian
	* nginx
	* mysql:5.5
	* redis
	* jenkins
	* python

4. Criar duas vms:
	* Master.vdi
	* Worker.vdi



5. Criar uma conta no [Dockerhub](https://hub.docker.com/)
	- Para se logar no docker via linha de comando:
		* ``` docker login ```

-------------------------------------------------------------------------------------------------------

# Lab01 - Docker - Baixando imagens

1. Baixando imagens:
	* Vamos baixar a imagem do python para criamos um webserver:
	  - ```docker pull python:latest```
2. Validando a imagem baixada:
	* ```docker run -i -t --rm python:latest /bin/bash```
	* ```run```: Comando para informar ao docker que a imagem necessita ser executada
	*  ```-i -t```: Modo interativo/tty, utilizamos para poder acessar uma sessao de console no container
	*  ```--rm```: Apagar container e volumes apos execucao
	*  ```python:latest``` : Imagem e tag de versao a ser rodado
	*  ```/bin/bash``` : comando a ser executado no container

-------------------------------------------------------------------------------------------------------

# Lab02 - Docker - Gerenciando imagens

1. Na maquina virtual Worker, crie um diretorio chamado: '/opt/webserver/';
	- Acesse o diretorio e crie dois arquivos:
		* Dockerfile
		* webserver.py
	    * **Obs:** o conteudo dos arquivos estao na pasta [Lab01](https://github.com/rafabios/docker-basics/tree/master/Lab01) 			

2. Cria a primeira imagem no docker:
	* ```docker build -t python_webserver:v1.0 .```
	* `build: ` Comando para buildar uma nova imagem
	* `-t :`    Comando para informar o nome e tag do projeto
	* `. :`	  Informa para o docker que o arquivo Dockerfile esta no mesmo diretorio de execucao

3. Agora vamos testar a imagem criada, como o comando abaixo:
	* ``` docker run -it --rm -e WEBSERVICE_PORT='8080' -e WEBSERVICE_NAME=' teste_rafael  ' -e WEBSERVICE_VERSION='v1.0 ' -p 8080:8080 python_webserver:v1.0```		
	* `run`	 Comando para informar ao docker que a imagem necessita ser executada
	* `-it` Modo interativo/tty, utilizamos para poder acessar uma sessao de console no container
	* `--rm`  Imagem e tag de versao a ser rodado
	* `-e` Informar variaveis de ambiente
	* `-p 8080:8080` Cria uma porta TCP entre container e host [PORTA_DO_HOST:PORTA_DO_CONTAINER]
	* `python_webserver:v1.0` Imagem:tag

4. Agora vamos subir a imagem para o dockerhub: 
	- ``` docker tag python_webserver:v1.0 <LOGIN_DO_DOCKERHUB>/python_webserver:v1.0 ```
	- ``` docker push <LOGIN_DO_DOCKERHUB>/python_webserver:v1.0 ```


5. Acesse via browser o site para checa o resultado:
	- http://IP_DO_WORKER:8080


-------------------------------------------------------------------------------------------------------
# Lab03 - Docker - Containers

1. Agora vamos acessar um container em execucao. Primeiro iremos subir um container em background:
	-  ``` docker run --name python_webserver -d -it --rm -e WEBSERVICE_PORT='8080' -e WEBSERVICE_NAME=' teste_rafael  ' -e WEBSERVICE_VERSION='v1.0 ' -p 8080:8080 python_webserver:v1.0```
	- `--name` Informa o nome do container
	- `-d` Roda em modo background

2. Acessar console do container:
	- ``` docker exec -it python_webserver /bin/bash```
	- `exec` Comando correspondendo para acessar containers em execucao
	* ***Pressione CRTL + D para sair do container***	

-------------------------------------------------------------------------------------------------------
# Lab04 - Docker - Manutencao de espaco de disco

1. Como checar espaco em disco?
	- Verificar o arquivo de logs do docker: 
		* ```/var/log/daemon```  Em caso de problema no docker o arquivo cresce demais
	- Verificar os logs dos containers: 
		* ```du -h /var/lib/docker/containers/*/*-json.log```    Correspondente ao docker logs <container>
	- Verificar tamanho dos containes: 
		* ```docker system df```   Mostra tamanho de imagnes, containers e volumes
		* ```docker ps --size```   Mostra tamanho dos containers, individualmente

2. Como apagar recursos nao usados:
	- Apagar arquivos de log:
		* ```echo "" > Nome_do_Arquivo```    Utilizar o echo ou truncate para apagar aquivos, se utilizar o rm, o arquivo se apagado e o espaco nao sera liberado;
		- Exemplos:
			```
			echo "" > /var/log/daemon		
			echo "" >  /var/lib/docker/containers/f071f64633/f071f64c98dbe6a62633-json.log 
			```

	- Apagar imagens, volumes e containers nao utilizados pelo docker:
		* ```docker system prune```   Limpa diversos recursos do docker  
		* ```docker volume prune```   Limpa volumes nao utilizados do docker
		* ```docker image prune```    Limpa imagens nao utilizadas pelo docker
		* ```docker rmi <nome_da_imagem>```      Exclui uma imagem especifica
		* ```docker rm <nome_do_container>```    Exclui uma container espeficico


-------------------------------------------------------------------------------------------------------
# Lab04 - Instalando o Rancher

1. Na maquina virtual worker, executar o seguinte comando:
	* ``` docker run -d -v /var/lib/mysql:/var/lib/mysql --restart=unless-stopped -p 8080:8080 rancher/server```
	* `-v` Parametro para manter os dados persistentes mesmo quando o container for excluido;
	* `--restart` Politica para estrategia de restart em caso  de falhas
		- Para mais informacoes de instalacao do Rancher, acessar o link: [Rancher 1.6 - Install](https://rancher.com/docs/rancher/v1.6/en/installing-rancher/installing-server/#single-container-bind-mount)

2. Acesse o Rancher Server via web:
	* **http://IP_DO_MASTER:8080**


-------------------------------------------------------------------------------------------------------
# Lab05 - Rancher primeiras configuracoes

1. Ainda no Web, iremos criar um novo envroniment:
	- No canto superior esquerdo, clique em "Default" e em "Manage Envronments"
	- Clique em "Add Enviroment"
	- Em Name coloque o nome "Homol"
	- Selecione o tipo de orquestrador "Cattle"

2. Agora vamos adicionar um node (WORKER):
	- Acesse o enviroment **"Homol"**
	- Clique em **"INFRAESTRUTURE"** e em **"HOSTS"**
	- Clique em **"Add Host"**
	- Copie a saida que dever se parecida com o comando abaixo:
``` docker run --rm --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/rancher:/var/lib/rancher rancher/agent:v1.2.11-rc1 http://<IP_DO_MASTER>:8080/v1/scripts/F7559D8C5CE4B3A7462A:1546214400000:xZy9o4jrbLwKiHR3CC4J8HqLyqs
```
		* **Cole a saida no console da maquina WORKER**

3. Validando se o node WORKER foi adicionado ao cluster do Rancher:
	- Acesse novamente o browser na interface web do Rancher e clique em **HOSTS**
	- Veja se aparecerá uma caixa com as informação do node WORKER;

4. Troubleshooting:
	- Caso nao aparece no browser o Node Worker, você pode executar os comandos abaixo para verificar a conexão:
		* `docker ps -a | grep agent`
	 	* `docker logs -f <ID_DO_CONTAINER>`
	 - Com os comandos acima, é possivel verificar o porque a conexão nao esta sendo estabelecida entre os servidores virtuais				

-------------------------------------------------------------------------------------------------------
# Lab06 - Rancher - Subindo o Primeiro Stack

-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------



