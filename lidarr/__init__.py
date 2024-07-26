# coding: utf-8

# flake8: noqa

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.4.3.4248
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.1.0" # x-release-please-version

# import apis into sdk package
from lidarr.api.album_api import AlbumApi
from lidarr.api.album_lookup_api import AlbumLookupApi
from lidarr.api.album_studio_api import AlbumStudioApi
from lidarr.api.api_info_api import ApiInfoApi
from lidarr.api.artist_api import ArtistApi
from lidarr.api.artist_editor_api import ArtistEditorApi
from lidarr.api.artist_lookup_api import ArtistLookupApi
from lidarr.api.authentication_api import AuthenticationApi
from lidarr.api.auto_tagging_api import AutoTaggingApi
from lidarr.api.backup_api import BackupApi
from lidarr.api.blocklist_api import BlocklistApi
from lidarr.api.calendar_api import CalendarApi
from lidarr.api.calendar_feed_api import CalendarFeedApi
from lidarr.api.command_api import CommandApi
from lidarr.api.custom_filter_api import CustomFilterApi
from lidarr.api.custom_format_api import CustomFormatApi
from lidarr.api.cutoff_api import CutoffApi
from lidarr.api.delay_profile_api import DelayProfileApi
from lidarr.api.disk_space_api import DiskSpaceApi
from lidarr.api.download_client_api import DownloadClientApi
from lidarr.api.download_client_config_api import DownloadClientConfigApi
from lidarr.api.file_system_api import FileSystemApi
from lidarr.api.health_api import HealthApi
from lidarr.api.history_api import HistoryApi
from lidarr.api.host_config_api import HostConfigApi
from lidarr.api.import_list_api import ImportListApi
from lidarr.api.import_list_exclusion_api import ImportListExclusionApi
from lidarr.api.indexer_api import IndexerApi
from lidarr.api.indexer_config_api import IndexerConfigApi
from lidarr.api.indexer_flag_api import IndexerFlagApi
from lidarr.api.language_api import LanguageApi
from lidarr.api.localization_api import LocalizationApi
from lidarr.api.log_api import LogApi
from lidarr.api.log_file_api import LogFileApi
from lidarr.api.manual_import_api import ManualImportApi
from lidarr.api.media_cover_api import MediaCoverApi
from lidarr.api.media_management_config_api import MediaManagementConfigApi
from lidarr.api.metadata_api import MetadataApi
from lidarr.api.metadata_profile_api import MetadataProfileApi
from lidarr.api.metadata_profile_schema_api import MetadataProfileSchemaApi
from lidarr.api.metadata_provider_config_api import MetadataProviderConfigApi
from lidarr.api.missing_api import MissingApi
from lidarr.api.naming_config_api import NamingConfigApi
from lidarr.api.notification_api import NotificationApi
from lidarr.api.parse_api import ParseApi
from lidarr.api.ping_api import PingApi
from lidarr.api.quality_definition_api import QualityDefinitionApi
from lidarr.api.quality_profile_api import QualityProfileApi
from lidarr.api.quality_profile_schema_api import QualityProfileSchemaApi
from lidarr.api.queue_api import QueueApi
from lidarr.api.queue_action_api import QueueActionApi
from lidarr.api.queue_details_api import QueueDetailsApi
from lidarr.api.queue_status_api import QueueStatusApi
from lidarr.api.release_api import ReleaseApi
from lidarr.api.release_profile_api import ReleaseProfileApi
from lidarr.api.release_push_api import ReleasePushApi
from lidarr.api.remote_path_mapping_api import RemotePathMappingApi
from lidarr.api.rename_track_api import RenameTrackApi
from lidarr.api.retag_track_api import RetagTrackApi
from lidarr.api.root_folder_api import RootFolderApi
from lidarr.api.search_api import SearchApi
from lidarr.api.static_resource_api import StaticResourceApi
from lidarr.api.system_api import SystemApi
from lidarr.api.tag_api import TagApi
from lidarr.api.tag_details_api import TagDetailsApi
from lidarr.api.task_api import TaskApi
from lidarr.api.track_api import TrackApi
from lidarr.api.track_file_api import TrackFileApi
from lidarr.api.ui_config_api import UiConfigApi
from lidarr.api.update_api import UpdateApi
from lidarr.api.update_log_file_api import UpdateLogFileApi

# import ApiClient
from lidarr.api_response import ApiResponse
from lidarr.api_client import ApiClient
from lidarr.configuration import Configuration
from lidarr.exceptions import OpenApiException
from lidarr.exceptions import ApiTypeError
from lidarr.exceptions import ApiValueError
from lidarr.exceptions import ApiKeyError
from lidarr.exceptions import ApiAttributeError
from lidarr.exceptions import ApiException

# import models into sdk package
from lidarr.models.add_album_options import AddAlbumOptions
from lidarr.models.add_artist_options import AddArtistOptions
from lidarr.models.album_add_type import AlbumAddType
from lidarr.models.album_release_resource import AlbumReleaseResource
from lidarr.models.album_resource import AlbumResource
from lidarr.models.album_resource_paging_resource import AlbumResourcePagingResource
from lidarr.models.album_statistics_resource import AlbumStatisticsResource
from lidarr.models.album_studio_artist_resource import AlbumStudioArtistResource
from lidarr.models.album_studio_resource import AlbumStudioResource
from lidarr.models.albums_monitored_resource import AlbumsMonitoredResource
from lidarr.models.allow_fingerprinting import AllowFingerprinting
from lidarr.models.apply_tags import ApplyTags
from lidarr.models.artist_editor_resource import ArtistEditorResource
from lidarr.models.artist_resource import ArtistResource
from lidarr.models.artist_statistics_resource import ArtistStatisticsResource
from lidarr.models.artist_status_type import ArtistStatusType
from lidarr.models.artist_title_info import ArtistTitleInfo
from lidarr.models.authentication_required_type import AuthenticationRequiredType
from lidarr.models.authentication_type import AuthenticationType
from lidarr.models.auto_tagging_resource import AutoTaggingResource
from lidarr.models.auto_tagging_specification_schema import AutoTaggingSpecificationSchema
from lidarr.models.backup_resource import BackupResource
from lidarr.models.backup_type import BackupType
from lidarr.models.blocklist_bulk_resource import BlocklistBulkResource
from lidarr.models.blocklist_resource import BlocklistResource
from lidarr.models.blocklist_resource_paging_resource import BlocklistResourcePagingResource
from lidarr.models.certificate_validation_type import CertificateValidationType
from lidarr.models.command import Command
from lidarr.models.command_priority import CommandPriority
from lidarr.models.command_resource import CommandResource
from lidarr.models.command_result import CommandResult
from lidarr.models.command_status import CommandStatus
from lidarr.models.command_trigger import CommandTrigger
from lidarr.models.contract_field import ContractField
from lidarr.models.custom_filter_resource import CustomFilterResource
from lidarr.models.custom_format_resource import CustomFormatResource
from lidarr.models.custom_format_specification_schema import CustomFormatSpecificationSchema
from lidarr.models.database_type import DatabaseType
from lidarr.models.delay_profile_resource import DelayProfileResource
from lidarr.models.disk_space_resource import DiskSpaceResource
from lidarr.models.download_client_bulk_resource import DownloadClientBulkResource
from lidarr.models.download_client_config_resource import DownloadClientConfigResource
from lidarr.models.download_client_resource import DownloadClientResource
from lidarr.models.download_protocol import DownloadProtocol
from lidarr.models.entity_history_event_type import EntityHistoryEventType
from lidarr.models.file_date_type import FileDateType
from lidarr.models.health_check_result import HealthCheckResult
from lidarr.models.health_resource import HealthResource
from lidarr.models.history_resource import HistoryResource
from lidarr.models.history_resource_paging_resource import HistoryResourcePagingResource
from lidarr.models.host_config_resource import HostConfigResource
from lidarr.models.import_list_bulk_resource import ImportListBulkResource
from lidarr.models.import_list_exclusion_resource import ImportListExclusionResource
from lidarr.models.import_list_monitor_type import ImportListMonitorType
from lidarr.models.import_list_resource import ImportListResource
from lidarr.models.import_list_type import ImportListType
from lidarr.models.indexer_bulk_resource import IndexerBulkResource
from lidarr.models.indexer_config_resource import IndexerConfigResource
from lidarr.models.indexer_flag_resource import IndexerFlagResource
from lidarr.models.indexer_resource import IndexerResource
from lidarr.models.iso_country import IsoCountry
from lidarr.models.language_resource import LanguageResource
from lidarr.models.links import Links
from lidarr.models.localization_resource import LocalizationResource
from lidarr.models.log_file_resource import LogFileResource
from lidarr.models.log_resource import LogResource
from lidarr.models.log_resource_paging_resource import LogResourcePagingResource
from lidarr.models.manual_import_resource import ManualImportResource
from lidarr.models.manual_import_update_resource import ManualImportUpdateResource
from lidarr.models.media_cover import MediaCover
from lidarr.models.media_cover_types import MediaCoverTypes
from lidarr.models.media_info_model import MediaInfoModel
from lidarr.models.media_info_resource import MediaInfoResource
from lidarr.models.media_management_config_resource import MediaManagementConfigResource
from lidarr.models.medium_resource import MediumResource
from lidarr.models.member import Member
from lidarr.models.metadata_profile_resource import MetadataProfileResource
from lidarr.models.metadata_provider_config_resource import MetadataProviderConfigResource
from lidarr.models.metadata_resource import MetadataResource
from lidarr.models.monitor_types import MonitorTypes
from lidarr.models.monitoring_options import MonitoringOptions
from lidarr.models.naming_config_resource import NamingConfigResource
from lidarr.models.new_item_monitor_types import NewItemMonitorTypes
from lidarr.models.notification_resource import NotificationResource
from lidarr.models.parse_resource import ParseResource
from lidarr.models.parsed_album_info import ParsedAlbumInfo
from lidarr.models.parsed_track_info import ParsedTrackInfo
from lidarr.models.ping_resource import PingResource
from lidarr.models.primary_album_type import PrimaryAlbumType
from lidarr.models.privacy_level import PrivacyLevel
from lidarr.models.profile_format_item_resource import ProfileFormatItemResource
from lidarr.models.profile_primary_album_type_item_resource import ProfilePrimaryAlbumTypeItemResource
from lidarr.models.profile_release_status_item_resource import ProfileReleaseStatusItemResource
from lidarr.models.profile_secondary_album_type_item_resource import ProfileSecondaryAlbumTypeItemResource
from lidarr.models.proper_download_types import ProperDownloadTypes
from lidarr.models.provider_message import ProviderMessage
from lidarr.models.provider_message_type import ProviderMessageType
from lidarr.models.proxy_type import ProxyType
from lidarr.models.quality import Quality
from lidarr.models.quality_definition_resource import QualityDefinitionResource
from lidarr.models.quality_model import QualityModel
from lidarr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource
from lidarr.models.quality_profile_resource import QualityProfileResource
from lidarr.models.queue_bulk_resource import QueueBulkResource
from lidarr.models.queue_resource import QueueResource
from lidarr.models.queue_resource_paging_resource import QueueResourcePagingResource
from lidarr.models.queue_status_resource import QueueStatusResource
from lidarr.models.ratings import Ratings
from lidarr.models.rejection import Rejection
from lidarr.models.rejection_type import RejectionType
from lidarr.models.release_profile_resource import ReleaseProfileResource
from lidarr.models.release_resource import ReleaseResource
from lidarr.models.release_status import ReleaseStatus
from lidarr.models.remote_path_mapping_resource import RemotePathMappingResource
from lidarr.models.rename_track_resource import RenameTrackResource
from lidarr.models.rescan_after_refresh_type import RescanAfterRefreshType
from lidarr.models.retag_track_resource import RetagTrackResource
from lidarr.models.revision import Revision
from lidarr.models.root_folder_resource import RootFolderResource
from lidarr.models.runtime_mode import RuntimeMode
from lidarr.models.secondary_album_type import SecondaryAlbumType
from lidarr.models.select_option import SelectOption
from lidarr.models.sort_direction import SortDirection
from lidarr.models.system_resource import SystemResource
from lidarr.models.tag_details_resource import TagDetailsResource
from lidarr.models.tag_difference import TagDifference
from lidarr.models.tag_resource import TagResource
from lidarr.models.task_resource import TaskResource
from lidarr.models.track_file_list_resource import TrackFileListResource
from lidarr.models.track_file_resource import TrackFileResource
from lidarr.models.track_resource import TrackResource
from lidarr.models.tracked_download_state import TrackedDownloadState
from lidarr.models.tracked_download_status import TrackedDownloadStatus
from lidarr.models.tracked_download_status_message import TrackedDownloadStatusMessage
from lidarr.models.ui_config_resource import UiConfigResource
from lidarr.models.update_changes import UpdateChanges
from lidarr.models.update_mechanism import UpdateMechanism
from lidarr.models.update_resource import UpdateResource
from lidarr.models.write_audio_tags_type import WriteAudioTagsType
