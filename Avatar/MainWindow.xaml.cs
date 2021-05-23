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
            
        }

        MapGeometry cleanedmap = new MapGeometry("MapFile/base_srx.mapgeo");

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
                   

                    //Get Path for visualization
                    var folderpath = System.IO.Path.GetDirectoryName(FileName);
                    Selected_Path.Text = folderpath;

                    
                }
                count_base.Text = BaseFile.Items.Count.ToString();
                count_infernal.Text = InfernalFile.Items.Count.ToString();
                count_mountain.Text = MountainFile.Items.Count.ToString();
                count_ocean.Text = OceanFile.Items.Count.ToString();
                count_cloud.Text = CloudFile.Items.Count.ToString();

                var totalfiles = BaseFile.Items.Count + InfernalFile.Items.Count + MountainFile.Items.Count + OceanFile.Items.Count + CloudFile.Items.Count;

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
        private void OnMapgeoFileSave_Click(object sender, RoutedEventArgs e)
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
                        
                        OBJs[i] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_AllLayers(OBJs[i], $"MapGeo_Instance_room{i}{prefix_base.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}{prefix_base.Text}", cleanedmap);
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
                    
                    int OBJsToCreate = BasefileCount + 1;
                    int OBJsToCreate2 = InfernalfileCount + 1;
                    int OBJsToCreate3 = MountainfileCount + 1;
                    int OBJsToCreate4 = OceanfileCount + 1;
                    int OBJsToCreate5 = CloudfileCount + 1;
                    OBJFile[] OBJs = new OBJFile[OBJsToCreate];
                    OBJFile[] OBJ2s = new OBJFile[OBJsToCreate2];
                    OBJFile[] OBJ3s = new OBJFile[OBJsToCreate3];
                    OBJFile[] OBJ4s = new OBJFile[OBJsToCreate4];
                    OBJFile[] OBJ5s = new OBJFile[OBJsToCreate5];
                    
                    for (int i = 1; i < OBJsToCreate; i++)
                {
                    

                    try
                    {
                        var fullpath = Selected_Path.Text + @"\" + $"room{i}{prefix_base.Text}.obj";
                        
                        OBJs[i] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer1(OBJs[i], $"MapGeo_Instance_room{i}{prefix_base.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}{prefix_base.Text}", cleanedmap);
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
                        
                        OBJ2s[f] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer2(OBJ2s[f], $"MapGeo_Instance_room{f}{prefix_infernal.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_infernal.Text}", cleanedmap);
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
                        
                        OBJ3s[f] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer3(OBJ3s[f], $"MapGeo_Instance_room{f}{prefix_mountain.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_mountain.Text}", cleanedmap);
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
                        
                        OBJ4s[f] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer4(OBJ4s[f], $"MapGeo_Instance_room{f}{prefix_ocean.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_ocean.Text}", cleanedmap);
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
                        
                        OBJ5s[f] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer5(OBJ5s[f], $"MapGeo_Instance_room{f}{prefix_cloud.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{f}{prefix_cloud.Text}", cleanedmap);
                        //System.Windows.Forms.MessageBox.Show($"MapGeo_Instance_room{f}{prefix_cloud.Text}", "Debug:", MessageBoxButtons.OK, MessageBoxIcon.Information);
                       

                    }

                    catch (Exception)
                    {
                        continue;
                        //var fullpath = Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj";
                       // System.Windows.Forms.MessageBox.Show(Selected_Path.Text + @"\" + $"room{f}{prefix_cloud.Text}.obj" + " is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }

                } //Cloud
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
                        
                        OBJs[i] = new OBJFile(fullpath);
                        AddModels.AddModels.Add_Layer1(OBJs[i], $"MapGeo_Instance_room{i}{prefix_base.Text}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}{prefix_base.Text}", cleanedmap);
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
                
                //Write the mapgeo file and get some infos about it.
                string namemapgeo = dialogsave.FileName;
                string pathmapgeo = System.IO.Path.GetFullPath(namemapgeo);
                cleanedmap.Write(pathmapgeo, 11);

                System.Windows.Forms.MessageBox.Show($"Map Name: bilgewater\nLightMode: Baked Light\nFog: Enabled\nLayers: {layern}\n\nPath: {pathmapgeo}", "Done!", MessageBoxButtons.OK, MessageBoxIcon.Information);


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
    }
}
