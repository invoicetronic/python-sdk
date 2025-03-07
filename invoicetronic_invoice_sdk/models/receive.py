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
from invoicetronic_invoice_sdk.models.document_data import DocumentData
from typing import Optional, Set
from typing_extensions import Self

class Receive(BaseModel):
    """
    Receive
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier. Leave it at 0 for new records as it will be set automatically.")
    created: Optional[datetime] = Field(default=None, description="Creation date. It is set automatically.")
    version: Optional[StrictInt] = Field(default=None, description="Row version, for optimistic concurrency. It is set automatically.")
    user_id: Optional[StrictInt] = Field(default=None, description="User id.")
    company_id: Optional[StrictInt] = Field(default=None, description="Company id. On send, this is the sender and must be set in advance. On receive, it will be  automatically set based on the recipient's VAT number. If a matching company is not found, the invoice will be rejected until the company is created.")
    committente: Optional[StrictStr] = Field(default=None, description="VAT number of the Cessionario/Committente (customer). This is automatically set based on the recipient's VAT number.")
    prestatore: Optional[StrictStr] = Field(default=None, description="VAT number of the Cedente/Prestatore (vendor). This is automatically set based on the sender's VAT number.")
    identifier: Optional[StrictStr] = Field(default=None, description="SDI identifier. This is set by the SDI and is guaranted to be unique within the SDI system.")
    file_name: Optional[StrictStr] = Field(default=None, description="Xml file name.")
    format: Optional[StrictStr] = Field(default=None, description="SDI format (FPA12, FPR12, FSM10, ...)")
    payload: Optional[StrictStr] = Field(default=None, description="Xml payloaad. This is the actual xml content, as string. On send, it can be base64 encoded. If it's not, it will be encoded before sending. It is guaranteed to be cyphered at rest.")
    last_update: Optional[datetime] = Field(default=None, description="Last update from SDI.")
    date_sent: Optional[datetime] = Field(default=None, description="When the invoice was sent to SDI.")
    documents: Optional[List[DocumentData]] = Field(default=None, description="The invoices included in the payload. This is set by the system, based on the xml content.")
    encoding: Optional[StrictStr] = Field(default=None, description="Whether the payload is Base64 encoded or a plain XML (text).")
    is_read: Optional[StrictBool] = Field(default=None, description="Wether the invoice has been read at least once.")
    message_id: Optional[StrictStr] = Field(default=None, description="SDI message id.")
    __properties: ClassVar[List[str]] = ["id", "created", "version", "user_id", "company_id", "committente", "prestatore", "identifier", "file_name", "format", "payload", "last_update", "date_sent", "documents", "encoding", "is_read", "message_id"]

    @field_validator('encoding')
    def encoding_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Xml', 'Base64']):
            raise ValueError("must be one of enum values ('Xml', 'Base64')")
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
        """Create an instance of Receive from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item_documents in self.documents:
                if _item_documents:
                    _items.append(_item_documents.to_dict())
            _dict['documents'] = _items
        # set to None if committente (nullable) is None
        # and model_fields_set contains the field
        if self.committente is None and "committente" in self.model_fields_set:
            _dict['committente'] = None

        # set to None if prestatore (nullable) is None
        # and model_fields_set contains the field
        if self.prestatore is None and "prestatore" in self.model_fields_set:
            _dict['prestatore'] = None

        # set to None if identifier (nullable) is None
        # and model_fields_set contains the field
        if self.identifier is None and "identifier" in self.model_fields_set:
            _dict['identifier'] = None

        # set to None if file_name (nullable) is None
        # and model_fields_set contains the field
        if self.file_name is None and "file_name" in self.model_fields_set:
            _dict['file_name'] = None

        # set to None if format (nullable) is None
        # and model_fields_set contains the field
        if self.format is None and "format" in self.model_fields_set:
            _dict['format'] = None

        # set to None if payload (nullable) is None
        # and model_fields_set contains the field
        if self.payload is None and "payload" in self.model_fields_set:
            _dict['payload'] = None

        # set to None if last_update (nullable) is None
        # and model_fields_set contains the field
        if self.last_update is None and "last_update" in self.model_fields_set:
            _dict['last_update'] = None

        # set to None if date_sent (nullable) is None
        # and model_fields_set contains the field
        if self.date_sent is None and "date_sent" in self.model_fields_set:
            _dict['date_sent'] = None

        # set to None if documents (nullable) is None
        # and model_fields_set contains the field
        if self.documents is None and "documents" in self.model_fields_set:
            _dict['documents'] = None

        # set to None if message_id (nullable) is None
        # and model_fields_set contains the field
        if self.message_id is None and "message_id" in self.model_fields_set:
            _dict['message_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Receive from a dict"""
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
            "committente": obj.get("committente"),
            "prestatore": obj.get("prestatore"),
            "identifier": obj.get("identifier"),
            "file_name": obj.get("file_name"),
            "format": obj.get("format"),
            "payload": obj.get("payload"),
            "last_update": obj.get("last_update"),
            "date_sent": obj.get("date_sent"),
            "documents": [DocumentData.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None,
            "encoding": obj.get("encoding"),
            "is_read": obj.get("is_read"),
            "message_id": obj.get("message_id")
        })
        return _obj


