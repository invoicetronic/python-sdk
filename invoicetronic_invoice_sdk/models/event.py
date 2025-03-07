# coding: utf-8

"""
    Invoicetronic API

    The [Invoicetronic API][2] is a RESTful service that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. It provides advanced features as encryption at rest, multi-language pre-flight invoice validation, multiple upload formats, webhooks, event logging, client SDKs, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Event(BaseModel):
    """
    Event
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier. Leave it at 0 for new records as it will be set automatically.")
    created: Optional[datetime] = Field(default=None, description="Creation date. It is set automatically.")
    version: Optional[StrictInt] = Field(default=None, description="Row version, for optimistic concurrency. It is set automatically.")
    user_id: Optional[StrictInt] = Field(default=None, description="User id.")
    api_key_id: Optional[StrictInt] = Field(default=None, description="Api key id.")
    company_id: Optional[StrictInt] = Field(default=None, description="Company id.")
    method: Optional[StrictStr] = Field(default=None, description="Request method.")
    query: Optional[StrictStr] = Field(default=None, description="Request query.")
    endpoint: Optional[StrictStr] = Field(default=None, description="API endpoint.")
    api_version: Optional[StrictInt] = Field(default=None, description="Api version.")
    status_code: Optional[StrictInt] = Field(default=None, description="Status code returned by the API.")
    date_time: Optional[datetime] = Field(default=None, description="Date and time of the request.")
    error: Optional[StrictStr] = Field(default=None, description="Response error.")
    success: Optional[StrictBool] = Field(default=None, description="Wether the request was successful.")
    response_body: Optional[StrictStr] = Field(default=None, description="Response payload. It is guaranteed to be cyphered at rest.")
    __properties: ClassVar[List[str]] = ["id", "created", "version", "user_id", "api_key_id", "company_id", "method", "query", "endpoint", "api_version", "status_code", "date_time", "error", "success", "response_body"]

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
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "success",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if company_id (nullable) is None
        # and model_fields_set contains the field
        if self.company_id is None and "company_id" in self.model_fields_set:
            _dict['company_id'] = None

        # set to None if method (nullable) is None
        # and model_fields_set contains the field
        if self.method is None and "method" in self.model_fields_set:
            _dict['method'] = None

        # set to None if query (nullable) is None
        # and model_fields_set contains the field
        if self.query is None and "query" in self.model_fields_set:
            _dict['query'] = None

        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and "endpoint" in self.model_fields_set:
            _dict['endpoint'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if response_body (nullable) is None
        # and model_fields_set contains the field
        if self.response_body is None and "response_body" in self.model_fields_set:
            _dict['response_body'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created": obj.get("created"),
            "version": obj.get("version"),
            "user_id": obj.get("user_id"),
            "api_key_id": obj.get("api_key_id"),
            "company_id": obj.get("company_id"),
            "method": obj.get("method"),
            "query": obj.get("query"),
            "endpoint": obj.get("endpoint"),
            "api_version": obj.get("api_version"),
            "status_code": obj.get("status_code"),
            "date_time": obj.get("date_time"),
            "error": obj.get("error"),
            "success": obj.get("success"),
            "response_body": obj.get("response_body")
        })
        return _obj


