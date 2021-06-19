using MaterialDesignExtensions.Controls;
using Microsoft.WindowsAPICodePack.Dialogs;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using LeagueToolkit.IO.MapGeometry;
using System.Drawing.Imaging;
using System.IO;
using Xceed.Wpf.Toolkit;
using System.Windows.Forms.Design;
using MaterialDesignThemes.Wpf;
using Avatar.Tools;
using System.Numerics;
using Avatar.AddModels;
using LeagueToolkit.IO.OBJ;
using System.Windows.Forms;
using SharpGLTF.Schema2;
using Xceed.Wpf.Toolkit.Core.Converters;
using System.Drawing;
using Egorozh.ColorPicker.Dialog;
using Egorozh.ColorPicker;
using System.Threading;

namespace Avatar
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : MaterialWindow
    {
        
        public MainWindow()
        {

            InitializeComponent();
            

            //Load SR Templates
            foreach (string srtemp in srfiles)
            {
                New.Items.Add(srtemp.Replace("Templates/SR/New/", "").Replace(".materials.py", ""));
            }
            foreach (string srtemp2 in srfiles2)
            {
                Old.Items.Add(srtemp2.Replace("Templates/SR/Old/", "").Replace(".materials.py", ""));
            }

            //Load ARAM Templates
            foreach (string aramtemp in aramfiles)
            {
                ARAM.Items.Add(aramtemp.Replace("Templates/ARAM/", "").Replace(".materials.py", ""));
            }

            //Load NexusBlitz Templates
            foreach (string nexusblitztemp in nexusblitzfiles)
            {
                NexusBlitz.Items.Add(nexusblitztemp.Replace("Templates/NexusBlitz/", "").Replace(".materials.py", ""));
            }

            //Load TFT Templates
            foreach (string tft1filestemp in tft1files)
            {
                Base.Items.Add(tft1filestemp.Replace("Templates/TFT/base/", "").Replace(".materials.py", ""));
            }
            foreach (string tft2filestemp in tft2files)
            {
                Carousel.Items.Add(tft2filestemp.Replace("Templates/TFT/carousel/", "").Replace(".materials.py", ""));
            }
            foreach (string tft3filestemp in tft3files)
            {
                Darkstar.Items.Add(tft3filestemp.Replace("Templates/TFT/darkstar/", "").Replace(".materials.py", ""));
            }
            foreach (string tft4filestemp in tft4files)
            {
                Freljord.Items.Add(tft4filestemp.Replace("Templates/TFT/freljord/", "").Replace(".materials.py", ""));
            }
            foreach (string tft5filestemp in tft5files)
            {
                Galaxy.Items.Add(tft5filestemp.Replace("Templates/TFT/galaxy/", "").Replace(".materials.py", ""));
            }
            foreach (string tft6filestemp in tft6files)
            {
                Journeys.Items.Add(tft6filestemp.Replace("Templates/TFT/journeys/", "").Replace(".materials.py", ""));
            }
            foreach (string tft7filestemp in tft7files)
            {
                Lunarrevel.Items.Add(tft7filestemp.Replace("Templates/TFT/lunarrevel/", "").Replace(".materials.py", ""));
            }
            foreach (string tft8filestemp in tft8files)
            {
                Odyssey.Items.Add(tft8filestemp.Replace("Templates/TFT/odyssey/", "").Replace(".materials.py", ""));
            }
            foreach (string tft9filestemp in tft9files)
            {
                Set5.Items.Add(tft9filestemp.Replace("Templates/TFT/set5/", "").Replace(".materials.py", ""));
            }
            foreach (string tft10filestemp in tft10files)
            {
                Spiritblossom.Items.Add(tft10filestemp.Replace("Templates/TFT/spiritblossom/", "").Replace(".materials.py", ""));
            }

        }

        

        MapGeometry cleanedmap = new MapGeometry("MapFile/base_srx.mapgeo");
        List<string> cleanedbin = new List<string>();

        string[] templatefolder = Directory.GetDirectories("Templates/");
        string[] templatefiles = Directory.GetFiles("Templates/");
        string[] srfiles = Directory.GetFiles("Templates/SR/New/");
        string[] srfiles2 = Directory.GetFiles("Templates/SR/Old/");
        string[] aramfiles = Directory.GetFiles("Templates/ARAM/");
        string[] nexusblitzfiles = Directory.GetFiles("Templates/NexusBlitz/");

        //TFT Files
        string[] tft1files = Directory.GetFiles("Templates/TFT/base/");
        string[] tft2files = Directory.GetFiles("Templates/TFT/carousel/");
        string[] tft3files = Directory.GetFiles("Templates/TFT/darkstar/");
        string[] tft4files = Directory.GetFiles("Templates/TFT/freljord/");
        string[] tft5files = Directory.GetFiles("Templates/TFT/galaxy/");
        string[] tft6files = Directory.GetFiles("Templates/TFT/journeys/");
        string[] tft7files = Directory.GetFiles("Templates/TFT/lunarrevel/");
        string[] tft8files = Directory.GetFiles("Templates/TFT/odyssey/");
        string[] tft9files = Directory.GetFiles("Templates/TFT/set5/");
        string[] tft10files = Directory.GetFiles("Templates/TFT/spiritblossom/");
        

        private void MenuItem_Click(object sender, RoutedEventArgs e)
        {

        }

        //Open OBJ files
        private void OnOBJFileOpen_Click(object sender, RoutedEventArgs e)
        {
            using CommonOpenFileDialog dialog = new CommonOpenFileDialog();
            dialog.Multiselect = true;
            dialog.Filters.Add(new CommonFileDialogFilter("OBJ Files", "*.obj"));

            



            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {
                AssetBox_Map.Items.Clear();

                TreeViewItem BaseFile = new TreeViewItem();
                BaseFile.Header = "Base Map";
                AssetBox_Map.Items.Add(BaseFile);

                TreeViewItem InfernalFile = new TreeViewItem();
                InfernalFile.Header = "Infernal Map";
                AssetBox_Map.Items.Add(InfernalFile);

                TreeViewItem MountainFile = new TreeViewItem();
                MountainFile.Header = "Mountain Map";
                AssetBox_Map.Items.Add(MountainFile);

                TreeViewItem OceanFile = new TreeViewItem();
                OceanFile.Header = "Ocean Map";
                AssetBox_Map.Items.Add(OceanFile);

                TreeViewItem CloudFile = new TreeViewItem();
                CloudFile.Header = "Cloud Map";
                AssetBox_Map.Items.Add(CloudFile);

                TreeViewItem AllLayerFile = new TreeViewItem();
                AllLayerFile.Header = "All Layer";
                AssetBox_Map.Items.Add(AllLayerFile);



                foreach (string FileName in dialog.FileNames)
                {
                    

                    //Add Files to List Box and group by prefix

                    if (FileName.Contains(prefix_base.Text))
                    {
                        TreeViewItem file1 = new TreeViewItem();
                        file1.Header = System.IO.Path.GetFileName(FileName);
                        BaseFile.Items.Add(file1);
                        //var rootbase = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }
                    if (FileName.Contains(prefix_infernal.Text))
                    {
                        TreeViewItem file2 = new TreeViewItem();
                        file2.Header = System.IO.Path.GetFileName(FileName);
                        InfernalFile.Items.Add(file2);
                        //var rootinfernal = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }
                    if (FileName.Contains(prefix_mountain.Text))
                    {
                        TreeViewItem file3 = new TreeViewItem();
                        file3.Header = System.IO.Path.GetFileName(FileName);
                        MountainFile.Items.Add(file3);
                        //var rootmountain = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }
                    if (FileName.Contains(prefix_ocean.Text))
                    {
                        TreeViewItem file4 = new TreeViewItem();
                        file4.Header = System.IO.Path.GetFileName(FileName);
                        OceanFile.Items.Add(file4);
                        //var rootocean = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }
                    if (FileName.Contains(prefix_cloud.Text))
                    {
                        TreeViewItem file5 = new TreeViewItem();
                        file5.Header = System.IO.Path.GetFileName(FileName);
                        CloudFile.Items.Add(file5);
                        //var rootcloud = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }
                    if (FileName.Contains(prefix_alllayers.Text))
                    {
                        TreeViewItem file6 = new TreeViewItem();
                        file6.Header = System.IO.Path.GetFileName(FileName);
                        AllLayerFile.Items.Add(file6);
                        //var rootcloud = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }


                    //Get Path for visualization
                    var folderpath = System.IO.Path.GetDirectoryName(FileName);
                    Selected_Path.Text = folderpath;

                    
                }
                count_base.Text = BaseFile.Items.Count.ToString();
                count_infernal.Text = InfernalFile.Items.Count.ToString();
                count_mountain.Text = MountainFile.Items.Count.ToString();
                count_ocean.Text = OceanFile.Items.Count.ToString();
                count_cloud.Text = CloudFile.Items.Count.ToString();
                count_alllayers.Text = AllLayerFile.Items.Count.ToString();

                var totalfiles = BaseFile.Items.Count + InfernalFile.Items.Count + MountainFile.Items.Count + OceanFile.Items.Count + AllLayerFile.Items.Count;

                if (AssetBox_Map.Items.Count == 1)
                {

                    System.Windows.MessageBox.Show(totalfiles.ToString() + " file is loaded!", "Done!", MessageBoxButton.OK, MessageBoxImage.Information);
                }

                if (AssetBox_Map.Items.Count > 1)
                {
                    System.Windows.MessageBox.Show(totalfiles.ToString() + " files are loaded!", "Done!", MessageBoxButton.OK, MessageBoxImage.Information);
                }
            }
        }

        //Save the file as MAPGEO
        public void OnMapgeoFileSave_Click(object sender, RoutedEventArgs e)
        {
            using CommonSaveFileDialog dialogsave = new CommonSaveFileDialog();
            dialogsave.Filters.Add(new CommonFileDialogFilter("MAPGEO File", "*.mapgeo"));

            
            

            if (dialogsave.ShowDialog() == CommonFileDialogResult.Ok)
            {
                //Infos for saving
                var layern = "";
                var layers = LayerMode.SelectedIndex;
                if (layers == 0)
                {
                    layern = "All Layers";
                    var BasefileCount = Int32.Parse(count_base.Text);
                    
                    int OBJsToCreate = BasefileCount  + 1;
                    
                    OBJFile[] OBJs = new OBJFile[OBJsToCreate];
                    
                    for (int i = 1; i < OBJsToCreate; i++)
                {
                    

                    try
                    {
                        var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                        var fullpathmtl = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.mtl";
                        var mapname = Map_Name.Text.ToString();

                        //Light Mode
                        //--------------------------------------------------------
                        var lightmodes = "";
                        var lightmode = LightMode.SelectedIndex; //1 is baked
                        if (lightmode == 1)
                            {
                                lightmodes = "\"NO_BAKED_LIGHTING\" = \"1\"";
                            }
                        if (lightmode == 0)
                            {
                                lightmodes = "";
                            }
                        //--------------------------------------------------------

                        //FOG
                        //--------------------------------------------------------
                        var fogmodes = "";
                        var fogmode = FogSet.SelectedIndex; //1 is disable
                        if (fogmode == 1)
                            {
                                fogmodes = "\"DISABLE_DEPTH_FOG\" = \"1\"";
                            }
                        if (fogmode == 0)
                            {
                                fogmodes = "";
                            }
                        //--------------------------------------------------------

                        //Premuliplied Alpha
                        //--------------------------------------------------------
                        var alphamodes = "";
                        var alphamode = AlphaSet.SelectedIndex; //1 is disable
                        if (alphamode == 1)
                            {
                                alphamodes = "";
                            }
                        if (alphamode == 0)
                            {
                                alphamodes = "\"PREMULTIPLIED_ALPHA\" = \"1\"";
                            }
                        //--------------------------------------------------------
                        
                        OBJs[i] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_AllLayers(OBJs[i], $"MapGeo_Instance_room{i}{prefix_base.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}{prefix_base.Text}", cleanedmap, i, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                        //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{i}{prefix_base.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);
                       

                    }

                    catch (Exception)
                    {
                        continue;
                        
                        //var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                        //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }

                } //Base

                } //All Layers
                if (layers == 1)
                {
                    layern = "Auto Layers";
                    var BasefileCount = Int32.Parse(count_base.Text);
                    var InfernalfileCount = Int32.Parse(count_infernal.Text);
                    var MountainfileCount = Int32.Parse(count_mountain.Text);
                    var OceanfileCount = Int32.Parse(count_ocean.Text);
                    var CloudfileCount = Int32.Parse(count_cloud.Text);
                    var AllLayerfileCount = Int32.Parse(count_alllayers.Text);

                    int OBJsToCreate = BasefileCount + 1;
                    int OBJsToCreate2 = InfernalfileCount + 1;
                    int OBJsToCreate3 = MountainfileCount + 1;
                    int OBJsToCreate4 = OceanfileCount + 1;
                    int OBJsToCreate5 = CloudfileCount + 1;
                    int OBJsToCreate6 = AllLayerfileCount + 1;

                    OBJFile[] OBJs = new OBJFile[OBJsToCreate];
                    OBJFile[] OBJ2s = new OBJFile[OBJsToCreate2];
                    OBJFile[] OBJ3s = new OBJFile[OBJsToCreate3];
                    OBJFile[] OBJ4s = new OBJFile[OBJsToCreate4];
                    OBJFile[] OBJ5s = new OBJFile[OBJsToCreate5];
                    OBJFile[] OBJ6s = new OBJFile[OBJsToCreate6];

                    for (int i = 1; i < OBJsToCreate; i++)
                {
                    

                    try
                    {
                        var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                        var fullpathmtl = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.mtl";
                        var mapname = Map_Name.Text.ToString();
                        //Light Mode
                        //--------------------------------------------------------
                        var lightmodes = "";
                        var lightmode = LightMode.SelectedIndex; //1 is baked
                        if (lightmode == 1)
                            {
                                lightmodes = "\"NO_BAKED_LIGHTING\" = \"1\"";
                            }
                        if (lightmode == 0)
                            {
                                lightmodes = "";
                            }
                        //--------------------------------------------------------

                        //FOG
                        //--------------------------------------------------------
                        var fogmodes = "";
                        var fogmode = FogSet.SelectedIndex; //1 is disable
                        if (fogmode == 1)
                            {
                                fogmodes = "";
                            }
                        if (fogmode == 0)
                            {
                                fogmodes = "\"DISABLE_DEPTH_FOG\" = \"1\"";
                            }
                        //--------------------------------------------------------

                        //Premuliplied Alpha
                        //--------------------------------------------------------
                        var alphamodes = "";
                        var alphamode = AlphaSet.SelectedIndex; //1 is disable
                        if (alphamode == 1)
                            {
                                alphamodes = "";
                            }
                        if (alphamode == 0)
                            {
                                alphamodes = "\"PREMULTIPLIED_ALPHA\" = \"1\"";
                            }
                        //--------------------------------------------------------
                        
                        OBJs[i] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer1(OBJs[i], $"MapGeo_Instance_room{i}{prefix_base.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}{prefix_base.Text}", cleanedmap, i, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                        //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{i}{prefix_base.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);
                       

                    }

                    catch (Exception)
                    {
                        continue;
                        
                        //var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                        //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }

                } //Base
                    
                    for (int f = 1; f < OBJsToCreate2; f++) //Fire
                {
                    

                    try
                    {
                        var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_infernal.Text}.obj";
                            var fullpathmtl = Selected_Path.Text + @"\" + $"room{f}{prefix_infernal.Text}.mtl";
                        var mapname = Map_Name.Text.ToString();

                        //Light Mode
                        //--------------------------------------------------------
                        var lightmodes = "";
                        var lightmode = LightMode.SelectedIndex; //1 is baked
                        if (lightmode == 1)
                            {
                                lightmodes = "\"NO_BAKED_LIGHTING\" = \"1\"";
                            }
                        if (lightmode == 0)
                            {
                                lightmodes = "";
                            }
                        //--------------------------------------------------------

                        //FOG
                        //--------------------------------------------------------
                        var fogmodes = "";
                        var fogmode = FogSet.SelectedIndex; //1 is disable
                        if (fogmode == 1)
                            {
                                fogmodes = "";
                            }
                        if (fogmode == 0)
                            {
                                fogmodes = "\"DISABLE_DEPTH_FOG\" = \"1\"";
                            }
                        //--------------------------------------------------------

                        //Premuliplied Alpha
                        //--------------------------------------------------------
                        var alphamodes = "";
                        var alphamode = AlphaSet.SelectedIndex; //1 is disable
                        if (alphamode == 1)
                            {
                                alphamodes = "";
                            }
                        if (alphamode == 0)
                            {
                                alphamodes = "\"PREMULTIPLIED_ALPHA\" = \"1\"";
                            }
                        //--------------------------------------------------------
                        
                        OBJ2s[f] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer2(OBJ2s[f], $"MapGeo_Instance_room{f}{prefix_infernal.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_infernal.Text}", cleanedmap, f, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                        //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_infernal.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);
                       

                    }

                    catch (Exception)
                    {
                        continue;
                        //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_infernal.Text}.obj";
                        //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_infernal.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }

                } //Fire
                    
                    for (int f = 1; f < OBJsToCreate3; f++) //Mountain
                {
                    

                    try
                    {
                        var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_mountain.Text}.obj";
                        var fullpathmtl = Selected_Path.Text + @"\" + $"room{f}{prefix_mountain.Text}.mtl";
                        var mapname = Map_Name.Text.ToString();

                        //Light Mode
                        //--------------------------------------------------------
                        var lightmodes = "";
                        var lightmode = LightMode.SelectedIndex; //1 is baked
                        if (lightmode == 1)
                            {
                                lightmodes = "\"NO_BAKED_LIGHTING\" = \"1\"";
                            }
                        if (lightmode == 0)
                            {
                                lightmodes = "";
                            }
                        //--------------------------------------------------------

                        //FOG
                        //--------------------------------------------------------
                        var fogmodes = "";
                        var fogmode = FogSet.SelectedIndex; //1 is disable
                        if (fogmode == 1)
                            {
                                fogmodes = "";
                            }
                        if (fogmode == 0)
                            {
                                fogmodes = "\"DISABLE_DEPTH_FOG\" = \"1\"";
                            }
                        //--------------------------------------------------------

                        //Premuliplied Alpha
                        //--------------------------------------------------------
                        var alphamodes = "";
                        var alphamode = AlphaSet.SelectedIndex; //1 is disable
                        if (alphamode == 1)
                            {
                                alphamodes = "";
                            }
                        if (alphamode == 0)
                            {
                                alphamodes = "\"PREMULTIPLIED_ALPHA\" = \"1\"";
                            }
                        //--------------------------------------------------------
                        
                        OBJ3s[f] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer3(OBJ3s[f], $"MapGeo_Instance_room{f}{prefix_mountain.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_mountain.Text}", cleanedmap, f, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                        //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_mountain.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);
                       

                    }

                    catch (Exception)
                    {
                        continue;
                        //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_mountain.Text}.obj";
                        //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_mountain.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }

                } //Mountain
                    
                    for (int f = 1; f < OBJsToCreate4; f++) //Ocean
                {
                    

                    try
                    {
                        var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_ocean.Text}.obj";
                        var fullpathmtl = Selected_Path.Text + @"\" + $"room{f}{prefix_ocean.Text}.mtl";
                        var mapname = Map_Name.Text.ToString();

                        //Light Mode
                        //--------------------------------------------------------
                        var lightmodes = "";
                        var lightmode = LightMode.SelectedIndex; //1 is baked
                        if (lightmode == 1)
                            {
                                lightmodes = "\"NO_BAKED_LIGHTING\" = \"1\"";
                            }
                        if (lightmode == 0)
                            {
                                lightmodes = "";
                            }
                        //--------------------------------------------------------

                        //FOG
                        //--------------------------------------------------------
                        var fogmodes = "";
                        var fogmode = FogSet.SelectedIndex; //1 is disable
                        if (fogmode == 1)
                            {
                                fogmodes = "";
                            }
                        if (fogmode == 0)
                            {
                                fogmodes = "\"DISABLE_DEPTH_FOG\" = \"1\"";
                            }
                        //--------------------------------------------------------

                        //Premuliplied Alpha
                        //--------------------------------------------------------
                        var alphamodes = "";
                        var alphamode = AlphaSet.SelectedIndex; //1 is disable
                        if (alphamode == 1)
                            {
                                alphamodes = "";
                            }
                        if (alphamode == 0)
                            {
                                alphamodes = "\"PREMULTIPLIED_ALPHA\" = \"1\"";
                            }
                        //--------------------------------------------------------
                        
                        OBJ4s[f] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer4(OBJ4s[f], $"MapGeo_Instance_room{f}{prefix_ocean.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_ocean.Text}", cleanedmap, f, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                        //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_ocean.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);
                       

                    }

                    catch (Exception)
                    {
                        continue;
                        //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_ocean.Text}.obj";
                        //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_ocean.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }

                } //Ocean
                    
                    for (int f = 1; f < OBJsToCreate5; f++) //Cloud
                    {
                    

                        try
                        {
                            var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj";
                            var fullpathmtl = Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.mtl";
                            var mapname = Map_Name.Text.ToString();
                        
                            //Light Mode
                            //--------------------------------------------------------
                            var lightmodes = "";
                            var lightmode = LightMode.SelectedIndex; //1 is baked
                            if (lightmode == 1)
                                {
                                    lightmodes = "\"NO_BAKED_LIGHTING\" = \"1\"";
                                }
                            if (lightmode == 0)
                                {
                                    lightmodes = "";
                                }
                            //--------------------------------------------------------
                        
                            //FOG
                            //--------------------------------------------------------
                            var fogmodes = "";
                            var fogmode = FogSet.SelectedIndex; //1 is disable
                            if (fogmode == 1)
                                {
                                    fogmodes = "";
                                }
                            if (fogmode == 0)
                                {
                                    fogmodes = "\"DISABLE_DEPTH_FOG\" = \"1\"";
                                }
                            //--------------------------------------------------------
                        
                            //Premuliplied Alpha
                            //--------------------------------------------------------
                            var alphamodes = "";
                            var alphamode = AlphaSet.SelectedIndex; //1 is disable
                            if (alphamode == 1)
                                {
                                    alphamodes = "";
                                }
                            if (alphamode == 0)
                                {
                                    alphamodes = "\"PREMULTIPLIED_ALPHA\" = \"1\"";
                                }
                            //--------------------------------------------------------
                            
                            OBJ5s[f] = new OBJFile(fullpath);
                            AddModels.AddModels.Add_Layer5(OBJ5s[f], $"MapGeo_Instance_room{f}{prefix_cloud.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_cloud.Text}", cleanedmap, f, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                            //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_cloud.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);
                           
                        
                        }
                        
                        catch (Exception)
                        {
                            continue;
                            //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj";
                           // System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }

                    } //Cloud

                    for (int f = 1; f < OBJsToCreate6; f++) //AllLayers
                    {


                        try
                        {
                            var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_alllayers.Text}.obj";
                            var fullpathmtl = Selected_Path.Text + @"\" + $"room{f}{prefix_alllayers.Text}.mtl";
                            var mapname = Map_Name.Text.ToString();

                            //Light Mode
                            //--------------------------------------------------------
                            var lightmodes = "";
                            var lightmode = LightMode.SelectedIndex; //1 is baked
                            if (lightmode == 1)
                            {
                                lightmodes = "\"NO_BAKED_LIGHTING\" = \"1\"";
                            }
                            if (lightmode == 0)
                            {
                                lightmodes = "";
                            }
                            //--------------------------------------------------------

                            //FOG
                            //--------------------------------------------------------
                            var fogmodes = "";
                            var fogmode = FogSet.SelectedIndex; //1 is disable
                            if (fogmode == 1)
                            {
                                fogmodes = "";
                            }
                            if (fogmode == 0)
                            {
                                fogmodes = "\"DISABLE_DEPTH_FOG\" = \"1\"";
                            }
                            //--------------------------------------------------------

                            //Premuliplied Alpha
                            //--------------------------------------------------------
                            var alphamodes = "";
                            var alphamode = AlphaSet.SelectedIndex; //1 is disable
                            if (alphamode == 1)
                            {
                                alphamodes = "";
                            }
                            if (alphamode == 0)
                            {
                                alphamodes = "\"PREMULTIPLIED_ALPHA\" = \"1\"";
                            }
                            //--------------------------------------------------------

                            OBJ6s[f] = new OBJFile(fullpath);
                            AddModels.AddModels.Add_Layer5(OBJ6s[f], $"MapGeo_Instance_room{f}{prefix_alllayers.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_alllayers.Text}", cleanedmap, f, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                            //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_cloud.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);


                        }

                        catch (Exception)
                        {
                            continue;
                            //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj";
                            // System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }

                    } //AllLayers
                } //Auto Layers
                if (layers == 2)
                {
                    layern = "Layer 1";
                    var BasefileCount = Int32.Parse(count_base.Text);

                    int OBJsToCreate = BasefileCount + 1;
                    OBJFile[] OBJs = new OBJFile[OBJsToCreate];
                    
                    for (int i = 1; i < OBJsToCreate; i++)
                {
                    

                    try
                    {
                        var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                        var fullpathmtl = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.mtl";
                        var mapname = Map_Name.Text.ToString();

                        //Light Mode
                        //--------------------------------------------------------
                        var lightmodes = "";
                        var lightmode = LightMode.SelectedIndex; //1 is baked
                        if (lightmode == 1)
                            {
                                lightmodes = "\"NO_BAKED_LIGHTING\" = \"1\"";
                            }
                        if (lightmode == 0)
                            {
                                lightmodes = "";
                            }
                        //--------------------------------------------------------

                        //FOG
                        //--------------------------------------------------------
                        var fogmodes = "";
                        var fogmode = FogSet.SelectedIndex; //1 is disable
                        if (fogmode == 1)
                            {
                                fogmodes = "";
                            }
                        if (fogmode == 0)
                            {
                                fogmodes = "\"DISABLE_DEPTH_FOG\" = \"1\"";
                            }
                        //--------------------------------------------------------

                        //Premuliplied Alpha
                        //--------------------------------------------------------
                        var alphamodes = "";
                        var alphamode = AlphaSet.SelectedIndex; //1 is disable
                        if (alphamode == 1)
                            {
                                alphamodes = "";
                            }
                        if (alphamode == 0)
                            {
                                alphamodes = "\"PREMULTIPLIED_ALPHA\" = \"1\"";
                            }
                        //--------------------------------------------------------
                        
                        OBJs[i] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer1(OBJs[i], $"MapGeo_Instance_room{i}{prefix_base.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}{prefix_base.Text}", cleanedmap, i, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                        //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{i}{prefix_base.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);
                       

                    }

                    catch (Exception)
                    {
                        continue;
                        
                        //var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                        //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }

                } //Base
                } //1 Layer

                
                //-----------------------------------------------
                
                //Writes the mapgeo file and get some infos about it.
                string namemapgeo = dialogsave.FileName;
                string pathmapgeo = System.IO.Path.GetFullPath(namemapgeo);
                string pathmat = pathmapgeo.Replace(".mapgeo", ".materials.py");
                string pathbin = pathmapgeo.Replace(".mapgeo", ".materials.bin");
                cleanedmap.Write(pathmapgeo, 11);
                

                //Get Sun Properties
                var matSunCol = "sunColor: vec4 = { " + $"{SunCR.Text}" + "," + $"{SunCG.Text}" + "," + $"{SunCB.Text}" + "," + $"{SunCA.Text}" + "}";
                var matSunDir = "sunDirection: vec3 = { " + $"{SunDX.Text}" + "," + $"{SunDY.Text}" + "," + $"{SunDZ.Text}" + "}";
                var matSkyCol = "skyLightColor: vec4 = { " + $"{SkyCR.Text}" + "," + $"{SkyCG.Text}" + "," + $"{SkyCB.Text}" + "," + $"{SkyCA.Text}" + "}";
                var matSkyScl = $"skyLightScale: f32 = {SkyS.Text}";
                var matHorCol = "horizonColor: vec4 = { " + $"{HorCR.Text}" + "," + $"{HorCG.Text}" + "," + $"{HorCB.Text}" + "," + $"{HorCA.Text}" + "}";
                var matGrdCol = "groundColor: vec4 = { " + $"{GroundCR.Text}" + "," + $"{GroundCG.Text}" + "," + $"{GroundCB.Text}" + "," + $"{GroundCA.Text}" + "}";
                var matLmpScl = $"lightMapColorScale: f32 = {LMS.Text}";
                var matFog    = $"fogEnabled: bool = {Fog.Text}";
                var matFogSuE = "fogStartAndEnd: vec2 = { " + $"{SliderStart.Value}" + "," + $"{SliderEnd.Value}" + "}";
                var matFogCol = "fogColor: vec4 = { " + $"{FogCR.Text}" + "," + $"{FogCG.Text}" + "," + $"{FogCB.Text}" + "," + $"{FogCA.Text}" + "}";
                var mataFogCol= "fogAlternateColor: vec4 = { " + $"{aFogCR.Text}" + "," + $"{aFogCG.Text}" + "," + $"{aFogCB.Text}" + "," + $"{aFogCA.Text}" + "}";
                var matFEmScl = $"fogEmissiveRemap: f32 = {FogEmRe.Text}";
                var matbloom  = $"useBloom: bool = {Bloom.Text}";

                var matProp   = matSunCol + "\n" + matSunDir + "\n" + matSkyCol + "\n" + matSkyScl + "\n" + matHorCol + "\n" + matGrdCol + "\n" + matLmpScl + "\n" + matFog + "\n" + matFogSuE + "\n" + matFogCol + "\n" + mataFogCol + "\n" + matFEmScl + "\n" + matbloom;
                File.AppendAllText(@"material_output\"+"sunprop.py", matProp);

                string particleplace = "";
                //Load Map Particles and check if they are available
                if (File.Exists("material_output/particles.py"))
                {
                    particleplace = File.ReadAllText("material_output/particles.py");
                }
                

                //Exporting the material bin file
                string sunprops = File.ReadAllText("material_output/sunprop.py");
                string matorginal = File.ReadAllText("MapFile/base_srx.materials.py");
                string matexp = File.ReadAllText("material_output/material.py");
                string originalmtl = matorginal.Replace("PutMatInHere", matexp);
                string originalmtl2 = originalmtl.Replace("SetSunProps", sunprops);
                string originalmtl3 = originalmtl2.Replace("SetParticle", particleplace);
                File.WriteAllText(pathmat, originalmtl3);

                var binfile = System.Diagnostics.Process.Start("ritobin/txt2ritobin.exe", $"{pathmat} {pathbin}");
                

                System.Windows.Forms.MessageBox.Show($"Map Name: {Map_Name.Text}\nLightMode: {LightMode.SelectedIndex}\nFog: {FogSet.SelectedIndex}\nLayers: {layern}\nPremultiplied Alpha: {AlphaSet.SelectedIndex}\n\nPath: {pathmapgeo}", "Done!", MessageBoxButtons.OK, MessageBoxIcon.Information);
                //Cleanes the files to avoid merging
                cleanedmap.Models.Clear();
                binfile.WaitForExit();
                //Deletes the OUTPUT Folder
                System.IO.DirectoryInfo di = new DirectoryInfo("material_output");

                foreach (FileInfo file in di.GetFiles())
                {
                    file.Delete();
                }
                foreach (DirectoryInfo dir in di.GetDirectories())
                {
                    dir.Delete(true);
                }
            }

        }

        //Load Particle Converter
        private void DATParticleButton_Click(object sender, RoutedEventArgs e)
        {
            
            MapParticleDat mapParticleDat = new MapParticleDat();
            mapParticleDat.Show();
        }

        //Load Light Converter
        private void DATLightButton_Click(object sender, RoutedEventArgs e)
        {
            MapLightDat mapLightDat = new MapLightDat();
            mapLightDat.Show();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
           
            
            var dialog = new ColorPickerDialog
            {
              Owner = Owner,
              
            };
            
            SolidColorBrush brush = new SolidColorBrush(System.Windows.Media.Color.FromRgb(21,28,39));
            
            dialog.Background = brush;
            var res = dialog.ShowDialog();
            SolidColorBrush currentColorA = new SolidColorBrush(System.Windows.Media.Color.FromArgb(dialog.Color.A, dialog.Color.R, dialog.Color.G, dialog.Color.B));
            SolidColorBrush currentColor = new SolidColorBrush(System.Windows.Media.Color.FromRgb(dialog.Color.R, dialog.Color.G, dialog.Color.B));
            if (res == true)
            {
                var test = dialog.Color.ToColor();
                CPSun.Background = currentColorA;
                CPSun.BorderBrush = currentColor;

                //Convert Colors to League Values
                var ColorRed = currentColorA.Color.R / 255.0;
                var ColorGreen = currentColorA.Color.G / 255.0;
                var ColorBlue = currentColorA.Color.B / 255.0;
                var ColorAlpha = currentColorA.Color.A / 255.0;

                //Set Split for RGB Color in Buttons
                SunCR.Text = ColorRed.ToString();
                SunCG.Text = ColorGreen.ToString();
                SunCB.Text = ColorBlue.ToString();
                SunCA.Text = ColorAlpha.ToString();
            }
            
            
            

            
        }

        private void CPSky_Click(object sender, RoutedEventArgs e)
        {

            var dialog = new ColorPickerDialog
            {
              Owner = Owner,
              
            };
            
            SolidColorBrush brush = new SolidColorBrush(System.Windows.Media.Color.FromRgb(21,28,39));
            
            dialog.Background = brush;
            var res = dialog.ShowDialog();
            SolidColorBrush currentColorA = new SolidColorBrush(System.Windows.Media.Color.FromArgb(dialog.Color.A, dialog.Color.R, dialog.Color.G, dialog.Color.B));
            SolidColorBrush currentColor = new SolidColorBrush(System.Windows.Media.Color.FromRgb(dialog.Color.R, dialog.Color.G, dialog.Color.B));
            if (res == true)
            {
                var test = dialog.Color.ToColor();
                CPSky.Background = currentColorA;
                CPSky.BorderBrush = currentColor;

                //Convert Colors to League Values
                var ColorRed = currentColorA.Color.R / 255.0;
                var ColorGreen = currentColorA.Color.G / 255.0;
                var ColorBlue = currentColorA.Color.B / 255.0;
                var ColorAlpha = currentColorA.Color.A / 255.0;

                //Set Split for RGB Color in Buttons
                SkyCR.Text = ColorRed.ToString();
                SkyCG.Text = ColorGreen.ToString();
                SkyCB.Text = ColorBlue.ToString();
                SkyCA.Text = ColorAlpha.ToString();
            }

        }

        private void CPHor_Click(object sender, RoutedEventArgs e)
        {

            var dialog = new ColorPickerDialog
            {
              Owner = Owner,
              
            };
            
            SolidColorBrush brush = new SolidColorBrush(System.Windows.Media.Color.FromRgb(21,28,39));
            
            dialog.Background = brush;
            var res = dialog.ShowDialog();
            SolidColorBrush currentColorA = new SolidColorBrush(System.Windows.Media.Color.FromArgb(dialog.Color.A, dialog.Color.R, dialog.Color.G, dialog.Color.B));
            SolidColorBrush currentColor = new SolidColorBrush(System.Windows.Media.Color.FromRgb(dialog.Color.R, dialog.Color.G, dialog.Color.B));
            if (res == true)
            {
                var test = dialog.Color.ToColor();
                CPHor.Background = currentColorA;
                CPHor.BorderBrush = currentColor;

                //Convert Colors to League Values
                var ColorRed = currentColorA.Color.R / 255.0;
                var ColorGreen = currentColorA.Color.G / 255.0;
                var ColorBlue = currentColorA.Color.B / 255.0;
                var ColorAlpha = currentColorA.Color.A / 255.0;

                //Set Split for RGB Color in Buttons
                HorCR.Text = ColorRed.ToString();
                HorCG.Text = ColorGreen.ToString();
                HorCB.Text = ColorBlue.ToString();
                HorCA.Text = ColorAlpha.ToString();
            }

        }

        private void CPGround_Click(object sender, RoutedEventArgs e)
        {
            var dialog = new ColorPickerDialog
            {
              Owner = Owner,
              
            };
            
            SolidColorBrush brush = new SolidColorBrush(System.Windows.Media.Color.FromRgb(21,28,39));
            
            dialog.Background = brush;
            var res = dialog.ShowDialog();
            SolidColorBrush currentColorA = new SolidColorBrush(System.Windows.Media.Color.FromArgb(dialog.Color.A, dialog.Color.R, dialog.Color.G, dialog.Color.B));
            SolidColorBrush currentColor = new SolidColorBrush(System.Windows.Media.Color.FromRgb(dialog.Color.R, dialog.Color.G, dialog.Color.B));
            if (res == true)
            {
                var test = dialog.Color.ToColor();
                CPGround.Background = currentColorA;
                CPGround.BorderBrush = currentColor;

                //Convert Colors to League Values
                var ColorRed = currentColorA.Color.R / 255.0;
                var ColorGreen = currentColorA.Color.G / 255.0;
                var ColorBlue = currentColorA.Color.B / 255.0;
                var ColorAlpha = currentColorA.Color.A / 255.0;

                //Set Split for RGB Color in Buttons
                GroundCR.Text = ColorRed.ToString();
                GroundCG.Text = ColorGreen.ToString();
                GroundCB.Text = ColorBlue.ToString();
                GroundCA.Text = ColorAlpha.ToString();
            }
        }

        private void CPFog_Click(object sender, RoutedEventArgs e)
        {
            var dialog = new ColorPickerDialog
            {
              Owner = Owner,
              
            };
            
            SolidColorBrush brush = new SolidColorBrush(System.Windows.Media.Color.FromRgb(21,28,39));
            
            dialog.Background = brush;
            var res = dialog.ShowDialog();
            SolidColorBrush currentColorA = new SolidColorBrush(System.Windows.Media.Color.FromArgb(dialog.Color.A, dialog.Color.R, dialog.Color.G, dialog.Color.B));
            SolidColorBrush currentColor = new SolidColorBrush(System.Windows.Media.Color.FromRgb(dialog.Color.R, dialog.Color.G, dialog.Color.B));
            if (res == true)
            {
                var test = dialog.Color.ToColor();
                CPFog.Background = currentColorA;
                CPFog.BorderBrush = currentColor;

                //Convert Colors to League Values
                var ColorRed = currentColorA.Color.R / 255.0;
                var ColorGreen = currentColorA.Color.G / 255.0;
                var ColorBlue = currentColorA.Color.B / 255.0;
                var ColorAlpha = currentColorA.Color.A / 255.0;

                //Set Split for RGB Color in Buttons
                FogCR.Text = ColorRed.ToString();
                FogCG.Text = ColorGreen.ToString();
                FogCB.Text = ColorBlue.ToString();
                FogCA.Text = ColorAlpha.ToString();
            }
        }

        private void CPaFog_Click(object sender, RoutedEventArgs e)
        {
            var dialog = new ColorPickerDialog
            {
              Owner = Owner,
              
            };
            
            SolidColorBrush brush = new SolidColorBrush(System.Windows.Media.Color.FromRgb(21,28,39));
            
            dialog.Background = brush;
            var res = dialog.ShowDialog();
            SolidColorBrush currentColorA = new SolidColorBrush(System.Windows.Media.Color.FromArgb(dialog.Color.A, dialog.Color.R, dialog.Color.G, dialog.Color.B));
            SolidColorBrush currentColor = new SolidColorBrush(System.Windows.Media.Color.FromRgb(dialog.Color.R, dialog.Color.G, dialog.Color.B));
            if (res == true)
            {
                var test = dialog.Color.ToColor();
                CPaFog.Background = currentColorA;
                CPaFog.BorderBrush = currentColor;

                //Convert Colors to League Values
                var ColorRed = currentColorA.Color.R / 255.0;
                var ColorGreen = currentColorA.Color.G / 255.0;
                var ColorBlue = currentColorA.Color.B / 255.0;
                var ColorAlpha = currentColorA.Color.A / 255.0;

                //Set Split for RGB Color in Buttons
                aFogCR.Text = ColorRed.ToString();
                aFogCG.Text = ColorGreen.ToString();
                aFogCB.Text = ColorBlue.ToString();
                aFogCA.Text = ColorAlpha.ToString();
            }
        }

        private void ToggleSunC_Checked(object sender, RoutedEventArgs e)
        {
            SunCR.IsEnabled = true;
            SunCG.IsEnabled = true;
            SunCB.IsEnabled = true;
            SunCA.IsEnabled = true;
            CPSun.IsEnabled = true;
        }

        private void ToggleSunC_Unchecked(object sender, RoutedEventArgs e)
        {
            SunCR.IsEnabled = false;
            SunCG.IsEnabled = false;
            SunCB.IsEnabled = false;
            SunCA.IsEnabled = false;
            CPSun.IsEnabled = false;
        }

        private void ToggleSunD_Checked(object sender, RoutedEventArgs e)
        {
            SunDX.IsEnabled = true;
            SunDY.IsEnabled = true;
            SunDZ.IsEnabled = true;
        }

        private void ToggleSunD_Unchecked(object sender, RoutedEventArgs e)
        {
            SunDX.IsEnabled = false;
            SunDY.IsEnabled = false;
            SunDZ.IsEnabled = false;
        }

        private void ToggleSkyC_Checked(object sender, RoutedEventArgs e)
        {
            SkyCR.IsEnabled = true;
            SkyCG.IsEnabled = true;
            SkyCB.IsEnabled = true;
            SkyCA.IsEnabled = true;
            CPSky.IsEnabled = true;
        }

        private void ToggleSkyC_Unchecked(object sender, RoutedEventArgs e)
        {
            SkyCR.IsEnabled = false;
            SkyCG.IsEnabled = false;
            SkyCB.IsEnabled = false;
            SkyCA.IsEnabled = false;
            CPSky.IsEnabled = false;
        }

        private void ToogleSkyS_Checked(object sender, RoutedEventArgs e)
        {
            SkyS.IsEnabled = true;
        }

        private void ToogleSkyS_Unchecked(object sender, RoutedEventArgs e)
        {
            SkyS.IsEnabled = false;
        }

        private void ToggleHorC_Checked(object sender, RoutedEventArgs e)
        {
            HorCR.IsEnabled = true;
            HorCG.IsEnabled = true;
            HorCB.IsEnabled = true;
            HorCA.IsEnabled = true;
            CPHor.IsEnabled = true;
        }

        private void ToggleHorC_Unchecked(object sender, RoutedEventArgs e)
        {
            HorCR.IsEnabled = false;
            HorCG.IsEnabled = false;
            HorCB.IsEnabled = false;
            HorCA.IsEnabled = false;
            CPHor.IsEnabled = false;
        }

        private void ToggleGroundC_Checked(object sender, RoutedEventArgs e)
        {
            GroundCR.IsEnabled = true;
            GroundCG.IsEnabled = true;
            GroundCB.IsEnabled = true;
            GroundCA.IsEnabled = true;
            CPGround.IsEnabled = true;
        }

        private void ToggleGroundC_Unchecked(object sender, RoutedEventArgs e)
        {
            GroundCR.IsEnabled = false;
            GroundCG.IsEnabled = false;
            GroundCB.IsEnabled = false;
            GroundCA.IsEnabled = false;
            CPGround.IsEnabled = false;
        }

        private void ToggleLMS_Checked(object sender, RoutedEventArgs e)
        {
            LMS.IsEnabled = true;
        }

        private void ToggleLMS_Unchecked(object sender, RoutedEventArgs e)
        {
            LMS.IsEnabled = false;
        }

        private void ToggleFog_Checked(object sender, RoutedEventArgs e)
        {
            Fog.IsEnabled = true;

        }

        private void ToggleFog_Unchecked(object sender, RoutedEventArgs e)
        {
            Fog.IsEnabled = false;
            ToggleFogStartEnd.IsChecked = false;
            ToggleFogC.IsChecked = false;
            ToggleFogaC.IsChecked = false;
            ToggleFogEmRe.IsChecked = false;
        }

        private void ToggleFogStartEnd_Checked(object sender, RoutedEventArgs e)
        {
            FogStart.IsEnabled = true;
            FogEnd.IsEnabled = true;
        }

        private void ToggleFogStartEnd_Unchecked(object sender, RoutedEventArgs e)
        {
            FogStart.IsEnabled = false;
            FogEnd.IsEnabled = false;
        }

        private void ToggleFogC_Checked(object sender, RoutedEventArgs e)
        {
            FogCR.IsEnabled = true;
            FogCG.IsEnabled = true;
            FogCB.IsEnabled = true;
            FogCA.IsEnabled = true;
            CPFog.IsEnabled = true;
        }

        private void ToggleFogC_Unchecked(object sender, RoutedEventArgs e)
        {
            FogCR.IsEnabled = false;
            FogCG.IsEnabled = false;
            FogCB.IsEnabled = false;
            FogCA.IsEnabled = false;
            CPFog.IsEnabled = false;
        }

        private void ToggleFogaC_Checked(object sender, RoutedEventArgs e)
        {
            aFogCR.IsEnabled = true;
            aFogCG.IsEnabled = true;
            aFogCB.IsEnabled = true;
            aFogCA.IsEnabled = true;
            CPaFog.IsEnabled = true;
        }

        private void ToggleFogaC_Unchecked(object sender, RoutedEventArgs e)
        {
            aFogCR.IsEnabled = false;
            aFogCG.IsEnabled = false;
            aFogCB.IsEnabled = false;
            aFogCA.IsEnabled = false;
            CPaFog.IsEnabled = false;
        }

        private void ToggleFogEmRe_Checked(object sender, RoutedEventArgs e)
        {
            FogEmRe.IsEnabled = true;
        }

        private void ToggleFogEmRe_Unchecked(object sender, RoutedEventArgs e)
        {
            FogEmRe.IsEnabled = false;
        }

        private void ToggleBloom_Checked(object sender, RoutedEventArgs e)
        {
            Bloom.IsEnabled = true;
        }

        private void ToggleBloom_Unchecked(object sender, RoutedEventArgs e)
        {
            Bloom.IsEnabled = false;
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void TemplatesButton_Click(object sender, RoutedEventArgs e)
        {
            
            
            
        }

        private void SelectIMG_Click(object sender, RoutedEventArgs e)
        {
            using CommonOpenFileDialog dialog = new CommonOpenFileDialog();
            dialog.Multiselect = true;
            dialog.Filters.Add(new CommonFileDialogFilter("DDS Files", "*.dds"));

            



            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {
                loadingscreenpic.Source = new BitmapImage(new Uri(dialog.FileName));
            }
        }

        private void SliderEnd_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }
    }
}
