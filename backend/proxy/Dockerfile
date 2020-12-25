FROM nginxinc/nginx-unprivileged:1.19.6-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d

USER root

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

USER nginx