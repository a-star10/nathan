# Nathan

Nathan est un petit script Python qui vous permet de tester des URLs à la recherche de vulnérabilités Cross-Site Scripting (XSS). Le script utilise Curl pour récupérer le contenu des URL, applique des payloads XSS, et enregistre les résultats dans un fichier PDF.

## Installation

1. Assurez-vous d'avoir Python installé sur votre système.

2. Téléchargez le script Nathan depuis ce référentiel.

3. Exécutez le script en utilisant la commande suivante :

   ```bash
   python Nathan.py

Utilisation
Lorsque vous exécutez le script, il vous demandera de saisir des URLs à tester. Entrez l'URL que vous souhaitez tester.

Le script exclura automatiquement les URLs avec des extensions de fichier spécifiées (par exemple, .jpg, .js) pour se concentrer sur les fichiers HTML.

Il appliquera plusieurs payloads XSS courants pour tester la vulnérabilité.

Les résultats, indiquant si l'URL est vulnérable ou non, seront enregistrés dans un fichier PDF nommé "xss_results.pdf".

Personnalisation
Vous pouvez personnaliser le script en ajoutant ou en modifiant les payloads XSS dans le code.

Contribution
Nous accueillons les contributions de la communauté. Si vous souhaitez contribuer à ce projet, veuillez ouvrir une issue ou soumettre une demande de fusion sur GitHub.

Licence
Ce projet est sous licence . Voir le fichier LICENSE.txt pour plus de détails.

Auteur
Ce script a été développé par Léon Meizou et est disponible en open source pour aider à la détection des vulnérabilités XSS.

Pour toute question ou commentaire, veuillez nous contacter.
