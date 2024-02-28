#!/bin/bash
IMAGE=test

docker run --rm -it\
 -v ./md_ws:/root/md_ws/\
 --name test\
 $IMAGE bash
