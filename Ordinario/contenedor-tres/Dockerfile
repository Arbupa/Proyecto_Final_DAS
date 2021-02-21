FROM python:3.7-alpine

RUN pip install --upgrade pip
RUN pip install -r requirementstwo.txt
RUN mkdir /new
WORKDIR /new
COPY . .
#COPY ./contenedor_tres /new
# COPY ./contenedor_tres/scraper.py /new
# COPY ./contenedor_tres/interface.py /new
# COPY ./contenedor_tres/puerto.py /new
# COPY ./contenedor_tres/requirementstwo.txt /new
# COPY ./contenedor_tres/dbinteraction.py /new
#COPY contenedor_tres/ /new/
#COPY /contenedor_cinco/requirements.txt .
#RUN pip freeze > puerto.py
#WORKDIR /new
#CMD [ "python","/contenedor-tres/puerto.py" ]