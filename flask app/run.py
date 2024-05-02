from flask_1 import app
from flask_1 import db

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    #it is true only if we run the script directly
