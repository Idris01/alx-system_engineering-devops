# install flask version 2.1.0

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask_v2.1.0':
  command => 'pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}
