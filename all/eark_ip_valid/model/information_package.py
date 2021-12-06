# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from eark_ip_valid.model.base_model_ import Model
from eark_ip_valid.model.package_details import PackageDetails  # noqa: F401,E501
from eark_ip_valid.model.profile_details import ProfileDetails  # noqa: F401,E501
from eark_ip_valid.model.representation import Representation  # noqa: F401,E501
from eark_ip_valid import util


class InformationPackage(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, details: PackageDetails=None, profile: ProfileDetails=None, representations: Representation=None):  # noqa: E501
        """InformationPackage - a model defined in Swagger

        :param details: The details of this InformationPackage.  # noqa: E501
        :type details: PackageDetails
        :param profile: The profile of this InformationPackage.  # noqa: E501
        :type profile: ProfileDetails
        :param representations: The representations of this InformationPackage.  # noqa: E501
        :type representations: Representation
        """
        self.swagger_types = {
            'details': PackageDetails,
            'profile': ProfileDetails,
            'representations': Representation
        }

        self.attribute_map = {
            'details': 'details',
            'profile': 'profile',
            'representations': 'representations'
        }
        self._details = details
        self._profile = profile
        self._representations = representations

    @classmethod
    def from_dict(cls, dikt) -> 'InformationPackage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The informationPackage of this InformationPackage.  # noqa: E501
        :rtype: InformationPackage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def details(self) -> PackageDetails:
        """Gets the details of this InformationPackage.


        :return: The details of this InformationPackage.
        :rtype: PackageDetails
        """
        return self._details

    @details.setter
    def details(self, details: PackageDetails):
        """Sets the details of this InformationPackage.


        :param details: The details of this InformationPackage.
        :type details: PackageDetails
        """

        self._details = details

    @property
    def profile(self) -> ProfileDetails:
        """Gets the profile of this InformationPackage.


        :return: The profile of this InformationPackage.
        :rtype: ProfileDetails
        """
        return self._profile

    @profile.setter
    def profile(self, profile: ProfileDetails):
        """Sets the profile of this InformationPackage.


        :param profile: The profile of this InformationPackage.
        :type profile: ProfileDetails
        """

        self._profile = profile

    @property
    def representations(self) -> Representation:
        """Gets the representations of this InformationPackage.


        :return: The representations of this InformationPackage.
        :rtype: Representation
        """
        return self._representations

    @representations.setter
    def representations(self, representations: Representation):
        """Sets the representations of this InformationPackage.


        :param representations: The representations of this InformationPackage.
        :type representations: Representation
        """

        self._representations = representations
