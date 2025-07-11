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

from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Allegati(BaseModel):
    """
    Allegati
    """ # noqa: E501
    nome_attachment: Optional[StrictStr] = None
    algoritmo_compressione: Optional[StrictStr] = None
    formato_attachment: Optional[StrictStr] = None
    descrizione_attachment: Optional[StrictStr] = None
    attachment: Optional[Union[StrictBytes, StrictStr]] = None
    __properties: ClassVar[List[str]] = ["nome_attachment", "algoritmo_compressione", "formato_attachment", "descrizione_attachment", "attachment"]

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
        """Create an instance of Allegati from a JSON string"""
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
        # set to None if nome_attachment (nullable) is None
        # and model_fields_set contains the field
        if self.nome_attachment is None and "nome_attachment" in self.model_fields_set:
            _dict['nome_attachment'] = None

        # set to None if algoritmo_compressione (nullable) is None
        # and model_fields_set contains the field
        if self.algoritmo_compressione is None and "algoritmo_compressione" in self.model_fields_set:
            _dict['algoritmo_compressione'] = None

        # set to None if formato_attachment (nullable) is None
        # and model_fields_set contains the field
        if self.formato_attachment is None and "formato_attachment" in self.model_fields_set:
            _dict['formato_attachment'] = None

        # set to None if descrizione_attachment (nullable) is None
        # and model_fields_set contains the field
        if self.descrizione_attachment is None and "descrizione_attachment" in self.model_fields_set:
            _dict['descrizione_attachment'] = None

        # set to None if attachment (nullable) is None
        # and model_fields_set contains the field
        if self.attachment is None and "attachment" in self.model_fields_set:
            _dict['attachment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Allegati from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nome_attachment": obj.get("nome_attachment"),
            "algoritmo_compressione": obj.get("algoritmo_compressione"),
            "formato_attachment": obj.get("formato_attachment"),
            "descrizione_attachment": obj.get("descrizione_attachment"),
            "attachment": obj.get("attachment")
        })
        return _obj


