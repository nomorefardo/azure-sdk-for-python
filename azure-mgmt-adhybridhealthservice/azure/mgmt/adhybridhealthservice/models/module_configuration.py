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


class ModuleConfiguration(Model):
    """The module configuration as required by the Agent service.

    :param agent_service: The name of agent service.
    :type agent_service: str
    :param module_name: The name of the module for which the configuration is
     applicable.
    :type module_name: str
    :param properties: The key value pairs of properties required for
     configuration.
    :type properties: dict[str, str]
    """

    _attribute_map = {
        'agent_service': {'key': 'agentService', 'type': 'str'},
        'module_name': {'key': 'moduleName', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(ModuleConfiguration, self).__init__(**kwargs)
        self.agent_service = kwargs.get('agent_service', None)
        self.module_name = kwargs.get('module_name', None)
        self.properties = kwargs.get('properties', None)