Dataset **morado_5may** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/S/j/KU/EHfiez4EJA561Fe4IrhmkT4SkkSZYal6nG7J68ONnWPDSkuasjmUISjrcvbCic1UnO3QfVCw5wklTB5qtHRogq2Pueqd3hi2q2rDj1cuaIN3Bzyya1gcALugZW8d.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='morado_5may', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/teddevrieslentsch/morado-5may/download?datasetVersionNumber=4)