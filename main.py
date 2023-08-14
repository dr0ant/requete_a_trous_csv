import pandas as pd

# Charger le fichier CSV dans un DataFrame
csv_file = "test_py.csv"
df = pd.read_csv(csv_file)

# Créer une liste pour stocker les requêtes modifiées
queries = []

# Parcourir chaque ligne du DataFrame
for index, row in df.iterrows():
    query = row[0]  # Prendre la valeur de la première colonne (texte avec variables)

    # Remplacer les variables dans la requête
    for i in range(1, len(row)):
        placeholder = f"£{i}"
        value = row[i]
        query = query.replace(placeholder, str(value))

    queries.append(query)  # Ajouter la requête modifiée à la liste

# Créer un nouveau DataFrame avec les colonnes d'origine et la colonne 'query'
new_df = df.copy()
new_df['query'] = queries

# Afficher le nouveau DataFrame
print(new_df)



# Créer un nouveau DataFrame avec les colonnes d'origine et la colonne 'query'
new_df = df.copy()
new_df['query'] = queries

# Exporter le nouveau DataFrame au format CSV
export_csv = "nouveau_fichier.csv"
new_df.to_csv(export_csv, index=False)

print("Export terminé.")
