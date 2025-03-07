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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from invoicetronic_invoice_sdk.models.fattura_elettronica_body import FatturaElettronicaBody
from invoicetronic_invoice_sdk.models.fattura_elettronica_header import FatturaElettronicaHeader
from typing import Optional, Set
from typing_extensions import Self

class FatturaOrdinaria(BaseModel):
    """
    FatturaOrdinaria
    """ # noqa: E501
    sistema_emittente: Optional[StrictStr] = None
    fattura_elettronica_header: Optional[FatturaElettronicaHeader] = None
    fattura_elettronica_body: Optional[List[FatturaElettronicaBody]] = None
    __properties: ClassVar[List[str]] = ["sistema_emittente", "fattura_elettronica_header", "fattura_elettronica_body"]

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
        """Create an instance of FatturaOrdinaria from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fattura_elettronica_header
        if self.fattura_elettronica_header:
            _dict['fattura_elettronica_header'] = self.fattura_elettronica_header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fattura_elettronica_body (list)
        _items = []
        if self.fattura_elettronica_body:
            for _item_fattura_elettronica_body in self.fattura_elettronica_body:
                if _item_fattura_elettronica_body:
                    _items.append(_item_fattura_elettronica_body.to_dict())
            _dict['fattura_elettronica_body'] = _items
        # set to None if sistema_emittente (nullable) is None
        # and model_fields_set contains the field
        if self.sistema_emittente is None and "sistema_emittente" in self.model_fields_set:
            _dict['sistema_emittente'] = None

        # set to None if fattura_elettronica_body (nullable) is None
        # and model_fields_set contains the field
        if self.fattura_elettronica_body is None and "fattura_elettronica_body" in self.model_fields_set:
            _dict['fattura_elettronica_body'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FatturaOrdinaria from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sistema_emittente": obj.get("sistema_emittente"),
            "fattura_elettronica_header": FatturaElettronicaHeader.from_dict(obj["fattura_elettronica_header"]) if obj.get("fattura_elettronica_header") is not None else None,
            "fattura_elettronica_body": [FatturaElettronicaBody.from_dict(_item) for _item in obj["fattura_elettronica_body"]] if obj.get("fattura_elettronica_body") is not None else None
        })
        return _obj


