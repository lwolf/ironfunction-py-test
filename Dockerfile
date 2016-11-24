FROM iron/python:3.5.1

MAINTAINER Sergii Nuzhdin <ipaq.lw@gmail.com>

WORKDIR /function

ADD . /function/

CMD python func.py

