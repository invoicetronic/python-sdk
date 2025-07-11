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
from invoicetronic_sdk.models.allegati import Allegati
from invoicetronic_sdk.models.dati_beni_servizi import DatiBeniServizi
from invoicetronic_sdk.models.dati_generali import DatiGenerali
from invoicetronic_sdk.models.dati_pagamento import DatiPagamento
from invoicetronic_sdk.models.dati_veicoli import DatiVeicoli
from typing import Optional, Set
from typing_extensions import Self

class FatturaElettronicaBody(BaseModel):
    """
    FatturaElettronicaBody
    """ # noqa: E501
    dati_generali: Optional[DatiGenerali] = None
    dati_beni_servizi: Optional[DatiBeniServizi] = None
    dati_veicoli: Optional[DatiVeicoli] = None
    dati_pagamento: Optional[List[DatiPagamento]] = None
    allegati: Optional[List[Allegati]] = None
    __properties: ClassVar[List[str]] = ["dati_generali", "dati_beni_servizi", "dati_veicoli", "dati_pagamento", "allegati"]

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
        """Create an instance of FatturaElettronicaBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dati_generali
        if self.dati_generali:
            _dict['dati_generali'] = self.dati_generali.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dati_beni_servizi
        if self.dati_beni_servizi:
            _dict['dati_beni_servizi'] = self.dati_beni_servizi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dati_veicoli
        if self.dati_veicoli:
            _dict['dati_veicoli'] = self.dati_veicoli.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dati_pagamento (list)
        _items = []
        if self.dati_pagamento:
            for _item_dati_pagamento in self.dati_pagamento:
                if _item_dati_pagamento:
                    _items.append(_item_dati_pagamento.to_dict())
            _dict['dati_pagamento'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in allegati (list)
        _items = []
        if self.allegati:
            for _item_allegati in self.allegati:
                if _item_allegati:
                    _items.append(_item_allegati.to_dict())
            _dict['allegati'] = _items
        # set to None if dati_pagamento (nullable) is None
        # and model_fields_set contains the field
        if self.dati_pagamento is None and "dati_pagamento" in self.model_fields_set:
            _dict['dati_pagamento'] = None

        # set to None if allegati (nullable) is None
        # and model_fields_set contains the field
        if self.allegati is None and "allegati" in self.model_fields_set:
            _dict['allegati'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FatturaElettronicaBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dati_generali": DatiGenerali.from_dict(obj["dati_generali"]) if obj.get("dati_generali") is not None else None,
            "dati_beni_servizi": DatiBeniServizi.from_dict(obj["dati_beni_servizi"]) if obj.get("dati_beni_servizi") is not None else None,
            "dati_veicoli": DatiVeicoli.from_dict(obj["dati_veicoli"]) if obj.get("dati_veicoli") is not None else None,
            "dati_pagamento": [DatiPagamento.from_dict(_item) for _item in obj["dati_pagamento"]] if obj.get("dati_pagamento") is not None else None,
            "allegati": [Allegati.from_dict(_item) for _item in obj["allegati"]] if obj.get("allegati") is not None else None
        })
        return _obj


