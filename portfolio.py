import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image

# Configurer la page de l'application
st.set_page_config(page_title="Portfolio Zseno Fouopa", page_icon="📊", layout="wide")

# Titre principal
#st.title("Bienvenue sur mon Portfolio") => titre optionnel
st.title("""Bienvenue dans mon univers, où les données prennent vie! """)
#st.title("où les données prennent vie!") 

# Fonction pour charger le fichier CSS
def load_css():
    """Charge le fichier CSS pour appliquer les styles"""
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Fonction pour afficher la barre de navigation avec option_menu()
def navbar():
    """Affiche la barre de navigation avec des liens"""
    selection = option_menu(
        menu_title="Mon Portfolio",  # Titre du menu
        options=["Accueil","Projets Techniques", "CV motivationnel", "Expertise métier", "Contact"],
        icons=["🏠", "📊", "💼", "📧"],
        menu_icon="cast",  # Icône du menu principal
        default_index=0,  # Option sélectionnée par défaut
        orientation="horizontal",  # Orientation horizontale
    )
    # Fonction appelée en fonction de l'option sélectionnée
    if selection == "Accueil":
        accueil()
    elif selection == "CV motivationnel":
        CV()
    elif selection == "Expertise métier":
        Experiences()
    elif selection == "Projets Techniques":
        projets()
    elif selection == "Contact":
        contact()

#--- ONGLET 1 ____

# Fonction pour afficher la section Accueil et À propos combinées
def accueil():
    """Affiche la section d'accueil"""
    st.markdown("<div id='accueil'></div>", unsafe_allow_html=True)

    # Charger et afficher l'image r
    image = Image.open("images/profil.png")  # Remplacez par votre image locale ou une URL

    #st.subheader("Profil")
   
    # Créer un conteneur pour l'image et le texte avec des colonnes
    col1, col2 = st.columns([3, 1])
    with col2:
        
        # Afficher l'image ronde
        st.image(image, width=300)  # Ajuste la largeur de l'image
        
    with col1:
        # Ajouter le texte à côté de l'image
        st.subheader(""" **Zséno Fouopa** """)
        #st.subheader(""" **Mes valeurs : rigueur, analyse et impact.**""")
        st.write("""
            
                 
            Mon parcours en tant que Data Analyst est le fruit d’une passion pour la transformation des données en leviers décisionnels.
                  
            **Mon rôle ?**  **Exploiter les datasets pour en extraire des insights précieux qui éclairent les choix métiers**. 
            
            Grâce à des **outils** comme **Python**, **SQL**, **Power BI** et **DAX**,
            j'explore, qualifie et analyse les données, identifie les tendances, et propose des solutions concrètes.
                 
            **Alors prêt(e) à découvrir ce que chaque ligne de code et chaque graphique peuvent révéler ? >>>>** 
                 
        
        """)
        
        st.write(""" **#rigueur #analyse #impact.**""")

#--- ONGLET CV ____

# Fonction pour afficher la section CV
def CV():
    """Affiche la section des CV"""
    st.markdown("<div id='CV'></div>", unsafe_allow_html=True)
    #st.header("Mon CV")
    # Titre de la page
    #st.title("Affichage de mon CV Motivationnel")

    # Chemin du fichier JPG
    image_path = "images/cvf.png"  # Assurez-vous que ce chemin est correct
    #st.image(image, width=350)  # Ajuste la largeur de l'image

    # Créer un conteneur pour l'image et le texte avec des colonnes
    col1cv, col2cv = st.columns([1, 8])
    with col1cv:
        # rien
        st.write(""" """)
    with col2cv:
        # Ajouter le texte à côté de l'image
        try:
            img = Image.open(image_path)
            st.image(img, caption="CV Motivationnel", width=950)
        except FileNotFoundError:
            st.error(f"L'image '{image_path}' est introuvable. Vérifiez le chemin et réessayez.")
        except Exception as e:
            st.error(f"Erreur lors de l'affichage de l'image : {e}")


#--- ONGLET 2 Expertise métier____

# Fonction pour afficher la section des Expériences
def Experiences():
    """Affiche la section des Experiences proposés"""
    st.markdown("<div id='Experiences'></div>", unsafe_allow_html=True)
    st.header("Mon Expertise Métier")

    st.write("""
            
            **Ma passion pour les données n’est pas arrivée par hasard**. Pendant 8 ans, j’ai œuvré dans l’univers de la **finance et de la comptabilité**, 
            en analysant les rapports financiers et en élaborant des recommandations pour guider les entreprises. 
            
            Au fil du temps, j’ai pris conscience de **la puissance cachée des données** et de leur capacité à aller bien au-delà des chiffres classiques. 
            
            J’ai alors décidé de monter en compétences et de m’immerger dans **le monde fascinant de la Data**.
            
            **Aujourd’hui**, j’utilise cette expertise pour **accompagner des projets ambitieux**, où chaque donnée raconte une histoire 
            et où chaque analyse mène à des **décisions éclairées**.     
        
        """)

    # Liste des compétences et descriptions
    competences = [
        {"titre": "Analyse des données financières", 
        "description": "Interprétation des chiffres pour détecter les tendances et les anomalies.", 
        "icone": "💹 "},
        {"titre": "Rigueur et précision dans la gestion des données", 
        "description": "Validation et nettoyage des données pour garantir leur exactitude.", 
        "icone": "🔍"},
        {"titre": "Esprit critique et résolution de problèmes", 
        "description": "Capacité à  identifier les incohérences et proposer des solutions adaptées.", 
        "icone": "🔧"},
        {"titre": "Reporting", 
        "description": "Création de tableaux de bord pour le suivi des KPI et la communication des résultats.", 
        "icone": "📊"},
        {"titre": "Collaboration interdisciplinaire", 
        "description": "Amélioration des workflows en collaboration avec les équipes IT et Data..", 
        "icone": "🤝"},
        {"titre": "Confidentialité et éthique", 
        "description": "Respect strict de la confidentialité des informations sensibles, savoir les manipuler avec discrétion.", 
        "icone": "🛡️"}
    ]

    # Création des colonnes
    cols = st.columns(3)  # Divise la page en 3 colonnes

    # Remplir chaque colonne avec les compétences
    for i, competence in enumerate(competences):
        with cols[i % 3]:  # Alterne entre les colonnes
            st.markdown(f"""
                <div style="border: 1px solid #ddd; border-radius: 5px; padding: 15px; margin: 10px; background-color: #f9f9f9; text-align: center;">
                    <div style="font-size: 30px;">{competence['icone']}</div>
                    <h4 style="color: #0078D7;">{competence['titre']}</h4>
                    <p>{competence['description']}</p>
                </div>
            """, unsafe_allow_html=True)



#-----  ONGLET 3 ------


# Fonction pour afficher un projet avec texte, image et lien de téléchargement
def portfolio(titre, description, technologies, pdf_file_path, github_link, github_label="Voir sur GitHub", image_file_path=None, key_prefix=""):
    col_texte, col_image, col_telechargement = st.columns([8, 2, 2])  # Proportions : 6 pour le texte, 2 pour l'image, 2 pour le lien de téléchargement
    
    # Texte à gauche
    with col_texte:
        st.markdown(
            f"""
            <div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; margin-bottom: 20px; background-color: #f9f9f9;">
                <h4 style="color: #0078D7;">{titre}</h4>
                <p><b>Technologies :</b> {technologies}</p>
                <p>{description}</p>
                <a href="{github_link}" target="_blank" style="color: #0078D7; text-decoration: none; font-weight: bold;">🌐 {github_label}</a>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    # Image 
    with col_image:
        if image_file_path:
            image = Image.open(image_file_path)  # Charger l'image spécifiée
            st.image(image, width=400)
    
    # Lien telechargement
    with col_telechargement:
        if os.path.exists(pdf_file_path):
            # Utilisation de st.download_button pour créer le bouton de téléchargement
            with open(pdf_file_path, "rb") as pdf_file:
                st.download_button(
                    label="Télécharge le PDF",
                    data=pdf_file,
                    file_name=os.path.basename(pdf_file_path),
                    mime="application/pdf",
                    use_container_width=True,  # Cela permet au bouton de s'étendre sur toute la largeur de la colonne
                    key=f"download_button_{key_prefix}"
                )
        else:
            st.error("En-cours")


# Fonction pour afficher la section des Projets
def projets():
    """Affiche les projets du portfolio avec texte à gauche, image au centre et lien de téléchargement à droite"""
    st.markdown("<div id='portfolio'></div>", unsafe_allow_html=True)
    st.header("Mes Projets")

    st.write("""
        <p>  </p>  <!-- Saut de paragraphe -->
        <p>  </p>  <!-- Saut de paragraphe -->
       
        """, unsafe_allow_html=True)
    
    # Créer un conteneur pour l'image et le texte avec des colonnes
    colim1, colim2, colim3, colim4, colim5, colim6, colim7 = st.columns([2, 2, 2, 2, 2, 2, 2])
    
    with colim1:
        image1 = Image.open("outils/sql.png")
        st.image(image1, width=120)  # Ajuste la largeur de l'image
    with colim2:
        image2 = Image.open("outils/Python.jpg")
        st.image(image2, width=120)  # Ajuste la largeur de l'image
    with colim3:
        image3 = Image.open("outils/Pandas.png")
        st.image(image3, width=120)  # Ajuste la largeur de l'image
    with colim4:
        image4 = Image.open("outils/sklearn.png")
        st.image(image4, width=120)  # Ajuste la largeur de l'image
    with colim5:
        image5 = Image.open("outils/vsc.png")
        st.image(image5, width=120)  # Ajuste la largeur de l'image
    with colim6:
        image6 = Image.open("outils/streamlit.jpg")
        st.image(image6, width=120)  # Ajuste la largeur de l'image
    with colim7:
        image7 = Image.open("outils/pbi.jpg")
        st.image(image7, width=120)  # Ajuste la largeur de l'image
    


    st.write("""
        <p>   </p>  <!-- Saut de paragraphe -->
        <p>   </p>  <!-- Saut de paragraphe -->
        <p>   </p>  <!-- Saut de paragraphe -->
       
        """, unsafe_allow_html=True)
    
    # Projet 1 - Toys and model
    pdf_file_1 = "assets/Projet_toys_and_models_ZFO.pdf"  # je n'ai plus besoin d'afficher ce pdf : à bloquer
    portfolio(
        titre="📍 Dashboard interactif de suivi des KPI métiers",
        description="Conception d’un tableau de bord pour suivre les performances de l'entreprise dans les domaines métiers : ventes, finances, logistique et RH.",
        technologies="SQL, Power BI, DAX",
        pdf_file_path=pdf_file_1,
        github_link="https://github.com/zsenof/Toys_and_Models_KPI_metiers/tree/main/requ%C3%AAte",
        github_label="Requête SQL sur GitHub",
        image_file_path="images/P1-image.png",  # Exemple d'image
        key_prefix="projet1"
    )

    # Projet 2 - recommandation de films
    pdf_file_2 = "assets/Presentation_projet.pdf"  # Assurez-vous que le fichier est dans le dossier "assets"
    portfolio(
        titre="📍 Système de recommandation de films",
        description="Développement d’un modèle de recommandations de films pour augmenter la fréquentation d’un cinéma, après une analyse approfondie des données locales.",
        technologies="Pandas, Scikit-learn, Matplotlib, Seaborn, Streamlit",
        pdf_file_path=pdf_file_2,
        github_link="https://github.com/zsenof/Systeme_recommandation_films_creuse/tree/main/Code",
        github_label="Code transformation des données sur Github",
        image_file_path="images/P2-image.png",  # Exemple d'image
        key_prefix="projet2"
    )

    # Projet 3 - revenus menage
    pdf_file_3 = "assets/Projet_analyse_revenus_menage_ZFO.pdf"  # Assurez-vous que le fichier est dans le dossier "assets"
    portfolio(
        titre="📍 Hackathon - Analyse des revenus des ménages",
        description="Un délai de 48H, pour répondre au besoin client. Analyse et segmentation des prospects pour optimiser les offres de produits d’épargne.",
        technologies="APIs REST, Web Scraping, Pandas, PostgreSQL",
        pdf_file_path=pdf_file_3,
        github_link= "https://github.com/zsenof/Hackathon_Analyse_revenu_foyer/blob/main/Nettoyage_analyse_donnees.ipynb",
        github_label="Code transformation des données sur Github",
        image_file_path="images/P3-image.png",  # Exemple d'image
        key_prefix="projet3"
    )

    # Projet 4
    pdf_file_4 = "assets/Presentation_projet.pdf"  # Assurez-vous que le fichier est dans le dossier "assets"
    portfolio(
        titre="📍 Wild Data Hub | En cours",
        description="Intégration d’un pipeline de données complet pour développer un outil de conseil nutritionnel permettant de recommander des plans alimentaires personnalisés.",
        technologies="APIs REST, Web Scraping, Pandas, PostgreSQL",
        pdf_file_path=pdf_file_4,
        github_link= "[]()",
        github_label="En-cours",
        image_file_path="images/P4.png",  # Exemple d'image
        key_prefix="projet4"
    )

# --- ONGLET CONTACT

    # Fonction pour afficher la section Contact de manière ludique avec une photo
def contact():
    """Affiche la section de contact de manière ludique avec un message personnalisé et une photo"""
    st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
    #st.header("Me Contacter")
    
    # Créer une mise en page avec des colonnes
    col_gauche, col_droite = st.columns([1, 2])  # Proportions : 2 pour l'image, 3 pour les liens
    
    # Colonne gauche : Image
    with col_gauche:
        # Ajouter une image pour rendre la section plus visuelle
        image = Image.open("images/profil.png")  # Assurez-vous que l'image est dans le bon dossier
        st.image(image, width=320)  # Ajustez la taille de l'image si nécessaire

    # Colonne droite : Texte et Liens de contact
    with col_droite:
        # Message personnalisé (texte)
        st.markdown("""
        <div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; margin-top: 10px; background-color: #f9f9f9;">
            <h4 style="color: #0078D7;">Merci pour votre visite !</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        <p> </p>  <!-- Saut de paragraphe -->
        <p> </p>  <!-- Saut de paragraphe -->
       
        """, unsafe_allow_html=True)
        

        st.write("""
        <p> </p>  <!-- Saut de paragraphe -->
                 <p> </p>  <!-- Saut de paragraphe -->
                 
        Envie d'en savoir plus ou de discuter d'un projet ?
                 
        N’hésitez pas à me contacter, **votre curiosité est le début de notre collaboration !** 
        """, unsafe_allow_html=True)
        
        # Ajouter un fond agréable et des liens interactifs
        st.markdown("""
        <style>
        .contact-links {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            gap: 10px;
            margin-top: 10px;
        }
        .contact-links a {
            font-size: 1.2em;
            color: #0078D7;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.3s ease, color 0.3s ease;
        }
        .contact-links a:hover {
            transform: scale(1.1);
            color: #FF5733;  /* Couleur au survol */
        }
        .contact-icons {
            font-size: 1.5em;
        }
        </style>
        """, unsafe_allow_html=True)

        # Liens de contact avec icônes et survol
        st.markdown("""
        <div class="contact-links">
            <a href="mailto:zseno.fouopa@gmail.com" class="contact-icons" title="Envoyer un email">
                📧 Email
            </a>
            <a href="https://www.linkedin.com/in/zs%C3%A9no-fouopa-17708576/" class="contact-icons" title="Voir mon LinkedIn">
                💼 LinkedIn
            </a>
            <a href="https://github.com/zsenof" class="contact-icons" title="Voir mes projets GitHub">
                🌐 GitHub
            </a>
        </div>
        """, unsafe_allow_html=True)


# Main App
if __name__ == "__main__":
    load_css()  # Charge le fichier CSS
    navbar()  # Affiche la barre de navigation avec option_menu




# streamlit run portfolio.py
# pipreqs /Users/ztadjouzem/Desktop/VSCODE/PortFolio/
