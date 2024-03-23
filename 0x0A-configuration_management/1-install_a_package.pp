#install flask using pip3
exec { 'pip3 install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}

