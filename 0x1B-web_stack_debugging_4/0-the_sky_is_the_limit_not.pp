# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
}

# Restart Nginx
service { 'nginx-restart':
  ensure => 'running',
  enable => 'true',
  subscribe => Exec['fix--for-nginx'],
}

