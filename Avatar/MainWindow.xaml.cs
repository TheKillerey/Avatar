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
using Avatar.MapConvert;
using System.Windows.Media.Effects;
using System.Diagnostics;
using LeagueToolkit.IO.PropertyBin;
using LeagueToolkit.Meta;
using System.Reflection;
using LeagueToolkit.Meta.Classes;
using LeagueToolkit.Meta.Attributes;
using LeagueToolkit.Meta.Dump;
using LiveSearchTextBoxControl;
using System.Net;


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
            BundledTheme bundledTheme = new BundledTheme();
            MaterialEditorGrid.Visibility = Visibility.Hidden;
            SunProp.Visibility = Visibility.Hidden;
            AssetFilesMatGrid.Visibility = Visibility.Hidden;

            if (File.Exists("MapFile/base_srx.materials.py"))
            {
                File.Delete("MapFile/base_srx.materials.py");
            }

            if (File.Exists("ritobin/base_srx.materials.bin"))
            {
                File.Delete("ritobin/base_srx.materials.bin");
            }


            //Update League Material File
            WebClient client = new WebClient();
            //System.Windows.MessageBox.Show("Downloading the latest Material Version of Summoners Rift!", "Update", MessageBoxButton.OK, MessageBoxImage.Exclamation);
            client.DownloadFile("https://raw.communitydragon.org/latest/game/data/maps/mapgeometry/map11/base_srx.materials.bin", "MapFile/base_srx.materials.bin");
            if (!client.IsBusy)
            {
                File.Copy("MapFile/base_srx.materials.bin", "ritobin/base_srx.materials.bin");
                System.Diagnostics.Process process = new System.Diagnostics.Process();
                System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
                //System.Windows.MessageBox.Show("DONE!", "Update", MessageBoxButton.OK, MessageBoxImage.Exclamation);
                if (File.Exists("MapFile/base_srx.materials.bin"))
                {
                    startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
                    startInfo.FileName = "cmd.exe";
                    startInfo.WorkingDirectory = "ritobin/";
                    startInfo.Arguments = @$"/c ritobin_cli.exe base_srx.materials.bin";

                    process.StartInfo = startInfo;
                    process.Start();
                    process.WaitForExit();
                    
                    
                }
            }
            if (File.Exists("ritobin/base_srx.materials.py"))
            {
                File.Copy("ritobin/base_srx.materials.py", "MapFile/base_srx.materials.py");
                File.Delete("ritobin/base_srx.materials.py");
                File.Delete("ritobin/base_srx.materials.bin");
            }

            

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

        //Dragons TreeView Setup
        public CommonOpenFileDialog dialogmgeo = new CommonOpenFileDialog();
        //public TreeViewItem BaseFile = new TreeViewItem();
        //public TreeViewItem InfernalFile = new TreeViewItem();
        //public TreeViewItem MountainFile = new TreeViewItem();
        //public TreeViewItem OceanFile = new TreeViewItem();
        //public TreeViewItem CloudFile = new TreeViewItem();
        //public TreeViewItem HextechFile = new TreeViewItem();
        //public TreeViewItem ChemtechFile = new TreeViewItem();
        //public TreeViewItem AllLayerFile = new TreeViewItem();
        //public TreeViewItem DecalsFile = new TreeViewItem();

        //public TreeViewItem file1 = new TreeViewItem();
        //public TreeViewItem file2 = new TreeViewItem();
        //public TreeViewItem file3 = new TreeViewItem();
        //public TreeViewItem file4 = new TreeViewItem();
        //public TreeViewItem file5 = new TreeViewItem();
        //public TreeViewItem file6 = new TreeViewItem();
        //public TreeViewItem file7 = new TreeViewItem();
        //public TreeViewItem file8 = new TreeViewItem();
        //public TreeViewItem file1_decal = new TreeViewItem();

        //Material Editor Setup
        public string MatNames = "";
        public int Version = 0;
        public int MaterialsCount = 0;
        public int SunPropsCount = 0;
        public int RitoParticleCount = 0;
        public int RitoLightCount = 0;


        //----------

        MapGeometry cleanedmap = new MapGeometry("MapFile/base_srx.mapgeo");
        MapGeometry fullmap = new MapGeometry("MapFile/base_srx.mapgeo");
        List<string> cleanedbin = new List<string>();
        public int CountAddModels = 0;
        public string MaterialPath = "";

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
            //using CommonOpenFileDialog dialogmgeo = new CommonOpenFileDialog();
            dialogmgeo.Multiselect = true;
            dialogmgeo.Filters.Add(new CommonFileDialogFilter("Blender OBJ Files", "*.obj"));

            



            if (dialogmgeo.ShowDialog() == CommonFileDialogResult.Ok)
            {
                //Load Objects into AssetBox
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

                TreeViewItem HextechFile = new TreeViewItem();
                HextechFile.Header = "Hextech Map";
                AssetBox_Map.Items.Add(HextechFile);

                TreeViewItem ChemtechFile = new TreeViewItem();
                ChemtechFile.Header = "Chemtech Map";
                AssetBox_Map.Items.Add(ChemtechFile);

                TreeViewItem AllLayerFile = new TreeViewItem();
                AllLayerFile.Header = "All Layer";
                AssetBox_Map.Items.Add(AllLayerFile);

                TreeViewItem DecalsFile = new TreeViewItem();
                DecalsFile.Header = "Decals";
                AssetBox_Map.Items.Add(DecalsFile);

                foreach (string FileName in dialogmgeo.FileNames)
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
                    if (FileName.Contains(prefix_hextech.Text))
                    {
                        TreeViewItem file7 = new TreeViewItem();
                        file7.Header = System.IO.Path.GetFileName(FileName);
                        HextechFile.Items.Add(file7);
                        //var rootcloud = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }
                    if (FileName.Contains(prefix_chemtech.Text))
                    {
                        TreeViewItem file8 = new TreeViewItem();
                        file8.Header = System.IO.Path.GetFileName(FileName);
                        ChemtechFile.Items.Add(file8);
                        //var rootcloud = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }
                    if (FileName.Contains(prefix_alllayers.Text))
                    {
                        TreeViewItem file6 = new TreeViewItem();
                        file6.Header = System.IO.Path.GetFileName(FileName);
                        AllLayerFile.Items.Add(file6);
                        //var rootcloud = AssetBox_Map.Items.Add(System.IO.Path.GetFileName(FileName));
                    }
                    if (FileName.Contains(prefix_decals.Text))
                    {
                        TreeViewItem file1_decal = new TreeViewItem();
                        file1_decal.Header = System.IO.Path.GetFileName(FileName);
                        DecalsFile.Items.Add(file1_decal);
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
                count_hextech.Text = HextechFile.Items.Count.ToString();
                count_chemtech.Text = ChemtechFile.Items.Count.ToString();
                count_alllayers.Text = AllLayerFile.Items.Count.ToString();
                count_decals.Text = DecalsFile.Items.Count.ToString();

                var totalfiles = BaseFile.Items.Count + InfernalFile.Items.Count + MountainFile.Items.Count + OceanFile.Items.Count + HextechFile.Items.Count + ChemtechFile.Items.Count + AllLayerFile.Items.Count + DecalsFile.Items.Count;

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
                    var DecalfileCount = Int32.Parse(count_decals.Text);
                    
                    int OBJsToCreate = BasefileCount  + 1;
                    int OBJsToCreateDecal = DecalfileCount + 1;
                    
                    OBJFile[] OBJs = new OBJFile[OBJsToCreate];
                    OBJFile[] OBJsD = new OBJFile[OBJsToCreateDecal];
                    

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

                    for (int k = 1; k < OBJsToCreateDecal; k++)
                    {


                        try
                        {

                            var fullpath = Selected_Path.Text + @"\" + $"room{k}{prefix_decals.Text}.obj";
                            var fullpathmtl = Selected_Path.Text + @"\" + $"room{k}{prefix_decals.Text}.mtl";
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

                            OBJsD[k] = new OBJFile(fullpath);
                            AddModels.AddModels.Add_AllLayersDecal(OBJsD[k], $"MapGeo_Instance_room{k}{prefix_decals.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{k}{prefix_decals.Text}", cleanedmap, k, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                            //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{i}{prefix_base.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);


                        }

                        catch (Exception)
                        {
                            continue;

                            //var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                            //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }

                    } //Decals

                } //All Layers
                if (layers == 1)
                {
                    layern = "Auto Layers";
                    var BasefileCount = Int32.Parse(count_base.Text);
                    var InfernalfileCount = Int32.Parse(count_infernal.Text);
                    var MountainfileCount = Int32.Parse(count_mountain.Text);
                    var OceanfileCount = Int32.Parse(count_ocean.Text);
                    var CloudfileCount = Int32.Parse(count_cloud.Text);
                    var HextechfileCount = Int32.Parse(count_hextech.Text);
                    var ChemtechfileCount = Int32.Parse(count_chemtech.Text);
                    var AllLayerfileCount = Int32.Parse(count_alllayers.Text);
                    var DecalfileCount = Int32.Parse(count_decals.Text);

                    int OBJsToCreate = BasefileCount + 1;
                    int OBJsToCreate2 = InfernalfileCount + 1;
                    int OBJsToCreate3 = MountainfileCount + 1;
                    int OBJsToCreate4 = OceanfileCount + 1;
                    int OBJsToCreate5 = CloudfileCount + 1;
                    int OBJsToCreate7 = HextechfileCount + 1;
                    int OBJsToCreate8 = ChemtechfileCount + 1;
                    int OBJsToCreate6 = AllLayerfileCount + 1;
                    int OBJsToCreate9 = DecalfileCount + 1;

                    OBJFile[] OBJs = new OBJFile[OBJsToCreate];
                    OBJFile[] OBJ2s = new OBJFile[OBJsToCreate2];
                    OBJFile[] OBJ3s = new OBJFile[OBJsToCreate3];
                    OBJFile[] OBJ4s = new OBJFile[OBJsToCreate4];
                    OBJFile[] OBJ5s = new OBJFile[OBJsToCreate5];
                    OBJFile[] OBJ6s = new OBJFile[OBJsToCreate6];
                    OBJFile[] OBJ7s = new OBJFile[OBJsToCreate7];
                    OBJFile[] OBJ8s = new OBJFile[OBJsToCreate8];
                    OBJFile[] OBJ9s = new OBJFile[OBJsToCreate9];

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

                    for (int f = 1; f < OBJsToCreate7; f++) //Hextech
                    {


                        try
                        {
                            var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_hextech.Text}.obj";
                            var fullpathmtl = Selected_Path.Text + @"\" + $"room{f}{prefix_hextech.Text}.mtl";
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

                            OBJ7s[f] = new OBJFile(fullpath);
                            AddModels.AddModels.Add_Layer6(OBJ7s[f], $"MapGeo_Instance_room{f}{prefix_hextech.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_hextech.Text}", cleanedmap, f, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                            //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_cloud.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);


                        }

                        catch (Exception)
                        {
                            continue;
                            //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj";
                            // System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }

                    } //Hextech

                    for (int f = 1; f < OBJsToCreate8; f++) //Chemtech
                    {


                        try
                        {
                            var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_chemtech.Text}.obj";
                            var fullpathmtl = Selected_Path.Text + @"\" + $"room{f}{prefix_chemtech.Text}.mtl";
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

                            OBJ8s[f] = new OBJFile(fullpath);
                            AddModels.AddModels.Add_Layer7(OBJ8s[f], $"MapGeo_Instance_room{f}{prefix_chemtech.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_chemtech.Text}", cleanedmap, f, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                            //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_cloud.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);


                        }

                        catch (Exception)
                        {
                            continue;
                            //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj";
                            // System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }

                    } //Chemtech

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
                            AddModels.AddModels.Add_AllLayers(OBJ6s[f], $"MapGeo_Instance_room{f}{prefix_alllayers.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_alllayers.Text}", cleanedmap, f, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                            //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_cloud.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);


                        }

                        catch (Exception)
                        {
                            continue;
                            //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj";
                            // System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }

                    } //AllLayers

                    for (int k = 1; k < OBJsToCreate9; k++)
                    {


                        try
                        {

                            var fullpath = Selected_Path.Text + @"\" + $"room{k}{prefix_decals.Text}.obj";
                            var fullpathmtl = Selected_Path.Text + @"\" + $"room{k}{prefix_decals.Text}.mtl";
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

                            OBJ9s[k] = new OBJFile(fullpath);
                            AddModels.AddModels.Add_AllLayersDecal(OBJ9s[k], $"MapGeo_Instance_room{k}{prefix_decals.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{k}{prefix_decals.Text}", cleanedmap, k, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                            //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{i}{prefix_base.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);


                        }

                        catch (Exception)
                        {
                            continue;

                            //var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                            //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }

                    } //Decals
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
                
                if (File.Exists("ritobin/exported_file.bin"))
                {
                    File.Delete("ritobin/exported_file.bin");
                }
                if (File.Exists("ritobin/exported_file.py"))
                {
                    File.Delete("ritobin/exported_file.py");
                }

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

                //Search for Material Place
                string matsearch = "entries: map[hash,embed] = {";
                string matsearch2 = "entries: map[hash,embed] = {\n    SetMat";
                //Seach for Particle Place
                string partsearch = "0x9c6cdb3d = MapPlaceableContainer {\n            0x204433a4 = MapParticle {";
                

                //Old SunProps from base_srx
                string sunDir = "sunDirection: vec3 = { -0.25, 0.75, -0.0500000007 }";
                string skyLig = "skyLightColor: vec4 = { 1, 1, 1, 1 }";
                string horizo = "horizonColor: vec4 = { 1, 1, 1, 1 }";
                string ground = "groundColor: vec4 = { 1, 1, 1, 1 }";
                string skysca = "skyLightScale: f32 = 1";
                string ligmap = "lightMapColorScale: f32 = 0.600000024";
                string fogena = "fogEnabled: bool = false";
                string fogsen = "fogStartAndEnd: vec2 = { -10000, -50000 }";


                string sunpropsearch = matorginal.Replace(sunDir, "SetSunProps").Replace(skyLig, "").Replace(horizo, "").Replace(ground, "").Replace(skysca, "").Replace(ligmap, "").Replace(fogena, "").Replace(fogsen, "");
                string particlesearch = sunpropsearch.Replace(partsearch, "0x9c6cdb3d = MapPlaceableContainer {\n            SetParticle");
                string materialssearch = particlesearch.Replace(matsearch, matsearch2);

                //Old Method
                string originalmtl = materialssearch.Replace("SetMat", matexp);
                string originalmtl2 = originalmtl.Replace("SetSunProps", sunprops);
                string originalmtl3 = originalmtl2.Replace("SetParticle", particleplace);
                File.WriteAllText(pathmat, originalmtl3);
                File.Copy(pathmat, $"ritobin/exported_file.py");
                //Old Convertion
                //var binfile = System.Diagnostics.Process.Start("ritobin/txt2ritobin.exe", $"{pathmat} {pathbin}");
                System.Diagnostics.Process process = new System.Diagnostics.Process();
                System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
                startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
                startInfo.FileName = "cmd.exe";
                startInfo.WorkingDirectory = "ritobin/";
                startInfo.Arguments = @$"/c ritobin_cli.exe exported_file.py";

                process.StartInfo = startInfo;
                process.Start();
                process.WaitForExit();
                File.Copy("ritobin/exported_file.bin", pathbin);

                System.Windows.Forms.MessageBox.Show($"Map Name: {Map_Name.Text}\nLightMode: {LightMode.SelectedIndex}\nFog: {FogSet.SelectedIndex}\nLayers: {layern}\nPremultiplied Alpha: {AlphaSet.SelectedIndex}\n\nPath: {pathmapgeo}", "Done!", MessageBoxButtons.OK, MessageBoxIcon.Information);
                //Cleanes the files to avoid merging
                cleanedmap.Models.Clear();
                
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

        

        private void SliderEnd_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        private void LightMode_Copy2_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }

        private void NVRConvertButton_Click(object sender, RoutedEventArgs e)
        {
            ConvertNVR convertNVR = new ConvertNVR();
            convertNVR.Show();
        }

        private void WGEOConvertButton_Click(object sender, RoutedEventArgs e)
        {

        }

        private void MGEOConvertButton_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            SunProp.Visibility = Visibility.Visible;
        }

        private void ExitButton_Click(object sender, RoutedEventArgs e)
        {
            SunProp.Visibility = Visibility.Collapsed;
        }

        private void MATEditorButton_Click(object sender, RoutedEventArgs e)
        {
            MapEditorGrid.Visibility = Visibility.Collapsed;
            AssetFilesGrid.Visibility = Visibility.Collapsed;
            MaterialEditorGrid.Visibility = Visibility.Visible;
            AssetFilesMatGrid.Visibility = Visibility.Visible;
        }

        private void OpenMatButton_Click(object sender, RoutedEventArgs e)
        {
            

        }

        private void OpenMatButton_Click_1(object sender, RoutedEventArgs e)
        {
            using CommonOpenFileDialog dialog = new CommonOpenFileDialog();
            dialog.Multiselect = true;
            dialog.Filters.Add(new CommonFileDialogFilter("Map Material File", "*.materials.bin"));
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            


            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {

                TextRange range;
                FileStream fStream;
                if (File.Exists("ritobin/output.bin") == true)
                {
                    File.Delete("ritobin/output.bin");
                }

                var path = dialog.FileName;
                string filename = null;
                var fixpath = path.Replace("\\", "/");
                var output = "ritobin/output.bin";
                string arguments = $"{fixpath}";
                var ritobinpath = "ritobin/ritobin_cli.exe";
                var command = $"{ritobinpath} {arguments}";
                File.Copy(path, output);

                //Mat Name
                filename = System.IO.Path.GetFileName(path);
                MatNames = filename.Replace(".bin", "");

               


                //Material Editor Setup

                MatNameTB.Text = MatNames;
                VersionTB.Text = Version.ToString();
                
                PartCountTB.Text = RitoParticleCount.ToString();
                LightCountTB.Text = RitoLightCount.ToString();


                startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
                startInfo.FileName = "cmd.exe";
                startInfo.WorkingDirectory = "ritobin/";
                startInfo.Arguments = @$"/c ritobin_cli.exe output.bin";
                
                process.StartInfo = startInfo;
                process.Start();
                process.WaitForExit();

                TextMat.Text = File.ReadAllText("ritobin/output.py");
                //TextMat.Document.Blocks.Add(new Paragraph(new Run("ritobin/output.py")));

                

                //Version

                var GetVersion = File.ReadAllText("ritobin/output.py");

                //Version 1
                if (GetVersion.Contains("version: u32 = 1"))
                {
                    Version = 1;
                    VersionTB.Text = Version.ToString();
                }
                //Version 2
                if (GetVersion.Contains("version: u32 = 2"))
                {
                    Version = 2;
                    VersionTB.Text = Version.ToString();
                }
                //Version 3
                if (GetVersion.Contains("version: u32 = 3"))
                {
                    Version = 3;
                    VersionTB.Text = Version.ToString();
                }

                //Get Material, Light and Particle Counter

                var matinst = 0;
                var matfile = 0;
                var partfile = 0;
                var lightfile = 0;
                using (StreamReader sr = new StreamReader("ritobin/output.py"))
                {

                    while (!sr.EndOfStream)
                    {
                        var counts = sr
                            .ReadLine()
                            .Split(' ')
                            .GroupBy(s => s)
                            .Select(g => new { Word = g.Key, Count = g.Count() });
                        var wc = counts.SingleOrDefault(c => c.Word == "MaterialInstanceDef");
                        var wc2 = counts.SingleOrDefault(c => c.Word == "StaticMaterialDef");
                        var wc3 = counts.SingleOrDefault(c => c.Word == "MapParticle");
                        var wc4 = counts.SingleOrDefault(c => c.Word == "MapPointLight");
                        matinst += (wc == null) ? 0 : wc.Count;
                        matfile += (wc2 == null) ? 0 : wc2.Count;
                        partfile += (wc3 == null) ? 0 : wc3.Count;
                        lightfile += (wc4 == null) ? 0 : wc4.Count;

                    }

                }
                var matcount = matinst + matfile;
                MatCountTB.Text = matcount.ToString();
                PartCountTB.Text = partfile.ToString();
                LightCountTB.Text = lightfile.ToString();
                SaveMatButton.IsEnabled = true;
            }
        }

        private void ExitButton1_Click(object sender, RoutedEventArgs e)
        {
            AssetFilesMatGrid.Visibility = Visibility.Collapsed;
            MaterialEditorGrid.Visibility = Visibility.Collapsed;
            AssetFilesGrid.Visibility = Visibility.Visible;
            MapEditorGrid.Visibility = Visibility.Visible;
            SaveMatButton.IsEnabled = false;
            TextMat.Text = "";
            MatNameTB.Text = "";
            VersionTB.Text = "";
            MatCountTB.Text = "";
            PartCountTB.Text = "";
            LightCountTB.Text = "";

        }

        private void SaveMatButton_Click(object sender, RoutedEventArgs e)
        {
            
            //Updates BIN File Version
            if (TextMat.Text.Contains("version: u32 = 1"))
            {
                TextMat.Text.Replace("version: u32 = 1", "version: u32 = 3");
            }
            if (TextMat.Text.Contains("version: u32 = 2"))
            {
                TextMat.Text.Replace("version: u32 = 2", "version: u32 = 3");
            }

            if (File.Exists("ritobin/output_new.bin"))
            {
                File.Delete("ritobin/output_new.bin");
            }

            if (File.Exists("ritobin/output_new.py"))
            {
                File.Delete("ritobin/output_new.py");
            }

            File.WriteAllText("ritobin/output_new.py", TextMat.Text);


            using CommonSaveFileDialog dialog = new CommonSaveFileDialog();
            dialog.Filters.Add(new CommonFileDialogFilter("Map Material File", "*.materials.bin"));
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();

            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            startInfo.FileName = "cmd.exe";
            startInfo.WorkingDirectory = "ritobin/";
            startInfo.Arguments = @$"/c ritobin_cli.exe output_new.py";

            process.StartInfo = startInfo;
            process.Start();
            process.WaitForExit();


            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {
                var Path = dialog.FileName;
                
                File.Copy("ritobin/output_new.bin", Path);
            }
        }

        private void MAPGEOOpenButton_Click(object sender, RoutedEventArgs e)
        {
            //Opens a Custom Map to added more models to the Map
            using CommonOpenFileDialog dialog = new CommonOpenFileDialog();
            dialog.Multiselect = false;
            dialog.Filters.Add(new CommonFileDialogFilter("Map Geometry File", "*.mapgeo"));



            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {
                var MapPath = dialog.FileName;
                MapNameTextBox.Text = System.IO.Path.GetFileName(MapPath);
                MapGeometry map = new MapGeometry(MapPath);
                fullmap = map;
                LayerNumberTextBox.Text = map.Models.Count.ToString(); //Will be replaced later with Layer Number if we know how to do it.
                MaterialPath = dialog.FileName.Replace(".mapgeo", ".materials.bin");
            }

            
        }

        private void AddModels_Click(object sender, RoutedEventArgs e)
        {
            //Add Custom Models to Opened Mapgeo File
            using CommonOpenFileDialog dialog = new CommonOpenFileDialog();
            dialog.Multiselect = true;
            dialog.Filters.Add(new CommonFileDialogFilter("Blender OBJ File", "*.obj"));
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();

            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {
                CountAddModels = 0;
                var ModelPath = dialog.FileNames;
                int count = ModelPath.Count();
                CountAddModels = count + 1;
                OBJFile[] OBJs = new OBJFile[CountAddModels];
                var DirectoryPath = System.IO.Path.GetDirectoryName(dialog.FileNames.First());
                

                //Convert Material BIN
                var path = MaterialPath;
                string filename = System.IO.Path.GetFileName(path);
                var fixpath = path.Replace("\\", "/");
                var output = $"ritobin/output_solo.bin";
                if (File.Exists(output))
                {
                    File.Delete(output);
                }
                if (File.Exists("material_output/material_solo.py"))
                {
                    File.Delete("material_output/material_solo.py");
                }
                string arguments = $"{fixpath}";
                var ritobinpath = "ritobin/ritobin_cli.exe";
                var command = $"{ritobinpath} {arguments}";
                File.Copy(path, output);

                startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
                startInfo.FileName = "cmd.exe";
                startInfo.WorkingDirectory = "ritobin/";
                startInfo.Arguments = @$"/c ritobin_cli.exe output_solo.bin";

                process.StartInfo = startInfo;
                process.Start();
                process.WaitForExit();


                //Adding now the OBJ Files to MAPGEO Format
                for (int i = 1; i < CountAddModels; i++)
                {


                    try
                    {
                        var fullpath = DirectoryPath + @"\" + $"room{i}{prefix_base.Text}.obj";
                        var fullpathmtl = DirectoryPath + @"\" + $"room{i}{prefix_base.Text}.mtl";
                        var mapname = MapNameTextBox.Text.Replace(".mapgeo", "");

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
                        AddModels.AddModels.Add_SoloAllLayers(OBJs[i], $"MapGeo_Instance_room{i}{prefix_base.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}{prefix_base.Text}", fullmap, i, fullpathmtl, mapname, lightmodes, fogmodes, alphamodes);
                        //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{i}{prefix_base.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);


                    }

                    catch (Exception)
                    {
                        continue;

                        //var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                        //System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }

                } //Base
            }
        }

        private void MAPGEOAddSaveButton_Click(object sender, RoutedEventArgs e)
        {
            using CommonSaveFileDialog dialogsave = new CommonSaveFileDialog();
            dialogsave.Filters.Add(new CommonFileDialogFilter("MAPGEO File", "*.mapgeo"));




            if (dialogsave.ShowDialog() == CommonFileDialogResult.Ok)
            {
                //Export Mapgeo File
                fullmap.Write(dialogsave.FileName, 11);

                //Export Material File
                var matconv = "ritobin/output_solo.py";
                var matset = "material_output/material_solo.py";
                var search = "entries: map[hash,embed] = {";

                var matinput = File.ReadAllText(matset);
                var input = File.ReadAllText(matconv).Replace($"{search}", $"{search}\n {matinput}");
                File.WriteAllText(dialogsave.FileName.Replace(".mapgeo", ".materials.py"), input);


            }
        }

        
    }
}
