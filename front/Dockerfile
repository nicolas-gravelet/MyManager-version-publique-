FROM node:14.16.0-alpine

WORKDIR /app

COPY package.json .
COPY yarn.lock .
RUN yarn install

COPY . .
ENV HOST 0.0.0.0
EXPOSE 8080
CMD [ "yarn", "run", "serve" ]