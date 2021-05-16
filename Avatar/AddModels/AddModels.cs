using System;
using System.Collections.Generic;
using System.Text;
using LeagueToolkit.IO.MapGeometry;
using LeagueToolkit.IO.OBJ;

namespace Avatar.AddModels
{
    public static class AddModels
    {
      public static void Add_Layer1(OBJFile obj, string name, string path, MapGeometry mgeo)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer1);
            mgeo.AddModel(room);
        }

      public static void Add_Layer2(OBJFile obj, string name, string path, MapGeometry mgeo)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer2);
            mgeo.AddModel(room);
        }

      public static void Add_Layer3(OBJFile obj, string name, string path, MapGeometry mgeo)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer3);
            mgeo.AddModel(room);
        }

      public static void Add_Layer4(OBJFile obj, string name, string path, MapGeometry mgeo)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer4);
            mgeo.AddModel(room);
        }

      public static void Add_Layer5(OBJFile obj, string name, string path, MapGeometry mgeo)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer5);
            mgeo.AddModel(room);
        }

      public static void Add_AllLayers(OBJFile obj, string name, string path, MapGeometry mgeo)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
            mgeo.AddModel(room);
        }
    }
}
