# coding: utf-8

"""
    Invoicetronic API

    The [Invoicetronic API][2] is a RESTful service that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. It provides advanced features as encryption at rest, multi-language pre-flight invoice validation, multiple upload formats, webhooks, event logging, client SDKs, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1
    Contact: info@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from invoicetronic_sdk.models.document_data import DocumentData
from typing import Optional, Set
from typing_extensions import Self

class SendReduced(BaseModel):
    """
    Reduced Send data for Update responses, containing only the essential fields.
    """ # noqa: E501
    identifier: Optional[StrictStr] = Field(default=None, description="SDI identifier.")
    prestatore: Optional[StrictStr] = Field(default=None, description="VAT number of the Cedente/Prestatore (vendor).")
    meta_data: Optional[Dict[str, StrictStr]] = Field(default=None, description="Optional metadata, as json.")
    documents: Optional[List[DocumentData]] = Field(default=None, description="The invoices included in the payload.")
    date_sent: Optional[datetime] = Field(default=None, description="When the invoice was sent to SDI.")
    __properties: ClassVar[List[str]] = ["identifier", "prestatore", "meta_data", "documents", "date_sent"]

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
        """Create an instance of SendReduced from a JSON string"""
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
        # set to None if identifier (nullable) is None
        # and model_fields_set contains the field
        if self.identifier is None and "identifier" in self.model_fields_set:
            _dict['identifier'] = None

        # set to None if prestatore (nullable) is None
        # and model_fields_set contains the field
        if self.prestatore is None and "prestatore" in self.model_fields_set:
            _dict['prestatore'] = None

        # set to None if meta_data (nullable) is None
        # and model_fields_set contains the field
        if self.meta_data is None and "meta_data" in self.model_fields_set:
            _dict['meta_data'] = None

        # set to None if documents (nullable) is None
        # and model_fields_set contains the field
        if self.documents is None and "documents" in self.model_fields_set:
            _dict['documents'] = None

        # set to None if date_sent (nullable) is None
        # and model_fields_set contains the field
        if self.date_sent is None and "date_sent" in self.model_fields_set:
            _dict['date_sent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SendReduced from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "prestatore": obj.get("prestatore"),
            "meta_data": obj.get("meta_data"),
            "documents": [DocumentData.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None,
            "date_sent": obj.get("date_sent")
        })
        return _obj


