exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html//wp-setting.php; sudo service apache2 restart',
  path => ['/bin', '/usr/bin', '/usr/sbin']
}
