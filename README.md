![Mac](https://img.shields.io/badge/OS X-Untested-lightgrey.svg)
![Windows](https://img.shields.io/badge/Windows-Untested-brightgreen.svg)
![Linux](https://img.shields.io/badge/Linux-Untested-lightgrey.svg)
![Version](https://img.shields.io/badge/Version-1.0.0/dev-brightgreen.svg)
![Development](https://img.shields.io/badge/Development-busy-brightgreen.svg)
![Repo size](https://reposs.herokuapp.com/?path=riptide00/gitupdate)

# Github Auto-Update (and installation...)

## Installation

	> pip install -r requirements.txt

## Description

First of all, for this system to work you need 3 things:
	1. Add 'requests' to the requirements.txt of your project
	2. A github repository
	3. A standard for 'Readme' files

## Use 

The standard
-------------

I use this as a head for my readme's:

![Mac](https://img.shields.io/badge/OS X-Untested-lightgrey.svg)
![Windows](https://img.shields.io/badge/Windows-Untested-lightgrey.svg)
![Linux](https://img.shields.io/badge/Linux-Untested-lightgrey.svg)
![Version](https://img.shields.io/badge/Version-1.0.0/dev-brightgreen.svg)
![Development](https://img.shields.io/badge/Development-halted-lightgrey.svg)
![Repo size](https://reposs.herokuapp.com/?path=)

See the version shield? That's what i use to detect versions.
So now we now that how do we proceed.

Ok configuring (atm) is a b*atch so here we go:
	- Rename 'gitupdate.py' to something pretty.
	  (this is where you start your program from)
	- Complete the 'def _start_app()' to your liking.
	- Configure 'config.py'.
		- master_url > Point this to the raw Readme usually,
		              'https://raw.githubusercontent.com/USERNAME/REPOSITORY/master/README.md'.
		- zip_url > Point to a zip of your project usually, 
		           'https://github.com/USERNAME/REPOSITORY/zipball/master'.

## Todo

- [ ] Cleanup after update.