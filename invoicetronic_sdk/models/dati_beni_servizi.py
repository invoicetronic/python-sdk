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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from invoicetronic_sdk.models.dati_riepilogo import DatiRiepilogo
from invoicetronic_sdk.models.dettaglio_linee import DettaglioLinee
from typing import Optional, Set
from typing_extensions import Self

class DatiBeniServizi(BaseModel):
    """
    DatiBeniServizi
    """ # noqa: E501
    dettaglio_linee: Optional[List[DettaglioLinee]] = None
    dati_riepilogo: Optional[List[DatiRiepilogo]] = None
    __properties: ClassVar[List[str]] = ["dettaglio_linee", "dati_riepilogo"]

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
        """Create an instance of DatiBeniServizi from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dettaglio_linee (list)
        _items = []
        if self.dettaglio_linee:
            for _item_dettaglio_linee in self.dettaglio_linee:
                if _item_dettaglio_linee:
                    _items.append(_item_dettaglio_linee.to_dict())
            _dict['dettaglio_linee'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dati_riepilogo (list)
        _items = []
        if self.dati_riepilogo:
            for _item_dati_riepilogo in self.dati_riepilogo:
                if _item_dati_riepilogo:
                    _items.append(_item_dati_riepilogo.to_dict())
            _dict['dati_riepilogo'] = _items
        # set to None if dettaglio_linee (nullable) is None
        # and model_fields_set contains the field
        if self.dettaglio_linee is None and "dettaglio_linee" in self.model_fields_set:
            _dict['dettaglio_linee'] = None

        # set to None if dati_riepilogo (nullable) is None
        # and model_fields_set contains the field
        if self.dati_riepilogo is None and "dati_riepilogo" in self.model_fields_set:
            _dict['dati_riepilogo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatiBeniServizi from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dettaglio_linee": [DettaglioLinee.from_dict(_item) for _item in obj["dettaglio_linee"]] if obj.get("dettaglio_linee") is not None else None,
            "dati_riepilogo": [DatiRiepilogo.from_dict(_item) for _item in obj["dati_riepilogo"]] if obj.get("dati_riepilogo") is not None else None
        })
        return _obj


