# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from eark_ip_valid.model.base_model_ import Model
from eark_ip_valid.model.ip_type import IpType  # noqa: F401,E501
from eark_ip_valid import util


class ProfileDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: IpType=None, name: str=None, version: str=None):  # noqa: E501
        """ProfileDetails - a model defined in Swagger

        :param type: The type of this ProfileDetails.  # noqa: E501
        :type type: IpType
        :param name: The name of this ProfileDetails.  # noqa: E501
        :type name: str
        :param version: The version of this ProfileDetails.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'type': IpType,
            'name': str,
            'version': str
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'version': 'version'
        }
        self._type = type
        self._name = name
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'ProfileDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The profileDetails of this ProfileDetails.  # noqa: E501
        :rtype: ProfileDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> IpType:
        """Gets the type of this ProfileDetails.


        :return: The type of this ProfileDetails.
        :rtype: IpType
        """
        return self._type

    @type.setter
    def type(self, type: IpType):
        """Sets the type of this ProfileDetails.


        :param type: The type of this ProfileDetails.
        :type type: IpType
        """

        self._type = type

    @property
    def name(self) -> str:
        """Gets the name of this ProfileDetails.


        :return: The name of this ProfileDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ProfileDetails.


        :param name: The name of this ProfileDetails.
        :type name: str
        """

        self._name = name

    @property
    def version(self) -> str:
        """Gets the version of this ProfileDetails.


        :return: The version of this ProfileDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this ProfileDetails.


        :param version: The version of this ProfileDetails.
        :type version: str
        """

        self._version = version