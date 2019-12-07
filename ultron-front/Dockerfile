# base image
FROM node:alpine

# set working directory
WORKDIR /usr/app

COPY package.json ./

# install and cache app dependencies
RUN yarn

COPY . .

RUN yarn run build