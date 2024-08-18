# Fixes Apache 500 error

exec { 'fix typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.phpp /var/www/html/wp-includes/class-wp-locale.php',
  path    => '/usr/local/bin/:/bin/'
}
