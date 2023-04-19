Images Directory
This directory contains images for the Issue Tracking System Django project. Images are served directly to the client without modification by the server.

Directory Structure
The `images` directory is organized into subdirectories for each type of image. The current directory structure is as follows:

`static/`
    `images/`
        `icons/`
            `icon1.png`
            `icon2.png`
        `logos/`
            `logo1.png`
            `logo2.png`

- icons/: Contains icons used throughout the project.
- logos/: Contains logos used throughout the project.
## Usage
To use images in your Django templates, you can use the <img> tag. For example, to include the `logo1.png` file in your `base.html` template, you would use the following code:

`<img src="{% static 'images/logos/logo1.png' %}" alt="Logo 1">`

This assumes that the `logo1.png` file is located in the `logos/` subdirectory of the images directory.

## Contributing
If you need to add or modify images for the project, please follow these guidelines:

- Create a new subdirectory for the type of image you are adding (e.g. 
`icons/`, `logos/`, etc.).

Use descriptive names for your image files and directories.
