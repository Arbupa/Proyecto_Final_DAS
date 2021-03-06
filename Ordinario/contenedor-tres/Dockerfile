FROM python:3.7-alpine

#RUN mkdir /new
WORKDIR /contenedor-tres
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirementstwo.txt
#EXPOSE 3306
CMD ["python3","puerto.py"]