#connecting to a server using puppet

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config':
  path    => '/bin/'
}
