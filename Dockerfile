# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /home/app

RUN apt-get update
RUN apt-get install net-tools

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080:5000

COPY . .

# ENTRYPOINT [ "python3" ]
# CMD [ "main.py" ]

CMD [ "python3", "main.py" ]