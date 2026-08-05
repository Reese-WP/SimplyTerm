
# Simply Term

A lightweight, customizable terminal user interface framework built in Python for creating interactive command-line applications with full-screen layouts, keyboard input, and dynamic rendering focused on simplicity

Simply Term dose not need any dependancys as it only uses defalt python packages.
Simply Term is not yet on PyPI so this is the only place to get it.

[![GitHub release](https://img.shields.io/github/v/release/Reese-WP/SimplyTerm.svg)](https://github.com/Reese-WP/SimplyTerm/releases)
[![GitHub license](https://img.shields.io/github/license/Reese-WP/SimplyTerm.svg)](https://github.com/Reese-WP/SimplyTerm/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/Reese-WP/SimplyTerm.svg)](https://github.com/Reese-WP/SimplyTerm/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)


[![GitHub watchers](https://img.shields.io/github/watchers/Reese-WP/SimplyTerm.svg?style=social&label=Watch)](https://github.com/Reese-WP/SimplyTerm/watchers)
[![GitHub forks](https://img.shields.io/github/forks/Reese-WP/SimplyTerm.svg?style=social&label=Fork)](https://github.com/Reese-WP/SimplyTerm/network)
[![GitHub stars](https://img.shields.io/github/stars/Reese-WP/SimplyTerm.svg?style=social&label=Star)](https://github.com/Reese-WP/SimplyTerm/stargazers)

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB.svg)](https://www.python.org/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)](https://github.com/Reese-WP/SimplyTerm)
## Features

- Full terminal UI
- Dynamic sized boxes
- Text rendering with centering, and text cut of
- keyboard input
- Screen Buffer rendering for preformance


## Roadmap

- features for 1.1.0\
☐ Color support\
☐ text wrap / crawl\
☐ "pixel" based displays\
☐ buttons / cursor support for selecting options

- features for 1.2.0\
☐ Sub screens / feilds

## Usage/Examples

```python
from simplyterm import *

#start up the GUI, clearing screen and formating things
enter()
try:
    #make the screen and buffer system
    screen = Screen()
    while True:
        #do stuff here
        screen.push() #update the screen from the buffer    
finally:
    #make the users terminal useable again, even on a crash
    exit()
```


## Authors

- [@Reese-WP](https://www.github.com/Reese-WP)


## Contributers

- none yet 🥲


## Contributing

Contributions are always welcome!

To contribute, simply make a PR. Nothing fancy to it, just try and stick with the same coding conventions I use and keep it readable/commented for others. If I think the change is good, I'll add it, and add you to the contributors.
