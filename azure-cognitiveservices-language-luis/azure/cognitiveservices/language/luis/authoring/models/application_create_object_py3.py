# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationCreateObject(Model):
    """Properties for creating a new LUIS Application.

    All required parameters must be populated in order to send to Azure.

    :param culture: Required. The culture for the new application. It is the
     language that your app understands and speaks. E.g.: "en-us". Note: the
     culture cannot be changed after the app is created.
    :type culture: str
    :param domain: The domain for the new application. Optional. E.g.: Comics.
    :type domain: str
    :param description: Description of the new application. Optional.
    :type description: str
    :param initial_version_id: The initial version ID. Optional. Default value
     is: "0.1"
    :type initial_version_id: str
    :param usage_scenario: Defines the scenario for the new application.
     Optional. E.g.: IoT.
    :type usage_scenario: str
    :param name: Required. The name for the new application.
    :type name: str
    """

    _validation = {
        'culture': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'culture': {'key': 'culture', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'initial_version_id': {'key': 'initialVersionId', 'type': 'str'},
        'usage_scenario': {'key': 'usageScenario', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, culture: str, name: str, domain: str=None, description: str=None, initial_version_id: str=None, usage_scenario: str=None, **kwargs) -> None:
        super(ApplicationCreateObject, self).__init__(**kwargs)
        self.culture = culture
        self.domain = domain
        self.description = description
        self.initial_version_id = initial_version_id
        self.usage_scenario = usage_scenario
        self.name = name