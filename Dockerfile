FROM python:3.8

RUN pip install filelock==3.0.12
RUN pip install pytest==6.2.5
RUN pip install pytest-forked==1.3.0
RUN pip install pytest-html==3.1.1
RUN pip install pytest-metadata==1.11.0
RUN pip install pytest-xdist==2.2.1
RUN pip install selenium==3.141.0
RUN pip install urllib3==1.26.5
RUN pip install webdriver-manager==3.5.2

RUN mkdir -p /home/app

COPY . /home/app

EXPOSE 6969
CMD ["pip", "list"]