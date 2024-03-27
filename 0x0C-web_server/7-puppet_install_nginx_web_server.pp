# Setup nginx

package { 'nginx':
  ensure => installed,
}
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80;
    server_name _;
    
    location /redirect_me {
        return 301 https://example.com;
    }

    location / {
        return 200 "Hello World!\n";
    }
}',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

