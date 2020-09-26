from app import create_app,db
from flask_script import Manager,Server
from app.models import User


# Creating app instance
# app = create_app('test')
app=create_app('development')

manager=Manager(app)
manager.add_command('server',Server)


#use the manager shell decorator to access the shell on the command line
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
    
@manager.command
def test():
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
if __name__=='__main__':
    manager.run()