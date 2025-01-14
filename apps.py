import streamlit as st
from streamlit_authenticator import Authenticate

# Configuration des utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'Utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur',
        },
        'root': {
            'name': 'Root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur',
        },
    }
}

# Initialisation de l'authentificateur
authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30,
)

# Authentification dans la barre latérale
#name, authentication_status, username = authenticator.login("Login", "sidebar")

# Authentification dans le corps de la page
authenticator.login()

if st.session_state["authentication_status"]:
    # Navigation principale après connexion
    
    # Bouton de déconnexion
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.sidebar.write("Bienvenue root")
    main_menu = st.sidebar.radio("Navigation", ["🏠 Accueil", "📸 Les photos de mon chat"])

    

    # Gestion des pages
    if main_menu == "🏠 Accueil":
        st.title("Bienvenue sur ma page")
        st.image("/Users/happy/Documents/Data_Engeneer-Chef_de_projet_IA/semaine_5/Quetes/Streamlit_partie_3/mamie_folle.jpg")
    elif main_menu == "📸 Les photos de mon chat":
        st.title("Bienvenue dans l'album de mon chat 🐱")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("/Users/happy/Documents/Data_Engeneer-Chef_de_projet_IA/semaine_5/Quetes/Streamlit_partie_3/Chat1.jpg")
        with col2:
            st.image("/Users/happy/Documents/Data_Engeneer-Chef_de_projet_IA/semaine_5/Quetes/Streamlit_partie_3/chat2.jpg")
        with col3:
            st.image("/Users/happy/Documents/Data_Engeneer-Chef_de_projet_IA/semaine_5/Quetes/Streamlit_partie_3/chat3.jpg")

elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
else:
    st.warning("Veuillez entrer votre nom d'utilisateur et mot de passe.")
##
