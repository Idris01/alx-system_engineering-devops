# configure a new ubuntu server to install with nginx and set custom header

class nginx_installation {
    package { 'nginx':
	ensure => 'installed',
    }
   
    file { '/etc/nginx/conf.d/global_headers.conf':
	ensure => 'file',
	owner => 'root',
	group => 'root',
        require => Package['nginx'],
	content => "add_header X-Served-By \$HOSTNAME;",
    }
   
    service { 'nginx':
	ensure => 'running',
	enable => true,
	require => File['/etc/nginx/conf.d/global_headers.conf'],
    }
}

include nginx_installation
