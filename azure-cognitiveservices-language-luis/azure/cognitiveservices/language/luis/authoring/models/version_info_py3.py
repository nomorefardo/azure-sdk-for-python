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


class VersionInfo(Model):
    """Object model of an application version.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. The version ID. E.g.: "0.1"
    :type version: str
    :param created_date_time: The version's creation timestamp.
    :type created_date_time: datetime
    :param last_modified_date_time: Timestamp of the last update.
    :type last_modified_date_time: datetime
    :param last_trained_date_time: Timestamp of the last time the model was
     trained.
    :type last_trained_date_time: datetime
    :param last_published_date_time: Timestamp when was last published.
    :type last_published_date_time: datetime
    :param endpoint_url: The Runtime endpoint URL for this model version.
    :type endpoint_url: str
    :param assigned_endpoint_key: The endpoint key.
    :type assigned_endpoint_key: dict[str, str]
    :param external_api_keys: External keys.
    :type external_api_keys: object
    :param intents_count: Number of intents in this model.
    :type intents_count: int
    :param entities_count: Number of entities in this model.
    :type entities_count: int
    :param endpoint_hits_count: Number of calls made to this endpoint.
    :type endpoint_hits_count: int
    :param training_status: Required. The current training status. Possible
     values include: 'NeedsTraining', 'InProgress', 'Trained'
    :type training_status: str or
     ~azure.cognitiveservices.language.luis.authoring.models.TrainingStatus
    """

    _validation = {
        'version': {'required': True},
        'training_status': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'last_trained_date_time': {'key': 'lastTrainedDateTime', 'type': 'iso-8601'},
        'last_published_date_time': {'key': 'lastPublishedDateTime', 'type': 'iso-8601'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'assigned_endpoint_key': {'key': 'assignedEndpointKey', 'type': '{str}'},
        'external_api_keys': {'key': 'externalApiKeys', 'type': 'object'},
        'intents_count': {'key': 'intentsCount', 'type': 'int'},
        'entities_count': {'key': 'entitiesCount', 'type': 'int'},
        'endpoint_hits_count': {'key': 'endpointHitsCount', 'type': 'int'},
        'training_status': {'key': 'trainingStatus', 'type': 'TrainingStatus'},
    }

    def __init__(self, *, version: str, training_status, created_date_time=None, last_modified_date_time=None, last_trained_date_time=None, last_published_date_time=None, endpoint_url: str=None, assigned_endpoint_key=None, external_api_keys=None, intents_count: int=None, entities_count: int=None, endpoint_hits_count: int=None, **kwargs) -> None:
        super(VersionInfo, self).__init__(**kwargs)
        self.version = version
        self.created_date_time = created_date_time
        self.last_modified_date_time = last_modified_date_time
        self.last_trained_date_time = last_trained_date_time
        self.last_published_date_time = last_published_date_time
        self.endpoint_url = endpoint_url
        self.assigned_endpoint_key = assigned_endpoint_key
        self.external_api_keys = external_api_keys
        self.intents_count = intents_count
        self.entities_count = entities_count
        self.endpoint_hits_count = endpoint_hits_count
        self.training_status = training_status
