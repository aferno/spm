FROM ubuntu:16.04

# Update OS
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade

# Install Python
RUN apt-get install -y python3-all-dev python3-pip
RUN echo 'alias python="python3"' >> ~/.bashrc

# Add requirements.txt
ADD app /webapp

# Set the default directory for our environment
ENV HOME /webapp
WORKDIR /webapp

# Install uwsgi Python web server
RUN pip3 install uwsgi
# Install app requirements
RUN pip3 install -r requirements.txt

# Create app directory
#ADD /home/philip/blog/web/project /webapp

# Expose port 8000 for uwsgi
EXPOSE 8000
