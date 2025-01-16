# coding: utf-8

"""
    Italian eInvoice API

    The Italian eInvoice API is a RESTful API that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed by Invoicetronic to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. The API also provides advanced features as encryption at rest, invoice validation, multiple upload formats, webhooks, event logging, client SDKs for commonly used languages, and CLI tools.  For more information, see  [Invoicetronic website][2]  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

    The version of the OpenAPI document: 1.0.0
    Contact: support@invoicetronic.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from invoicetronic_invoice_sdk.models.cedente_prestatore import CedentePrestatore

class TestCedentePrestatore(unittest.TestCase):
    """CedentePrestatore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CedentePrestatore:
        """Test CedentePrestatore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CedentePrestatore`
        """
        model = CedentePrestatore()
        if include_optional:
            return CedentePrestatore(
                dati_anagrafici = invoicetronic_invoice_sdk.models.dati_anagrafici_cedente_prestatore.DatiAnagraficiCedentePrestatore(
                    id_fiscale_iva = invoicetronic_invoice_sdk.models.id_fiscale_iva.IdFiscaleIVA(
                        id_paese = '', 
                        id_codice = '', ), 
                    codice_fiscale = '', 
                    anagrafica = invoicetronic_invoice_sdk.models.anagrafica.Anagrafica(
                        denominazione = '', 
                        nome = '', 
                        cognome = '', 
                        titolo = '', 
                        cod_eori = '', ), 
                    albo_professionale = '', 
                    provincia_albo = '', 
                    numero_iscrizione_albo = '', 
                    data_iscrizione_albo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    regime_fiscale = '', ),
                sede = invoicetronic_invoice_sdk.models.sede_cedente_prestatore.SedeCedentePrestatore(
                    indirizzo = '', 
                    numero_civico = '', 
                    cap = '', 
                    comune = '', 
                    provincia = '', 
                    nazione = 'IT', ),
                stabile_organizzazione = invoicetronic_invoice_sdk.models.stabile_organizzazione.StabileOrganizzazione(
                    indirizzo = '', 
                    numero_civico = '', 
                    cap = '', 
                    comune = '', 
                    provincia = '', 
                    nazione = 'IT', ),
                iscrizione_rea = invoicetronic_invoice_sdk.models.iscrizione_rea.IscrizioneREA(
                    ufficio = '', 
                    numero_rea = '', 
                    capitale_sociale = 1.337, 
                    socio_unico = '', 
                    stato_liquidazione = '', ),
                contatti = invoicetronic_invoice_sdk.models.contatti.Contatti(
                    telefono = '', 
                    fax = '', 
                    email = '', ),
                riferimento_amministrazione = ''
            )
        else:
            return CedentePrestatore(
        )
        """

    def testCedentePrestatore(self):
        """Test CedentePrestatore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
