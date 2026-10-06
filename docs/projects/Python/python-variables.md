# Python Variables

In python, you can use variables to store your data to be reused in multiple places in your code. 

## Table Of Contents



## Quickstart

1. - Make sure you have the latest stable python installed on your system. In the case of linux it should already be isntalled. On Windows, go to python.org and install the latest, stable version.

2. Make sure you select "Add python.exe to (envrionment variable) PATH" (if you forget this step, see the section on environment variables to correct it).

3. - once it finnishes installation, you should now be able to run python from the command prompt by typing "python" in the powershell window.

## Environment variables

In windows, environment variables are dynamic, named, text values that store system and application configuration settings outside of code and scripts. They are esentially a name (for example USERNAME) mapped to a value (for example "Mary"). This name can then be used by the OS and other programs to act as shortcuts to dynamic paths such as %USERPROFILE% (which changes depending on the current user profile), the PATH variable, which is used to tell the command line where to find program executables and store configurations or secure keys without having them in the source files.

To make sure the command line can run python, you need to add its path to the PATH environment variables

1. in the windows search, type "environment variables" and click on "Edit the System Environment Variables"

2. On the bottom right of the popup window, click on the "Environment Variables" button. A new window will popup.

3. In the bottom section, under System variables, click on "Path" and then "Edit"

4. In the new window, click on New and then Browse to the folder where you installed Python, click on the folder and thn "OK"

5. Repeat the same steps for the "python/scripts" folder. This will allow you to run installed python scripts from the command line.

6. To test if it works, open a command line window and type python. The python parser should open.

## PIP

PIP stands for "Pip Installs Packages" and is the standard package manager for Python. With PIP you can install and manage any python applications, dependencies and other necessary software packages.

1. You can use PIP on the command line to install packages and requirements for your python projects. using the following command:

```bash
pip install packageName
```

2. You can also uninstall packages you no longer want or need by typing the follwoing:

```bash
pip uninstall packageName
```

3. If you want to see which packages are currently installed and what versions you use the command:

```bash
pip freeze
```
This will provide you with a list of package names and their installed versions

4. To avoid having to install packages one by one, you can create a requirements.txt from the freeze command to use to batch install packages:

```bash
pip freeze -r fileName.txt
```

5. You can then use that file to install all the packages in one go:

```bash
pip install -r fileName.txt
```

