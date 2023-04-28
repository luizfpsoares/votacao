FROM python:3

WORKDIR /opt/labsite

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm -f requirements.txt

COPY ./main.py .
COPY ./templates ./templates

CMD [ "python", "./main.py" ]
