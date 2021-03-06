# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Marketplace, we offer a wide selection of financial data feeds sourced by our own proprietary processes as well as from many data vendors. The primary application of the Intrinio API is for use in third-party applications and integrations or for end-users utilizing the Excel add-in and Google Sheets add-on. The Intrinio API uses HTTPS verbs and a RESTful endpoint structure, which makes it easy to request data from Intrinio. Responses are delivered in JSON format. If you need additional help in using the API, go to our home page (https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MutualFund(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'cusip': 'str',
        'vendor_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cusip': 'cusip',
        'vendor_id': 'vendor_id'
    }

    def __init__(self, id=None, name=None, cusip=None, vendor_id=None):  # noqa: E501
        """MutualFund - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._cusip = None
        self._vendor_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if cusip is not None:
            self.cusip = cusip
        if vendor_id is not None:
            self.vendor_id = vendor_id

    @property
    def id(self):
        """Gets the id of this MutualFund.  # noqa: E501

        The Intrinio ID of the mutual fund  # noqa: E501

        :return: The id of this MutualFund.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MutualFund.

        The Intrinio ID of the mutual fund  # noqa: E501

        :param id: The id of this MutualFund.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MutualFund.  # noqa: E501

        The mutual fund's common name  # noqa: E501

        :return: The name of this MutualFund.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MutualFund.

        The mutual fund's common name  # noqa: E501

        :param name: The name of this MutualFund.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cusip(self):
        """Gets the cusip of this MutualFund.  # noqa: E501

        The nine-character CUSIP identifier  # noqa: E501

        :return: The cusip of this MutualFund.  # noqa: E501
        :rtype: str
        """
        return self._cusip

    @cusip.setter
    def cusip(self, cusip):
        """Sets the cusip of this MutualFund.

        The nine-character CUSIP identifier  # noqa: E501

        :param cusip: The cusip of this MutualFund.  # noqa: E501
        :type: str
        """

        self._cusip = cusip

    @property
    def vendor_id(self):
        """Gets the vendor_id of this MutualFund.  # noqa: E501

        The vendor-provided id of the mutual fund  # noqa: E501

        :return: The vendor_id of this MutualFund.  # noqa: E501
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this MutualFund.

        The vendor-provided id of the mutual fund  # noqa: E501

        :param vendor_id: The vendor_id of this MutualFund.  # noqa: E501
        :type: str
        """

        self._vendor_id = vendor_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MutualFund):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
