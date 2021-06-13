from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def mto_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='mto:login'):
    """
    Decorator for views that checks that the logged in user is mto,
    redirects to the applicant's log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_mto and not u.is_archived and u.is_verified,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def varal_admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='varal_admin:login'):
    """
    Decorator for views that checks that the logged in user is varal admin,
    redirects to the applicant's log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_varal_admin and not u.is_archived,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
