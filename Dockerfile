FROM node:16.15.1-alpine

RUN mkdir -p /code/

WORKDIR /code

COPY ./eventapp /code/
COPY ./eventproject /code/
COPY ./entrypoint.sh /code

RUN npm install
# RUN cd /code/apps/console_ui; npm run build; cd /code/apps/appstore_ui; npm run build

ENTRYPOINT ["sh", "entrypoint.sh"]

