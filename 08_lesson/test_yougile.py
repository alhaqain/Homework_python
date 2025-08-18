import requests


base_url = 'https://ru.yougile.com'
key = ''


headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + key
}


def test_create_project_positive():
    # Создаем проект
    body = {
        "title": "test create"
    }
    new_project = requests.post(
        base_url + "/api-v2/projects", json=body, headers=headers)
    assert new_project.status_code == 201


def test_create_project_negative():
    # Создаем проект без названия
    body = {
        "title": ""
    }
    new_project = requests.post(
        base_url + "/api-v2/projects", json=body, headers=headers)
    assert new_project.status_code == 400


def test_change_project_positive():
    # Создаем проект
    body = {
        "title": "test create poz"
    }
    project = requests.post(
        base_url + "/api-v2/projects", json=body, headers=headers)
    project_id = project.json()['id']

    # Изменяем проект
    new_title = "test change"
    new_body = {
        "title": new_title
    }

    modified_project = requests.put(
        base_url + "/api-v2/projects/" + project_id,
        json=new_body, headers=headers)

    assert modified_project.status_code == 200


def test_change_project_negative():
    # Создаем проект
    body = {
        "title": "test create neg"
    }
    project = requests.post(
        base_url + "/api-v2/projects",
        json=body, headers=headers)
    project_id = project.json()['id']

    # Изменяем проект с помощью ошибочного метода
    new_title = "test change"
    new_body = {
        "title": new_title
    }

    modified_project = requests.post(
        base_url + "/api-v2/projects/" + project_id,
        json=new_body, headers=headers)

    assert modified_project.status_code == 404


def test_get_project_positive():
    # Создаем проект
    body = {
        "title": "test get poz"
    }
    project = requests.post(
        base_url+"/api-v2/projects",
        json=body, headers=headers)
    # Получаем проект по ID
    project_id = project.json()['id']

    get_project = requests.get(
        base_url + "/api-v2/projects/" + project_id,
        headers=headers)

    assert get_project.status_code == 200
    assert get_project.json()["title"] == "test get poz"


def test_get_project_negative():
    # Создаем проект
    body = {
        "title": "test get neg"
    }
    project = requests.post(
        base_url+"/api-v2/projects",
        json=body, headers=headers)

    # Удаляем проект
    project_id = project.json()['id']

    body = {
        "deleted": True,
        "title": "test get neg"
    }
    project = requests.put(
        base_url + "/api-v2/projects" + project_id,
        json=body, headers=headers)

    # Получаем удаленный проект
    get_project = requests.get(
        base_url + "/api-v2/projects" + project_id,
        headers=headers)

    assert get_project.status_code == 404
