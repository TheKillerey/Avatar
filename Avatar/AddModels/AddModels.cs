using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using LeagueToolkit.IO.MapGeometry;
using LeagueToolkit.IO.OBJ;
using Avatar;
using System.Linq;
using LeagueToolkit.IO.MapParticles;
using LeagueToolkit.IO.MaterialLibrary;
using System.Text.RegularExpressions;

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
            if (room.Vertices.Count > 0)
            {
                mgeo.AddModel(room);
            }
            else
            {
                return;
            }

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Master.py";
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
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Master.py";
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
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Master.py";
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
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Master.py";
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
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Master.py";
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
        //Hextech Map
      public static void Add_Layer6(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer6);
            mgeo.AddModel(room);

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Master.py";
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
            File.AppendAllLines(@"material_output\" + "material.py", newList6);
        }
        //Chemtech Map
      public static void Add_Layer7(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer7);
            mgeo.AddModel(room);

            //Porting material file to league format
            string ShaderPath = "MapFile/ShaderTemp/SRX_Blend_Master.py";
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
            File.AppendAllLines(@"material_output\" + "material.py", newList6);
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
            string DecalPath = "MapFile/ShaderTemp/DefaultEnv_Flat_AlphaTest_decal.py";
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
        //All in One but for adding solo objects to original maps
      public static void Add_SoloAllLayers(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
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
            File.AppendAllLines(@"material_output\" + "material_solo.py", newList6);
        }

      public static void Add_AllLayersDecal(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
            mgeo.AddModel(room);

            //Porting material file to league format
            
            string DecalPath = "MapFile/ShaderTemp/DefaultEnv_Flat_AlphaTest_decal.py";
            List<string> materials = new List<string>();



            materials = File.ReadAllLines(DecalPath).ToList();

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
            File.AppendAllLines(@"material_output\" + "material.py", newList6);
        }

      public static void Add_AllLayersEmissive(OBJFile obj, string name, string path, MapGeometry mgeo, int i, string fullpath, string mapname, string Lightmode, string Fogmode, string Alphamode)
        {
            
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
            mgeo.AddModel(room);

            //Porting material file to league format

            string EmissivePath = $"MapFile/ShaderTemp/Default_Emissive.py";
            string OnlyEmissivePath = $"MapFile/ShaderTemp/Emissive_Basic.py";
            string ReadMTLFile = File.ReadAllText(fullpath);

            //Since MTL uses a different color range we need to multiply it with 0.058479539 to get 0-1 rgb


            List<string> materials = new List<string>();

            if (!ReadMTLFile.Contains(".dds"))
            {
                EmissivePath = OnlyEmissivePath;
            }


            materials = File.ReadAllLines(EmissivePath).ToList();

            if (ReadMTLFile.Contains(".dds")) //If the mtl contains .dds do this
            {
                string readfile = File.ReadLines($@"{fullpath}").Skip(12).Take(1).First(); //Diffuse Line
                string readfileem = File.ReadLines($@"{fullpath}").Skip(13).Take(1).First(); //Emissive Line
                //string readcolor = File.ReadLines($@"{fullpath}").Skip(8).Take(1).First();



                //Get texture name without extension
                string replace = readfile.Replace("\\\\", " \\\\ ");
                string replaceem = readfileem.Replace("\\\\", " \\\\ ");
                

                //Get Diffuse Texture
                var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
                //Get Emissive Texture
                var gettexturenameem = string.Join(" ", replaceem.Split().Reverse().Take(1).Reverse());
                
                string text = gettexturename.Replace(".dds", "");
                string textem = gettexturenameem.Replace(".dds", "");
                
                string texturename = gettexturename;
                string emissivename = gettexturenameem;
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
                var newList7 = newList6.Select(s => s.Replace("Emissive_Name", emissivename)).ToList();
                

                //Writes
                Directory.CreateDirectory("material_output");
                File.AppendAllLines(@"material_output\" + "material.py", newList7);
            } 
            else
            {
                //Get color line of mtl file
                string readcolor = File.ReadLines($@"{fullpath}").Skip(6).Take(1).First();

                string replacecolor = readcolor.Replace("\\\\", " \\\\ ");

                //Get Color Codes

                var getcolorred = Regex.Matches(replacecolor, @"\d+\.*\d*")[0].Value;
                var getcolorgreen = Regex.Matches(replacecolor, @"\d+\.*\d*")[1].Value;
                var getcolorblue = Regex.Matches(replacecolor, @"\d+\.*\d*")[2].Value;

                //Convert mtl color to 0-1 RGB. Not sure if it's a bug that we get 17 as big number

                var colorred = (int)(Double.Parse(getcolorred)) * 0.058479539 + 0.5;
                var colorgreen = (int)(Double.Parse(getcolorgreen)) * 0.058479539 + 0.5;
                var colorblue = (int)(Double.Parse(getcolorblue)) * 0.058479539 + 0.5;

                if (mapname == string.Empty)
                {
                    mapname = "textures";
                }


                //Add Settings to material
                
                var newList2 = materials.Select(s => s.Replace("Map_Name", mapname)).ToList();
                var newList3 = newList2.Select(s => s.Replace("Material_Name", path)).ToList();
                var newList4 = newList3.Select(s => s.Replace("NOBAKEDLIGHTINGTEMP", Lightmode)).ToList();
                var newList5 = newList4.Select(s => s.Replace("DISABLEDEPTHFOG", Fogmode)).ToList();
                var newList6 = newList5.Select(s => s.Replace("PREMULTIPLIEDALPHA", Alphamode)).ToList();
                
                var newList7 = newList6.Select(s => s.Replace("EM_Red", getcolorred.ToString())).ToList();
                var newList8 = newList7.Select(s => s.Replace("EM_Green", getcolorgreen.ToString())).ToList();
                var newList9 = newList8.Select(s => s.Replace("EM_Blue", getcolorblue.ToString())).ToList();

                //Writes
                Directory.CreateDirectory("material_output");
                File.AppendAllLines(@"material_output\" + "material.py", newList9);
            }

            
        }
    }
}
