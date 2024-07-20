import streamlit as st
import smtplib
import dns.resolver

def verify_email(email):
    try:
        # Verification of email domain
        domain = email.split('@')[1]
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = records[0].exchange
        mx_record = str(mx_record)
        
        # Connecting into mail server
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        
        #  time of connexion
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('me@mydomain.com')
        code, message = server.rcpt(email)
        server.quit()
        
        # Code 250 is a vidation sign
        if code == 250:
            return True
        else:
            return False
    except Exception as e:
        print("Une erreur est survenue :", e)
        return False

def generate_emails(first_name, last_name, domain):
# Generation of mails
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

# Use Examples 
first_name = input("Prénom de la personne :")
last_name = "Nom de la personne :"
domain = "Domaine du site internet auquel la personne appartient"

st.title("Email Finder")
st.write("Enter the details below to find the possible email addresses and verify them.")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
domain = st.text_input("Domain (example.com)")

if st.button("Find Email"):
    if first_name and last_name and domain:
        possible_emails = generate_emails(first_name, last_name, domain)
        st.write("Generated Emails:")
        st.write(possible_emails)

        valid_email = None
        for email in possible_emails:
            if verify_email(email):
                valid_email = email
                break

        if valid_email:
            st.success(f"L'email qui serait valide est: {valid_email}")
        else:
            st.error("Il n'y a pas de mail valide trouvé")
    else:
        st.error("S'il vous plait, renseignez tous les champs requis")
