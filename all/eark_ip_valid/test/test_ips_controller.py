# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from eark_ip_valid.model.information_package import InformationPackage  # noqa: E501
from eark_ip_valid.model.package_details import PackageDetails  # noqa: E501
from eark_ip_valid.model.upload import Upload  # noqa: E501
from eark_ip_valid.test import BaseTestCase


class TestIpsController(BaseTestCase):
    """IpsController integration test stubs"""

    def test_get_ip_by_uid(self):
        """Test case for get_ip_by_uid

        Get package info.
        """
        response = self.client.open(
            '/ips/{uid}'.format(uid='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ips(self):
        """Test case for get_ips

        Retrieve package binary details.
        """
        response = self.client.open(
            '/ips',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_ip(self):
        """Test case for post_ip

        Upload package binary.
        """
        data = dict(sha1='sha1_example',
                    ip_file='ip_file_example')
        response = self.client.open(
            '/ips',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
