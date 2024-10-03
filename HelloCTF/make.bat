set tag=helloctf:0.1
powershell "docker rm -f $(docker ps -a -q --filter ancestor=%tag%)"
docker rmi %tag%
docker build -f ./HelloCTF/Dockerfile -t %tag% .
docker run --memory="1G" --name helloctf -d -p 5001:5000 %tag%