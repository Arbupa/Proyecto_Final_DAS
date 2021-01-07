FROM python:3.7-alpine

COPY . /contenedor_tres
WORKDIR /contenedor_tres
RUN pip install --upgrade pip
#COPY /contenedor_cinco/requirements.txt .
RUN pip install -r requirementstwo.txt
#COPY . .
CMD ["python3","puerto.py"]