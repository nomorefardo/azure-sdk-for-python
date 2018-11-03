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


class UpdateKbOperationDTO(Model):
    """Contains list of QnAs to be updated.

    :param add: An instance of CreateKbInputDTO for add operation
    :type add:
     ~azure.cognitiveservices.qnamaker.models.UpdateKbOperationDTOAdd
    :param delete: An instance of DeleteKbContentsDTO for delete Operation
    :type delete:
     ~azure.cognitiveservices.qnamaker.models.UpdateKbOperationDTODelete
    :param update: An instance of UpdateKbContentsDTO for Update Operation
    :type update:
     ~azure.cognitiveservices.qnamaker.models.UpdateKbOperationDTOUpdate
    """

    _attribute_map = {
        'add': {'key': 'add', 'type': 'UpdateKbOperationDTOAdd'},
        'delete': {'key': 'delete', 'type': 'UpdateKbOperationDTODelete'},
        'update': {'key': 'update', 'type': 'UpdateKbOperationDTOUpdate'},
    }

    def __init__(self, **kwargs):
        super(UpdateKbOperationDTO, self).__init__(**kwargs)
        self.add = kwargs.get('add', None)
        self.delete = kwargs.get('delete', None)
        self.update = kwargs.get('update', None)