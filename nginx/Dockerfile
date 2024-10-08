FROM nginx:1.23-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
#COPY apple-app-site-association.json /etc/nginx/conf.d
#COPY assetlinks.json /etc/nginx/conf.d