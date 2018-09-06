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

from .resource_py3 import Resource


class PowerShellCommandStatus(Resource):
    """Result status from invoking a PowerShell command.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Manager Resource ID.
    :vartype id: str
    :ivar type: Resource Manager Resource Type.
    :vartype type: str
    :ivar name: Resource Manager Resource Name.
    :vartype name: str
    :ivar location: Resource Manager Resource Location.
    :vartype location: str
    :param tags: Resource Manager Resource Tags.
    :type tags: dict[str, str]
    :param etag:
    :type etag: str
    :param results:
    :type results:
     list[~azure.mgmt.servermanager.models.PowerShellCommandResult]
    :param pssession:
    :type pssession: str
    :param command:
    :type command: str
    :param completed:
    :type completed: bool
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'location': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'results': {'key': 'properties.results', 'type': '[PowerShellCommandResult]'},
        'pssession': {'key': 'properties.pssession', 'type': 'str'},
        'command': {'key': 'properties.command', 'type': 'str'},
        'completed': {'key': 'properties.completed', 'type': 'bool'},
    }

    def __init__(self, *, tags=None, etag: str=None, results=None, pssession: str=None, command: str=None, completed: bool=None, **kwargs) -> None:
        super(PowerShellCommandStatus, self).__init__(tags=tags, etag=etag, **kwargs)
        self.results = results
        self.pssession = pssession
        self.command = command
        self.completed = completed