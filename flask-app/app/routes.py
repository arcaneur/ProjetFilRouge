from flask import Blueprint, render_template, jsonify, request
from . import db
from .models import Contact
import socket

main = Blueprint('main', __name__)

@main.route('/')
def index():
    hostname = socket.gethostname()
    return render_template('index.html', hostname=hostname)

@main.route('/health')
def health():
    return jsonify({"status": "healthy", "host": socket.gethostname()})

@main.route('/api/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([{
        "id": contact.id, 
        "nom": contact.nom, 
        "prenom": contact.prenom,
        "adresse": contact.adresse,
        "telephone": contact.telephone,
        "email": contact.email
    } for contact in contacts])

@main.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.json
    if not data or not 'nom' in data or not 'prenom' in data:
        return jsonify({"error": "Les champs nom et prenom sont requis"}), 400
    
    contact = Contact(
        nom=data['nom'], 
        prenom=data['prenom'],
        adresse=data.get('adresse', ''),
        telephone=data.get('telephone', ''),
        email=data.get('email', '')
    )
    db.session.add(contact)
    
    try:
        db.session.commit()
        return jsonify({
            "id": contact.id, 
            "nom": contact.nom, 
            "prenom": contact.prenom,
            "adresse": contact.adresse,
            "telephone": contact.telephone,
            "email": contact.email
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
