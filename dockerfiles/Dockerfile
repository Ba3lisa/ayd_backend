FROM ubuntu:18.04

# Build tools and essential libraries
RUN apt-get update -yqq && apt-get install --yes --no-install-recommends build-essential \
    python3-pip python3-dev

# Upgrade pip
RUN apt-get update -yqq && apt install python3-pip -y
RUN python3 -m pip install --upgrade pip

# Symlink python3 -> python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Python requirements
ADD ./dockerfiles/requirements.txt /
RUN pip3 install -r /requirements.txt

# Init working dir
RUN mkdir /backend

# ENV VARS
ENV DJANGO_PORT=5000
ENV WORKING_DIR=/backend

# Init startup script
COPY ./dockerfiles/startup.sh /usr/src/startup.sh
ENV STARTUP_SH=/usr/src/startup.sh
RUN chmod +x $STARTUP_SH

CMD $STARTUP_SH
