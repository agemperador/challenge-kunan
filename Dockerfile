FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "-m", "flask", "--app", "main.py", "run", "--host", "0.0.0.0" ]