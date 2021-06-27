class DBRouter:
    """
    A router to control all database operations on models
    """

    COLLEGE_DB = 'colleges'
    STUDENT_DB = 'students'

    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['student']:
            return self.STUDENT_DB
        return self.COLLEGE_DB

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['student']:
            return self.STUDENT_DB
        return self.COLLEGE_DB

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in ['student']:
            return db == self.STUDENT_DB
        return db == self.COLLEGE_DB
