from univer_table import UniverTable


db = UniverTable("postgresql://postgres:E$3L@localhost:5432/QA")


def test_insert_subject():
    test_title = "test_insert"
    max_id_before = db.get_max_id()
    db.insert_subject(test_title, max_id_before + 1)
    max_id_after = db.get_max_id()
    subject = db.get_subject_by_id(max_id_after)

    assert max_id_before < max_id_after
    assert subject[0]["subject_title"] == test_title
    db.delete_subject(max_id_after)


def test_update_subject():
    test_title_up = "test_update"
    max_id = db.get_max_id()
    db.insert_subject("test_intermediate", max_id + 1)
    new_id = db.get_max_id()
    db.update_subject(test_title_up, new_id)
    subject = db.get_subject_by_id(new_id)

    assert len(subject) == 1
    assert subject[0]["subject_title"] == test_title_up
    db.delete_subject(new_id)


def test_delete_subject():
    test_title = "test_delete"
    max_id_before = db.get_max_id()
    db.insert_subject(test_title, max_id_before + 1)
    max_id_after_insert = db.get_max_id()
    subject = db.get_subject_by_id(max_id_after_insert)

    assert max_id_before < max_id_after_insert
    assert subject[0]["subject_title"] == test_title

    db.delete_subject(max_id_after_insert)
    subject = db.get_subject_by_id(max_id_after_insert)
    max_id_after_delete = db.get_max_id()

    assert len(subject) == 0
    assert max_id_after_insert > max_id_after_delete
