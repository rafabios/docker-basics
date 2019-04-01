#!/bin/bash

DOCKER_COMMAND=$(docker pull $image)

for image  in  $(cat docker_image_list.txt);
 do    docker pull $image
done




