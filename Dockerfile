FROM python:3.7-slim-bookworm

RUN apt-get -y update
RUN apt-get -y install python3-dev python3-setuptools libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev

# Set the work directory
WORKDIR /usr/app

# RUN easy_install Pillow
# RUN pip install carto-print

RUN pip install carto-print

COPY . .

# Start the service
CMD ["bash", "./start-service"]
