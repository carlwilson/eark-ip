# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from eark_ip.model.base_model_ import Model
from eark_ip import util


class StructStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UNKNOWN = "Unknown"
    NOTWELLFORMED = "NotWellFormed"
    WELLFORMED = "WellFormed"
    def __init__(self):  # noqa: E501
        """StructStatus - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'StructStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The structStatus of this StructStatus.  # noqa: E501
        :rtype: StructStatus
        """
        return util.deserialize_model(dikt, cls)
