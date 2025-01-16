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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DatiFattureCollegate(BaseModel):
    """
    DatiFattureCollegate
    """ # noqa: E501
    riferimento_numero_linea: Optional[List[StrictInt]] = None
    id_documento: Optional[StrictStr] = None
    data: Optional[datetime] = None
    num_item: Optional[StrictStr] = None
    codice_commessa_convenzione: Optional[StrictStr] = None
    codice_cup: Optional[StrictStr] = None
    codice_cig: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["riferimento_numero_linea", "id_documento", "data", "num_item", "codice_commessa_convenzione", "codice_cup", "codice_cig"]

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
        """Create an instance of DatiFattureCollegate from a JSON string"""
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
        # set to None if riferimento_numero_linea (nullable) is None
        # and model_fields_set contains the field
        if self.riferimento_numero_linea is None and "riferimento_numero_linea" in self.model_fields_set:
            _dict['riferimento_numero_linea'] = None

        # set to None if id_documento (nullable) is None
        # and model_fields_set contains the field
        if self.id_documento is None and "id_documento" in self.model_fields_set:
            _dict['id_documento'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if num_item (nullable) is None
        # and model_fields_set contains the field
        if self.num_item is None and "num_item" in self.model_fields_set:
            _dict['num_item'] = None

        # set to None if codice_commessa_convenzione (nullable) is None
        # and model_fields_set contains the field
        if self.codice_commessa_convenzione is None and "codice_commessa_convenzione" in self.model_fields_set:
            _dict['codice_commessa_convenzione'] = None

        # set to None if codice_cup (nullable) is None
        # and model_fields_set contains the field
        if self.codice_cup is None and "codice_cup" in self.model_fields_set:
            _dict['codice_cup'] = None

        # set to None if codice_cig (nullable) is None
        # and model_fields_set contains the field
        if self.codice_cig is None and "codice_cig" in self.model_fields_set:
            _dict['codice_cig'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DatiFattureCollegate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "riferimento_numero_linea": obj.get("riferimento_numero_linea"),
            "id_documento": obj.get("id_documento"),
            "data": obj.get("data"),
            "num_item": obj.get("num_item"),
            "codice_commessa_convenzione": obj.get("codice_commessa_convenzione"),
            "codice_cup": obj.get("codice_cup"),
            "codice_cig": obj.get("codice_cig")
        })
        return _obj


