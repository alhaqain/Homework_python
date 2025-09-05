from sqlalchemy import create_engine
from sqlalchemy.sql import text


class UniverTable:
    __scripts = {
        "select": text("select * from subject"),
        "select_by_id": text("select * from subject "
                             "where subject_id =:id_to_select"),
        "insert_new": text("insert into subject(\"subject_title\", "
                           "\"subject_id\") values (:new_title, :new_id)"),
        "delete_by_id": text("delete from subject "
                             "where subject_id =:id_to_delete"),
        "update_by_id": text("update subject set subject_title =:new_title "
                             "where subject_id =:id_to_update"),
        "get_max_id": text("select max (\"subject_id\") from subject")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_subject_by_id(self, id):
        return self.__db.execute(self.__scripts["select_by_id"],
                                 {"id_to_select": id}).fetchall()

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]

    def insert_subject(self, title, id):
        self.__db.execute(self.__scripts["insert_new"],
                          {"new_title": title, "new_id": id})

    def delete_subject(self, id):
        self.__db.execute(self.__scripts["delete_by_id"],
                          {"id_to_delete": id})

    def update_subject(self, title, id):
        self.__db.execute(self.__scripts["update_by_id"],
                          {"new_title": title, "id_to_update": id})
