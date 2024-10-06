FROM python:3.10-slim-buster

# ENV
ENV user mjsec
ENV port 8000

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    wget \
    curl \
    unzip \
    gnupg2 \
    software-properties-common

# Chrome 및 ChromeDriver 설치
RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable

RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -N https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver

# Set up user and application
RUN adduser --disabled-password --gecos '' $user
ADD ./deploy /app
WORKDIR /app
RUN pip3 install -r requirements.txt

# Set permissions
RUN chown root:$user /app/flag.txt

# Switch to non-root user
USER $user
EXPOSE $port

# Start the application
ENTRYPOINT ["python3"]
CMD ["app.py"]
