# coding: utf-8

"""
    Lidarr

    Lidarr API docs

    The version of the OpenAPI document: v2.8.2.4493
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lidarr.models.artist_title_info import ArtistTitleInfo
from lidarr.models.iso_country import IsoCountry
from lidarr.models.media_info_model import MediaInfoModel
from lidarr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class ParsedTrackInfo(BaseModel):
    """
    ParsedTrackInfo
    """ # noqa: E501
    title: Optional[StrictStr] = None
    clean_title: Optional[StrictStr] = Field(default=None, alias="cleanTitle")
    artist_title: Optional[StrictStr] = Field(default=None, alias="artistTitle")
    album_title: Optional[StrictStr] = Field(default=None, alias="albumTitle")
    artist_title_info: Optional[ArtistTitleInfo] = Field(default=None, alias="artistTitleInfo")
    artist_mbid: Optional[StrictStr] = Field(default=None, alias="artistMBId")
    album_mbid: Optional[StrictStr] = Field(default=None, alias="albumMBId")
    release_mbid: Optional[StrictStr] = Field(default=None, alias="releaseMBId")
    recording_mbid: Optional[StrictStr] = Field(default=None, alias="recordingMBId")
    track_mbid: Optional[StrictStr] = Field(default=None, alias="trackMBId")
    disc_number: Optional[StrictInt] = Field(default=None, alias="discNumber")
    disc_count: Optional[StrictInt] = Field(default=None, alias="discCount")
    country: Optional[IsoCountry] = None
    year: Optional[StrictInt] = None
    label: Optional[StrictStr] = None
    catalog_number: Optional[StrictStr] = Field(default=None, alias="catalogNumber")
    disambiguation: Optional[StrictStr] = None
    duration: Optional[StrictStr] = None
    quality: Optional[QualityModel] = None
    media_info: Optional[MediaInfoModel] = Field(default=None, alias="mediaInfo")
    track_numbers: Optional[List[StrictInt]] = Field(default=None, alias="trackNumbers")
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    release_hash: Optional[StrictStr] = Field(default=None, alias="releaseHash")
    __properties: ClassVar[List[str]] = ["title", "cleanTitle", "artistTitle", "albumTitle", "artistTitleInfo", "artistMBId", "albumMBId", "releaseMBId", "recordingMBId", "trackMBId", "discNumber", "discCount", "country", "year", "label", "catalogNumber", "disambiguation", "duration", "quality", "mediaInfo", "trackNumbers", "releaseGroup", "releaseHash"]

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
        """Create an instance of ParsedTrackInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of artist_title_info
        if self.artist_title_info:
            _dict['artistTitleInfo'] = self.artist_title_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if clean_title (nullable) is None
        # and model_fields_set contains the field
        if self.clean_title is None and "clean_title" in self.model_fields_set:
            _dict['cleanTitle'] = None

        # set to None if artist_title (nullable) is None
        # and model_fields_set contains the field
        if self.artist_title is None and "artist_title" in self.model_fields_set:
            _dict['artistTitle'] = None

        # set to None if album_title (nullable) is None
        # and model_fields_set contains the field
        if self.album_title is None and "album_title" in self.model_fields_set:
            _dict['albumTitle'] = None

        # set to None if artist_mbid (nullable) is None
        # and model_fields_set contains the field
        if self.artist_mbid is None and "artist_mbid" in self.model_fields_set:
            _dict['artistMBId'] = None

        # set to None if album_mbid (nullable) is None
        # and model_fields_set contains the field
        if self.album_mbid is None and "album_mbid" in self.model_fields_set:
            _dict['albumMBId'] = None

        # set to None if release_mbid (nullable) is None
        # and model_fields_set contains the field
        if self.release_mbid is None and "release_mbid" in self.model_fields_set:
            _dict['releaseMBId'] = None

        # set to None if recording_mbid (nullable) is None
        # and model_fields_set contains the field
        if self.recording_mbid is None and "recording_mbid" in self.model_fields_set:
            _dict['recordingMBId'] = None

        # set to None if track_mbid (nullable) is None
        # and model_fields_set contains the field
        if self.track_mbid is None and "track_mbid" in self.model_fields_set:
            _dict['trackMBId'] = None

        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if catalog_number (nullable) is None
        # and model_fields_set contains the field
        if self.catalog_number is None and "catalog_number" in self.model_fields_set:
            _dict['catalogNumber'] = None

        # set to None if disambiguation (nullable) is None
        # and model_fields_set contains the field
        if self.disambiguation is None and "disambiguation" in self.model_fields_set:
            _dict['disambiguation'] = None

        # set to None if track_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.track_numbers is None and "track_numbers" in self.model_fields_set:
            _dict['trackNumbers'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if release_hash (nullable) is None
        # and model_fields_set contains the field
        if self.release_hash is None and "release_hash" in self.model_fields_set:
            _dict['releaseHash'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParsedTrackInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "cleanTitle": obj.get("cleanTitle"),
            "artistTitle": obj.get("artistTitle"),
            "albumTitle": obj.get("albumTitle"),
            "artistTitleInfo": ArtistTitleInfo.from_dict(obj["artistTitleInfo"]) if obj.get("artistTitleInfo") is not None else None,
            "artistMBId": obj.get("artistMBId"),
            "albumMBId": obj.get("albumMBId"),
            "releaseMBId": obj.get("releaseMBId"),
            "recordingMBId": obj.get("recordingMBId"),
            "trackMBId": obj.get("trackMBId"),
            "discNumber": obj.get("discNumber"),
            "discCount": obj.get("discCount"),
            "country": IsoCountry.from_dict(obj["country"]) if obj.get("country") is not None else None,
            "year": obj.get("year"),
            "label": obj.get("label"),
            "catalogNumber": obj.get("catalogNumber"),
            "disambiguation": obj.get("disambiguation"),
            "duration": obj.get("duration"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "mediaInfo": MediaInfoModel.from_dict(obj["mediaInfo"]) if obj.get("mediaInfo") is not None else None,
            "trackNumbers": obj.get("trackNumbers"),
            "releaseGroup": obj.get("releaseGroup"),
            "releaseHash": obj.get("releaseHash")
        })
        return _obj


