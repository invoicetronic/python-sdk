# coding: utf-8

"""
    Invoicetronic API

    The [Invoicetronic API][2] is a RESTful service that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. It provides advanced features as encryption at rest, multi-language pre-flight invoice validation, multiple upload formats, webhooks, event logging, client SDKs, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1
    Contact: info@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from invoicetronic_sdk.models.dati_trasporto import DatiTrasporto

class TestDatiTrasporto(unittest.TestCase):
    """DatiTrasporto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiTrasporto:
        """Test DatiTrasporto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiTrasporto`
        """
        model = DatiTrasporto()
        if include_optional:
            return DatiTrasporto(
                dati_anagrafici_vettore = invoicetronic_sdk.models.dati_anagrafici_vettore.DatiAnagraficiVettore(
                    id_fiscale_iva = invoicetronic_sdk.models.id_fiscale_iva.IdFiscaleIVA(
                        id_paese = '', 
                        id_codice = '', ), 
                    codice_fiscale = '', 
                    anagrafica = invoicetronic_sdk.models.anagrafica.Anagrafica(
                        denominazione = '', 
                        nome = '', 
                        cognome = '', 
                        titolo = '', 
                        cod_eori = '', ), 
                    numero_licenza_guida = '', ),
                mezzo_trasporto = '',
                causale_trasporto = '',
                numero_colli = 56,
                descrizione = '',
                unita_misura_peso = '',
                peso_lordo = 1.337,
                peso_netto = 1.337,
                data_ora_ritiro = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data_inizio_trasporto = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tipo_resa = '',
                indirizzo_resa = invoicetronic_sdk.models.indirizzo_resa.IndirizzoResa(
                    indirizzo = '', 
                    numero_civico = '', 
                    cap = '', 
                    comune = '', 
                    provincia = '', 
                    nazione = 'IT', ),
                data_ora_consegna = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DatiTrasporto(
        )
        """

    def testDatiTrasporto(self):
        """Test DatiTrasporto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
