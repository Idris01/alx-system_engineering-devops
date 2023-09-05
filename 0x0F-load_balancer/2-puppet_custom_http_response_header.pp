class nginx_installation {
    package { 'nginx':
	ensure => 'installed',
    }

    file { '/etc/nginx/sites-available/default':
	ensure => 'file',
	owner => 'root',
	group => 'root',
	content => "

server {
    listen 80;
    server_name _;

    root /var/www/html;

    add_header X-Served-By $HOSTNAME;

    index index.html index.htm index.nginx-debian.html;

    location /redirect_me {
        return 301 http://www.idrisoft.tech;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
	root /usr/share/nginx/html;
	internal;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}
    ",
    }
    
    service { 'nginx':
	ensure => 'running',
	enable => true,
	subscribe => File['/etc/nginx/sites-available/default'],
    }
}

include nginx_installation
