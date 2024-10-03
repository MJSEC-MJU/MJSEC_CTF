#!/bin/bash

tag=helloctf:0.1

# 현재 실행 중인 컨테이너 중에서 해당 이미지를 기반으로 실행된 모든 컨테이너 삭제
sudo docker rm -f $(sudo docker ps -a -q --filter ancestor=$tag)

# 이미지를 삭제
sudo docker rmi $tag

# Docker 이미지 빌드
sudo docker build -f ./HelloCTF/Dockerfile -t $tag .

# Docker 컨테이너 실행 (메모리 제한 1GB, 포트 매핑 5001:5000)
sudo docker run --memory="1G" --name helloctf -d -p 5001:5000 $tag
