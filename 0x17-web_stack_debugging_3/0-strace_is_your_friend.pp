#this file is to solve the problem of the server

$file = '/var/www/html/wordpress/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file}",
  path => ['/bin', '/usr/bin']
}
