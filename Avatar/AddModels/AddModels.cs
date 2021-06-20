using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using LeagueToolkit.IO.MapGeometry;
using LeagueToolkit.IO.OBJ;
using Avatar;
using System.Linq;
using LeagueToolkit.IO.MapParticles;

namespace Avatar.AddModels
{
    public static class AddModels
    {
        //Base Map
      public static void Add_Layer1(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer1);
            mgeo.AddModel(room);

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/DefaultEnv_Flat_AlphaTest.py";
            List<string> materials = new List<string>();
            materials = File.ReadAllLines(ShaderPath).ToList();
            
            
            string number = $"{i}";
            string readfile = File.ReadLines($@"{fullpath}").Skip(12).Take(1).First();
            
            
            //Get texture name without extension
            string replace = readfile.Replace("\\\\", " \\\\ ");
            var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
            string text = gettexturename.Replace(".dds", "");
            string texturename = gettexturename;
            if (mapname == string.Empty)
            {
                mapname = "textures";
            }
            
            //Add Settings to material
            var newList = materials.Select(s => s.Replace("Texture_Name", texturename)).ToList();
            var newList2 = newList.Select(s => s.Replace("Map_Name", mapname)).ToList();
            var newList3 = newList2.Select(s => s.Replace("Material_Name", path)).ToList();
            var newList4 = newList3.Select(s => s.Replace("NOBAKEDLIGHTINGTEMP", Lightmode)).ToList();
            var newList5 = newList4.Select(s => s.Replace("DISABLEDEPTHFOG", Fogmode)).ToList();
            var newList6 = newList5.Select(s => s.Replace("PREMULTIPLIEDALPHA", Alphamode)).ToList();

            //Sun Properties
            
            
            //Writes
            Directory.CreateDirectory("material_output");
            File.AppendAllLines(@"material_output\"+"material.py", newList6);
        }
        //Infernal Map
      public static void Add_Layer2(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer2);
            mgeo.AddModel(room);

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Infernal_Ground.py";
            List<string> materials = new List<string>();
            materials = File.ReadAllLines(ShaderPath).ToList();
            
            //Read Material File
            string number = $"{i}";
            string readfile = File.ReadLines($@"{fullpath}").Skip(12).Take(1).First();
            
            
            //Get texture name without extension
            string replace = readfile.Replace("\\\\", " \\\\ ");
            var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
            string text = gettexturename.Replace(".dds", "");
            string texturename = gettexturename;
            if (mapname == string.Empty)
            {
                mapname = "textures";
            }
            
            //Add Settings to material
            var newList = materials.Select(s => s.Replace("Texture_Name", texturename)).ToList();
            var newList2 = newList.Select(s => s.Replace("Map_Name", mapname)).ToList();
            var newList3 = newList2.Select(s => s.Replace("Material_Name", path)).ToList();
            var newList4 = newList3.Select(s => s.Replace("NOBAKEDLIGHTINGTEMP", Lightmode)).ToList();
            var newList5 = newList4.Select(s => s.Replace("DISABLEDEPTHFOG", Fogmode)).ToList();
            var newList6 = newList5.Select(s => s.Replace("PREMULTIPLIEDALPHA", Alphamode)).ToList();
            
            //Writes
            Directory.CreateDirectory("material_output");
            File.AppendAllLines(@"material_output\"+"material.py", newList6);
        }
        //Mountain Map                                                                     
      public static void Add_Layer3(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer3);
            mgeo.AddModel(room);

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Earth_Ground.py";
            List<string> materials = new List<string>();
            materials = File.ReadAllLines(ShaderPath).ToList();
            
            
            string number = $"{i}";
            string readfile = File.ReadLines($@"{fullpath}").Skip(12).Take(1).First();
            
            
            //Get texture name without extension
            string replace = readfile.Replace("\\\\", " \\\\ ");
            var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
            string text = gettexturename.Replace(".dds", "");
            string texturename = gettexturename;
            if (mapname == string.Empty)
            {
                mapname = "textures";
            }
            
            //Add Settings to material
            var newList = materials.Select(s => s.Replace("Texture_Name", texturename)).ToList();
            var newList2 = newList.Select(s => s.Replace("Map_Name", mapname)).ToList();
            var newList3 = newList2.Select(s => s.Replace("Material_Name", path)).ToList();
            var newList4 = newList3.Select(s => s.Replace("NOBAKEDLIGHTINGTEMP", Lightmode)).ToList();
            var newList5 = newList4.Select(s => s.Replace("DISABLEDEPTHFOG", Fogmode)).ToList();
            var newList6 = newList5.Select(s => s.Replace("PREMULTIPLIEDALPHA", Alphamode)).ToList();
            
            //Writes
            Directory.CreateDirectory("material_output");
            File.AppendAllLines(@"material_output\"+"material.py", newList6);
        }
        //Ocean Map                                                                        
      public static void Add_Layer4(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer4);
            mgeo.AddModel(room);

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Ocean.py";
            List<string> materials = new List<string>();
            materials = File.ReadAllLines(ShaderPath).ToList();
            
            
            string number = $"{i}";
            string readfile = File.ReadLines($@"{fullpath}").Skip(12).Take(1).First();
            
            
            //Get texture name without extension
            string replace = readfile.Replace("\\\\", " \\\\ ");
            var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
            string text = gettexturename.Replace(".dds", "");
            string texturename = gettexturename;
            if (mapname == string.Empty)
            {
                mapname = "textures";
            }
            
            //Add Settings to material
            var newList = materials.Select(s => s.Replace("Texture_Name", texturename)).ToList();
            var newList2 = newList.Select(s => s.Replace("Map_Name", mapname)).ToList();
            var newList3 = newList2.Select(s => s.Replace("Material_Name", path)).ToList();
            var newList4 = newList3.Select(s => s.Replace("NOBAKEDLIGHTINGTEMP", Lightmode)).ToList();
            var newList5 = newList4.Select(s => s.Replace("DISABLEDEPTHFOG", Fogmode)).ToList();
            var newList6 = newList5.Select(s => s.Replace("PREMULTIPLIEDALPHA", Alphamode)).ToList();
            
            //Writes
            Directory.CreateDirectory("material_output");
            File.AppendAllLines(@"material_output\"+"material.py", newList6);
        }
        //Cloud Map                                                                        
      public static void Add_Layer5(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer5);
            mgeo.AddModel(room);

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Cloud_Ground.py";
            List<string> materials = new List<string>();
            materials = File.ReadAllLines(ShaderPath).ToList();
            
            
            string number = $"{i}";
            string readfile = File.ReadLines($@"{fullpath}").Skip(12).Take(1).First();
            
            
            //Get texture name without extension
            string replace = readfile.Replace("\\\\", " \\\\ ");
            var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
            string text = gettexturename.Replace(".dds", "");
            string texturename = gettexturename;
            if (mapname == string.Empty)
            {
                mapname = "textures";
            }
            
            //Add Settings to material
            var newList = materials.Select(s => s.Replace("Texture_Name", texturename)).ToList();
            var newList2 = newList.Select(s => s.Replace("Map_Name", mapname)).ToList();
            var newList3 = newList2.Select(s => s.Replace("Material_Name", path)).ToList();
            var newList4 = newList3.Select(s => s.Replace("NOBAKEDLIGHTINGTEMP", Lightmode)).ToList();
            var newList5 = newList4.Select(s => s.Replace("DISABLEDEPTHFOG", Fogmode)).ToList();
            var newList6 = newList5.Select(s => s.Replace("PREMULTIPLIEDALPHA", Alphamode)).ToList();
            
            //Writes
            Directory.CreateDirectory("material_output");
            File.AppendAllLines(@"material_output\"+"material.py", newList6);
        }
        //All in One :P
      public static void Add_AllLayers(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
            mgeo.AddModel(room);

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/DefaultEnv_Flat_AlphaTest.py";
            List<string> materials = new List<string>();
            materials = File.ReadAllLines(ShaderPath).ToList();
            
            
            string number = $"{i}";
            string readfile = File.ReadLines($@"{fullpath}").Skip(12).Take(1).First();
            
            
            //Get texture name without extension
            string replace = readfile.Replace("\\\\", " \\\\ ");
            var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
            string text = gettexturename.Replace(".dds", "");
            string texturename = gettexturename;
            if (mapname == string.Empty)
            {
                mapname = "textures";
            }
            
            //Add Settings to material
            var newList = materials.Select(s => s.Replace("Texture_Name", texturename)).ToList();
            var newList2 = newList.Select(s => s.Replace("Map_Name", mapname)).ToList();
            var newList3 = newList2.Select(s => s.Replace("Material_Name", path)).ToList();
            var newList4 = newList3.Select(s => s.Replace("NOBAKEDLIGHTINGTEMP", Lightmode)).ToList();
            var newList5 = newList4.Select(s => s.Replace("DISABLEDEPTHFOG", Fogmode)).ToList();
            var newList6 = newList5.Select(s => s.Replace("PREMULTIPLIEDALPHA", Alphamode)).ToList();
            
            //Writes
            Directory.CreateDirectory("material_output");
            File.AppendAllLines(@"material_output\"+"material.py", newList6);
        }
    }
}
