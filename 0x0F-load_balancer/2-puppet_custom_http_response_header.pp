# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Define the custom header configuration in Nginx
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "# Custom HTTP header configuration\nserver {\n  listen 80;\n  server_name _;\n  location / {\n    add_header X-Served-By $hostname;\n    # Other configuration options\n  }\n}\n",
  notify  => Service['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
  require => File['/etc/nginx/sites-available/custom_header'],
}

# Reload Nginx to apply the changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/custom_header'],
}

# Notify when the custom header is applied
notify { 'Custom header applied':
  message => 'The custom X-Served-By header has been configured on this server.',
}
