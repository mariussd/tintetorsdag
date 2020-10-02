FROM node AS build-frontend

WORKDIR /build

COPY package.json yarn.lock ./

RUN yarn

COPY public ./public
COPY src ./src

RUN yarn build

FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y nginx

COPY req.txt .

RUN pip install -r req.txt

COPY tintetorsdag ./tintetorsdag
COPY manage.py .

COPY --from=build-frontend /build/build /static

RUN python manage.py collectstatic && mv django-static /static/django-static

COPY nginx.conf /usr/share/nginx/nginx.conf
COPY entrypoint.sh .

CMD ["bash", "entrypoint.sh"]
