import pandas as pd
import requests
import streamlit as st


def fazer_request(url, params=None):
    resposta = requests.get(url=url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f"Erro no request: {e}")
        resultado = None
    else:
        resultado = resposta.json()
    return resultado


def pegar_nome_por_decada(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    nome_por_decada = fazer_request(url=url)
    if not nome_por_decada:  # Sem resultados para a chamada da API!
        return {}
    dict_decadas = {}
    for dados in nome_por_decada[0]['res']:
        decada = dados['periodo']
        quantidade = dados['frequencia']
        dict_decadas[decada] = quantidade
    return dict_decadas


def main():
    # Cabeçalho do Web App
    st.title('Web App Nomes 🇧🇷')
    st.write('Dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)')
    nome = st.text_input('Consulte um nome:')
    if not nome:
        st.stop()

    # Acessa dados do IBGE
    dict_decadas = pegar_nome_por_decada(nome=nome)
    if not dict_decadas:  # Sem dados do IBGE para este nome
        st.warning(f'Nenhum dado encontrado para o nome "{nome}"!')
        st.stop()

    # Exibe dados do IBGE
    df = pd.DataFrame.from_dict(dict_decadas, orient='index')
    col1, col2 = st.columns([0.3, 0.7])
    with col1:  # coluna esquerda
        st.write('Frequência por década')
        st.dataframe(df)
    with col2:  # coluna direita
        st.write('Evolução no tempo')
        st.line_chart(df)


if __name__ == '__main__':
    main()
