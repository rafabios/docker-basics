# Lab00 - Preparando o ambiente 

1. Criar duas maquinas virtuais, os sistemas operacionais podem ser:
	- Ubuntu
	- RancherOS
	- Debian

2. Baixar o docker-ce nas VMs: Worker e Master:
	- [Download Docker]()

3. Baixar imagens do docker na VM Worker:
	- Utilizar o script localizado no Lab00 - [download_docker_images.sh](download_docker_images.sh)
	- Copiar o arquivo de nomes de imagens Lab00 - [docker_image_list.txt](docker_image_list.txt)
	 * Executar o comando ``` bash download_docker_images.sh ```

4. Criar uma conta no Dockerhub
	- Crie uma conta e conecte a sua maquina virtual WORKER:
		* `docker login`
		