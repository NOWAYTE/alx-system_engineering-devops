# Fixe apache error

exec { 'Fix typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.phpp /var/www/html/wp-includes/class-wp-locale.php',
  onlyif  => 'test -f /var/www/html/wp-includes/class-wp-locale.phpp',
}

