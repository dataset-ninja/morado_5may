Dataset **morado_5may** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/S/j/KU/EHfiez4EJA561Fe4IrhmkT4SkkSZYal6nG7J68ONnWPDSkuasjmUISjrcvbCic1UnO3QfVCw5wklTB5qtHRogq2Pueqd3hi2q2rDj1cuaIN3Bzyya1gcALugZW8d.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='morado_5may', dst_path='~/dtools/datasets/morado_5may.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/teddevrieslentsch/morado-5may/download?datasetVersionNumber=4)