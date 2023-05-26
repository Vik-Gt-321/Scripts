#!/bin/bash

var=$(gsettings get org.gnome.settings-daemon.plugins.color night-light-enabled)
echo $var
night () {
	echo "inside function"
	if $1 == true;
	then 
		gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled false
	
	else
		gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true
	
	fi
}

night $var
