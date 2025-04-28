# -*- coding: utf-8 -*-
__title__   = "Activate Linework 1"
__doc__     = """Version = 1.0
Date    = 15.06.2024
________________________________________________________________
Description:

________________________________________________________________
Author: Zwe"""

import os
import json
from pyrevit import revit, forms, script
from Autodesk.Revit.UI import RevitCommandId, PostableCommand

# Load config
config_path = os.path.join(script.get_script_path(), "..", "linestyle_config.json")
if not os.path.exists(config_path):
    forms.alert("Line style not set yet. Please run the Set Line Style button first.")
    script.exit()

with open(config_path, "r") as f:
    saved_style = json.load(f).get("linestyle")

if not saved_style:
    forms.alert("Invalid config file.")
    script.exit()

# Get UI app (not DB app)
uiapp = revit.uidoc.Application
linework_cmd = RevitCommandId.LookupPostableCommandId(PostableCommand.Linework)

# Post command to start linework tool
if uiapp.CanPostCommand(linework_cmd):
    uiapp.PostCommand(linework_cmd)
    forms.alert("Linework tool activated.\nNow select '{}' in the Type Selector.".format(saved_style), title="Linework Ready")
else:
    forms.alert("Failed to activate Linework tool.")