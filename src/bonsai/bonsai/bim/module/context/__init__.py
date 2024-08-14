# Bonsai - OpenBIM Blender Add-on
# Copyright (C) 2020, 2021 Dion Moult <dion@thinkmoult.com>
#
# This file is part of Bonsai.
#
# Bonsai is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Bonsai is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Bonsai.  If not, see <http://www.gnu.org/licenses/>.

import bpy
from . import ui, prop, operator

classes = (
    operator.AddContext,
    operator.DisableEditingContext,
    operator.EditContext,
    operator.EnableEditingContext,
    operator.RemoveContext,
    prop.BIMContextProperties,
    ui.BIM_PT_context,
)


def register():
    bpy.types.Scene.BIMContextProperties = bpy.props.PointerProperty(type=prop.BIMContextProperties)


def unregister():
    del bpy.types.Scene.BIMContextProperties