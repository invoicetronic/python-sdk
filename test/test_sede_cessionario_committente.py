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

from invoicetronic_invoice_sdk.models.sede_cessionario_committente import SedeCessionarioCommittente

class TestSedeCessionarioCommittente(unittest.TestCase):
    """SedeCessionarioCommittente unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SedeCessionarioCommittente:
        """Test SedeCessionarioCommittente
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SedeCessionarioCommittente`
        """
        model = SedeCessionarioCommittente()
        if include_optional:
            return SedeCessionarioCommittente(
                indirizzo = '',
                numero_civico = '',
                cap = '',
                comune = '',
                provincia = '',
                nazione = 'IT'
            )
        else:
            return SedeCessionarioCommittente(
        )
        """

    def testSedeCessionarioCommittente(self):
        """Test SedeCessionarioCommittente"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
