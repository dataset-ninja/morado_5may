Dataset **Morado 5 May** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/P/W/tD/6UMlhoCXPpMQdQI9fYiES0kNWl2o5w17Tl1SRdiokOEcZ1KBbU5g7DJN9LiU056YtgzHjIZq5WzHl0xzO4ks2u81A797RPYrtZAtRo0EGhf4wkVzl81KbzsEZpRZ.tar)

As an alternative, it can be downloaded with dataset-tools package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Morado 5 May', dst_path='~/dtools/datasets/Morado 5 May.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/teddevrieslentsch/morado-5may/download?datasetVersionNumber=4)