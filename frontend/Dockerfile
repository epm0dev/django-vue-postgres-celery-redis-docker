FROM node:15.4.0-alpine3.10

ENV PATH="/scripts:${PATH}"

RUN mkdir /app
WORKDIR /app

COPY package*.json /app/
RUN npm install

COPY . /app/

COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN adduser -D user
USER user

CMD ["entrypoint.sh"]