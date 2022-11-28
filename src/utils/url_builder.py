"""
Module to deal with building URLs
"""
from typing import *
import urllib.parse


class UrlBuilder:
    """
    Class to build URLs from a set of inputs

    Attributes:
        base_url: str, the base url to build from (i.e. https://github.com)
        subdomains: a list of strings, the sub-pages from the base url (i.e. olincollege and noodlemaps in
            https://github.com/olincollege/noodlemaps
        properties: a dict from strings to strings or lists of strings, the variables to add to the end of the URL
    """
    def __init__(self, base_url: str, subdomains: Optional[List[str]] = None, properties:
                 Optional[Dict[str,Union[str,List[str]]]] = None):
        """
        Initializes this UrlBuilder
        """
        self.base_url = base_url
        self.subdomains = [] if subdomains is None else subdomains
        self.properties = {} if properties is None else properties

    def append_subdomain(self, subdomain: str):
        """
        Adds a new subdomain to the end of this URL

        :param subdomain: a str, the subdomain to add
        """
        self.subdomains.append(subdomain)

    def append_subdomains(self, subdomains: List[str]):
        """
        Adds new subdomains to the end of this URL

        :param subdomains: the ordered list of subdomains (strings) to add
        """
        self.subdomains.extend(subdomains)

    def set_properties(self, **props):
        """
        Adds new properies and values to the end of this URL

        :param props: a dict of strings to either strings or lists of strings, the properties to add
        """
        for k, v in props.items():
            self.properties[k] = v

    def _property_string(self, prop):
        """
        Formats the string of this given property

        :return: the formatted string of the given property
        """
        val = self.properties[prop]
        if isinstance(val, str):
            return urllib.parse.quote(val, safe='')
        return urllib.parse.quote('|'.join(val), safe='')

    def __str__(self) -> str:
        """
        Builds this URL

        :return: the string representation of this URL
        """
        domains = [self.base_url] + self.subdomains
        url_with_subpages = '/'.join(domains)
        if len(self.properties) == 0:
            return url_with_subpages
        final_url = url_with_subpages + '?' + '&'.join(f'{p}={self._property_string(p)}' for p in self.properties)
        return final_url
