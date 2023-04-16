# Fonts Directory
This directory contains fonts for the Issue Tracking System Django project. Fonts are served directly to the client without modification by the server.

## #Directory Structure
The fonts directory is organized into subdirectories for each type of font. The current directory structure is as follows:

`static/`
    `fonts/`
        `sans-serif/`
            `OpenSans-Regular.ttf`
            `OpenSans-Bold.ttf`
        `serif/`
            `TimesNewRoman-Regular.ttf`
            `TimesNewRoman-Bold.ttf`

- `sans-serif/`: Contains sans-serif fonts used throughout the project.
- `serif/`: Contains serif fonts used throughout the project.
## Usage
To use fonts in your CSS, you can use the `@font-face` rule. For example, to include the `OpenSans-Regular.ttf` font in your CSS, you would use the following code:

    @font-face {
    font-family: 'Open Sans';
    src: url('{% static 'fonts/sans-serif/OpenSans-Regular.ttf' %}');
}


This assumes that the `OpenSans-Regular.ttf` file is located in the sans-serif subdirectory of the fonts directory.

## Contributing
If you need to add or modify fonts for the project, please follow these guidelines:,

Create a new subdirectory for the type of font you are adding (e.g. `sans-serif/` `serif/`, etc.).

<b>Note:</b>

- Use descriptive names for your font files and directories.
- Ensure that you have the appropriate licenses or permissions to use the fonts.
- Test your changes thoroughly to ensure that they do not break existing functionality.
- Submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [`LICENSE`](`mit lincences`) file for details.