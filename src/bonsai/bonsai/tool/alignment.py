# Bonsai - OpenBIM Blender Add-on
# Copyright (C) 2022 Dion Moult <dion@thinkmoult.com>
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

# ############################################################################ #

# Hey there! Welcome to the Bonsai code. Please feel free to reach
# out if you have any questions or need further guidance. Happy hacking!

# ############################################################################ #

# Every module has a tool file which implements all the functions that the core
# needs. Whereas the core is simply high level code, the tool file has the
# concrete implementations, dealing with exactly how things interact with
# Blender's property systems, IFC's data structures, the filesystem, geometry
# processing, and more.

import ifcopenshell.settings
import bpy
import bonsai.core.tool
import bonsai.tool as tool
import ifcopenshell.api
import ifcopenshell.alignment
import ifcopenshell

# There is always one class in each tool file, which implements the interface
# defined by `core/tool.py`.
class Alignment(bonsai.core.tool.Alignment):
    @classmethod
    def build(cls):
        coordinates = [(0.0,0.0),(100.0,0.0),(200.0,200.0)]
        radii = [(50.0)]
        helper = ifcopenshell.alignment.IfcAlignmentHelper(tool.Ifc.get())
        alignment = helper.add_alignment("Dummy",coordinates,radii)
        # add_alignment isn't returning anything, so to 
        # get around that, get the alignment from the file
        # this is a bad soluton because it only works for the first
        # alignment in the file
        if not alignment:
            alignment = tool.Ifc.by_type("IfcAlignment")[0]
        
        # get the IfcCompositeCurve
        curve = alignment.Representation.Representations[0].Items[0]

        #need to get all of the "IfcSite" in the model and reference the alignment in the spatial structure with IfcRelReferencedInSpatialStructure
 
        s = ifcopenshell.geom.settings()
        shape = ifcopenshell.geom.create_shape(s,curve)
        mesh = bpy.data.meshes.new("IfcAlignment")
        m = tool.Loader.convert_geometry_to_mesh(shape,mesh)
        tool.Geometry.link(alignment,m)
        tool.Collector.assign(mesh)