
from companyblog import app, db

with app.app_context():
    connection = db.engine.connect()
    print(connection)

if __name__=='__main__':
    app.run(debug=True)