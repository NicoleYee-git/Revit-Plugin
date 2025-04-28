# -*- coding: utf-8 -*-
__title__   = "Set Line Style 1"
__doc__     = """Version = 1.0
Date    = 15.06.2024
________________________________________________________________
Description:

1. set line style
2. activate linework

________________________________________________________________
Author: Zwe"""

import os
import json
from pyrevit import revit, DB, forms, script

# Get all line styles
categories = revit.doc.Settings.Categories
lines_cat = categories.get_Item(DB.BuiltInCategory.OST_Lines)
subcats = lines_cat.SubCategories

line_styles = sorted([sc.Name for sc in subcats])
selected = forms.SelectFromList.show(line_styles, title="Select Line Style", multiselect=False)

if selected:
    # Save to config file
    config_path = os.path.join(script.get_script_path(), "..", "linestyle_config.json")
    with open(config_path, "w") as f:
        json.dump({"linestyle": selected}, f)
    forms.alert("Saved default line style: {}".format(selected))
else:
    forms.alert("No line style selected.")