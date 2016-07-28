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

from .pool_usage_metrics import PoolUsageMetrics
from .node_agent_sku import NodeAgentSku
from .image_reference import ImageReference
from .usage_statistics import UsageStatistics
from .resource_statistics import ResourceStatistics
from .pool_statistics import PoolStatistics
from .job_statistics import JobStatistics
from .name_value_pair import NameValuePair
from .delete_certificate_error import DeleteCertificateError
from .certificate import Certificate
from .application_package_reference import ApplicationPackageReference
from .application_summary import ApplicationSummary
from .certificate_add_parameter import CertificateAddParameter
from .file_properties import FileProperties
from .node_file import NodeFile
from .schedule import Schedule
from .job_constraints import JobConstraints
from .resource_file import ResourceFile
from .environment_setting import EnvironmentSetting
from .exit_conditions import ExitConditions
from .exit_code_mapping import ExitCodeMapping
from .exit_options import ExitOptions
from .exit_code_range_mapping import ExitCodeRangeMapping
from .task_constraints import TaskConstraints
from .job_manager_task import JobManagerTask
from .job_preparation_task import JobPreparationTask
from .job_release_task import JobReleaseTask
from .task_scheduling_policy import TaskSchedulingPolicy
from .start_task import StartTask
from .certificate_reference import CertificateReference
from .metadata_item import MetadataItem
from .pool_specification import PoolSpecification
from .cloud_service_configuration import CloudServiceConfiguration
from .virtual_machine_configuration import VirtualMachineConfiguration
from .windows_configuration import WindowsConfiguration
from .network_configuration import NetworkConfiguration
from .auto_pool_specification import AutoPoolSpecification
from .pool_information import PoolInformation
from .job_specification import JobSpecification
from .recent_job import RecentJob
from .job_schedule_execution_information import JobScheduleExecutionInformation
from .job_schedule_statistics import JobScheduleStatistics
from .cloud_job_schedule import CloudJobSchedule
from .job_schedule_add_parameter import JobScheduleAddParameter
from .job_scheduling_error import JobSchedulingError
from .job_execution_information import JobExecutionInformation
from .cloud_job import CloudJob
from .job_add_parameter import JobAddParameter
from .task_scheduling_error import TaskSchedulingError
from .job_preparation_task_execution_information import JobPreparationTaskExecutionInformation
from .job_release_task_execution_information import JobReleaseTaskExecutionInformation
from .job_preparation_and_release_task_execution_information import JobPreparationAndReleaseTaskExecutionInformation
from .auto_scale_run_error import AutoScaleRunError
from .auto_scale_run import AutoScaleRun
from .resize_error import ResizeError
from .cloud_pool import CloudPool
from .pool_add_parameter import PoolAddParameter
from .affinity_information import AffinityInformation
from .task_execution_information import TaskExecutionInformation
from .compute_node_information import ComputeNodeInformation
from .multi_instance_settings import MultiInstanceSettings
from .task_statistics import TaskStatistics
from .task_dependencies import TaskDependencies
from .task_id_range import TaskIdRange
from .cloud_task import CloudTask
from .task_add_parameter import TaskAddParameter
from .task_add_collection_parameter import TaskAddCollectionParameter
from .task_add_result import TaskAddResult
from .batch_error import BatchError, BatchErrorException
from .error_message import ErrorMessage
from .batch_error_detail import BatchErrorDetail
from .task_add_collection_result import TaskAddCollectionResult
from .subtask_information import SubtaskInformation
from .cloud_task_list_subtasks_result import CloudTaskListSubtasksResult
from .task_information import TaskInformation
from .start_task_information import StartTaskInformation
from .compute_node_error import ComputeNodeError
from .compute_node import ComputeNode
from .compute_node_user import ComputeNodeUser
from .compute_node_get_remote_login_settings_result import ComputeNodeGetRemoteLoginSettingsResult
from .job_schedule_patch_parameter import JobSchedulePatchParameter
from .job_schedule_update_parameter import JobScheduleUpdateParameter
from .job_disable_parameter import JobDisableParameter
from .job_terminate_parameter import JobTerminateParameter
from .job_patch_parameter import JobPatchParameter
from .job_update_parameter import JobUpdateParameter
from .pool_enable_auto_scale_parameter import PoolEnableAutoScaleParameter
from .pool_evaluate_auto_scale_parameter import PoolEvaluateAutoScaleParameter
from .pool_resize_parameter import PoolResizeParameter
from .pool_update_properties_parameter import PoolUpdatePropertiesParameter
from .pool_upgrade_os_parameter import PoolUpgradeOSParameter
from .pool_patch_parameter import PoolPatchParameter
from .task_update_parameter import TaskUpdateParameter
from .node_update_user_parameter import NodeUpdateUserParameter
from .node_reboot_parameter import NodeRebootParameter
from .node_reimage_parameter import NodeReimageParameter
from .node_disable_scheduling_parameter import NodeDisableSchedulingParameter
from .node_remove_parameter import NodeRemoveParameter
from .application_list_options import ApplicationListOptions
from .application_get_options import ApplicationGetOptions
from .pool_list_pool_usage_metrics_options import PoolListPoolUsageMetricsOptions
from .account_list_node_agent_skus_options import AccountListNodeAgentSkusOptions
from .pool_get_all_pools_lifetime_statistics_options import PoolGetAllPoolsLifetimeStatisticsOptions
from .job_get_all_jobs_lifetime_statistics_options import JobGetAllJobsLifetimeStatisticsOptions
from .certificate_add_options import CertificateAddOptions
from .certificate_list_options import CertificateListOptions
from .certificate_cancel_deletion_options import CertificateCancelDeletionOptions
from .certificate_delete_options import CertificateDeleteOptions
from .certificate_get_options import CertificateGetOptions
from .file_delete_from_task_options import FileDeleteFromTaskOptions
from .file_get_from_task_options import FileGetFromTaskOptions
from .file_get_node_file_properties_from_task_options import FileGetNodeFilePropertiesFromTaskOptions
from .file_delete_from_compute_node_options import FileDeleteFromComputeNodeOptions
from .file_get_from_compute_node_options import FileGetFromComputeNodeOptions
from .file_get_node_file_properties_from_compute_node_options import FileGetNodeFilePropertiesFromComputeNodeOptions
from .file_list_from_task_options import FileListFromTaskOptions
from .file_list_from_compute_node_options import FileListFromComputeNodeOptions
from .job_schedule_exists_options import JobScheduleExistsOptions
from .job_schedule_delete_options import JobScheduleDeleteOptions
from .job_schedule_get_options import JobScheduleGetOptions
from .job_schedule_patch_options import JobSchedulePatchOptions
from .job_schedule_update_options import JobScheduleUpdateOptions
from .job_schedule_disable_options import JobScheduleDisableOptions
from .job_schedule_enable_options import JobScheduleEnableOptions
from .job_schedule_terminate_options import JobScheduleTerminateOptions
from .job_schedule_add_options import JobScheduleAddOptions
from .job_schedule_list_options import JobScheduleListOptions
from .job_delete_options import JobDeleteOptions
from .job_get_options import JobGetOptions
from .job_patch_options import JobPatchOptions
from .job_update_options import JobUpdateOptions
from .job_disable_options import JobDisableOptions
from .job_enable_options import JobEnableOptions
from .job_terminate_options import JobTerminateOptions
from .job_add_options import JobAddOptions
from .job_list_options import JobListOptions
from .job_list_from_job_schedule_options import JobListFromJobScheduleOptions
from .job_list_preparation_and_release_task_status_options import JobListPreparationAndReleaseTaskStatusOptions
from .pool_add_options import PoolAddOptions
from .pool_list_options import PoolListOptions
from .pool_delete_options import PoolDeleteOptions
from .pool_exists_options import PoolExistsOptions
from .pool_get_options import PoolGetOptions
from .pool_patch_options import PoolPatchOptions
from .pool_disable_auto_scale_options import PoolDisableAutoScaleOptions
from .pool_enable_auto_scale_options import PoolEnableAutoScaleOptions
from .pool_evaluate_auto_scale_options import PoolEvaluateAutoScaleOptions
from .pool_resize_options import PoolResizeOptions
from .pool_stop_resize_options import PoolStopResizeOptions
from .pool_update_properties_options import PoolUpdatePropertiesOptions
from .pool_upgrade_os_options import PoolUpgradeOSOptions
from .pool_remove_nodes_options import PoolRemoveNodesOptions
from .task_add_options import TaskAddOptions
from .task_list_options import TaskListOptions
from .task_add_collection_options import TaskAddCollectionOptions
from .task_delete_options import TaskDeleteOptions
from .task_get_options import TaskGetOptions
from .task_update_options import TaskUpdateOptions
from .task_list_subtasks_options import TaskListSubtasksOptions
from .task_terminate_options import TaskTerminateOptions
from .compute_node_add_user_options import ComputeNodeAddUserOptions
from .compute_node_delete_user_options import ComputeNodeDeleteUserOptions
from .compute_node_update_user_options import ComputeNodeUpdateUserOptions
from .compute_node_get_options import ComputeNodeGetOptions
from .compute_node_reboot_options import ComputeNodeRebootOptions
from .compute_node_reimage_options import ComputeNodeReimageOptions
from .compute_node_disable_scheduling_options import ComputeNodeDisableSchedulingOptions
from .compute_node_enable_scheduling_options import ComputeNodeEnableSchedulingOptions
from .compute_node_get_remote_login_settings_options import ComputeNodeGetRemoteLoginSettingsOptions
from .compute_node_get_remote_desktop_options import ComputeNodeGetRemoteDesktopOptions
from .compute_node_list_options import ComputeNodeListOptions
from .application_summary_paged import ApplicationSummaryPaged
from .pool_usage_metrics_paged import PoolUsageMetricsPaged
from .node_agent_sku_paged import NodeAgentSkuPaged
from .certificate_paged import CertificatePaged
from .node_file_paged import NodeFilePaged
from .cloud_job_schedule_paged import CloudJobSchedulePaged
from .cloud_job_paged import CloudJobPaged
from .job_preparation_and_release_task_execution_information_paged import JobPreparationAndReleaseTaskExecutionInformationPaged
from .cloud_pool_paged import CloudPoolPaged
from .cloud_task_paged import CloudTaskPaged
from .compute_node_paged import ComputeNodePaged
from .batch_service_client_enums import (
    OSType,
    CertificateState,
    CertificateFormat,
    JobAction,
    ComputeNodeFillType,
    CertificateStoreLocation,
    CertificateVisibility,
    PoolLifetimeOption,
    JobScheduleState,
    SchedulingErrorCategory,
    JobState,
    OnAllTasksComplete,
    OnTaskFailure,
    JobPreparationTaskState,
    JobReleaseTaskState,
    PoolState,
    AllocationState,
    TaskState,
    TaskAddStatus,
    StartTaskState,
    ComputeNodeState,
    SchedulingState,
    DisableJobOption,
    ComputeNodeDeallocationOption,
    ComputeNodeRebootOption,
    ComputeNodeReimageOption,
    DisableComputeNodeSchedulingOption,
)

__all__ = [
    'PoolUsageMetrics',
    'NodeAgentSku',
    'ImageReference',
    'UsageStatistics',
    'ResourceStatistics',
    'PoolStatistics',
    'JobStatistics',
    'NameValuePair',
    'DeleteCertificateError',
    'Certificate',
    'ApplicationPackageReference',
    'ApplicationSummary',
    'CertificateAddParameter',
    'FileProperties',
    'NodeFile',
    'Schedule',
    'JobConstraints',
    'ResourceFile',
    'EnvironmentSetting',
    'ExitConditions',
    'ExitCodeMapping',
    'ExitOptions',
    'ExitCodeRangeMapping',
    'TaskConstraints',
    'JobManagerTask',
    'JobPreparationTask',
    'JobReleaseTask',
    'TaskSchedulingPolicy',
    'StartTask',
    'CertificateReference',
    'MetadataItem',
    'PoolSpecification',
    'CloudServiceConfiguration',
    'VirtualMachineConfiguration',
    'WindowsConfiguration',
    'NetworkConfiguration',
    'AutoPoolSpecification',
    'PoolInformation',
    'JobSpecification',
    'RecentJob',
    'JobScheduleExecutionInformation',
    'JobScheduleStatistics',
    'CloudJobSchedule',
    'JobScheduleAddParameter',
    'JobSchedulingError',
    'JobExecutionInformation',
    'CloudJob',
    'JobAddParameter',
    'TaskSchedulingError',
    'JobPreparationTaskExecutionInformation',
    'JobReleaseTaskExecutionInformation',
    'JobPreparationAndReleaseTaskExecutionInformation',
    'AutoScaleRunError',
    'AutoScaleRun',
    'ResizeError',
    'CloudPool',
    'PoolAddParameter',
    'AffinityInformation',
    'TaskExecutionInformation',
    'ComputeNodeInformation',
    'MultiInstanceSettings',
    'TaskStatistics',
    'TaskDependencies',
    'TaskIdRange',
    'CloudTask',
    'TaskAddParameter',
    'TaskAddCollectionParameter',
    'TaskAddResult',
    'BatchError', 'BatchErrorException',
    'ErrorMessage',
    'BatchErrorDetail',
    'TaskAddCollectionResult',
    'SubtaskInformation',
    'CloudTaskListSubtasksResult',
    'TaskInformation',
    'StartTaskInformation',
    'ComputeNodeError',
    'ComputeNode',
    'ComputeNodeUser',
    'ComputeNodeGetRemoteLoginSettingsResult',
    'JobSchedulePatchParameter',
    'JobScheduleUpdateParameter',
    'JobDisableParameter',
    'JobTerminateParameter',
    'JobPatchParameter',
    'JobUpdateParameter',
    'PoolEnableAutoScaleParameter',
    'PoolEvaluateAutoScaleParameter',
    'PoolResizeParameter',
    'PoolUpdatePropertiesParameter',
    'PoolUpgradeOSParameter',
    'PoolPatchParameter',
    'TaskUpdateParameter',
    'NodeUpdateUserParameter',
    'NodeRebootParameter',
    'NodeReimageParameter',
    'NodeDisableSchedulingParameter',
    'NodeRemoveParameter',
    'ApplicationListOptions',
    'ApplicationGetOptions',
    'PoolListPoolUsageMetricsOptions',
    'AccountListNodeAgentSkusOptions',
    'PoolGetAllPoolsLifetimeStatisticsOptions',
    'JobGetAllJobsLifetimeStatisticsOptions',
    'CertificateAddOptions',
    'CertificateListOptions',
    'CertificateCancelDeletionOptions',
    'CertificateDeleteOptions',
    'CertificateGetOptions',
    'FileDeleteFromTaskOptions',
    'FileGetFromTaskOptions',
    'FileGetNodeFilePropertiesFromTaskOptions',
    'FileDeleteFromComputeNodeOptions',
    'FileGetFromComputeNodeOptions',
    'FileGetNodeFilePropertiesFromComputeNodeOptions',
    'FileListFromTaskOptions',
    'FileListFromComputeNodeOptions',
    'JobScheduleExistsOptions',
    'JobScheduleDeleteOptions',
    'JobScheduleGetOptions',
    'JobSchedulePatchOptions',
    'JobScheduleUpdateOptions',
    'JobScheduleDisableOptions',
    'JobScheduleEnableOptions',
    'JobScheduleTerminateOptions',
    'JobScheduleAddOptions',
    'JobScheduleListOptions',
    'JobDeleteOptions',
    'JobGetOptions',
    'JobPatchOptions',
    'JobUpdateOptions',
    'JobDisableOptions',
    'JobEnableOptions',
    'JobTerminateOptions',
    'JobAddOptions',
    'JobListOptions',
    'JobListFromJobScheduleOptions',
    'JobListPreparationAndReleaseTaskStatusOptions',
    'PoolAddOptions',
    'PoolListOptions',
    'PoolDeleteOptions',
    'PoolExistsOptions',
    'PoolGetOptions',
    'PoolPatchOptions',
    'PoolDisableAutoScaleOptions',
    'PoolEnableAutoScaleOptions',
    'PoolEvaluateAutoScaleOptions',
    'PoolResizeOptions',
    'PoolStopResizeOptions',
    'PoolUpdatePropertiesOptions',
    'PoolUpgradeOSOptions',
    'PoolRemoveNodesOptions',
    'TaskAddOptions',
    'TaskListOptions',
    'TaskAddCollectionOptions',
    'TaskDeleteOptions',
    'TaskGetOptions',
    'TaskUpdateOptions',
    'TaskListSubtasksOptions',
    'TaskTerminateOptions',
    'ComputeNodeAddUserOptions',
    'ComputeNodeDeleteUserOptions',
    'ComputeNodeUpdateUserOptions',
    'ComputeNodeGetOptions',
    'ComputeNodeRebootOptions',
    'ComputeNodeReimageOptions',
    'ComputeNodeDisableSchedulingOptions',
    'ComputeNodeEnableSchedulingOptions',
    'ComputeNodeGetRemoteLoginSettingsOptions',
    'ComputeNodeGetRemoteDesktopOptions',
    'ComputeNodeListOptions',
    'ApplicationSummaryPaged',
    'PoolUsageMetricsPaged',
    'NodeAgentSkuPaged',
    'CertificatePaged',
    'NodeFilePaged',
    'CloudJobSchedulePaged',
    'CloudJobPaged',
    'JobPreparationAndReleaseTaskExecutionInformationPaged',
    'CloudPoolPaged',
    'CloudTaskPaged',
    'ComputeNodePaged',
    'OSType',
    'CertificateState',
    'CertificateFormat',
    'JobAction',
    'ComputeNodeFillType',
    'CertificateStoreLocation',
    'CertificateVisibility',
    'PoolLifetimeOption',
    'JobScheduleState',
    'SchedulingErrorCategory',
    'JobState',
    'OnAllTasksComplete',
    'OnTaskFailure',
    'JobPreparationTaskState',
    'JobReleaseTaskState',
    'PoolState',
    'AllocationState',
    'TaskState',
    'TaskAddStatus',
    'StartTaskState',
    'ComputeNodeState',
    'SchedulingState',
    'DisableJobOption',
    'ComputeNodeDeallocationOption',
    'ComputeNodeRebootOption',
    'ComputeNodeReimageOption',
    'DisableComputeNodeSchedulingOption',
]
