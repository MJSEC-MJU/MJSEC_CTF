# PHP와 Apache를 포함한 이미지 사용
FROM php:7.4-apache

# 프로젝트 파일 복사
COPY index.php /var/www/html/
COPY flag.php /var/www/html/

# Apache 설정에서 mod_rewrite 활성화
RUN a2enmod rewrite

# 권한 설정
RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html

# .htaccess 파일 복사
COPY .htaccess /var/www/html/

# Apache 포트 80 노출
EXPOSE 80
