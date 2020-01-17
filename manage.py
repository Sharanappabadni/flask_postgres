import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_script import Server
from app import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

server = Server(host='http://localhost',
                port=5432)
manager.add_command("runserver", server)

if __name__ == "__main__":
    manager.run()
