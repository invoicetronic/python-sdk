# coding: utf-8

"""
    Italian eInvoice API

    The Italian eInvoice API is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed by Invoicetronic to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. The API also provides advanced features as encryption at rest, invoice validation, multiple upload formats, webhooks, event logging, client SDKs for commonly used languages, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1.0.0
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
from invoicetronic_invoice_sdk.models.anagrafica import Anagrafica
from invoicetronic_invoice_sdk.models.id_fiscale_iva import IdFiscaleIVA
from typing import Optional, Set
from typing_extensions import Self

class DatiAnagrafici(BaseModel):
    """
    DatiAnagrafici
    """ # noqa: E501
    id_fiscale_iva: Optional[IdFiscaleIVA] = None
    codice_fiscale: Optional[StrictStr] = None
    anagrafica: Optional[Anagrafica] = None
    __properties: ClassVar[List[str]] = ["id_fiscale_iva", "codice_fiscale", "anagrafica"]

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
        """Create an instance of DatiAnagrafici from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of id_fiscale_iva
        if self.id_fiscale_iva:
            _dict['id_fiscale_iva'] = self.id_fiscale_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anagrafica
        if self.anagrafica:
            _dict['anagrafica'] = self.anagrafica.to_dict()
        # set to None if codice_fiscale (nullable) is None
        # and model_fields_set contains the field
        if self.codice_fiscale is None and "codice_fiscale" in self.model_fields_set:
            _dict['codice_fiscale'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatiAnagrafici from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id_fiscale_iva": IdFiscaleIVA.from_dict(obj["id_fiscale_iva"]) if obj.get("id_fiscale_iva") is not None else None,
            "codice_fiscale": obj.get("codice_fiscale"),
            "anagrafica": Anagrafica.from_dict(obj["anagrafica"]) if obj.get("anagrafica") is not None else None
        })
        return _obj


