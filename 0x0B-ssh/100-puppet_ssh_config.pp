#!/usr/bin/env bash
# Changes SSH config file

file { 'ect/ssh/ssh_cofig':
	ensure => present,

content =>"
	
	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}
