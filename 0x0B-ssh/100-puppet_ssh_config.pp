#client configuration file

	file_line { 'ssh_config_file no password':
		path    => '/etc/ssh/ssh_config',
		line    => 'passwordAuthentication no',
		ensure  => present,
	}

	file_line { 'ssh_config_file':
		path   => '/etc/ssh/ssh_config',
		line   => 'IdentityFile ~/.ssh/school',
		ensure => present,
	}

