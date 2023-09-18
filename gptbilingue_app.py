import os
import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fonction pour initialiser ou récupérer l'historique des messages de la session
def get_message_history():
    if 'message_history' not in st.session_state:
        st.session_state.message_history = [{'role': 'system', 'content': "Tu es un assistant intelligent capable de répondre à des questions sur l'enseignement bilingue dans les pays d'Afrique francophone, particuliérement les pays partenaire de l'initiative Ecole et langues nationales en Afrique (ELAN-Afrique) mise en oeuvre par l'IFEF"}]
    return st.session_state.message_history

def main():
    st.markdown("<h2 style='text-align: center; color: navy;'>Assistant Intelligent programmé pour repondre à vos questions sur le Bilinguisme</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: green;'>Auteur : Hamaya AG-ABDOULAYE</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: blue;'>Ce chatbot est réglé sur le modéle gpt-3.5-turbo de ChatGPT, les prédictions peuvent souvent produire des informations inexactes sur des personnes, des lieux ou des faits. Son assistant a été programmé sur la situation de l'enseignement bilingue dans les pays Francophones d'Afrique, le plus souvant partenaires du programme ELAN. N'hésitez pas à rebondir sur les reponses prédites, le relancé pour recadrer et ainsi tiré profit du meilleur de cet assistant intelligent</h6>", unsafe_allow_html=True)

    st.sidebar.header("PARAMETRES")
    slider1 = st.sidebar.slider("Max tokens", min_value=80, max_value=500, value=270, step=10)
    slider2 = st.sidebar.slider("Reglage de la temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    
    

    input_user = st.text_input("Posez une question en rapport avec l'enseignement bilingue en Afrique Francophone:")

    if st.button("Exécuter"):
        if input_user:
            message_history = get_message_history()
            message_history.append({'role': 'user', 'content': input_user})
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=message_history,
                max_tokens=slider1,
                temperature=slider2
            ).choices[0].message
            message_history.append(response)

            st.write(response['content'])

if __name__ == '__main__':
    main()
