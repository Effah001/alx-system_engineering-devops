#replacing a line in a file using puppet

$file_to_edit = '/var/www/html/wp-settings.php'

# Replace line containing "phpp" with "php"
exec { 'replace_line':
  command => "sed -i 's#phpp#php#g' ${file_to_edit}",
  path    => ['/bin','/usr/bin'],
  onlyif  => "grep -q 'phpp' ${file_to_edit}",  # Check if the line needs replacement
  unless  => "grep -q 'php' ${file_to_edit}",   # Check if the replacement has already been made
}
