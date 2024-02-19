import requests

def test_lista_paises():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    assert response.status_code ==  200
    country_list = response.json()
    assert isinstance(country_list, list)
    assert len(country_list) >  0

def test_pais_especifico():
    country_name = 'brazil'
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    assert response.status_code ==  200
    country_data = response.json()
    assert len(country_data) ==  1
    assert country_data[0]['name']['common'] == 'Brazil'
    assert 'capital' in country_data[0]
    assert 'population' in country_data[0]

def test_lista_paises_duplicado():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    assert response.status_code ==  200
    country_list = response.json()
    assert isinstance(country_list, list)
    assert len(country_list) >  0

def test_pais_nome_incompleto():
    country_name = 'br'
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    assert response.status_code ==  400
    country_data = response.json()
    assert isinstance(country_data, list)
    assert any(country_name.lower() in country['name']['common'].lower() for country in country_data)

def test_pais_codigo_especifico():
    country_code = 'BR'
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    response = requests.get(url)
    assert response.status_code ==  200
    country_data = response.json()
    assert len(country_data) ==  1
    assert country_data[0]['name']['common'] == 'Brazil'
    assert 'capital' in country_data[0]
    assert 'population' in country_data[0]