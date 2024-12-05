# DettaglioLinee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_linea** | **int** |  | [optional] 
**tipo_cessione_prestazione** | **str** |  | [optional] 
**codice_articolo** | [**List[CodiceArticolo]**](CodiceArticolo.md) |  | [optional] 
**descrizione** | **str** |  | [optional] 
**quantita** | **float** |  | [optional] 
**unita_misura** | **str** |  | [optional] 
**data_inizio_periodo** | **datetime** |  | [optional] 
**data_fine_periodo** | **datetime** |  | [optional] 
**prezzo_unitario** | **float** |  | [optional] 
**sconto_maggiorazione** | [**List[ScontoMaggiorazione]**](ScontoMaggiorazione.md) |  | [optional] 
**prezzo_totale** | **float** |  | [optional] 
**aliquota_iva** | **float** |  | [optional] 
**ritenuta** | **str** |  | [optional] 
**natura** | **str** |  | [optional] 
**riferimento_amministrazione** | **str** |  | [optional] 
**altri_dati_gestionali** | [**List[AltriDatiGestionali]**](AltriDatiGestionali.md) |  | [optional] 

## Example

```python
from invoicetronic_einvoice_sdk.models.dettaglio_linee import DettaglioLinee

# TODO update the JSON string below
json = "{}"
# create an instance of DettaglioLinee from a JSON string
dettaglio_linee_instance = DettaglioLinee.from_json(json)
# print the JSON string representation of the object
print(DettaglioLinee.to_json())

# convert the object into a dict
dettaglio_linee_dict = dettaglio_linee_instance.to_dict()
# create an instance of DettaglioLinee from a dict
dettaglio_linee_from_dict = DettaglioLinee.from_dict(dettaglio_linee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


