class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin', 'user', 'mto'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'vendor_os'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'vendor_os'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'vendor_os'
        return 'varal_job_posting'


class AccountRouter:
    """
    A router to control all accounts database operations on models in the
    account application.
    """
    route_app_labels = {'account'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'accounts'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write account models go to accounts.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'accounts'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the account apps is
        involved.
        """
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the account app only appear in the
        'accounts' database.
        """
        if app_label in self.route_app_labels:
            return db == 'accounts'
        return None


class JobRouter:
    """
    A router to control all varal_job_posting database operations on models in the
    jobs application.
    """
    route_app_labels = {'user', 'jobs'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read jobs models go to varal_job_posting.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'varal_job_posting'
        return 'vendor_os'

    def db_for_write(self, model, **hints):
        """
        Attempts to write jobs models go to varal_job_posting.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'varal_job_posting'
        return 'vendor_os'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the jobs apps is
        involved.
        """
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        elif 'vendor_os' in [obj1._meta.app_label, obj2._meta.app_label]:
            return True

        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the jos app only appear in the
        'varal_job_posting' database.
        """
        if app_label in self.route_app_labels:
            return db == 'varal_job_posting'
        return 'vendor_os'
