# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:30:13 2022

@author: fanao
"""


from select import select
import sqlite3

#ouvrir une connexion ou créer un fichier si une base de données n'existe pas
connexion = sqlite3.connect("myBD.db")

#création du curser sur les différentes table
curseur1 = connexion.cursor()
curseur2 = connexion.cursor()
curseur3 = connexion.cursor()
curseur4 = connexion.cursor()
#Exécution unique
# création des base des tables DROP

curseur1.execute('''CREATE TABLE IF NOT EXISTS etudiants
                    ( id_et TEXT PRIMARY KEY, 
                    nom_et TEXT, prenom_et TEXT, 
                    matricule_et INTEGER,Genre_et TEXT)
                    ''')

curseur2.execute('''CREATE TABLE IF NOT EXISTS enseignants
                    ( id_ens INTEGER,
                    nom_ens TEXT, prenom_ens TEXT,contact_ens INTEGER
                    )
                    ''')

curseur3.execute('''CREATE TABLE IF NOT EXISTS emprunt
                  (id_emp TEXT PRIMARY KEY,
                   matricule TEXT, nom TEXT,filiere INTEGER, titre_du_livre INTEGER,
                   auteur_du_livre INTEGER, date_emprunt DATE,date_remise DATE)   
              ''')
curseur4.execute(''' CREATE TABLE IF NOT EXISTS login(user_name TEXT,Password INTEGER)
                 ''')
#Exécution d'un script 
# enrégistre plusieurs etudiants
curseur1.executescript('''
                      INSERT INTO etudiants(id_et, nom_et ) VALUES ("natha@123", "bessala" );
                      INSERT INTO etudiants(id_et, nom_et) VALUES ("gyu67", "onana");
                      ''')
# enrégistrement des enseignants
curseur2.executescript('''
                      INSERT INTO enseignants(id_ens, nom_ens, contact_ens) VALUES ("hend@12", "onembele", "657574536");
                      INSERT INTO enseignants(id_ens, nom_ens, contact_ens) VALUES ("bnje@34", "tagne", "693309173")
                      ''')
#enregistrement des differents emprunts
curseur3.executescript('''
                       INSERT INTO emprunt(titre_du_livre,date_emprunt) VALUES("madame bovarie","10/05/2022");
                        INSERT INTO emprunt(titre_du_livre,date_emprunt) VALUES("une saison blanche et seche","7/12/2022")

                       ''')
curseur4.executescript('''
                       INSERT INTO login(user_name,Password) VALUES("nathalie",12345678)
                       ''')


connexion.commit()








connexion.close()      
