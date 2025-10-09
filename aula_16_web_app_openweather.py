import requests
import streamlit as st

dict_clima = {
    'céu limpo': 'Céu limpo ☀️',
    'algumas nuvens': 'Céu com algumas nuvens ⛅',
    'nublado': 'Nublado ☁️',
    'névoa': 'Névoa 🌫️',
}

# 🔑 Coloque sua chave da API aqui
API_KEY = "9fcd7309d6062063ad83397457c86412"


def fazer_request(url, params=None):
    resposta = requests.get(url=url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        return None
    else:
        return resposta.json()


def pegar_tempo_para_local(local):
    if not local:
        return None

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": local,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br",
    }
    return fazer_request(url, params)


def main():
    st.title("Web App Tempo ☀️")
    st.write("Dados do OpenWeather (fonte: https://openweathermap.org/current)")

    local = st.text_input("Busque uma cidade:")
    if not local:
        st.info("Digite o nome de uma cidade acima e pressione Enter.")
        st.stop()

    dados_tempo = pegar_tempo_para_local(local)
    if not dados_tempo or "weather" not in dados_tempo:
        st.error("❌ Não foi possível obter os dados. Verifique o nome da cidade ou a chave da API.")
        st.stop()

    clima_atual = dados_tempo["weather"][0]["description"]
    clima_atual = dict_clima.get(clima_atual, clima_atual)
    temperatura = dados_tempo["main"]["temp"]
    sensacao_termica = dados_tempo["main"]["feels_like"]
    umidade = dados_tempo["main"]["humidity"]
    cobertura_nuvens = dados_tempo["clouds"]["all"]

    st.metric(label="Tempo atual", value=clima_atual)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Temperatura", value=f"{temperatura} °C")
        st.metric(label="Sensação térmica", value=f"{sensacao_termica} °C")
    with col2:
        st.metric(label="Umidade do ar", value=f"{umidade}%")
        st.metric(label="Cobertura de nuvens", value=f"{cobertura_nuvens}%")


if __name__ == "__main__":
    main()
