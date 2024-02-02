Flask migrate :

flask db init
flask db migrate
flask db upgrade

and add to app.py

migrate = Migrate(app, db)
