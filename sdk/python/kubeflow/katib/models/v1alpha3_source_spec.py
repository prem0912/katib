# coding: utf-8

"""
    katib

    swagger description for katib  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha3SourceSpec(object):
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
        'file_system_path': 'V1alpha3FileSystemPath',
        'filter': 'V1alpha3FilterSpec',
        'http_get': 'V1HTTPGetAction'
    }

    attribute_map = {
        'file_system_path': 'fileSystemPath',
        'filter': 'filter',
        'http_get': 'httpGet'
    }

    def __init__(self, file_system_path=None, filter=None, http_get=None):  # noqa: E501
        """V1alpha3SourceSpec - a model defined in Swagger"""  # noqa: E501

        self._file_system_path = None
        self._filter = None
        self._http_get = None
        self.discriminator = None

        if file_system_path is not None:
            self.file_system_path = file_system_path
        if filter is not None:
            self.filter = filter
        if http_get is not None:
            self.http_get = http_get

    @property
    def file_system_path(self):
        """Gets the file_system_path of this V1alpha3SourceSpec.  # noqa: E501

        During training model, metrics may be persisted into local file in source code, such as tfEvent use case  # noqa: E501

        :return: The file_system_path of this V1alpha3SourceSpec.  # noqa: E501
        :rtype: V1alpha3FileSystemPath
        """
        return self._file_system_path

    @file_system_path.setter
    def file_system_path(self, file_system_path):
        """Sets the file_system_path of this V1alpha3SourceSpec.

        During training model, metrics may be persisted into local file in source code, such as tfEvent use case  # noqa: E501

        :param file_system_path: The file_system_path of this V1alpha3SourceSpec.  # noqa: E501
        :type: V1alpha3FileSystemPath
        """

        self._file_system_path = file_system_path

    @property
    def filter(self):
        """Gets the filter of this V1alpha3SourceSpec.  # noqa: E501

        Default metric output format is {\"metric\": \"<metric_name>\", \"value\": <int_or_float>, \"epoch\": <int>, \"step\": <int>}, but if the output doesn't follow default format, please extend it here  # noqa: E501

        :return: The filter of this V1alpha3SourceSpec.  # noqa: E501
        :rtype: V1alpha3FilterSpec
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this V1alpha3SourceSpec.

        Default metric output format is {\"metric\": \"<metric_name>\", \"value\": <int_or_float>, \"epoch\": <int>, \"step\": <int>}, but if the output doesn't follow default format, please extend it here  # noqa: E501

        :param filter: The filter of this V1alpha3SourceSpec.  # noqa: E501
        :type: V1alpha3FilterSpec
        """

        self._filter = filter

    @property
    def http_get(self):
        """Gets the http_get of this V1alpha3SourceSpec.  # noqa: E501

        Model-train source code can expose metrics by http, such as HTTP endpoint in prometheus metric format  # noqa: E501

        :return: The http_get of this V1alpha3SourceSpec.  # noqa: E501
        :rtype: V1HTTPGetAction
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """Sets the http_get of this V1alpha3SourceSpec.

        Model-train source code can expose metrics by http, such as HTTP endpoint in prometheus metric format  # noqa: E501

        :param http_get: The http_get of this V1alpha3SourceSpec.  # noqa: E501
        :type: V1HTTPGetAction
        """

        self._http_get = http_get

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
        if issubclass(V1alpha3SourceSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha3SourceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
