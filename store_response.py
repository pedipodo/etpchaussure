import csv
import json
import os
from datetime import datetime

# Récupère les données de l'événement GitHub
with open(os.environ['GITHUB_EVENT_PATH']) as f:
    event = json.load(f)
    responses = event['client_payload']

# Chemin du fichier CSV
csv_file = "responses.csv"
file_exists = os.path.isfile(csv_file)

# Écrit les données dans le CSV
with open(csv_file, mode='a', newline='', encoding='utf-8') as f:
    fieldnames = [
        'id', 'date', 'profil', 'a_deja_vu', 'duree_visionnage',
        'a_terminé', 'moment_abandon', 'a_appris', 'a_aime',
        'commentaire', 'type', 'user_id'
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()

    # Convertit les types pour le CSV
    data = responses.copy()
    if 'a_terminé' in data:
        data['a_terminé'] = int(data['a_terminé'])
    if 'a_appris' in data and data['a_appris'] is not None:
        data['a_appris'] = 1 if data['a_appris'] == "Oui" else 0

    writer.writerow(data)
