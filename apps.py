import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
      st.sidebar.title("Menu")
      


if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion dans le sidebar
  with st.sidebar:
    authenticator.logout("Déconnexion")
    st.sidebar.write("Bienvenu root")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

import streamlit as st



# Menu principal avec un emoji
main_menu = st.sidebar.selectbox("Navigation", ["🏠 Accueil", "📸 Les photos de mon chat"])



# Afficher le contenu en fonction de la sélection
if main_menu == "🏠 Accueil":
    st.title("Bievenue sur ma page")
    st.image("/Users/happy/Documents/Data_Engeneer-Chef_de_projet_IA/semaine_5/Quetes/Streamlit_partie_3/mamie_folle.jpg")

elif main_menu == "📸 Les photos de mon chat":
    st.title("Bienvenue dans l'album de mon chat 🐱")
    # Utilisation des colonnes pour afficher les images côte à côte
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("/Users/happy/Documents/Data_Engeneer-Chef_de_projet_IA/semaine_5/Quetes/Streamlit_partie_3/chat1.jpg")
    with col2:
        st.image("/Users/happy/Documents/Data_Engeneer-Chef_de_projet_IA/semaine_5/Quetes/Streamlit_partie_3/chat2.jpg")
    with col3:
        st.image("/Users/happy/Documents/Data_Engeneer-Chef_de_projet_IA/semaine_5/Quetes/Streamlit_partie_3/Chat3.jpg")
    
