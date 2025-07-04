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

from invoicetronic_sdk.models.dati_beni_servizi import DatiBeniServizi

class TestDatiBeniServizi(unittest.TestCase):
    """DatiBeniServizi unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiBeniServizi:
        """Test DatiBeniServizi
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiBeniServizi`
        """
        model = DatiBeniServizi()
        if include_optional:
            return DatiBeniServizi(
                dettaglio_linee = [
                    invoicetronic_sdk.models.dettaglio_linee.DettaglioLinee(
                        numero_linea = 56, 
                        tipo_cessione_prestazione = '', 
                        codice_articolo = [
                            invoicetronic_sdk.models.codice_articolo.CodiceArticolo(
                                codice_tipo = '', 
                                codice_valore = '', )
                            ], 
                        descrizione = '', 
                        quantita = 1.337, 
                        unita_misura = '', 
                        data_inizio_periodo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        data_fine_periodo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        prezzo_unitario = 1.337, 
                        sconto_maggiorazione = [
                            invoicetronic_sdk.models.sconto_maggiorazione.ScontoMaggiorazione(
                                tipo = '', 
                                percentuale = 1.337, 
                                importo = 1.337, )
                            ], 
                        prezzo_totale = 1.337, 
                        aliquota_iva = 1.337, 
                        ritenuta = '', 
                        natura = '', 
                        riferimento_amministrazione = '', 
                        altri_dati_gestionali = [
                            invoicetronic_sdk.models.altri_dati_gestionali.AltriDatiGestionali(
                                tipo_dato = '', 
                                riferimento_testo = '', 
                                riferimento_numero = 1.337, 
                                riferimento_data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ],
                dati_riepilogo = [
                    invoicetronic_sdk.models.dati_riepilogo.DatiRiepilogo(
                        aliquota_iva = 1.337, 
                        natura = '', 
                        spese_accessorie = 1.337, 
                        arrotondamento = 1.337, 
                        imponibile_importo = 1.337, 
                        imposta = 1.337, 
                        esigibilita_iva = '', 
                        riferimento_normativo = '', )
                    ]
            )
        else:
            return DatiBeniServizi(
        )
        """

    def testDatiBeniServizi(self):
        """Test DatiBeniServizi"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
