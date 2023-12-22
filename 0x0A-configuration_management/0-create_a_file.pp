#create a file school in temp

file { '/tmp/school':
  ensure    => file,
  content   => 'I love pup',
  mode      => '0744',
  owner     => 'www-data',
  group     => 'www-data',
}
