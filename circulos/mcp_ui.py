import streamlit as st
import requests

# Tu URL del MCP en Cloud Run
MCP_URL = "https://mcp-aura-new-1074895574660.europe-west1.run.app"

# Opcional: Si usás Gemini, pon tu API key (creala en ai.google.dev)
GEMINI_API_KEY = "tu_gemini_api_key_aquí"  # Si no tenés, usa la web gratuita

st.title("Consulta tu Graph Database en Lenguaje Natural")

# Campo para la pregunta
question = st.text_input("Preguntá algo sobre tu base Neo4j (ej. cuántos nodos hay):")

if st.button("Consultar"):
    if question:
        st.write("Procesando tu pregunta...")
        # Llamada a la LLM (Gemini) para convertir a Cypher
        # (Si no tenés API key, podés usar la web de Gemini manualmente)
        cypher_query = "MATCH (n) RETURN count(n) AS total"  # Ejemplo; reemplaza con llamada real a Gemini

        # Llamada al MCP con el Cypher
        try:
           response = requests.post(MCP_URL, json={"command": "execute_cypher", "query": cypher_query})
           if response.status_code == 200:
               result = response.json()
               st.success(f"Respuesta: {result}")
           else:
               st.error(f"Error del MCP: {response.status_code} - {response.text}")
        except Exception as e:
           st.error(f"Error de conexión: {e}")
    else:
        st.warning("Escribí una pregunta.")