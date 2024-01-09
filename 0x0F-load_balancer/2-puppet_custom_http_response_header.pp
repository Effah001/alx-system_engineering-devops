# Nginx Installation and Configuration

# Package Management
package { 'nginx':
  ensure => 'installed',
}

# Set the localhost default page
file { '/var/www/html/index.html':
  content => 'Hello World!',
  ensure  => file,
}

# Add a redirect to the Nginx configuration
file_line { 'add_redirect':
  path  => '/etc/nginx/sites-available/default',
  line  => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=_S7WEVLbQ-Y permanent;',
}

# Create a default 404 error page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page",
  ensure  => file,
}

# Configure Nginx with custom error page
file_line { 'custom_error_page':
  path  => '/etc/nginx/sites-available/default',
  line  => "error_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t};",
}

# Modify the default location block to add a custom header
file_line { 'add_custom_header':
  path  => '/etc/nginx/sites-available/default',
  line  => 'location / {',
}

file_line { 'custom_header_content':
  path  => '/etc/nginx/sites-available/default',
  line  => '    add_header X-Served-By $hostname;',
}

# UFW Installation and Configuration
package { 'ufw':
  ensure => 'installed',
}

exec { 'allow_nginx_http':
  command => 'ufw allow "Nginx HTTP"',
  unless  => 'ufw status | grep "Nginx HTTP" | grep ALLOW',
  require => Package['ufw'],
}

# Nginx Restart
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
  require   => Package['nginx'],
}

