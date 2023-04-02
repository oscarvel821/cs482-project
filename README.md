In this tutorial, you will learn how to:

Create a Dockerfile file describing a simple Python container.
Build, run, and verify the functionality of a Django, Flask, or General Python app.
Debug the app running in a container.
Prerequisites
Install Docker on your machine and add it to the system path.

On Linux, you should also enable Docker CLI for the non-root user account that will be used to run VS Code.

The Docker extension. To install the extension, open the Extensions view (Ctrl+Shift+X), search for docker to filter results and select Docker extension authored by Microsoft.

Select Docker extension

Create a Python project
If you don't have a Python project already, follow the tutorial Getting started with Python.

Note: If you want to containerize a complete Django or Flask web app, you can start with one of the following samples:

python-sample-vscode-django-tutorial, which is the result of following the Django Tutorial

python-sample-vscode-flask-tutorial, which is the result of following the Flask Tutorial

Note: For this tutorial, be sure to use the tutorial branch of the sample repos.

After verifying your app runs properly, you can now containerize your application.

Add Docker files to the project
Open the project folder in VS Code.

Open the Command Palette (Ctrl+Shift+P) and choose Docker: Add Docker Files to Workspace...:

Add Dockerfile to a Python project

When prompted for the app type, select Python: Django, Python: Flask, or Python: General as the app type. For this tutorial, we'll focus on the Python: General case, but will also include notes for Django and Flask.

Enter the relative path to the app's entry point. This excludes the workspace folder you start from. If you created a python app with hello.py according to the Getting Started with Python tutorial, choose that.

Django: Choose manage.py (root folder) or subfolder_name/manage.py. See the official Django documentation.

Flask: Choose the path to where you create your Flask instance. See the official Flask documentation.

Tip: You may also enter the path to a folder name as long as this folder includes a __main__.py file.

Select the port number. We recommend selecting port 1024 or above to mitigate security concerns from running as a root user. Any unused will port, but Django and Flask use standard default ports.

Django: The default port 8000.

Flask: The default port is 5000.

When prompted to include Docker Compose, select No if you do not want a Docker Compose file. If you select Yes, you will need to verify the path to your wsgi.py file in the Dockerfile to run the Compose Up command successfully. Compose is typically used when running multiple containers at once.

With all this information, the Docker extension creates the following files:

A Dockerfile. To learn more about IntelliSense in this file, refer to the overview.

A .dockerignore file to reduce the image size by excluding files and folders that aren't needed such as .git, .vscode, and __pycache__.

If you're using Docker Compose, a docker-compose.yml and docker-compose.debug.yml file.

If one does not already exist, a requirements.txt file for capturing all app dependencies.

<<<<<<< HEAD
Important Note: To use our setup, the Python framework (Django/Flask) and Gunicorn must be included in the requirements.txt file. If the virtual environment/host machine already has these prerequisites installed and is supposed to be identical to the container environment, ensure app dependencies are ported over by running pip freeze > requirements.txt in the terminal. This will overwrite your current requirements.txt file.
=======
Important Note: To use our setup, the Python framework (Django/Flask) and Gunicorn must be included in the requirements.txt file. If the virtual environment/host machine already has these prerequisites installed and is supposed to be identical to the container environment, ensure app dependencies are ported over by running pip freeze > requirements.txt in the terminal. This will overwrite your current requirements.txt file.
>>>>>>> 0369f9185ea65f39206f590d4d723615789518ff
