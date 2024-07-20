# 📧 Email Finder
[banner image](assets/FindMail.jpeg)

## 🛠️ Pourquoi j'ai développé cette application
J'ai développé l'application **FindMail** pour aider les utilisateurs à trouver des adresses e-mail valides appartenant à des personnes travaillant dans une entreprise spécifique. En fournissant le prénom, le nom et le domaine de l'entreprise, l'application génère plusieurs formats d'e-mails couramment utilisés et vérifie leur validité. Cela peut être particulièrement utile pour :

- 🎓 **Soumettre des candidatures** : Les chercheurs d'emploi peuvent trouver les e-mails des recruteurs ou des responsables des ressources humaines pour envoyer directement leur candidature.
- 🤝 **Établir des connexions professionnelles** : Les professionnels peuvent entrer en contact avec des collègues potentiels ou des partenaires commerciaux.
- 📩 **Communiquer facilement** : Facilite la communication en trouvant rapidement des e-mails valides.

## 🚀 Fonctionnalités

- 🔍 **Génération d'e-mails** : Génère plusieurs formats d'e-mails couramment utilisés à partir du prénom, du nom et du domaine de l'entreprise.
- ✅ **Vérification des e-mails** : Vérifie la validité des e-mails générés pour s'assurer qu'ils existent.
- 📸 **Interface utilisateur conviviale** : Interface Streamlit intuitive avec une barre latérale fixe contenant une image et des champs de saisie interactifs.

## 🖥️ Comment utiliser l'application

### Prérequis

Assurez-vous d'avoir installé les dépendances nécessaires :

```sh
pip install streamlit dnspython
```

### Instructions

1. **Clonez ce dépôt** :

    ```sh
    git clone git@github.com:MohamedALMAHMOUD/FindMail.git
    cd FindMail
    ```

2. **Placez votre image dans le dossier `assets`** et assurez-vous qu'elle est nommée `photo.jpg` ou modifiez le chemin dans le script.

3. **Exécutez l'application Streamlit** :

    ```sh
    streamlit run main.py
    ```

4. **Utilisez l'application** :

    - Entrez le prénom, le nom et le domaine de l'entreprise dans les champs de saisie de la barre latérale.
    - Cliquez sur le bouton "trouver le mail" pour générer et vérifier les e-mails.
    - Les e-mails générés seront affichés, et l'application indiquera s'il y a un e-mail valide trouvé.

## 📂 Structure du projet

```plaintext
email-finder/
├── assets/
│   └── FindMail.jpeg  # Placez votre image ici
├── main.py  # Script principal de l'application
├── requirements.txt  # Fichier des dépendances
└── README.md  # Ce fichier
```

## 📝 Exemple de fichier `requirements.txt`

```plaintext
streamlit==1.10.0
dnspython==2.6.1
```

## 🌟 Fonctionnalités futures

- 🕵️ **Recherche avancée d'e-mails** : Ajouter des algorithmes plus avancés pour générer et vérifier les e-mails.
- 📬 **Intégration avec des API externes** : Connecter l'application à des API de vérification d'e-mails pour une vérification plus robuste.
- 📈 **Analyse des e-mails** : Ajouter des fonctionnalités pour analyser et classer les e-mails en fonction de leur validité et de leur utilisation.

---

💡 **Note** : L'application utilise des techniques basiques de vérification d'e-mails et peut ne pas être en mesure de vérifier tous les e-mails avec une précision parfaite. Utilisez cette application comme un outil complémentaire dans votre processus de recherche de contacts.
