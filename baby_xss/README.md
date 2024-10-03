# baby_XSS

## 서버 설치 단계
1. 시스템 패키지 업데이트 및 Docker 설치:
  ```sh
    sudo apt update
    sudo apt install docker.io
    sudo systemctl enable --now docker
    ```
2. 프로젝트 클론:
    ```sh
    git clone https://github.com/MJSEC-MJU/MJSEC_CTF.git
    cd baby_xss
    ```
3. 도커 컨데이터 빌드 및 실행
 ```sh
    sudo docker build -t my_express_app .  
    sudo docker run -d -p 3000:3000 -e FLAG="MJSEC{your_real_flag_here}" my_express_app
    ```