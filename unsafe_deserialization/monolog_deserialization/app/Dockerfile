FROM php:7.4-cli

WORKDIR /usr/src/myapp

RUN php -r "copy('https://getcomposer.org/installer', '/composer-setup.php');"
RUN php -r "if (hash_file('sha384', '/composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php /composer-setup.php 
RUN php -r "unlink('/composer-setup.php');" 
RUN mv /usr/src/myapp/composer.phar /usr/bin/composer

COPY . /usr/src/myapp

RUN composer install

CMD [ "php", "-S", "0.0.0.0:8001" ]
