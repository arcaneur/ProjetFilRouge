from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(instance_name='app', port=5000):
    app = Flask(__name__)
    
    # Configuration de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Frantz:apache2@mariadb/SalleFetes'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'cle_secrete_a_changer'
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Enregistrer les blueprints
    from .routes import main
    app.register_blueprint(main)
    
    return app
