import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Liste des extensions de fichiers à exclure
exclude_extensions = (".jpg", ".jpeg", ".js", ".css", ".gif", ".tiff", ".png", ".woff", ".woff2", ".ico", ".pdf", ".svg", ".txt")

vulnerable_urls = []
not_vulnerable_urls = []

# Demander à l'utilisateur de saisir des URLs jusqu'à ce qu'il quitte
while True:
    user_input = input("Entrez une URL à tester (ou 'q' pour quitter) : ")
    
    if user_input.lower() == 'q':
        break
    
    # Exclure les URLs avec des extensions de fichier spécifiées
    if not user_input.endswith(exclude_extensions):
        # Générer des payloads
        payloads = [' "><()', '<img src=x onerror=alert(1)>']  # Ajoutez d'autres payloads si nécessaire

        for payload in payloads:
            # Utiliser curl pour récupérer le contenu de l'URL
            response = subprocess.run(['curl', '--silent', '--path-as-is', '--insecure', user_input], capture_output=True, text=True)

            # Rechercher le payload dans la réponse
            if payload in response.stdout:
                vulnerable_urls.append(user_input)
                break
        else:
            not_vulnerable_urls.append(user_input)

# Enregistrer les résultats dans un fichier PDF
pdf_file = "nathan_results.pdf"

c = canvas.Canvas(pdf_file, pagesize=letter)
c.setFont("Helvetica", 12)

c.drawString(100, 750, "Résultats de la détection XSS :")
c.drawString(100, 730, "-----------------------------------")

c.drawString(100, 700, "Vulnérables :")
for i, url in enumerate(vulnerable_urls, start=1):
    c.drawString(120, 680 - i * 20, f"{i}. {url}")

c.drawString(100, 400, "Non vulnérables :")
for i, url in enumerate(not_vulnerable_urls, start=1):
    c.drawString(120, 380 - i * 20, f"{i}. {url}")

c.showPage()
c.save()

print(f"Les résultats ont été enregistrés dans {pdf_file}")
