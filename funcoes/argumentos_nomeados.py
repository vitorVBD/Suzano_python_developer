def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Mitsubishi", "Lancer", 2015, "XYZ-5678")
salvar_carro(marca="Mercedes", modelo="A200", ano=2016, placa="ABC-1234")
salvar_carro(**{"marca": "Volvo", "modelo": "XC-60", "ano": 2018, "placa": "DEF-5678"})