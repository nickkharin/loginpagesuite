import requests


def test_be_correct_responses():
    should_be_login_by_api_with_correct_data()
    should_not_be_login_by_api_with_invalid_data()
    should_be_logout_by_api()


def should_be_login_by_api_with_correct_data():
    url = "http://the-internet.herokuapp.com"
    data = {'username' : "tomsmith",
            "password" : "SuperSecretPassword!"
        }
    resp = requests.post(url + "/authenticate",  data=data)
    assert resp.status_code == requests.codes.ok, f"Failed response, status code: {resp.status_code}"
    assert resp.text.find("class='flash success'") != -1, "Incorrect login and password"
    resp.close()


def should_not_be_login_by_api_with_invalid_data():
    url = "http://the-internet.herokuapp.com"
    data = {'username' : "ghghdhdf",
            "password" : "ddfbdfb"
        }
    resp = requests.post(url + "/authenticate",  data=data)
    assert resp.status_code == requests.codes.ok, f"Failed response on login, status code: {resp.status_code}"
    assert resp.text.find("class='flash success'") == -1, "Incorrect login and password, but it could be logged"


def should_be_logout_by_api():
    url = "http://the-internet.herokuapp.com"
    data = {'username': "tomsmith",
            "password": "SuperSecretPassword!"
            }
    resp = requests.post(url + "/authenticate", data=data)
    pres = requests.get(url + "/logout")
    assert pres.status_code == requests.codes.ok, f"Failed response on logout, status code: {pres.status_code}"
