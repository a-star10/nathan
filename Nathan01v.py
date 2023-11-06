# ASCII art
ascii_art = """
 __   __     ______     ______   __  __     ______     __   __    
/\ "-.\ \   /\  __ \   /\__  _\ /\ \_\ \   /\  __ \   /\ "-.\ \   
\ \ \-.  \  \ \  __ \  \/_/\ \/ \ \  __ \  \ \  __ \  \ \ \-.  \  
 \ \_\\"\_\  \ \_\ \_\    \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_\\"\_\ 
  \/_/ \/_/   \/_/\/_/     \/_/   \/_/\/_/   \/_/\/_/   \/_/ \/_/ 

Auteur : Léon Meizou
Version : v0.1
"""

print(ascii_art)






import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
        payloads = [' "><()', '<img src=x onerror=alert(1)>', 
                   '<script>alert("XSS")</script>', 
                   '"><img src=x onerror=alert("XSS")>', 
                   '<img src=x onerror=alert(1) onload=alert(2)>',
                   '"><img src=x onerror=alert(1) onload=alert(2)>']
        
        is_vulnerable = False

        for payload in payloads:
            try:
                # Utiliser requests pour récupérer le contenu de l'URL
                response = requests.get(user_input, verify=False)
                response_text = response.text

                # Rechercher le payload dans la réponse
                if payload in response_text:
                    is_vulnerable = True
                    break
            except requests.exceptions.RequestException:
                pass

        if is_vulnerable:
            vulnerable_urls.append(user_input)
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
