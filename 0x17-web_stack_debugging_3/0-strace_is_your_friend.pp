# automated puppet fix (to find out why Apache is returning a 500 error)

exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wordpress/wp-settings.php',
  provider => shell,
}
