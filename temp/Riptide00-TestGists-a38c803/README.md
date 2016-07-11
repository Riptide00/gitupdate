![Mac](https://img.shields.io/badge/OS X-Untested-lightgrey.svg)
![Windows](https://img.shields.io/badge/Windows-Compatible-brightgreen.svg)
![Linux](https://img.shields.io/badge/Linux-Untested-lightgrey.svg)
![Version](https://img.shields.io/badge/Version-1.0.0/dev-brightgreen.svg)
![Development](https://img.shields.io/badge/Development-busy-brightgreen.svg)
![Repo size](https://reposs.herokuapp.com/?path=riptide00/testgists)

# Test Gists

## Installation

*By default not needed, only if any respective options are enabled*

	> pip install -r requirements.txt

Edit the 'config.py' file.

## Use

### File structure

If you want to use the automated testing features you will need to adhere to a certain naming convention.

	<Python_gists>
	├── <gista>
	│   ├── <gista>.py
	│   └── test.py
	└── <gistb>
	    ├── <gistb>.py
	    └── test.py

The 'Python_gists' location is configurable in the config.py.
The name of the directory should be the same as the name of the snippet.
a 'test.py' script should be present for well... testing the snippet, an example is provided. 

### command(-s)

	> py testgists.py

## Todo

- [ ] Find todos (it won't be hard)

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

v1.0.0/dev: Development build.

# License

[__License__](/LICENSE.txt)