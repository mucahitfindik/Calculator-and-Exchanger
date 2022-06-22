FROM php:7.3-apache
RUN docker-php-ext-install pdo_mysql
RUN a2enmod rewrite
ADD . /var/www
ADD ./public /var/www/html
WORKDIR /var/www
CMD php artisan serve --host=0.0.0.0 --port=8000
EXPOSE 8000