import connexion
import six

from eark_ip_valid.model.information_package import InformationPackage  # noqa: E501
from eark_ip_valid.model.package_details import PackageDetails  # noqa: E501
from eark_ip_valid.model.upload import Upload  # noqa: E501
from eark_ip_valid import util


def get_ip_by_uid(uid):  # noqa: E501
    """Get package info.

    Get the properties of an information package uid. # noqa: E501

    :param uid: UUID of the package to retrieve
    :type uid: 

    :rtype: InformationPackage
    """
    return 'do some magic!'


def get_ips():  # noqa: E501
    """Retrieve package binary details.

    Retrieve a list of package binaries uploaded to the validation service. # noqa: E501


    :rtype: List[Upload]
    """
    return 'do some magic!'


def post_ip(sha1=None, ip_file=None):  # noqa: E501
    """Upload package binary.

    Upload a package binary for validation, returns process identifier and digest. # noqa: E501

    :param sha1: 
    :type sha1: str
    :param ip_file: 
    :type ip_file: strstr

    :rtype: PackageDetails
    """
    return 'do some magic!'
