FROM python:3.9-slim
WORKDIR /home/crawler/
ADD . .
#RUN pip install --upgrade pip

RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "main.py" ]
CMD [ "--domain", "https://www.lipsum.com", "--task", "50" ]