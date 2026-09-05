# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added
- Color and style support
- Tile class to store color and style information
- Screen.set_tile() to set the charecter and style of specific charecters at specific locations in the buffer

### Changed
- buffer and screen now store Tile objects rather that simple charecters, draw now uses Screen.set_tile() withought any formating or color (so it uses the screens current color and style) to draw boxes and text

### Fixed
- Screen.resize() now automaticaly calls on Screen.push()

## [0.1.0] - 2026-08-5

### Added

- Initial release.
- Basic terminal screen and buffer system.
- Keyboard input.
- Drawing utilities.
- `Tile` system.