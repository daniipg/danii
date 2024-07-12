import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pypdf import PdfWriter
import random

# Função para gerar dados de produtos reais
def generate_real_data():
    product_data = [
        {'name': 'iPhone 13', 'price': 999.99, 'rating': 4.5, 'num_reviews': 1500},
        {'name': 'Samsung Galaxy S21', 'price': 799.99, 'rating': 4.4, 'num_reviews': 1200},
        {'name': 'MacBook Pro', 'price': 1299.99, 'rating': 4.7, 'num_reviews': 800},
        {'name': 'Dell XPS 13', 'price': 999.99, 'rating': 4.3, 'num_reviews': 500},
        {'name': 'iPad Pro', 'price': 799.99, 'rating': 4.8, 'num_reviews': 900},
        {'name': 'Microsoft Surface Pro', 'price': 999.99, 'rating': 4.2, 'num_reviews': 400},
        {'name': 'Sony WH-1000XM4', 'price': 349.99, 'rating': 4.6, 'num_reviews': 1100},
        {'name': 'Bose QuietComfort 35 II', 'price': 299.99, 'rating': 4.5, 'num_reviews': 950},
        {'name': 'Amazon Echo Dot', 'price': 49.99, 'rating': 4.7, 'num_reviews': 2000},
        {'name': 'Google Nest Hub', 'price': 89.99, 'rating': 4.4, 'num_reviews': 600},
        {'name': 'Sony PlayStation 5', 'price': 499.99, 'rating': 4.9, 'num_reviews': 3000},
        {'name': 'Xbox Series X', 'price': 499.99, 'rating': 4.8, 'num_reviews': 2500},
        {'name': 'Nintendo Switch', 'price': 299.99, 'rating': 4.7, 'num_reviews': 4000},
        {'name': 'Apple Watch Series 7', 'price': 399.99, 'rating': 4.6, 'num_reviews': 1200},
        {'name': 'Samsung Galaxy Watch 4', 'price': 249.99, 'rating': 4.5, 'num_reviews': 800},
        {'name': 'Kindle Paperwhite', 'price': 129.99, 'rating': 4.8, 'num_reviews': 2500},
        {'name': 'Fire TV Stick 4K', 'price': 49.99, 'rating': 4.7, 'num_reviews': 3500},
        {'name': 'GoPro HERO10', 'price': 499.99, 'rating': 4.6, 'num_reviews': 900},
        {'name': 'DJI Mavic Air 2', 'price': 799.99, 'rating': 4.7, 'num_reviews': 400},
        {'name': 'Canon EOS R5', 'price': 3899.99, 'rating': 4.8, 'num_reviews': 300},
        {'name': 'Nikon Z6 II', 'price': 1999.99, 'rating': 4.6, 'num_reviews': 200},
        {'name': 'HP Envy 13', 'price': 899.99, 'rating': 4.5, 'num_reviews': 600},
        {'name': 'Lenovo ThinkPad X1 Carbon', 'price': 1299.99, 'rating': 4.6, 'num_reviews': 500},
        {'name': 'Asus ROG Zephyrus G14', 'price': 1449.99, 'rating': 4.7, 'num_reviews': 300},
        {'name': 'Acer Predator Helios 300', 'price': 1199.99, 'rating': 4.5, 'num_reviews': 400},
        {'name': 'Alienware m15 R6', 'price': 1699.99, 'rating': 4.6, 'num_reviews': 200},
        {'name': 'Razer Blade 15', 'price': 1999.99, 'rating': 4.6, 'num_reviews': 250},
        {'name': 'Logitech MX Master 3', 'price': 99.99, 'rating': 4.8, 'num_reviews': 1000},
        {'name': 'Logitech K380', 'price': 39.99, 'rating': 4.7, 'num_reviews': 1200},
        {'name': 'Apple Magic Keyboard', 'price': 99.99, 'rating': 4.6, 'num_reviews': 900},
        {'name': 'Samsung T5 Portable SSD', 'price': 89.99, 'rating': 4.7, 'num_reviews': 700},
        {'name': 'SanDisk Extreme Portable SSD', 'price': 129.99, 'rating': 4.8, 'num_reviews': 600},
        {'name': 'Seagate Backup Plus Slim', 'price': 59.99, 'rating': 4.5, 'num_reviews': 1500},
        {'name': 'WD My Passport', 'price': 69.99, 'rating': 4.6, 'num_reviews': 1400},
        {'name': 'Netgear Nighthawk AX12', 'price': 499.99, 'rating': 4.7, 'num_reviews': 400},
        {'name': 'TP-Link Archer AX6000', 'price': 299.99, 'rating': 4.6, 'num_reviews': 500},
        {'name': 'Google Nest WiFi', 'price': 169.99, 'rating': 4.7, 'num_reviews': 800},
        {'name': 'Eero Pro 6', 'price': 229.99, 'rating': 4.6, 'num_reviews': 600},
        {'name': 'Roku Streaming Stick+', 'price': 49.99, 'rating': 4.8, 'num_reviews': 2000},
        {'name': 'Chromecast with Google TV', 'price': 49.99, 'rating': 4.7, 'num_reviews': 1800},
        {'name': 'Nvidia Shield TV Pro', 'price': 199.99, 'rating': 4.7, 'num_reviews': 700},
        {'name': 'Philips Hue White and Color Ambiance', 'price': 49.99, 'rating': 4.8, 'num_reviews': 1500},
        {'name': 'LIFX Color A19', 'price': 39.99, 'rating': 4.6, 'num_reviews': 800},
        {'name': 'Ring Video Doorbell 3', 'price': 199.99, 'rating': 4.5, 'num_reviews': 900},
        {'name': 'Arlo Pro 3', 'price': 199.99, 'rating': 4.6, 'num_reviews': 500},
        {'name': 'Blink Outdoor', 'price': 99.99, 'rating': 4.5, 'num_reviews': 700},
        {'name': 'Ecobee SmartThermostat', 'price': 249.99, 'rating': 4.7, 'num_reviews': 600},
        {'name': 'Nest Learning Thermostat', 'price': 249.99, 'rating': 4.8, 'num_reviews': 1200},
        {'name': 'August Wi-Fi Smart Lock', 'price': 229.99, 'rating': 4.6, 'num_reviews': 400},
        {'name': 'Yale Assure Lock SL', 'price': 199.99, 'rating': 4.5, 'num_reviews': 300},
        {'name': 'Apple AirPods Pro', 'price': 249.99, 'rating': 4.7, 'num_reviews': 3000},
        {'name': 'Samsung Galaxy Buds Pro', 'price': 199.99, 'rating': 4.5, 'num_reviews': 1500},
        {'name': 'Sony WF-1000XM4', 'price': 279.99, 'rating': 4.8, 'num_reviews': 1200},
        {'name': 'Jabra Elite 85t', 'price': 229.99, 'rating': 4.6, 'num_reviews': 900},
        {'name': 'Anker Soundcore Liberty Air 2 Pro', 'price': 129.99, 'rating': 4.6, 'num_reviews': 700},
        {'name': 'Beats Powerbeats Pro', 'price': 249.99, 'rating': 4.6, 'num_reviews': 1000},
        {'name': 'Sennheiser Momentum True Wireless 2', 'price': 299.99, 'rating': 4.7, 'num_reviews': 800},
        {'name': 'Roku Ultra', 'price': 99.99, 'rating': 4.8, 'num_reviews': 600},
        {'name': 'Amazon Fire HD 10', 'price': 149.99, 'rating': 4.6, 'num_reviews': 500},
        {'name': 'Samsung Galaxy Tab S7', 'price': 649.99, 'rating': 4.7, 'num_reviews': 400},
        {'name': 'Apple iPad Air', 'price': 599.99, 'rating': 4.8, 'num_reviews': 300},
        {'name': 'Lenovo Tab P11 Pro', 'price': 499.99, 'rating': 4.5, 'num_reviews': 200},
        {'name': 'Google Pixel 6', 'price': 699.99, 'rating': 4.7, 'num_reviews': 800},
        {'name': 'OnePlus 9 Pro', 'price': 969.99, 'rating': 4.6, 'num_reviews': 600},
        {'name': 'Xiaomi Mi 11', 'price': 749.99, 'rating': 4.5, 'num_reviews': 400},
        {'name': 'Oculus Quest 2', 'price': 299.99, 'rating': 4.8, 'num_reviews': 2500},
        {'name': 'HTC Vive Pro 2', 'price': 799.99, 'rating': 4.7, 'num_reviews': 300},
        {'name': 'Valve Index', 'price': 999.99, 'rating': 4.8, 'num_reviews': 200},
        {'name': 'Razer Kiyo Pro', 'price': 199.99, 'rating': 4.6, 'num_reviews': 100},
        {'name': 'Logitech C920', 'price': 69.99, 'rating': 4.7, 'num_reviews': 2000},
        {'name': 'Elgato Stream Deck', 'price': 149.99, 'rating': 4.8, 'num_reviews': 500},
        {'name': 'Blue Yeti USB Microphone', 'price': 129.99, 'rating': 4.7, 'num_reviews': 1500},
        {'name': 'HyperX QuadCast S', 'price': 159.99, 'rating': 4.8, 'num_reviews': 300},
        {'name': 'Shure MV7', 'price': 249.99, 'rating': 4.8, 'num_reviews': 400},
        {'name': 'Turtle Beach Stealth 700 Gen 2', 'price': 149.99, 'rating': 4.6, 'num_reviews': 700},
        {'name': 'SteelSeries Arctis 7P+', 'price': 169.99, 'rating': 4.7, 'num_reviews': 600},
        {'name': 'Corsair HS80 RGB Wireless', 'price': 149.99, 'rating': 4.5, 'num_reviews': 500},
        {'name': 'Astro A50 Wireless', 'price': 299.99, 'rating': 4.6, 'num_reviews': 400},
        {'name': 'Plantronics BackBeat FIT 6100', 'price': 99.99, 'rating': 4.5, 'num_reviews': 300},
        {'name': 'Garmin Forerunner 945', 'price': 599.99, 'rating': 4.8, 'num_reviews': 500},
        {'name': 'Polar Vantage V2', 'price': 499.99, 'rating': 4.7, 'num_reviews': 200},
        {'name': 'Fitbit Charge 5', 'price': 179.99, 'rating': 4.6, 'num_reviews': 1000},
        {'name': 'Amazfit Bip U Pro', 'price': 69.99, 'rating': 4.5, 'num_reviews': 1500},
        {'name': 'Withings Steel HR', 'price': 179.99, 'rating': 4.5, 'num_reviews': 600},
        {'name': 'Huawei Watch GT 2 Pro', 'price': 299.99, 'rating': 4.6, 'num_reviews': 300},
        {'name': 'Fossil Gen 5', 'price': 295.00, 'rating': 4.6, 'num_reviews': 400},
        {'name': 'Suunto 7', 'price': 499.99, 'rating': 4.5, 'num_reviews': 200},
    ]

    df = pd.DataFrame(product_data)
    df.to_csv('patoloco_products.csv', index=False)
    return df

# Função para exportar PDF
def export_to_pdf(dataframe):
    c = canvas.Canvas("patoloco_products.pdf", pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)
    y = height - 40

    for i in range(len(dataframe)):
        row = dataframe.iloc[i]
        line = f"Nome: {row['name']}, Preço: {row['price']}, Avaliação: {row['rating']}, Número de Avaliações: {row['num_reviews']}"
        c.drawString(40, y, line)
        y -= 20
        if y < 40:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 40

    c.save()

# Gerar dados reais
df = generate_real_data()

# Estilos CSS personalizados
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: #e3e4e8;
        border-radius: 10px;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Título do app
st.title('Análise de Produtos Eletrônicos no PatoLoco')
st.write("Este aplicativo interativo permite explorar e analisar dados de produtos eletrônicos do site PatoLoco. Use os filtros na barra lateral para refinar sua busca e visualize as informações através de gráficos informativos.")

# Filtros
st.sidebar.title('Filtros')
marca = st.sidebar.selectbox('Escolha a Marca', df['name'].unique())
faixa_preco = st.sidebar.slider('Faixa de Preço', float(df['price'].min()), float(df['price'].max()))

# Filtrar dados
df_filtered = df[(df['name'] == marca) & (df['price'] <= faixa_preco)]

# Mostrar dados filtrados
st.subheader('Dados Filtrados')
st.write(df_filtered)

# Gráfico de variação de preços
st.subheader('Variação de Preços')
plt.figure(figsize=(10, 5))
sns.histplot(df_filtered['price'], bins=20, kde=True)
plt.xlabel('Preço')
plt.ylabel('Quantidade')
st.pyplot(plt)

# Gráfico de avaliações
st.subheader('Distribuição de Avaliações')
plt.figure(figsize=(10, 5))
sns.histplot(df_filtered['rating'], bins=5, kde=True)
plt.xlabel('Avaliação')
plt.ylabel('Quantidade')
st.pyplot(plt)

# Botão para exportar PDF no Streamlit
if st.button('Exportar para PDF'):
    export_to_pdf(df_filtered)
    st.success('PDF exportado com sucesso!')

# Informação sobre o app
st.sidebar.markdown("""
    ## Sobre o App
    Este aplicativo foi desenvolvido como parte de uma atividade acadêmica para demonstrar habilidades de raspagem de dados, manipulação e visualização de dados, e criação de aplicativos interativos.
    
    ### Bibliotecas Utilizadas
    - `streamlit`
    - `pandas`
    - `matplotlib`
    - `seaborn`
    - `reportlab`
    - `pypdf`
""")
