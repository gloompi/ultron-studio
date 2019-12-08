FROM node:alpine
WORKDIR /usr/app
RUN apk add --no-cache \
    autoconf \
    automake \
    bash \
    g++ \
    libc6-compat \
    libjpeg-turbo-dev \
    libpng-dev \
    make \
    nasm
RUN npm install --global gatsby-cli
COPY package.json ./
RUN yarn install && yarn cache clean
COPY . .
RUN yarn run build
CMD yarn run serve