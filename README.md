# lidarr-py
Lidarr API docs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2.1.7.4030
- Package version: 1.1.0 <!--- x-release-please-version -->
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/devopsarr/lidarr-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/devopsarr/lidarr-py.git`)

Then import the package:
```python
import lidarr
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import lidarr
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import lidarr
from lidarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8686
# See configuration.py for a list of all supported configuration parameters.
configuration = lidarr.Configuration(
    host = "http://localhost:8686"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'


# Enter a context with an instance of the API client
with lidarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lidarr.AlbumApi(api_client)
    album_resource = lidarr.AlbumResource() # AlbumResource |  (optional)

    try:
        api_response = api_instance.create_album(album_resource=album_resource)
        print("The response of AlbumApi->create_album:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlbumApi->create_album: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8686*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlbumApi* | [**create_album**](docs/AlbumApi.md#create_album) | **POST** /api/v1/album | 
*AlbumApi* | [**delete_album**](docs/AlbumApi.md#delete_album) | **DELETE** /api/v1/album/{id} | 
*AlbumApi* | [**get_album_by_id**](docs/AlbumApi.md#get_album_by_id) | **GET** /api/v1/album/{id} | 
*AlbumApi* | [**list_album**](docs/AlbumApi.md#list_album) | **GET** /api/v1/album | 
*AlbumApi* | [**put_album_monitor**](docs/AlbumApi.md#put_album_monitor) | **PUT** /api/v1/album/monitor | 
*AlbumApi* | [**update_album**](docs/AlbumApi.md#update_album) | **PUT** /api/v1/album/{id} | 
*AlbumLookupApi* | [**get_album_lookup**](docs/AlbumLookupApi.md#get_album_lookup) | **GET** /api/v1/album/lookup | 
*AlbumStudioApi* | [**create_album_studio**](docs/AlbumStudioApi.md#create_album_studio) | **POST** /api/v1/albumstudio | 
*ApiInfoApi* | [**get_api**](docs/ApiInfoApi.md#get_api) | **GET** /api | 
*ArtistApi* | [**create_artist**](docs/ArtistApi.md#create_artist) | **POST** /api/v1/artist | 
*ArtistApi* | [**delete_artist**](docs/ArtistApi.md#delete_artist) | **DELETE** /api/v1/artist/{id} | 
*ArtistApi* | [**get_artist_by_id**](docs/ArtistApi.md#get_artist_by_id) | **GET** /api/v1/artist/{id} | 
*ArtistApi* | [**list_artist**](docs/ArtistApi.md#list_artist) | **GET** /api/v1/artist | 
*ArtistApi* | [**update_artist**](docs/ArtistApi.md#update_artist) | **PUT** /api/v1/artist/{id} | 
*ArtistEditorApi* | [**delete_artist_editor**](docs/ArtistEditorApi.md#delete_artist_editor) | **DELETE** /api/v1/artist/editor | 
*ArtistEditorApi* | [**put_artist_editor**](docs/ArtistEditorApi.md#put_artist_editor) | **PUT** /api/v1/artist/editor | 
*ArtistLookupApi* | [**get_artist_lookup**](docs/ArtistLookupApi.md#get_artist_lookup) | **GET** /api/v1/artist/lookup | 
*AuthenticationApi* | [**create_login**](docs/AuthenticationApi.md#create_login) | **POST** /login | 
*AuthenticationApi* | [**get_logout**](docs/AuthenticationApi.md#get_logout) | **GET** /logout | 
*AutoTaggingApi* | [**create_auto_tagging**](docs/AutoTaggingApi.md#create_auto_tagging) | **POST** /api/v1/autotagging | 
*AutoTaggingApi* | [**delete_auto_tagging**](docs/AutoTaggingApi.md#delete_auto_tagging) | **DELETE** /api/v1/autotagging/{id} | 
*AutoTaggingApi* | [**get_auto_tagging_by_id**](docs/AutoTaggingApi.md#get_auto_tagging_by_id) | **GET** /api/v1/autotagging/{id} | 
*AutoTaggingApi* | [**list_auto_tagging**](docs/AutoTaggingApi.md#list_auto_tagging) | **GET** /api/v1/autotagging | 
*AutoTaggingApi* | [**list_auto_tagging_schema**](docs/AutoTaggingApi.md#list_auto_tagging_schema) | **GET** /api/v1/autotagging/schema | 
*AutoTaggingApi* | [**update_auto_tagging**](docs/AutoTaggingApi.md#update_auto_tagging) | **PUT** /api/v1/autotagging/{id} | 
*BackupApi* | [**create_system_backup_restore_by_id**](docs/BackupApi.md#create_system_backup_restore_by_id) | **POST** /api/v1/system/backup/restore/{id} | 
*BackupApi* | [**create_system_backup_restore_upload**](docs/BackupApi.md#create_system_backup_restore_upload) | **POST** /api/v1/system/backup/restore/upload | 
*BackupApi* | [**delete_system_backup**](docs/BackupApi.md#delete_system_backup) | **DELETE** /api/v1/system/backup/{id} | 
*BackupApi* | [**list_system_backup**](docs/BackupApi.md#list_system_backup) | **GET** /api/v1/system/backup | 
*BlocklistApi* | [**delete_blocklist**](docs/BlocklistApi.md#delete_blocklist) | **DELETE** /api/v1/blocklist/{id} | 
*BlocklistApi* | [**delete_blocklist_bulk**](docs/BlocklistApi.md#delete_blocklist_bulk) | **DELETE** /api/v1/blocklist/bulk | 
*BlocklistApi* | [**get_blocklist**](docs/BlocklistApi.md#get_blocklist) | **GET** /api/v1/blocklist | 
*CalendarApi* | [**get_calendar_by_id**](docs/CalendarApi.md#get_calendar_by_id) | **GET** /api/v1/calendar/{id} | 
*CalendarApi* | [**list_calendar**](docs/CalendarApi.md#list_calendar) | **GET** /api/v1/calendar | 
*CalendarFeedApi* | [**get_feed_v1_calendar_lidarr_ics**](docs/CalendarFeedApi.md#get_feed_v1_calendar_lidarr_ics) | **GET** /feed/v1/calendar/lidarr.ics | 
*CommandApi* | [**create_command**](docs/CommandApi.md#create_command) | **POST** /api/v1/command | 
*CommandApi* | [**delete_command**](docs/CommandApi.md#delete_command) | **DELETE** /api/v1/command/{id} | 
*CommandApi* | [**get_command_by_id**](docs/CommandApi.md#get_command_by_id) | **GET** /api/v1/command/{id} | 
*CommandApi* | [**list_command**](docs/CommandApi.md#list_command) | **GET** /api/v1/command | 
*CustomFilterApi* | [**create_custom_filter**](docs/CustomFilterApi.md#create_custom_filter) | **POST** /api/v1/customfilter | 
*CustomFilterApi* | [**delete_custom_filter**](docs/CustomFilterApi.md#delete_custom_filter) | **DELETE** /api/v1/customfilter/{id} | 
*CustomFilterApi* | [**get_custom_filter_by_id**](docs/CustomFilterApi.md#get_custom_filter_by_id) | **GET** /api/v1/customfilter/{id} | 
*CustomFilterApi* | [**list_custom_filter**](docs/CustomFilterApi.md#list_custom_filter) | **GET** /api/v1/customfilter | 
*CustomFilterApi* | [**update_custom_filter**](docs/CustomFilterApi.md#update_custom_filter) | **PUT** /api/v1/customfilter/{id} | 
*CustomFormatApi* | [**create_custom_format**](docs/CustomFormatApi.md#create_custom_format) | **POST** /api/v1/customformat | 
*CustomFormatApi* | [**delete_custom_format**](docs/CustomFormatApi.md#delete_custom_format) | **DELETE** /api/v1/customformat/{id} | 
*CustomFormatApi* | [**get_custom_format_by_id**](docs/CustomFormatApi.md#get_custom_format_by_id) | **GET** /api/v1/customformat/{id} | 
*CustomFormatApi* | [**list_custom_format**](docs/CustomFormatApi.md#list_custom_format) | **GET** /api/v1/customformat | 
*CustomFormatApi* | [**list_custom_format_schema**](docs/CustomFormatApi.md#list_custom_format_schema) | **GET** /api/v1/customformat/schema | 
*CustomFormatApi* | [**update_custom_format**](docs/CustomFormatApi.md#update_custom_format) | **PUT** /api/v1/customformat/{id} | 
*CutoffApi* | [**get_wanted_cutoff**](docs/CutoffApi.md#get_wanted_cutoff) | **GET** /api/v1/wanted/cutoff | 
*CutoffApi* | [**get_wanted_cutoff_by_id**](docs/CutoffApi.md#get_wanted_cutoff_by_id) | **GET** /api/v1/wanted/cutoff/{id} | 
*DelayProfileApi* | [**create_delay_profile**](docs/DelayProfileApi.md#create_delay_profile) | **POST** /api/v1/delayprofile | 
*DelayProfileApi* | [**delete_delay_profile**](docs/DelayProfileApi.md#delete_delay_profile) | **DELETE** /api/v1/delayprofile/{id} | 
*DelayProfileApi* | [**get_delay_profile_by_id**](docs/DelayProfileApi.md#get_delay_profile_by_id) | **GET** /api/v1/delayprofile/{id} | 
*DelayProfileApi* | [**list_delay_profile**](docs/DelayProfileApi.md#list_delay_profile) | **GET** /api/v1/delayprofile | 
*DelayProfileApi* | [**update_delay_profile**](docs/DelayProfileApi.md#update_delay_profile) | **PUT** /api/v1/delayprofile/{id} | 
*DelayProfileApi* | [**update_delay_profile_reorder**](docs/DelayProfileApi.md#update_delay_profile_reorder) | **PUT** /api/v1/delayprofile/reorder/{id} | 
*DiskSpaceApi* | [**list_disk_space**](docs/DiskSpaceApi.md#list_disk_space) | **GET** /api/v1/diskspace | 
*DownloadClientApi* | [**create_download_client**](docs/DownloadClientApi.md#create_download_client) | **POST** /api/v1/downloadclient | 
*DownloadClientApi* | [**create_download_client_action_by_name**](docs/DownloadClientApi.md#create_download_client_action_by_name) | **POST** /api/v1/downloadclient/action/{name} | 
*DownloadClientApi* | [**delete_download_client**](docs/DownloadClientApi.md#delete_download_client) | **DELETE** /api/v1/downloadclient/{id} | 
*DownloadClientApi* | [**delete_download_client_bulk**](docs/DownloadClientApi.md#delete_download_client_bulk) | **DELETE** /api/v1/downloadclient/bulk | 
*DownloadClientApi* | [**get_download_client_by_id**](docs/DownloadClientApi.md#get_download_client_by_id) | **GET** /api/v1/downloadclient/{id} | 
*DownloadClientApi* | [**list_download_client**](docs/DownloadClientApi.md#list_download_client) | **GET** /api/v1/downloadclient | 
*DownloadClientApi* | [**list_download_client_schema**](docs/DownloadClientApi.md#list_download_client_schema) | **GET** /api/v1/downloadclient/schema | 
*DownloadClientApi* | [**put_download_client_bulk**](docs/DownloadClientApi.md#put_download_client_bulk) | **PUT** /api/v1/downloadclient/bulk | 
*DownloadClientApi* | [**test_download_client**](docs/DownloadClientApi.md#test_download_client) | **POST** /api/v1/downloadclient/test | 
*DownloadClientApi* | [**testall_download_client**](docs/DownloadClientApi.md#testall_download_client) | **POST** /api/v1/downloadclient/testall | 
*DownloadClientApi* | [**update_download_client**](docs/DownloadClientApi.md#update_download_client) | **PUT** /api/v1/downloadclient/{id} | 
*DownloadClientConfigApi* | [**get_download_client_config**](docs/DownloadClientConfigApi.md#get_download_client_config) | **GET** /api/v1/config/downloadclient | 
*DownloadClientConfigApi* | [**get_download_client_config_by_id**](docs/DownloadClientConfigApi.md#get_download_client_config_by_id) | **GET** /api/v1/config/downloadclient/{id} | 
*DownloadClientConfigApi* | [**update_download_client_config**](docs/DownloadClientConfigApi.md#update_download_client_config) | **PUT** /api/v1/config/downloadclient/{id} | 
*FileSystemApi* | [**get_file_system**](docs/FileSystemApi.md#get_file_system) | **GET** /api/v1/filesystem | 
*FileSystemApi* | [**get_file_system_mediafiles**](docs/FileSystemApi.md#get_file_system_mediafiles) | **GET** /api/v1/filesystem/mediafiles | 
*FileSystemApi* | [**get_file_system_type**](docs/FileSystemApi.md#get_file_system_type) | **GET** /api/v1/filesystem/type | 
*HealthApi* | [**list_health**](docs/HealthApi.md#list_health) | **GET** /api/v1/health | 
*HistoryApi* | [**create_history_failed_by_id**](docs/HistoryApi.md#create_history_failed_by_id) | **POST** /api/v1/history/failed/{id} | 
*HistoryApi* | [**get_history**](docs/HistoryApi.md#get_history) | **GET** /api/v1/history | 
*HistoryApi* | [**list_history_artist**](docs/HistoryApi.md#list_history_artist) | **GET** /api/v1/history/artist | 
*HistoryApi* | [**list_history_since**](docs/HistoryApi.md#list_history_since) | **GET** /api/v1/history/since | 
*HostConfigApi* | [**get_host_config**](docs/HostConfigApi.md#get_host_config) | **GET** /api/v1/config/host | 
*HostConfigApi* | [**get_host_config_by_id**](docs/HostConfigApi.md#get_host_config_by_id) | **GET** /api/v1/config/host/{id} | 
*HostConfigApi* | [**update_host_config**](docs/HostConfigApi.md#update_host_config) | **PUT** /api/v1/config/host/{id} | 
*ImportListApi* | [**create_import_list**](docs/ImportListApi.md#create_import_list) | **POST** /api/v1/importlist | 
*ImportListApi* | [**create_import_list_action_by_name**](docs/ImportListApi.md#create_import_list_action_by_name) | **POST** /api/v1/importlist/action/{name} | 
*ImportListApi* | [**delete_import_list**](docs/ImportListApi.md#delete_import_list) | **DELETE** /api/v1/importlist/{id} | 
*ImportListApi* | [**delete_import_list_bulk**](docs/ImportListApi.md#delete_import_list_bulk) | **DELETE** /api/v1/importlist/bulk | 
*ImportListApi* | [**get_import_list_by_id**](docs/ImportListApi.md#get_import_list_by_id) | **GET** /api/v1/importlist/{id} | 
*ImportListApi* | [**list_import_list**](docs/ImportListApi.md#list_import_list) | **GET** /api/v1/importlist | 
*ImportListApi* | [**list_import_list_schema**](docs/ImportListApi.md#list_import_list_schema) | **GET** /api/v1/importlist/schema | 
*ImportListApi* | [**put_import_list_bulk**](docs/ImportListApi.md#put_import_list_bulk) | **PUT** /api/v1/importlist/bulk | 
*ImportListApi* | [**test_import_list**](docs/ImportListApi.md#test_import_list) | **POST** /api/v1/importlist/test | 
*ImportListApi* | [**testall_import_list**](docs/ImportListApi.md#testall_import_list) | **POST** /api/v1/importlist/testall | 
*ImportListApi* | [**update_import_list**](docs/ImportListApi.md#update_import_list) | **PUT** /api/v1/importlist/{id} | 
*ImportListExclusionApi* | [**create_import_list_exclusion**](docs/ImportListExclusionApi.md#create_import_list_exclusion) | **POST** /api/v1/importlistexclusion | 
*ImportListExclusionApi* | [**delete_import_list_exclusion**](docs/ImportListExclusionApi.md#delete_import_list_exclusion) | **DELETE** /api/v1/importlistexclusion/{id} | 
*ImportListExclusionApi* | [**get_import_list_exclusion_by_id**](docs/ImportListExclusionApi.md#get_import_list_exclusion_by_id) | **GET** /api/v1/importlistexclusion/{id} | 
*ImportListExclusionApi* | [**list_import_list_exclusion**](docs/ImportListExclusionApi.md#list_import_list_exclusion) | **GET** /api/v1/importlistexclusion | 
*ImportListExclusionApi* | [**update_import_list_exclusion**](docs/ImportListExclusionApi.md#update_import_list_exclusion) | **PUT** /api/v1/importlistexclusion/{id} | 
*IndexerApi* | [**create_indexer**](docs/IndexerApi.md#create_indexer) | **POST** /api/v1/indexer | 
*IndexerApi* | [**create_indexer_action_by_name**](docs/IndexerApi.md#create_indexer_action_by_name) | **POST** /api/v1/indexer/action/{name} | 
*IndexerApi* | [**delete_indexer**](docs/IndexerApi.md#delete_indexer) | **DELETE** /api/v1/indexer/{id} | 
*IndexerApi* | [**delete_indexer_bulk**](docs/IndexerApi.md#delete_indexer_bulk) | **DELETE** /api/v1/indexer/bulk | 
*IndexerApi* | [**get_indexer_by_id**](docs/IndexerApi.md#get_indexer_by_id) | **GET** /api/v1/indexer/{id} | 
*IndexerApi* | [**list_indexer**](docs/IndexerApi.md#list_indexer) | **GET** /api/v1/indexer | 
*IndexerApi* | [**list_indexer_schema**](docs/IndexerApi.md#list_indexer_schema) | **GET** /api/v1/indexer/schema | 
*IndexerApi* | [**put_indexer_bulk**](docs/IndexerApi.md#put_indexer_bulk) | **PUT** /api/v1/indexer/bulk | 
*IndexerApi* | [**test_indexer**](docs/IndexerApi.md#test_indexer) | **POST** /api/v1/indexer/test | 
*IndexerApi* | [**testall_indexer**](docs/IndexerApi.md#testall_indexer) | **POST** /api/v1/indexer/testall | 
*IndexerApi* | [**update_indexer**](docs/IndexerApi.md#update_indexer) | **PUT** /api/v1/indexer/{id} | 
*IndexerConfigApi* | [**get_indexer_config**](docs/IndexerConfigApi.md#get_indexer_config) | **GET** /api/v1/config/indexer | 
*IndexerConfigApi* | [**get_indexer_config_by_id**](docs/IndexerConfigApi.md#get_indexer_config_by_id) | **GET** /api/v1/config/indexer/{id} | 
*IndexerConfigApi* | [**update_indexer_config**](docs/IndexerConfigApi.md#update_indexer_config) | **PUT** /api/v1/config/indexer/{id} | 
*LanguageApi* | [**get_language_by_id**](docs/LanguageApi.md#get_language_by_id) | **GET** /api/v1/language/{id} | 
*LanguageApi* | [**list_language**](docs/LanguageApi.md#list_language) | **GET** /api/v1/language | 
*LocalizationApi* | [**get_localization**](docs/LocalizationApi.md#get_localization) | **GET** /api/v1/localization | 
*LogApi* | [**get_log**](docs/LogApi.md#get_log) | **GET** /api/v1/log | 
*LogFileApi* | [**get_log_file_by_filename**](docs/LogFileApi.md#get_log_file_by_filename) | **GET** /api/v1/log/file/{filename} | 
*LogFileApi* | [**list_log_file**](docs/LogFileApi.md#list_log_file) | **GET** /api/v1/log/file | 
*ManualImportApi* | [**create_manual_import**](docs/ManualImportApi.md#create_manual_import) | **POST** /api/v1/manualimport | 
*ManualImportApi* | [**list_manual_import**](docs/ManualImportApi.md#list_manual_import) | **GET** /api/v1/manualimport | 
*MediaCoverApi* | [**get_media_cover_album_by_filename**](docs/MediaCoverApi.md#get_media_cover_album_by_filename) | **GET** /api/v1/mediacover/album/{albumId}/{filename} | 
*MediaCoverApi* | [**get_media_cover_artist_by_filename**](docs/MediaCoverApi.md#get_media_cover_artist_by_filename) | **GET** /api/v1/mediacover/artist/{artistId}/{filename} | 
*MediaManagementConfigApi* | [**get_media_management_config**](docs/MediaManagementConfigApi.md#get_media_management_config) | **GET** /api/v1/config/mediamanagement | 
*MediaManagementConfigApi* | [**get_media_management_config_by_id**](docs/MediaManagementConfigApi.md#get_media_management_config_by_id) | **GET** /api/v1/config/mediamanagement/{id} | 
*MediaManagementConfigApi* | [**update_media_management_config**](docs/MediaManagementConfigApi.md#update_media_management_config) | **PUT** /api/v1/config/mediamanagement/{id} | 
*MetadataApi* | [**create_metadata**](docs/MetadataApi.md#create_metadata) | **POST** /api/v1/metadata | 
*MetadataApi* | [**create_metadata_action_by_name**](docs/MetadataApi.md#create_metadata_action_by_name) | **POST** /api/v1/metadata/action/{name} | 
*MetadataApi* | [**delete_metadata**](docs/MetadataApi.md#delete_metadata) | **DELETE** /api/v1/metadata/{id} | 
*MetadataApi* | [**get_metadata_by_id**](docs/MetadataApi.md#get_metadata_by_id) | **GET** /api/v1/metadata/{id} | 
*MetadataApi* | [**list_metadata**](docs/MetadataApi.md#list_metadata) | **GET** /api/v1/metadata | 
*MetadataApi* | [**list_metadata_schema**](docs/MetadataApi.md#list_metadata_schema) | **GET** /api/v1/metadata/schema | 
*MetadataApi* | [**test_metadata**](docs/MetadataApi.md#test_metadata) | **POST** /api/v1/metadata/test | 
*MetadataApi* | [**testall_metadata**](docs/MetadataApi.md#testall_metadata) | **POST** /api/v1/metadata/testall | 
*MetadataApi* | [**update_metadata**](docs/MetadataApi.md#update_metadata) | **PUT** /api/v1/metadata/{id} | 
*MetadataProfileApi* | [**create_metadata_profile**](docs/MetadataProfileApi.md#create_metadata_profile) | **POST** /api/v1/metadataprofile | 
*MetadataProfileApi* | [**delete_metadata_profile**](docs/MetadataProfileApi.md#delete_metadata_profile) | **DELETE** /api/v1/metadataprofile/{id} | 
*MetadataProfileApi* | [**get_metadata_profile_by_id**](docs/MetadataProfileApi.md#get_metadata_profile_by_id) | **GET** /api/v1/metadataprofile/{id} | 
*MetadataProfileApi* | [**list_metadata_profile**](docs/MetadataProfileApi.md#list_metadata_profile) | **GET** /api/v1/metadataprofile | 
*MetadataProfileApi* | [**update_metadata_profile**](docs/MetadataProfileApi.md#update_metadata_profile) | **PUT** /api/v1/metadataprofile/{id} | 
*MetadataProfileSchemaApi* | [**get_metadataprofile_schema**](docs/MetadataProfileSchemaApi.md#get_metadataprofile_schema) | **GET** /api/v1/metadataprofile/schema | 
*MetadataProviderConfigApi* | [**get_metadata_provider_config**](docs/MetadataProviderConfigApi.md#get_metadata_provider_config) | **GET** /api/v1/config/metadataprovider | 
*MetadataProviderConfigApi* | [**get_metadata_provider_config_by_id**](docs/MetadataProviderConfigApi.md#get_metadata_provider_config_by_id) | **GET** /api/v1/config/metadataprovider/{id} | 
*MetadataProviderConfigApi* | [**update_metadata_provider_config**](docs/MetadataProviderConfigApi.md#update_metadata_provider_config) | **PUT** /api/v1/config/metadataprovider/{id} | 
*MissingApi* | [**get_wanted_missing**](docs/MissingApi.md#get_wanted_missing) | **GET** /api/v1/wanted/missing | 
*MissingApi* | [**get_wanted_missing_by_id**](docs/MissingApi.md#get_wanted_missing_by_id) | **GET** /api/v1/wanted/missing/{id} | 
*NamingConfigApi* | [**get_naming_config**](docs/NamingConfigApi.md#get_naming_config) | **GET** /api/v1/config/naming | 
*NamingConfigApi* | [**get_naming_config_by_id**](docs/NamingConfigApi.md#get_naming_config_by_id) | **GET** /api/v1/config/naming/{id} | 
*NamingConfigApi* | [**get_naming_config_examples**](docs/NamingConfigApi.md#get_naming_config_examples) | **GET** /api/v1/config/naming/examples | 
*NamingConfigApi* | [**update_naming_config**](docs/NamingConfigApi.md#update_naming_config) | **PUT** /api/v1/config/naming/{id} | 
*NotificationApi* | [**create_notification**](docs/NotificationApi.md#create_notification) | **POST** /api/v1/notification | 
*NotificationApi* | [**create_notification_action_by_name**](docs/NotificationApi.md#create_notification_action_by_name) | **POST** /api/v1/notification/action/{name} | 
*NotificationApi* | [**delete_notification**](docs/NotificationApi.md#delete_notification) | **DELETE** /api/v1/notification/{id} | 
*NotificationApi* | [**get_notification_by_id**](docs/NotificationApi.md#get_notification_by_id) | **GET** /api/v1/notification/{id} | 
*NotificationApi* | [**list_notification**](docs/NotificationApi.md#list_notification) | **GET** /api/v1/notification | 
*NotificationApi* | [**list_notification_schema**](docs/NotificationApi.md#list_notification_schema) | **GET** /api/v1/notification/schema | 
*NotificationApi* | [**test_notification**](docs/NotificationApi.md#test_notification) | **POST** /api/v1/notification/test | 
*NotificationApi* | [**testall_notification**](docs/NotificationApi.md#testall_notification) | **POST** /api/v1/notification/testall | 
*NotificationApi* | [**update_notification**](docs/NotificationApi.md#update_notification) | **PUT** /api/v1/notification/{id} | 
*ParseApi* | [**get_parse**](docs/ParseApi.md#get_parse) | **GET** /api/v1/parse | 
*PingApi* | [**get_ping**](docs/PingApi.md#get_ping) | **GET** /ping | 
*QualityDefinitionApi* | [**get_quality_definition_by_id**](docs/QualityDefinitionApi.md#get_quality_definition_by_id) | **GET** /api/v1/qualitydefinition/{id} | 
*QualityDefinitionApi* | [**list_quality_definition**](docs/QualityDefinitionApi.md#list_quality_definition) | **GET** /api/v1/qualitydefinition | 
*QualityDefinitionApi* | [**put_quality_definition_update**](docs/QualityDefinitionApi.md#put_quality_definition_update) | **PUT** /api/v1/qualitydefinition/update | 
*QualityDefinitionApi* | [**update_quality_definition**](docs/QualityDefinitionApi.md#update_quality_definition) | **PUT** /api/v1/qualitydefinition/{id} | 
*QualityProfileApi* | [**create_quality_profile**](docs/QualityProfileApi.md#create_quality_profile) | **POST** /api/v1/qualityprofile | 
*QualityProfileApi* | [**delete_quality_profile**](docs/QualityProfileApi.md#delete_quality_profile) | **DELETE** /api/v1/qualityprofile/{id} | 
*QualityProfileApi* | [**get_quality_profile_by_id**](docs/QualityProfileApi.md#get_quality_profile_by_id) | **GET** /api/v1/qualityprofile/{id} | 
*QualityProfileApi* | [**list_quality_profile**](docs/QualityProfileApi.md#list_quality_profile) | **GET** /api/v1/qualityprofile | 
*QualityProfileApi* | [**update_quality_profile**](docs/QualityProfileApi.md#update_quality_profile) | **PUT** /api/v1/qualityprofile/{id} | 
*QualityProfileSchemaApi* | [**get_qualityprofile_schema**](docs/QualityProfileSchemaApi.md#get_qualityprofile_schema) | **GET** /api/v1/qualityprofile/schema | 
*QueueApi* | [**delete_queue**](docs/QueueApi.md#delete_queue) | **DELETE** /api/v1/queue/{id} | 
*QueueApi* | [**delete_queue_bulk**](docs/QueueApi.md#delete_queue_bulk) | **DELETE** /api/v1/queue/bulk | 
*QueueApi* | [**get_queue**](docs/QueueApi.md#get_queue) | **GET** /api/v1/queue | 
*QueueActionApi* | [**create_queue_grab_bulk**](docs/QueueActionApi.md#create_queue_grab_bulk) | **POST** /api/v1/queue/grab/bulk | 
*QueueActionApi* | [**create_queue_grab_by_id**](docs/QueueActionApi.md#create_queue_grab_by_id) | **POST** /api/v1/queue/grab/{id} | 
*QueueDetailsApi* | [**list_queue_details**](docs/QueueDetailsApi.md#list_queue_details) | **GET** /api/v1/queue/details | 
*QueueStatusApi* | [**get_queue_status**](docs/QueueStatusApi.md#get_queue_status) | **GET** /api/v1/queue/status | 
*ReleaseApi* | [**create_release**](docs/ReleaseApi.md#create_release) | **POST** /api/v1/release | 
*ReleaseApi* | [**list_release**](docs/ReleaseApi.md#list_release) | **GET** /api/v1/release | 
*ReleaseProfileApi* | [**create_release_profile**](docs/ReleaseProfileApi.md#create_release_profile) | **POST** /api/v1/releaseprofile | 
*ReleaseProfileApi* | [**delete_release_profile**](docs/ReleaseProfileApi.md#delete_release_profile) | **DELETE** /api/v1/releaseprofile/{id} | 
*ReleaseProfileApi* | [**get_release_profile_by_id**](docs/ReleaseProfileApi.md#get_release_profile_by_id) | **GET** /api/v1/releaseprofile/{id} | 
*ReleaseProfileApi* | [**list_release_profile**](docs/ReleaseProfileApi.md#list_release_profile) | **GET** /api/v1/releaseprofile | 
*ReleaseProfileApi* | [**update_release_profile**](docs/ReleaseProfileApi.md#update_release_profile) | **PUT** /api/v1/releaseprofile/{id} | 
*ReleasePushApi* | [**create_release_push**](docs/ReleasePushApi.md#create_release_push) | **POST** /api/v1/release/push | 
*RemotePathMappingApi* | [**create_remote_path_mapping**](docs/RemotePathMappingApi.md#create_remote_path_mapping) | **POST** /api/v1/remotepathmapping | 
*RemotePathMappingApi* | [**delete_remote_path_mapping**](docs/RemotePathMappingApi.md#delete_remote_path_mapping) | **DELETE** /api/v1/remotepathmapping/{id} | 
*RemotePathMappingApi* | [**get_remote_path_mapping_by_id**](docs/RemotePathMappingApi.md#get_remote_path_mapping_by_id) | **GET** /api/v1/remotepathmapping/{id} | 
*RemotePathMappingApi* | [**list_remote_path_mapping**](docs/RemotePathMappingApi.md#list_remote_path_mapping) | **GET** /api/v1/remotepathmapping | 
*RemotePathMappingApi* | [**update_remote_path_mapping**](docs/RemotePathMappingApi.md#update_remote_path_mapping) | **PUT** /api/v1/remotepathmapping/{id} | 
*RenameTrackApi* | [**list_rename**](docs/RenameTrackApi.md#list_rename) | **GET** /api/v1/rename | 
*RetagTrackApi* | [**list_retag**](docs/RetagTrackApi.md#list_retag) | **GET** /api/v1/retag | 
*RootFolderApi* | [**create_root_folder**](docs/RootFolderApi.md#create_root_folder) | **POST** /api/v1/rootfolder | 
*RootFolderApi* | [**delete_root_folder**](docs/RootFolderApi.md#delete_root_folder) | **DELETE** /api/v1/rootfolder/{id} | 
*RootFolderApi* | [**get_root_folder_by_id**](docs/RootFolderApi.md#get_root_folder_by_id) | **GET** /api/v1/rootfolder/{id} | 
*RootFolderApi* | [**list_root_folder**](docs/RootFolderApi.md#list_root_folder) | **GET** /api/v1/rootfolder | 
*RootFolderApi* | [**update_root_folder**](docs/RootFolderApi.md#update_root_folder) | **PUT** /api/v1/rootfolder/{id} | 
*SearchApi* | [**get_search**](docs/SearchApi.md#get_search) | **GET** /api/v1/search | 
*StaticResourceApi* | [**get**](docs/StaticResourceApi.md#get) | **GET** / | 
*StaticResourceApi* | [**get_by_path**](docs/StaticResourceApi.md#get_by_path) | **GET** /{path} | 
*StaticResourceApi* | [**get_content_by_path**](docs/StaticResourceApi.md#get_content_by_path) | **GET** /content/{path} | 
*StaticResourceApi* | [**get_login**](docs/StaticResourceApi.md#get_login) | **GET** /login | 
*SystemApi* | [**create_system_restart**](docs/SystemApi.md#create_system_restart) | **POST** /api/v1/system/restart | 
*SystemApi* | [**create_system_shutdown**](docs/SystemApi.md#create_system_shutdown) | **POST** /api/v1/system/shutdown | 
*SystemApi* | [**get_system_routes**](docs/SystemApi.md#get_system_routes) | **GET** /api/v1/system/routes | 
*SystemApi* | [**get_system_routes_duplicate**](docs/SystemApi.md#get_system_routes_duplicate) | **GET** /api/v1/system/routes/duplicate | 
*SystemApi* | [**get_system_status**](docs/SystemApi.md#get_system_status) | **GET** /api/v1/system/status | 
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /api/v1/tag | 
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **DELETE** /api/v1/tag/{id} | 
*TagApi* | [**get_tag_by_id**](docs/TagApi.md#get_tag_by_id) | **GET** /api/v1/tag/{id} | 
*TagApi* | [**list_tag**](docs/TagApi.md#list_tag) | **GET** /api/v1/tag | 
*TagApi* | [**update_tag**](docs/TagApi.md#update_tag) | **PUT** /api/v1/tag/{id} | 
*TagDetailsApi* | [**get_tag_detail_by_id**](docs/TagDetailsApi.md#get_tag_detail_by_id) | **GET** /api/v1/tag/detail/{id} | 
*TagDetailsApi* | [**list_tag_detail**](docs/TagDetailsApi.md#list_tag_detail) | **GET** /api/v1/tag/detail | 
*TaskApi* | [**get_system_task_by_id**](docs/TaskApi.md#get_system_task_by_id) | **GET** /api/v1/system/task/{id} | 
*TaskApi* | [**list_system_task**](docs/TaskApi.md#list_system_task) | **GET** /api/v1/system/task | 
*TrackApi* | [**get_track_by_id**](docs/TrackApi.md#get_track_by_id) | **GET** /api/v1/track/{id} | 
*TrackApi* | [**list_track**](docs/TrackApi.md#list_track) | **GET** /api/v1/track | 
*TrackFileApi* | [**delete_track_file**](docs/TrackFileApi.md#delete_track_file) | **DELETE** /api/v1/trackfile/{id} | 
*TrackFileApi* | [**delete_track_file_bulk**](docs/TrackFileApi.md#delete_track_file_bulk) | **DELETE** /api/v1/trackfile/bulk | 
*TrackFileApi* | [**get_track_file_by_id**](docs/TrackFileApi.md#get_track_file_by_id) | **GET** /api/v1/trackfile/{id} | 
*TrackFileApi* | [**list_track_file**](docs/TrackFileApi.md#list_track_file) | **GET** /api/v1/trackfile | 
*TrackFileApi* | [**put_track_file_editor**](docs/TrackFileApi.md#put_track_file_editor) | **PUT** /api/v1/trackfile/editor | 
*TrackFileApi* | [**update_track_file**](docs/TrackFileApi.md#update_track_file) | **PUT** /api/v1/trackfile/{id} | 
*UiConfigApi* | [**get_ui_config**](docs/UiConfigApi.md#get_ui_config) | **GET** /api/v1/config/ui | 
*UiConfigApi* | [**get_ui_config_by_id**](docs/UiConfigApi.md#get_ui_config_by_id) | **GET** /api/v1/config/ui/{id} | 
*UiConfigApi* | [**update_ui_config**](docs/UiConfigApi.md#update_ui_config) | **PUT** /api/v1/config/ui/{id} | 
*UpdateApi* | [**list_update**](docs/UpdateApi.md#list_update) | **GET** /api/v1/update | 
*UpdateLogFileApi* | [**get_log_file_update_by_filename**](docs/UpdateLogFileApi.md#get_log_file_update_by_filename) | **GET** /api/v1/log/file/update/{filename} | 
*UpdateLogFileApi* | [**list_log_file_update**](docs/UpdateLogFileApi.md#list_log_file_update) | **GET** /api/v1/log/file/update | 


## Documentation For Models

 - [AddAlbumOptions](docs/AddAlbumOptions.md)
 - [AddArtistOptions](docs/AddArtistOptions.md)
 - [AlbumAddType](docs/AlbumAddType.md)
 - [AlbumReleaseResource](docs/AlbumReleaseResource.md)
 - [AlbumResource](docs/AlbumResource.md)
 - [AlbumResourcePagingResource](docs/AlbumResourcePagingResource.md)
 - [AlbumStatisticsResource](docs/AlbumStatisticsResource.md)
 - [AlbumStudioArtistResource](docs/AlbumStudioArtistResource.md)
 - [AlbumStudioResource](docs/AlbumStudioResource.md)
 - [AlbumsMonitoredResource](docs/AlbumsMonitoredResource.md)
 - [AllowFingerprinting](docs/AllowFingerprinting.md)
 - [ApplyTags](docs/ApplyTags.md)
 - [ArtistEditorResource](docs/ArtistEditorResource.md)
 - [ArtistResource](docs/ArtistResource.md)
 - [ArtistStatisticsResource](docs/ArtistStatisticsResource.md)
 - [ArtistStatusType](docs/ArtistStatusType.md)
 - [ArtistTitleInfo](docs/ArtistTitleInfo.md)
 - [AuthenticationRequiredType](docs/AuthenticationRequiredType.md)
 - [AuthenticationType](docs/AuthenticationType.md)
 - [AutoTaggingResource](docs/AutoTaggingResource.md)
 - [AutoTaggingSpecificationSchema](docs/AutoTaggingSpecificationSchema.md)
 - [BackupResource](docs/BackupResource.md)
 - [BackupType](docs/BackupType.md)
 - [BlocklistBulkResource](docs/BlocklistBulkResource.md)
 - [BlocklistResource](docs/BlocklistResource.md)
 - [BlocklistResourcePagingResource](docs/BlocklistResourcePagingResource.md)
 - [CertificateValidationType](docs/CertificateValidationType.md)
 - [Command](docs/Command.md)
 - [CommandPriority](docs/CommandPriority.md)
 - [CommandResource](docs/CommandResource.md)
 - [CommandResult](docs/CommandResult.md)
 - [CommandStatus](docs/CommandStatus.md)
 - [CommandTrigger](docs/CommandTrigger.md)
 - [ContractField](docs/ContractField.md)
 - [CustomFilterResource](docs/CustomFilterResource.md)
 - [CustomFormatResource](docs/CustomFormatResource.md)
 - [CustomFormatSpecificationSchema](docs/CustomFormatSpecificationSchema.md)
 - [DatabaseType](docs/DatabaseType.md)
 - [DelayProfileResource](docs/DelayProfileResource.md)
 - [DiskSpaceResource](docs/DiskSpaceResource.md)
 - [DownloadClientBulkResource](docs/DownloadClientBulkResource.md)
 - [DownloadClientConfigResource](docs/DownloadClientConfigResource.md)
 - [DownloadClientResource](docs/DownloadClientResource.md)
 - [DownloadProtocol](docs/DownloadProtocol.md)
 - [EntityHistoryEventType](docs/EntityHistoryEventType.md)
 - [FileDateType](docs/FileDateType.md)
 - [HealthCheckResult](docs/HealthCheckResult.md)
 - [HealthResource](docs/HealthResource.md)
 - [HistoryResource](docs/HistoryResource.md)
 - [HistoryResourcePagingResource](docs/HistoryResourcePagingResource.md)
 - [HostConfigResource](docs/HostConfigResource.md)
 - [ImportListBulkResource](docs/ImportListBulkResource.md)
 - [ImportListExclusionResource](docs/ImportListExclusionResource.md)
 - [ImportListMonitorType](docs/ImportListMonitorType.md)
 - [ImportListResource](docs/ImportListResource.md)
 - [ImportListType](docs/ImportListType.md)
 - [IndexerBulkResource](docs/IndexerBulkResource.md)
 - [IndexerConfigResource](docs/IndexerConfigResource.md)
 - [IndexerResource](docs/IndexerResource.md)
 - [IsoCountry](docs/IsoCountry.md)
 - [LanguageResource](docs/LanguageResource.md)
 - [Links](docs/Links.md)
 - [LocalizationResource](docs/LocalizationResource.md)
 - [LogFileResource](docs/LogFileResource.md)
 - [LogResource](docs/LogResource.md)
 - [LogResourcePagingResource](docs/LogResourcePagingResource.md)
 - [ManualImportResource](docs/ManualImportResource.md)
 - [ManualImportUpdateResource](docs/ManualImportUpdateResource.md)
 - [MediaCover](docs/MediaCover.md)
 - [MediaCoverTypes](docs/MediaCoverTypes.md)
 - [MediaInfoModel](docs/MediaInfoModel.md)
 - [MediaInfoResource](docs/MediaInfoResource.md)
 - [MediaManagementConfigResource](docs/MediaManagementConfigResource.md)
 - [MediumResource](docs/MediumResource.md)
 - [Member](docs/Member.md)
 - [MetadataProfileResource](docs/MetadataProfileResource.md)
 - [MetadataProviderConfigResource](docs/MetadataProviderConfigResource.md)
 - [MetadataResource](docs/MetadataResource.md)
 - [MonitorTypes](docs/MonitorTypes.md)
 - [MonitoringOptions](docs/MonitoringOptions.md)
 - [NamingConfigResource](docs/NamingConfigResource.md)
 - [NewItemMonitorTypes](docs/NewItemMonitorTypes.md)
 - [NotificationResource](docs/NotificationResource.md)
 - [ParseResource](docs/ParseResource.md)
 - [ParsedAlbumInfo](docs/ParsedAlbumInfo.md)
 - [ParsedTrackInfo](docs/ParsedTrackInfo.md)
 - [PingResource](docs/PingResource.md)
 - [PrimaryAlbumType](docs/PrimaryAlbumType.md)
 - [PrivacyLevel](docs/PrivacyLevel.md)
 - [ProfileFormatItemResource](docs/ProfileFormatItemResource.md)
 - [ProfilePrimaryAlbumTypeItemResource](docs/ProfilePrimaryAlbumTypeItemResource.md)
 - [ProfileReleaseStatusItemResource](docs/ProfileReleaseStatusItemResource.md)
 - [ProfileSecondaryAlbumTypeItemResource](docs/ProfileSecondaryAlbumTypeItemResource.md)
 - [ProperDownloadTypes](docs/ProperDownloadTypes.md)
 - [ProviderMessage](docs/ProviderMessage.md)
 - [ProviderMessageType](docs/ProviderMessageType.md)
 - [ProxyType](docs/ProxyType.md)
 - [Quality](docs/Quality.md)
 - [QualityDefinitionResource](docs/QualityDefinitionResource.md)
 - [QualityModel](docs/QualityModel.md)
 - [QualityProfileQualityItemResource](docs/QualityProfileQualityItemResource.md)
 - [QualityProfileResource](docs/QualityProfileResource.md)
 - [QueueBulkResource](docs/QueueBulkResource.md)
 - [QueueResource](docs/QueueResource.md)
 - [QueueResourcePagingResource](docs/QueueResourcePagingResource.md)
 - [QueueStatusResource](docs/QueueStatusResource.md)
 - [Ratings](docs/Ratings.md)
 - [Rejection](docs/Rejection.md)
 - [RejectionType](docs/RejectionType.md)
 - [ReleaseProfileResource](docs/ReleaseProfileResource.md)
 - [ReleaseResource](docs/ReleaseResource.md)
 - [ReleaseStatus](docs/ReleaseStatus.md)
 - [RemotePathMappingResource](docs/RemotePathMappingResource.md)
 - [RenameTrackResource](docs/RenameTrackResource.md)
 - [RescanAfterRefreshType](docs/RescanAfterRefreshType.md)
 - [RetagTrackResource](docs/RetagTrackResource.md)
 - [Revision](docs/Revision.md)
 - [RootFolderResource](docs/RootFolderResource.md)
 - [RuntimeMode](docs/RuntimeMode.md)
 - [SecondaryAlbumType](docs/SecondaryAlbumType.md)
 - [SelectOption](docs/SelectOption.md)
 - [SortDirection](docs/SortDirection.md)
 - [SystemResource](docs/SystemResource.md)
 - [TagDetailsResource](docs/TagDetailsResource.md)
 - [TagDifference](docs/TagDifference.md)
 - [TagResource](docs/TagResource.md)
 - [TaskResource](docs/TaskResource.md)
 - [TrackFileListResource](docs/TrackFileListResource.md)
 - [TrackFileResource](docs/TrackFileResource.md)
 - [TrackResource](docs/TrackResource.md)
 - [TrackedDownloadState](docs/TrackedDownloadState.md)
 - [TrackedDownloadStatus](docs/TrackedDownloadStatus.md)
 - [TrackedDownloadStatusMessage](docs/TrackedDownloadStatusMessage.md)
 - [UiConfigResource](docs/UiConfigResource.md)
 - [UpdateChanges](docs/UpdateChanges.md)
 - [UpdateMechanism](docs/UpdateMechanism.md)
 - [UpdateResource](docs/UpdateResource.md)
 - [WriteAudioTagsType](docs/WriteAudioTagsType.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="X-Api-Key"></a>
### X-Api-Key

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header

<a id="apikey"></a>
### apikey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Author




