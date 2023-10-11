exec {'debug':
  command   => '/bin/bash -c "sed -i s/phpp/php/g /var/www/html/wp-settings.php && service apache2 restart"',
  provider  => 'shell',
  logoutput => true,
}
