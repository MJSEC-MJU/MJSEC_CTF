FROM debian:bullseye-slim
MAINTAINER "201820903@kku.or.kr"


# RUN : 해당 명령어 실행, 필요한 패키지를 설치 
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# COPY: 현재 경로(.)에 존재하는 파일들을 이미지 /app 경로에 모두 추가 
COPY ./HelloCTF/file /app
COPY ./HelloCTF/docker-entrypoint.sh /app/docker-entrypoint.sh
COPY ./HelloCTF/flag/flag /flag
# WORKDIR: 작업 디렉토리 변경. 셸 cd /app 과 같은 기능 

# RUN: 명령어 실행. 복사된 requirements.txt 파일로 pip로 필요 라이브러리 설치 
RUN pip install -r /app/require/requirements.txt

# EXPOSE: 컨테이너 실행 시 노출될 포트
EXPOSE 5000

# ENTRYPOINT: 컨테이너 시작 시 기본으로 실행되는 명령어 
ENTRYPOINT [ "/bin/sh" ]

# CMD: 컨테이너 시작 시 실행되는 명령어로 위 ENTRYPOINT 명령어 뒤 인자로 실행하게 된다. 
# 결국 python app.py 명령어 실행 
CMD [ "/app/docker-entrypoint.sh" ]

