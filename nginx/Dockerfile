FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx/django-nginx.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/uploadsize.conf /etc/nginx/conf.d/uploadsize.conf