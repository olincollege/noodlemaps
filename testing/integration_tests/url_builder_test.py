import pytest
from src.utils.url_builder import UrlBuilder


@pytest.mark.parametrize('url', ['github.com', 'https://github.com', 'https://maps.google.com'])
def test_base_url(url):
    """
    Test for just a base URL (no subdomains or parameters)
    :param url: a string, the base URL
    """
    assert str(UrlBuilder(url)) == url


def test_single_subdomain():
    """
    Test a URL with a single subdomain
    """
    ub = UrlBuilder('https://github.com')
    ub.append_subdomain('olincollege')
    assert str(ub) == 'https://github.com/olincollege'


def test_multiple_single_subdomains():
    """
    Test a URL with multiple subdomains by calling the append_subdomain function multiple times
    """
    ub = UrlBuilder('https://github.com')
    ub.append_subdomain('olincollege')
    ub.append_subdomain('noodlemaps')
    assert str(ub) == 'https://github.com/olincollege/noodlemaps'


def test_multiple_subdomains():
    """
    Test a URL with multiple subdomains
    """
    ub = UrlBuilder('https://github.com')
    ub.append_subdomains(['olincollege', 'noodlemaps'])
    assert str(ub) == 'https://github.com/olincollege/noodlemaps'


def test_single_parameter():
    """
    Test a URL with one parameter
    """
    ub = UrlBuilder('https://maps.googleapis.com')
    ub.set_properties(origins='Boston')
    assert str(ub) == 'https://maps.googleapis.com?origins=Boston'


def test_special_character_parameter():
    """
    Test a URL with a parameter that uses special characters
    """
    ub = UrlBuilder('https://maps.googleapis.com')
    ub.set_properties(origins='Boston, MA')
    assert str(ub) == 'https://maps.googleapis.com?origins=Boston%2C%20MA'


def test_list_parameter():
    """
    Test a URL with a parameter which is a list
    """
    ub = UrlBuilder('https://maps.googleapis.com')
    ub.set_properties(origins=['Boston, MA', 'Needham, MA', 'Wellesley, MA'])
    assert str(ub) == 'https://maps.googleapis.com?origins=Boston%2C%20MA%7CNeedham%2C%20MA%7CWellesley%2C%20MA'


def test_multiple_single_parameters():
    """
    Test a URL with multiple parameters that calls set_properties multiple times
    """
    ub = UrlBuilder('https://maps.googleapis.com')
    ub.set_properties(origins='Boston, MA')
    ub.set_properties(destinations='Needham')
    assert str(ub) == 'https://maps.googleapis.com?origins=Boston%2C%20MA&destinations=Needham'


def test_multiple_parameters():
    """
    Test a URL with multiple parameters
    """
    ub = UrlBuilder('https://maps.googleapis.com')
    ub.set_properties(origins='Boston, MA', destinations='Needham')
    assert str(ub) == 'https://maps.googleapis.com?origins=Boston%2C%20MA&destinations=Needham'


def test_subpages_and_parameters():
    """
    Test a URL that has both subpages and parameters
    """
    ub = UrlBuilder('https://maps.googleapis.com')
    ub.append_subdomains(['maps', 'api', 'distancematrix', 'json'])
    ub.set_properties(origins=['Boston, MA', 'Needham, MA', 'Wellesley, MA'], destinations='Olin College')
    assert str(ub) == 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Boston%2C%20MA%7CNeedham%2C%20'\
        'MA%7CWellesley%2C%20MA&destinations=Olin%20College'
