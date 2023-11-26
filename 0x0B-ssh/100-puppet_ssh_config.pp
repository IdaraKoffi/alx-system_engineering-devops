#!/usr/bin/env bash
# Changes SSH config file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"
	
	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}
