'''Script to assign gate numbers to features in a QGIS layer for DAS
Each feature within a 100m x 100m cell is assigned a sequential gate number
based on its NW to SE position within that cell.'''

'''
Written by: Sam Kibui
Date: January 2026
'''

from qgis.PyQt.QtCore import QVariant
from qgis.core import *
import math

LAYER_NAME="Building Footprints" 
LAYER_NAME_INSTANCE=QgsProject.instance().mapLayersByName(LAYER_NAME)[0].name()
CELL_FIELD = "cell_100m"
GATE_FIELD = "gate_no"

GRID_M = 100
DEG_PER_M = 1 / 111320
GRID_DEG = GRID_M * DEG_PER_M

layer = QgsProject.instance().mapLayersByName(LAYER_NAME)[0]

# Ensure fields exist
provider = layer.dataProvider()
fields = [f.name() for f in layer.fields()]

if CELL_FIELD not in fields:
    provider.addAttributes([QgsField(CELL_FIELD, QVariant.String)])
if GATE_FIELD not in fields:
    provider.addAttributes([QgsField(GATE_FIELD, QVariant.Int)])

layer.updateFields()

def compute_cell(point):
    gx = math.floor(point.x() / GRID_DEG)
    gy = math.floor(point.y() / GRID_DEG)
    return f"{gx}_{gy}"

# Group features by 100m cell
cells = {}

for f in layer.getFeatures():
    
    p = f.geometry().centroid().asPoint()
    cell_id = compute_cell(p)

    if cell_id not in cells:
        cells[cell_id] = []

    cells[cell_id].append((f.id(), p))

layer.startEditing()

# Assign gate numbers per cell
for cell_id, items in cells.items():

    # NW → SE ordering
    items.sort(key=lambda x: (-x[1].y(), x[1].x()))

    for idx, (fid, point) in enumerate(items, start=1):
        layer.changeAttributeValue(fid,
            layer.fields().indexFromName(CELL_FIELD), cell_id)
        layer.changeAttributeValue(fid,
            layer.fields().indexFromName(GATE_FIELD), idx)

layer.commitChanges()

print("Gate numbers assigned successfully.")
