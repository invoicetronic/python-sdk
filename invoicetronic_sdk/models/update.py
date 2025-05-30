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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from invoicetronic_sdk.models.document_data import DocumentData
from invoicetronic_sdk.models.error import Error
from typing import Optional, Set
from typing_extensions import Self

class Update(BaseModel):
    """
    Update
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier. Leave it at 0 for new records as it will be set automatically.")
    created: Optional[datetime] = Field(default=None, description="Creation date. It is set automatically.")
    version: Optional[StrictInt] = Field(default=None, description="Row version, for optimistic concurrency. It is set automatically.")
    user_id: Optional[StrictInt] = Field(default=None, description="User id.")
    company_id: Optional[StrictInt] = Field(default=None, description="Company id.")
    send_id: Optional[StrictInt] = Field(default=None, description="Send id. This is the id of the sent invoice to which this update refers to.")
    date_sent: Optional[datetime] = Field(default=None, description="When the document was sent to the SDI.")
    last_update: Optional[datetime] = Field(default=None, description="Last update from SDI.")
    identifier: Optional[StrictStr] = Field(default=None, description="SDI identifier. This is set by the SDI and it is unique within the SDI system.")
    state: Optional[StrictStr] = Field(default=None, description="State of the document. Theses are the possible values, as per the SDI documentation:")
    description: Optional[StrictStr] = Field(default=None, description="Description for the state.")
    message_id: Optional[StrictStr] = Field(default=None, description="SDI message id.")
    errors: Optional[List[Error]] = Field(default=None, description="SDI errors, if any.")
    is_read: Optional[StrictBool] = Field(default=None, description="Wether the item has been read at least once.")
    meta_data: Optional[Dict[str, StrictStr]] = Field(default=None, description="Metadata from the Send item this update refers to.")
    documents: Optional[List[DocumentData]] = Field(default=None, description="Invoice references from the Send item this update refers to.")
    prestatore: Optional[StrictStr] = Field(default=None, description="Prestatore reference from the Send item this status refers to.")
    __properties: ClassVar[List[str]] = ["id", "created", "version", "user_id", "company_id", "send_id", "date_sent", "last_update", "identifier", "state", "description", "message_id", "errors", "is_read", "meta_data", "documents", "prestatore"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Inviato', 'Consegnato', 'NonConsegnato', 'Scartato', 'AccettatoDalDestinatario', 'RifiutatoDalDestinatario', 'ImpossibilitàDiRecapito', 'DecorrenzaTermini', 'AttestazioneTrasmissioneFattura']):
            raise ValueError("must be one of enum values ('Inviato', 'Consegnato', 'NonConsegnato', 'Scartato', 'AccettatoDalDestinatario', 'RifiutatoDalDestinatario', 'ImpossibilitàDiRecapito', 'DecorrenzaTermini', 'AttestazioneTrasmissioneFattura')")
        return value

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
        """Create an instance of Update from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item_documents in self.documents:
                if _item_documents:
                    _items.append(_item_documents.to_dict())
            _dict['documents'] = _items
        # set to None if date_sent (nullable) is None
        # and model_fields_set contains the field
        if self.date_sent is None and "date_sent" in self.model_fields_set:
            _dict['date_sent'] = None

        # set to None if identifier (nullable) is None
        # and model_fields_set contains the field
        if self.identifier is None and "identifier" in self.model_fields_set:
            _dict['identifier'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if message_id (nullable) is None
        # and model_fields_set contains the field
        if self.message_id is None and "message_id" in self.model_fields_set:
            _dict['message_id'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if meta_data (nullable) is None
        # and model_fields_set contains the field
        if self.meta_data is None and "meta_data" in self.model_fields_set:
            _dict['meta_data'] = None

        # set to None if documents (nullable) is None
        # and model_fields_set contains the field
        if self.documents is None and "documents" in self.model_fields_set:
            _dict['documents'] = None

        # set to None if prestatore (nullable) is None
        # and model_fields_set contains the field
        if self.prestatore is None and "prestatore" in self.model_fields_set:
            _dict['prestatore'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Update from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created": obj.get("created"),
            "version": obj.get("version"),
            "user_id": obj.get("user_id"),
            "company_id": obj.get("company_id"),
            "send_id": obj.get("send_id"),
            "date_sent": obj.get("date_sent"),
            "last_update": obj.get("last_update"),
            "identifier": obj.get("identifier"),
            "state": obj.get("state"),
            "description": obj.get("description"),
            "message_id": obj.get("message_id"),
            "errors": [Error.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "is_read": obj.get("is_read"),
            "meta_data": obj.get("meta_data"),
            "documents": [DocumentData.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None,
            "prestatore": obj.get("prestatore")
        })
        return _obj


