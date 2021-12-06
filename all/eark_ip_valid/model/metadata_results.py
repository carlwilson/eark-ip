# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from eark_ip_valid.model.base_model_ import Model
from eark_ip_valid.model.metadata_checks import MetadataChecks  # noqa: F401,E501
from eark_ip_valid import util


class MetadataResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, schema_results: MetadataChecks=None, schematron_results: MetadataChecks=None):  # noqa: E501
        """MetadataResults - a model defined in Swagger

        :param schema_results: The schema_results of this MetadataResults.  # noqa: E501
        :type schema_results: MetadataChecks
        :param schematron_results: The schematron_results of this MetadataResults.  # noqa: E501
        :type schematron_results: MetadataChecks
        """
        self.swagger_types = {
            'schema_results': MetadataChecks,
            'schematron_results': MetadataChecks
        }

        self.attribute_map = {
            'schema_results': 'schemaResults',
            'schematron_results': 'schematronResults'
        }
        self._schema_results = schema_results
        self._schematron_results = schematron_results

    @classmethod
    def from_dict(cls, dikt) -> 'MetadataResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metadataResults of this MetadataResults.  # noqa: E501
        :rtype: MetadataResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schema_results(self) -> MetadataChecks:
        """Gets the schema_results of this MetadataResults.


        :return: The schema_results of this MetadataResults.
        :rtype: MetadataChecks
        """
        return self._schema_results

    @schema_results.setter
    def schema_results(self, schema_results: MetadataChecks):
        """Sets the schema_results of this MetadataResults.


        :param schema_results: The schema_results of this MetadataResults.
        :type schema_results: MetadataChecks
        """

        self._schema_results = schema_results

    @property
    def schematron_results(self) -> MetadataChecks:
        """Gets the schematron_results of this MetadataResults.


        :return: The schematron_results of this MetadataResults.
        :rtype: MetadataChecks
        """
        return self._schematron_results

    @schematron_results.setter
    def schematron_results(self, schematron_results: MetadataChecks):
        """Sets the schematron_results of this MetadataResults.


        :param schematron_results: The schematron_results of this MetadataResults.
        :type schematron_results: MetadataChecks
        """

        self._schematron_results = schematron_results
