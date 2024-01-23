from app.extensions import db
from app import create_app

app = create_app()

with app.app_context():
    #db.drop_all()
    db.create_all()
app.run(debug=True)