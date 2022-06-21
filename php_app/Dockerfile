FROM php:7.3-apache
WORKDIR /php
COPY . .
RUN docker-php-ext-install pdo pdo_mysql mysqli
RUN chmod +x ./php_app/artisan
CMD php artisan serve --host=0.0.0.0 --port=8000
EXPOSE 8000

