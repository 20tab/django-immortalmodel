twentytab-immortalmodel
=======================

A django model, manager and queryset implementing undeletable models

## Installation

Use the following command: <b><i>pip install twentytab-immortalmodel</i></b>


## Usage

- models.py

```py
from immortalmodel.models import ImmortalModel

class MyEternalModel(ImmortalModel):
    pass

```

- admin.py

```py
from immortalmodel.admin import ImmortalAdmin

class MyEternalModel(ImmortalAdmin):
    pass

```