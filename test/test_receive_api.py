# coding: utf-8

"""
    Invoicetronic API

    The [Invoicetronic API][2] is a RESTful service that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. It provides advanced features as encryption at rest, multi-language pre-flight invoice validation, multiple upload formats, webhooks, event logging, client SDKs, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from invoicetronic_invoice_sdk.api.receive_api import ReceiveApi


class TestReceiveApi(unittest.TestCase):
    """ReceiveApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReceiveApi()

    def tearDown(self) -> None:
        pass

    def test_receive_get(self) -> None:
        """Test case for receive_get

        List incoming invoices
        """
        pass

    def test_receive_id_delete(self) -> None:
        """Test case for receive_id_delete

        Delete an incoming invoice by id
        """
        pass

    def test_receive_id_get(self) -> None:
        """Test case for receive_id_get

        Get an incoming invoice by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
