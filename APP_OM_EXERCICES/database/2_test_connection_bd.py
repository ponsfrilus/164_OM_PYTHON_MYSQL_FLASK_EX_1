"""Démonstration d'envoi d'une requête SQL à la BD
Fichier : 2_test_connection_bd.py
Auteur : OM 2021.03.03
"""

from APP_OM_EXERCICES.database.database_tools import DBconnection

try:
    """
        Une seule requête pour montrer la récupération des données de la BD en MySql.
    """
    strsql_genres_afficher = """SELECT id_genre, intitule_genre FROM t_genre ORDER BY id_genre ASC"""

    with DBconnection() as db:
        db.execute(strsql_genres_afficher)
        result = db.fetchall()
        print("data_genres ", result, " Type : ", type(result))


except Exception as ErreurConnectionBD:
    print(f"2547821146 Connection à la BD Impossible !"
          f"{ErreurConnectionBD.args[0]} , "
          f"{ErreurConnectionBD}")
