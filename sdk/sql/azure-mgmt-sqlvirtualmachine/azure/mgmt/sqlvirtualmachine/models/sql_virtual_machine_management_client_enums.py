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

from enum import Enum


class OperationOrigin(str, Enum):

    user = "user"
    system = "system"


class SqlVmGroupImageSku(str, Enum):

    developer = "Developer"
    enterprise = "Enterprise"


class ScaleType(str, Enum):

    ha = "HA"


class ClusterManagerType(str, Enum):

    wsfc = "WSFC"


class ClusterConfiguration(str, Enum):

    domainful = "Domainful"


class IdentityType(str, Enum):

    system_assigned = "SystemAssigned"


class SqlServerLicenseType(str, Enum):

    payg = "PAYG"
    ahub = "AHUB"


class SqlManagementMode(str, Enum):

    full = "Full"
    light_weight = "LightWeight"
    no_agent = "NoAgent"


class SqlImageSku(str, Enum):

    developer = "Developer"
    express = "Express"
    standard = "Standard"
    enterprise = "Enterprise"
    web = "Web"


class DayOfWeek(str, Enum):

    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class BackupScheduleType(str, Enum):

    manual = "Manual"
    automated = "Automated"


class FullBackupFrequencyType(str, Enum):

    daily = "Daily"
    weekly = "Weekly"


class ConnectivityType(str, Enum):

    local = "LOCAL"
    private = "PRIVATE"
    public = "PUBLIC"


class SqlWorkloadType(str, Enum):

    general = "GENERAL"
    oltp = "OLTP"
    dw = "DW"


class DiskConfigurationType(str, Enum):

    new = "NEW"
    extend = "EXTEND"
    add = "ADD"