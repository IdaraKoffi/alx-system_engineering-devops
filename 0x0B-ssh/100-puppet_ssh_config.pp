#!/usr/bin/env bash
# using puppet to make changes SSH cofig file

file { 'ect/ssh/ssh_cofig':
	ensure => present,

content =>"
	
	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}
