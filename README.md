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
		``` 
		docker run --rm --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/rancher:/var/lib/rancher rancher/agent:v1.2.11-rc1 http://<IP_DO_MASTER>:8080/v1/scripts/F7559D8C5CE4B3A7462A:1546214400000:xZy9o4jrbLwKiHR3CC4J8HqLyqs
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

1. Vamos criar um stack webserver no WORKER com a porta 8080 aberta:
	- Vá em **STACKS**/**USER**
	- Cliquem em **Add Stack**
	- Adicione as seguintes informações:
		* Name: webserver
		* Optional: docker-compose.yml : Coloque a info abaixo:
		```
		version: '2'
		services:
		  webserver:
		    image: vemcompy/python_webserver:v1.0
		    environment:
		      WEBSERVICE_PORT: '8080'
		      WEBSERVICE_NAME: 'WEB_SERVICE_RAFAEL'
		      WEBSERVICE_VERSION: 'v1.0'	
		    ports:
		    - 8080:8080/tcp
		 ```
2. Valide se o stack foi criado com sucesso:
	- Clique em stacks novamente e vá até o stack chamado **webserver**
	- Clique no servico **webserver**
	- Clique em **Ports**
		* Clique no link para acessar o webserver

-------------------------------------------------------------------------------------------------------
# Lab07 - Rancher - Troubleshooting Containers

1. Atualizando uma imagem (com problemas na nova versão - aplicação):
	- Clique em **STACKS**
	- Localize o stack chamado **webserver**, clique nele
	- Ao lado do serviço há um botao com 3 pontos na vertical
	- Clique nele e pressione a opção: **Upgrade**
	- Localize o campo **Select Image**
		* Mude a versão de v1.0 para v1.1
		* Clique em **Upgrade**
	- Após atualizar, o serviço irá entrar em 'crashing looping'	
		* **O comportamento apresentado é comum em situações que a API está com problemas**
	- Caso o container fique em estado de **stopped** é possivel visualizar os logs da saida do container, clicando nos 3 pontos na vertical e em **View Logs**
		* **Caso o container reinicie mais rapido que a possibilidade de visualizar os logs: acesse o sevidor correspondente via ssh e digite os dois comandos abaixo:**
		* ```docker ps -a | grep webserver ``` Copie o ID do container 
		* ```docker logs <ID_DO_CONTAINER> ``` Assim é possivel ver os ultimos logs do container
	- Clique nos 3 pontos na vertical novamente e clique em **Rollback**
		* **Essa opção irá voltar a API para a versão v1.0**		

2. Atualizando uma imagem (não existente no dockerhub): 		
	- Clique em **STACKS**
	- Localize o stack chamado **webserver**, clique nele
	- Ao lado do serviço há um botao com 3 pontos na vertical
	- Clique nele e pressione a opção: **Upgrade**
	- Localize o campo **Select Image**
		* Mude a versão de v1.0 para v5.0
		* Clique em **Upgrade**
	- Após atualizar, o Rancher irá retornar uma mensagem de 'image not found'
		* **O comportamento apresentado é comum em situações que a imagem ainda nao foi gerada ou que ocorreu erro de digitação**
	- Clique nos 3 pontos na vertical novamente e clique em **Rollback**
		* **Essa opção irá voltar a API para a versão v1.0**		

3. Criando uma imagem com problemas no secrets:
	- Iremos criar uma imagem com secrets que nao existe:
	- Vá em **STACKS**/**USER**
	- Cliquem em **Add Stack**
	- Adicione as seguintes informações:
		* Name: webserver-secrets
		* Optional: docker-compose.yml : Coloque a info abaixo:
		```
		version: '2'
		services:
		  webserver:
		    image: vemcompy/python_webserver:v1.0
		    environment:
		      WEBSERVICE_PORT: '8080'
		      WEBSERVICE_NAME: 'WEB_SERVICE_RAFAEL'
		      WEBSERVICE_VERSION: 'v1.0'	
		    ports:
		    - 8080:8080/tcp
		    secrets:
		    - SECRETS_DATABASE
		  secrets:
  		   DB_PASSWORD:
    	    external: 'true'   
		 ```
	- O Rancher irá retornar que o Secrets nao foi encontrado;
	- Remova o stack	 

-------------------------------------------------------------------------------------------------------
# Lab08 - Jenkins - Instalacao e configuracao

1. Iremos subir um servico do Jenkins via Rancher:
	- Vá em **STACKS**/**USER**
	- Cliquem em **Add Stack**	
	- Adicione as seguintes informações:
		* Name: Jenkins-Server
		* Cliquem em **ok**
	- No canto superior direito, clique em **Add Service**
	- Preencha as informacoes abaixo:
	- ```
		Name: jenkins-server
		Image: jenkins
		Port Map:
				80:8080/tcp

		Volumes:
				/opt/jenkins:/var/jenkins_home
				/bin/rancher:/usr/local/bin/rancher ```


	- Acesse o endereco http://IP_DO_WORKER:80 via browser
	- A senha inicial deve estar dentro do container do Jenkins no diretorio abaixo: 
	 * `/var/jenkins_home/secrets/initialAdminPassword`	
	- Para acessar o container execute os comandos abaixo:
		* `docker ps  | grep jenkins`
	 	* `docker exec -it <ID_DO_CONTAINER> cat /var/jenkins_home/secrets/initialAdminPassword`

2. Instalacao de plugins
	- Apos definir uma nova senha para o user admin do Jenkins, devemos instalar os plugins abaixo:
		* Git
		* Git Client
		* GitHub
		 - **Para instalar os plugins, va em Gerenciador do Jenkins / Gerenciar plugins e clique em disponiveis**

			
-------------------------------------------------------------------------------------------------------
# Lab09 - Jenkins - Criando o primeiro projeto

1. Primeiro devemos criar um par de chaves de seguranca do Rancher
	- Acesse o Rancher via browser
	- Clique em API / Keys
	- Clique em Advanced options
	- Selecione a opcao: Add Environment API Keys
	- Em Nome, digite Jenkins-KEY
	- Copie os valores apresentados para um bloco de notas, iremos usar os valores a seguir


2. Vamos subir o projeto webservice via github e integrar com o rancher via linha de comando:
	- Volte para a pagina inicial do Jenkins
	* Clique em **New Job**
	* Digite em nome do projeto **webserver-python**
	* Escolha o modelo **Free Style Project**
	* Clique em salvar
	- Agora dentro do projeto **webserver-python**, clique em configurar;
	* Em Gerenciador do Codigo Fonte, clique em **GIT**
	* Em Repository URL, digite: **https://github.com/rafabios/docker-basics.git**
	* Em Build, selecione a opcao **Execute Shell**
	* Na tela que ira se abrir, utilize o script abaixo:
	```
	# Acessar diretorio do projeto
	cd Lab09/


	# Criar um arquivo com as credencias do Rancher
	cat <<EOF> rancher.cfg
	{"accessKey":"ACESS_KEY_DO_RANCHER","secretKey":"SECRET_KEY_DO_RANCHER,"url":"http://IP_DO_MASTER:8080/v2-beta/schemas","environment":"ID_DO_AMBIENTE"}
	EOF

	# Criar uma variavel para mapear o aquivo de credenciais
	CFG_RANCHER="rancher.cfg"


	# Comando do rancher para subir um novo projeto 	
	 /usr/local/bin/rancher -c $CFG_RANCHER  --file docker-compose.yml  up -d --stack "webserver-python" 

	# Comando do rancher para atualizar um projeto existente 
	# /usr/local/bin/rancher  -c $CFG_RANCHER  --file docker-compose-update.yml  up -d --stack $JOB_NAME --force-upgrade --pull --confirm-upgrade
   

	```
	* Os campos acima sao necessarias substituicoes:
		- ACESS_KEY_DO_RANCHER
		- SECRET_KEY_DO_RANCHER
		- IP_DO_MASTER
		- ID_DO_AMBIENTE - Valor pode ser pego na url do Rancher /env/XXXX/
	- Salve a configuracao e clique em **play**
		* **Os status/log pode ser visto clicando em no build #1 / Saida console**
	- Acesse o Rancher e verifique em **STACKS** se o projeto webserver-python esta disponivel

3. Atualizando a versao do projeto
	- Edite o projeto no Jenkins: wevserver-python e modifique o script conforme mostrado abaixo:
	```
	 # Comando do rancher para subir um novo projeto 	
	 #/usr/local/bin/rancher -c $CFG_RANCHER  --file docker-compose.yml  up -d --stack "webserver-python" 

	# Comando do rancher para atualizar um projeto existente 
	 /usr/local/bin/rancher  -c $CFG_RANCHER  --file docker-compose-update.yml  up -d --stack $JOB_NAME --force-upgrade --pull --confirm-upgrade

	```
	* Comente a primeira linha (subir novo projeto) e descomente a linha abaixo (atualizar o projeto)
	- Clique em play e aguarde a atualizacao
	- Acesse o Rancher e veja se o projeto esta atualizado			
-------------------------------------------------------------------------------
# Lab10  - Configurando proxy no RancherOS

ros config set rancher.docker.environment '[http_proxy=, https_proxy=]'

ros config set rancher.system_docker.environment '[http_proxy=, https_proxy=]'

system-docker restart docker


------------------------
-------------------------------------------------------------------------------------------------------



