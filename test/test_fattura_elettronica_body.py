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

from invoicetronic_sdk.models.fattura_elettronica_body import FatturaElettronicaBody

class TestFatturaElettronicaBody(unittest.TestCase):
    """FatturaElettronicaBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FatturaElettronicaBody:
        """Test FatturaElettronicaBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FatturaElettronicaBody`
        """
        model = FatturaElettronicaBody()
        if include_optional:
            return FatturaElettronicaBody(
                dati_generali = invoicetronic_sdk.models.dati_generali.DatiGenerali(
                    dati_generali_documento = invoicetronic_sdk.models.dati_generali_documento.DatiGeneraliDocumento(
                        tipo_documento = '', 
                        divisa = '', 
                        data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        numero = '', 
                        dati_ritenuta = [
                            invoicetronic_sdk.models.dati_ritenuta.DatiRitenuta(
                                tipo_ritenuta = '', 
                                importo_ritenuta = 1.337, 
                                aliquota_ritenuta = 1.337, 
                                causale_pagamento = '', )
                            ], 
                        dati_bollo = invoicetronic_sdk.models.dati_bollo.DatiBollo(
                            bollo_virtuale = '', 
                            importo_bollo = 1.337, ), 
                        dati_cassa_previdenziale = [
                            invoicetronic_sdk.models.dati_cassa_previdenziale.DatiCassaPrevidenziale(
                                tipo_cassa = '', 
                                al_cassa = 1.337, 
                                importo_contributo_cassa = 1.337, 
                                imponibile_cassa = 1.337, 
                                aliquota_iva = 1.337, 
                                ritenuta = '', 
                                natura = '', 
                                riferimento_amministrazione = '', )
                            ], 
                        sconto_maggiorazione = [
                            invoicetronic_sdk.models.sconto_maggiorazione.ScontoMaggiorazione(
                                tipo = '', 
                                percentuale = 1.337, 
                                importo = 1.337, )
                            ], 
                        importo_totale_documento = 1.337, 
                        arrotondamento = 1.337, 
                        causale = [
                            ''
                            ], 
                        art73 = '', ), 
                    dati_ordine_acquisto = [
                        invoicetronic_sdk.models.dati_ordine_acquisto.DatiOrdineAcquisto(
                            riferimento_numero_linea = [
                                56
                                ], 
                            id_documento = '', 
                            data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            num_item = '', 
                            codice_commessa_convenzione = '', 
                            codice_cup = '', 
                            codice_cig = '', )
                        ], 
                    dati_contratto = [
                        invoicetronic_sdk.models.dati_contratto.DatiContratto(
                            id_documento = '', 
                            data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            num_item = '', 
                            codice_commessa_convenzione = '', 
                            codice_cup = '', 
                            codice_cig = '', )
                        ], 
                    dati_convenzione = [
                        invoicetronic_sdk.models.dati_convenzione.DatiConvenzione(
                            id_documento = '', 
                            data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            num_item = '', 
                            codice_commessa_convenzione = '', 
                            codice_cup = '', 
                            codice_cig = '', )
                        ], 
                    dati_ricezione = [
                        invoicetronic_sdk.models.dati_ricezione.DatiRicezione(
                            id_documento = '', 
                            data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            num_item = '', 
                            codice_commessa_convenzione = '', 
                            codice_cup = '', 
                            codice_cig = '', )
                        ], 
                    dati_fatture_collegate = [
                        invoicetronic_sdk.models.dati_fatture_collegate.DatiFattureCollegate(
                            id_documento = '', 
                            data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            num_item = '', 
                            codice_commessa_convenzione = '', 
                            codice_cup = '', 
                            codice_cig = '', )
                        ], 
                    dati_sal = [
                        invoicetronic_sdk.models.dati_sal.DatiSAL(
                            riferimento_fase = 56, )
                        ], 
                    dati_ddt = [
                        invoicetronic_sdk.models.dati_ddt.DatiDDT(
                            numero_ddt = '', 
                            data_ddt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    dati_trasporto = invoicetronic_sdk.models.dati_trasporto.DatiTrasporto(
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
                        data_ora_consegna = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    fattura_principale = invoicetronic_sdk.models.fattura_principale.FatturaPrincipale(
                        numero_fattura_principale = '', 
                        data_fattura_principale = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ),
                dati_beni_servizi = invoicetronic_sdk.models.dati_beni_servizi.DatiBeniServizi(
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
                        ], ),
                dati_veicoli = invoicetronic_sdk.models.dati_veicoli.DatiVeicoli(
                    data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    totale_percorso = '', ),
                dati_pagamento = [
                    invoicetronic_sdk.models.dati_pagamento.DatiPagamento(
                        condizioni_pagamento = '', 
                        dettaglio_pagamento = [
                            invoicetronic_sdk.models.dettaglio_pagamento.DettaglioPagamento(
                                beneficiario = '', 
                                modalita_pagamento = '', 
                                data_riferimento_termini_pagamento = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                giorni_termini_pagamento = 56, 
                                data_scadenza_pagamento = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                importo_pagamento = 1.337, 
                                cod_ufficio_postale = '', 
                                cognome_quietanzante = '', 
                                nome_quietanzante = '', 
                                cf_quietanzante = '', 
                                titolo_quietanzante = '', 
                                istituto_finanziario = '', 
                                iban = '', 
                                abi = '', 
                                cab = '', 
                                bic = '', 
                                sconto_pagamento_anticipato = 1.337, 
                                data_limite_pagamento_anticipato = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                penalita_pagamenti_ritardati = 1.337, 
                                data_decorrenza_penale = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                codice_pagamento = '', )
                            ], )
                    ],
                allegati = [
                    invoicetronic_sdk.models.allegati.Allegati(
                        nome_attachment = '', 
                        algoritmo_compressione = '', 
                        formato_attachment = '', 
                        descrizione_attachment = '', 
                        attachment = 'YQ==', )
                    ]
            )
        else:
            return FatturaElettronicaBody(
        )
        """

    def testFatturaElettronicaBody(self):
        """Test FatturaElettronicaBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
