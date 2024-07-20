import smtplib
import dns.resolver
import itertools

def verify_email(email):
    try:
        # Vérifier le domaine de l'adresse e-mail
        domain = email.split('@')[1]
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = records[0].exchange
        mx_record = str(mx_record)
        
        # Connecter au serveur de mail
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        
        # Définir le délai de connexion
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('me@mydomain.com')
        code, message = server.rcpt(email)
        server.quit()
        
        # Le code 250 signifie que l'adresse est valide
        if code == 250:
            return True
        else:
            return False
    except Exception as e:
        return False

def generate_emails(first_name, last_name, domain):
    # Générer des adresses e-mail en utilisant différents formats courants
    formats = [
        "{first_name}.{last_name}@{domain}",
        "{first_name}{last_name}@{domain}",
        "{first_name}@{domain}",
        "{last_name}@{domain}",
        "{first_initial}{last_name}@{domain}",
        "{first_name}{last_initial}@{domain}",
        "{first_initial}.{last_name}@{domain}",
        "{first_name}.{last_initial}@{domain}"
    ]
    
    first_initial = first_name[0]
    last_initial = last_name[0]
    
    emails = [f.format(first_name=first_name, last_name=last_name, domain=domain,
                       first_initial=first_initial, last_initial=last_initial)
              for f in formats]
    return emails

# Exemples d'utilisation
first_name = input("Prénom de la personne :")
last_name = "Nom de la personne :"
domain = "Domaine du site internet auquel la personne appartient"

possible_emails = generate_emails(first_name, last_name, domain)

for email in possible_emails:
    if verify_email(email):
        print(f"L'email qui serait valide est: {email}")
        break
else:
    print("Il n'y a pas de mail valide trouvé")