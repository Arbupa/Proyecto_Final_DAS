FROM python:3.7-alpine

COPY requirements.txt /contenedor_cinco
WORKDIR /contenedor_cinco
RUN pip install --upgrade pip
#COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "app.py"]

