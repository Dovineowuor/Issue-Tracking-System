# Static files directory.
This directory contains static files for the Issue Tracking System Django project. Static files include CSS, JavaScript, images, and other files that are served directly to the client without modification by the server.

## Directory Structure
The static directory is organized into subdirectories for each type of static file. The current directory structure is as follows:

`Code;`

`static/`
    `css/`
        `style.css`
    `js/`
        `script.js`
    `images/`
        `image.png`
    `fonts/`
        `font-file`
    
`css/`: Contains CSS files for styling the HTML templates.<br>
`js/` : Contains JavaScript files for client-side interactivity.<br>
## Usage
To use static files in your Django templates, you can use the 
`{% static %}` template tag. For example, to include the style.css file in your base.html template, you would use the following code:

`Code`
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
This assumes that the style.css file is located in the css subdirectory of the static directory.

## Contributing
If you need to add or modify static files for the project, please follow these guidelines:

Create a new subdirectory for the type of file you are adding (e.g. images/, fonts/, etc.).

Use descriptive names for your files and directories.

Minimize the size of your files by compressing images and minifying CSS and JavaScript.
Test your changes thoroughly to ensure that they do not break existing functionality.
Submit a pull request with your changes.
## License
This project is licensed under the MIT License - see the LICENSE file for details.