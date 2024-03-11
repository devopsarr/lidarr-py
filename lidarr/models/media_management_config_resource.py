# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.1.7.4030
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from lidarr.models.allow_fingerprinting import AllowFingerprinting
from lidarr.models.file_date_type import FileDateType
from lidarr.models.proper_download_types import ProperDownloadTypes
from lidarr.models.rescan_after_refresh_type import RescanAfterRefreshType
from typing import Optional, Set
from typing_extensions import Self

class MediaManagementConfigResource(BaseModel):
    """
    MediaManagementConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    auto_unmonitor_previously_downloaded_tracks: Optional[StrictBool] = Field(default=None, alias="autoUnmonitorPreviouslyDownloadedTracks")
    recycle_bin: Optional[StrictStr] = Field(default=None, alias="recycleBin")
    recycle_bin_cleanup_days: Optional[StrictInt] = Field(default=None, alias="recycleBinCleanupDays")
    download_propers_and_repacks: Optional[ProperDownloadTypes] = Field(default=None, alias="downloadPropersAndRepacks")
    create_empty_artist_folders: Optional[StrictBool] = Field(default=None, alias="createEmptyArtistFolders")
    delete_empty_folders: Optional[StrictBool] = Field(default=None, alias="deleteEmptyFolders")
    file_date: Optional[FileDateType] = Field(default=None, alias="fileDate")
    watch_library_for_changes: Optional[StrictBool] = Field(default=None, alias="watchLibraryForChanges")
    rescan_after_refresh: Optional[RescanAfterRefreshType] = Field(default=None, alias="rescanAfterRefresh")
    allow_fingerprinting: Optional[AllowFingerprinting] = Field(default=None, alias="allowFingerprinting")
    set_permissions_linux: Optional[StrictBool] = Field(default=None, alias="setPermissionsLinux")
    chmod_folder: Optional[StrictStr] = Field(default=None, alias="chmodFolder")
    chown_group: Optional[StrictStr] = Field(default=None, alias="chownGroup")
    skip_free_space_check_when_importing: Optional[StrictBool] = Field(default=None, alias="skipFreeSpaceCheckWhenImporting")
    minimum_free_space_when_importing: Optional[StrictInt] = Field(default=None, alias="minimumFreeSpaceWhenImporting")
    copy_using_hardlinks: Optional[StrictBool] = Field(default=None, alias="copyUsingHardlinks")
    import_extra_files: Optional[StrictBool] = Field(default=None, alias="importExtraFiles")
    extra_file_extensions: Optional[StrictStr] = Field(default=None, alias="extraFileExtensions")
    __properties: ClassVar[List[str]] = ["id", "autoUnmonitorPreviouslyDownloadedTracks", "recycleBin", "recycleBinCleanupDays", "downloadPropersAndRepacks", "createEmptyArtistFolders", "deleteEmptyFolders", "fileDate", "watchLibraryForChanges", "rescanAfterRefresh", "allowFingerprinting", "setPermissionsLinux", "chmodFolder", "chownGroup", "skipFreeSpaceCheckWhenImporting", "minimumFreeSpaceWhenImporting", "copyUsingHardlinks", "importExtraFiles", "extraFileExtensions"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MediaManagementConfigResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if recycle_bin (nullable) is None
        # and model_fields_set contains the field
        if self.recycle_bin is None and "recycle_bin" in self.model_fields_set:
            _dict['recycleBin'] = None

        # set to None if chmod_folder (nullable) is None
        # and model_fields_set contains the field
        if self.chmod_folder is None and "chmod_folder" in self.model_fields_set:
            _dict['chmodFolder'] = None

        # set to None if chown_group (nullable) is None
        # and model_fields_set contains the field
        if self.chown_group is None and "chown_group" in self.model_fields_set:
            _dict['chownGroup'] = None

        # set to None if extra_file_extensions (nullable) is None
        # and model_fields_set contains the field
        if self.extra_file_extensions is None and "extra_file_extensions" in self.model_fields_set:
            _dict['extraFileExtensions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaManagementConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "autoUnmonitorPreviouslyDownloadedTracks": obj.get("autoUnmonitorPreviouslyDownloadedTracks"),
            "recycleBin": obj.get("recycleBin"),
            "recycleBinCleanupDays": obj.get("recycleBinCleanupDays"),
            "downloadPropersAndRepacks": obj.get("downloadPropersAndRepacks"),
            "createEmptyArtistFolders": obj.get("createEmptyArtistFolders"),
            "deleteEmptyFolders": obj.get("deleteEmptyFolders"),
            "fileDate": obj.get("fileDate"),
            "watchLibraryForChanges": obj.get("watchLibraryForChanges"),
            "rescanAfterRefresh": obj.get("rescanAfterRefresh"),
            "allowFingerprinting": obj.get("allowFingerprinting"),
            "setPermissionsLinux": obj.get("setPermissionsLinux"),
            "chmodFolder": obj.get("chmodFolder"),
            "chownGroup": obj.get("chownGroup"),
            "skipFreeSpaceCheckWhenImporting": obj.get("skipFreeSpaceCheckWhenImporting"),
            "minimumFreeSpaceWhenImporting": obj.get("minimumFreeSpaceWhenImporting"),
            "copyUsingHardlinks": obj.get("copyUsingHardlinks"),
            "importExtraFiles": obj.get("importExtraFiles"),
            "extraFileExtensions": obj.get("extraFileExtensions")
        })
        return _obj


