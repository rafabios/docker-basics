# Lab0

- Instalar o Ubuntu 16.04 (VirtualBox);
- Instalar o docker-ce 19.03
- Baixar as imagens:
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

- Criar duas vms:
	* Master.vdi
	* Worker.vdi


- Criar uma imagem com o python SImple WebServer: Pegando valores da variavel de ambiente

-------------------------------------------------------------------------------------------------------

# Lab01


-------------------------------------------------------------------------------------------------------
# Lab02

- Baixando imagens:
	Vamos baixar a imagem do python para criamos um webserver:
		```docker pull python:latest```
- Validando a imagem baixada:
	```docker run -i -t --rm python:latest /bin/bash```
		* run: Comando para informar ao docker que a imagem necessita ser executada
		* -i -t: Modo interativo/tty, utilizamos para poder acessar uma sessao de console no container
		* --rm: Apagar container e volumes apos execucao
		* python:latest : Imagem e tag de versao a ser rodado
		* /bin/bash : comando a ser executado no container



-------------------------------------------------------------------------------------------------------
# Lab03

- Como checar espaco em disco?
	- Verificar o arquivo de logs do docker: ```/var/log/daemon```  Em caso de problema no docker o arquivo cresce demais
	- Verificar os logs dos containers: ```du -h /var/lib/docker/containers/*/*-json.log```    Correspondente ao docker logs <container>
	- Verificar tamanho dos containes: 
		```docker system df```   Mostra tamanho de imagnes, containers e volumes
		```docker ps --size```   Mostra tamanho dos containers, individualmente

- Como apagar recursos nao usados:
	- Apagar arquivos de log:
		```echo "" > Nome_do_Arquivo```    Utilizar o echo ou truncate para apagar aquivos, se utilizar o rm, o arquivo se apagado e o espaco nao sera liberado;
		Exemplos:
			```
			echo "" > /var/log/daemon		
			echo "" >  /var/lib/docker/containers/f071f64633/f071f64c98dbe6a62633-json.log 
			```

	- Apagar imagens, volumes e containers nao utilizados pelo docker:
		```docker system prune```   Limpa diversos recursos do docker  
		```docker volume prune```   Limpa volumes nao utilizados do docker
		```docker image prune```    Limpa imagens nao utilizadas pelo docker
		```docker rmi <nome_da_imagem>```      Exclui uma imagem especifica
		```docker rm <nome_do_container>```    Exclui uma container espeficico


-------------------------------------------------------------------------------------------------------
# Lab04







-------------------------------------------------------------------------------------------------------
# Lab05

-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------



