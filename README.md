# Zoho Contact App
Sample app developed for Zoho test

----

## Instructions to run
1. Clone the repo using any of the following commands
   - `git clone https://github.com/abhinand-c/ZohoContactApp.git`
   - `git clone git@github.com:abhinand-c/ZohoContactApp.git`
   - `gh repo clone abhinand-c/ZohoContactApp`
2. Paste the dummy .env file below to your cloned repo
3. Set values in .env file, as provided by admin or for development set demo values
3. Setup & activate virtual python environment  (Refer: [Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or [Python venv](https://docs.python.org/3/tutorial/venv.html))
4. Collect static files `python manage.py collectstatic`
5. Install requirements `pip install -r requirements.txt`
6. Run migrations with `python manage.py migrate`
7. Run server using `python manage.py runserver 80`



#### Dummy .env file

Copy the code below or use [env.sample](env.sample) file and save it in your cloned repo as `.env` file, also add the change values as needed.

```

DEBUG=True
SECRET_KEY=dummysecretkey12312412

```