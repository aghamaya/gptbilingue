import os
import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fonction pour initialiser ou récupérer l'historique des messages de la session
def get_message_history():
    if 'message_history' not in st.session_state:
        st.session_state.message_history = [{'role': 'system', 'content': "Tu es un assistant intelligent capable de répondre à des questions sur l'enseignement bilingue dans les pays d'Afrique francophone"}]
    return st.session_state.message_history

def main():
    st.markdown("<h1 style='text-align: center; color: navy;'>Assistant Intelligent pour l'Enseignement Bilingue</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: green;'>Auteur : Hamaya AG-ABDOULAYE</h6>", unsafe_allow_html=True)

    st.sidebar.header("PARAMETRES")
    slider1 = st.sidebar.slider("Max tokens", min_value=100, max_value=1000, value=400, step=1)
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
