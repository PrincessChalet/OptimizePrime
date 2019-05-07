# OptimizePrime

In order to use our program make sure that you have Python 3.7.2 installed. Our team used pip 19.0.2 as our package manager and the following instruction will use pip commands.

NOTES
- You may download a specific python version from https://www.python.org/downloads/
	- pip will be installed along with the python download
- If you have multiple versions of python installed on your system, replace `python` with `python3`.
- All of the following commands are executed in a powershell terminal. Changes may be necessary for other terminal types.


1. Once you confirm that python and pip are installed on your system, install virtualenv using the line\
	`pip install virtualenv`
2. Next create your virtual environment inside the folder where you add this project using the line\
	`python -m venv environmentName`

	 An example of our file hierarchy
		
		|-- projectsRoot
			|--degreePlan                    
				|-- (create virtual environment here)
				|-- (place the github OptimizePrime folder here)

3. Next run the virtual environment using the line\
		  `./Scripts/activate`
4. Next enter the directory OptimizePrime using `cd OptimizePrime` and then the src directory using `cd src`
5. Next install the following packages using pip
```
	pip install django             (our project was written using django 2.1.7)
      	pip install psycopg2           (our project used 2.7.7) 
      	pip install bootstrap4         (our project used 0.1.0)
      	pip install jinja2	       (our project used 2.10)
```
6. Once everything is installed and making sure that you are in the src directory run the following two lines
```
	python manage.py makemigrations
	python manage.py migrate
```
7. Lastly, you can launch the server using the line\
      `python manage.py runserver`


