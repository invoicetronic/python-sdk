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
from typing import Optional, Set
from typing_extensions import Self

class SedeCedentePrestatore(BaseModel):
    """
    SedeCedentePrestatore
    """ # noqa: E501
    indirizzo: Optional[StrictStr] = None
    numero_civico: Optional[StrictStr] = None
    cap: Optional[StrictStr] = None
    comune: Optional[StrictStr] = None
    provincia: Optional[StrictStr] = None
    nazione: Optional[StrictStr] = 'IT'
    __properties: ClassVar[List[str]] = ["indirizzo", "numero_civico", "cap", "comune", "provincia", "nazione"]

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
        """Create an instance of SedeCedentePrestatore from a JSON string"""
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
        # set to None if indirizzo (nullable) is None
        # and model_fields_set contains the field
        if self.indirizzo is None and "indirizzo" in self.model_fields_set:
            _dict['indirizzo'] = None

        # set to None if numero_civico (nullable) is None
        # and model_fields_set contains the field
        if self.numero_civico is None and "numero_civico" in self.model_fields_set:
            _dict['numero_civico'] = None

        # set to None if cap (nullable) is None
        # and model_fields_set contains the field
        if self.cap is None and "cap" in self.model_fields_set:
            _dict['cap'] = None

        # set to None if comune (nullable) is None
        # and model_fields_set contains the field
        if self.comune is None and "comune" in self.model_fields_set:
            _dict['comune'] = None

        # set to None if provincia (nullable) is None
        # and model_fields_set contains the field
        if self.provincia is None and "provincia" in self.model_fields_set:
            _dict['provincia'] = None

        # set to None if nazione (nullable) is None
        # and model_fields_set contains the field
        if self.nazione is None and "nazione" in self.model_fields_set:
            _dict['nazione'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SedeCedentePrestatore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "indirizzo": obj.get("indirizzo"),
            "numero_civico": obj.get("numero_civico"),
            "cap": obj.get("cap"),
            "comune": obj.get("comune"),
            "provincia": obj.get("provincia"),
            "nazione": obj.get("nazione") if obj.get("nazione") is not None else 'IT'
        })
        return _obj


