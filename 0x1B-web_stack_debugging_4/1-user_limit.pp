# configure holberton user to login without error

exec {'configure1':
  provider => 'shell',
  cwd      => '/etc/security',
  command  => 'sudo sed -i s/"holberton hard nofile .*"/"holberton hard nofile 200/" limits.conf'
}

exec {'configure2':
  provider => 'shell',
  cwd      => '/etc/security',
  command  => 'sudo sed -i s/"holberton soft nofile .*"/"holberton soft nofile 200/" limits.conf'
}
