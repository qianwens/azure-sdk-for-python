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

from msrest.paging import Paged


class BatchAccountPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BatchAccount <azure.mgmt.batch.models.BatchAccount>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BatchAccount]'}
    }

    def __init__(self, *args, **kwargs):

        super(BatchAccountPaged, self).__init__(*args, **kwargs)


class ApplicationPackagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationPackage <azure.mgmt.batch.models.ApplicationPackage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationPackage]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationPackagePaged, self).__init__(*args, **kwargs)


class ApplicationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Application <azure.mgmt.batch.models.Application>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Application]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationPaged, self).__init__(*args, **kwargs)


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.batch.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)


class CertificatePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Certificate <azure.mgmt.batch.models.Certificate>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Certificate]'}
    }

    def __init__(self, *args, **kwargs):

        super(CertificatePaged, self).__init__(*args, **kwargs)


class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.batch.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)


class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.batch.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)


class PoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Pool <azure.mgmt.batch.models.Pool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Pool]'}
    }

    def __init__(self, *args, **kwargs):

        super(PoolPaged, self).__init__(*args, **kwargs)
