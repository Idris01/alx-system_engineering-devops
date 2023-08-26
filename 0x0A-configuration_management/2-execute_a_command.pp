# A manifest file that kill a process "killmenow

exec { 'teminate_killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'], # location of system executables
  onlyif  => 'pgrep -f killmenow', # the process must exist
}
