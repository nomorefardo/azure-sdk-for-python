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


class Error(Model):
    """The error object. As per Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. One of a server-defined set of error codes.
     Possible values include: 'BadArgument', 'Forbidden', 'NotFound',
     'KbNotFound', 'Unauthorized', 'Unspecified', 'EndpointKeysError',
     'QuotaExceeded', 'QnaRuntimeError', 'SKULimitExceeded',
     'OperationNotFound', 'ServiceError', 'ValidationFailure',
     'ExtractionFailure'
    :type code: str or ~azure.cognitiveservices.qnamaker.models.enum
    :param message: A human-readable representation of the error.
    :type message: str
    :param target: The target of the error.
    :type target: str
    :param details: An array of details about specific errors that led to this
     reported error.
    :type details: list[~azure.cognitiveservices.qnamaker.models.Error]
    :param inner_error: An object containing more specific information than
     the current object about the error.
    :type inner_error:
     ~azure.cognitiveservices.qnamaker.models.InnerErrorModel
    """

    _validation = {
        'code': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Error]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorModel'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.inner_error = kwargs.get('inner_error', None)