using MaterialDesignExtensions.Controls;
using System;
using System.Collections.Generic;
using System.Reflection;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using LeagueToolkit.IO.MapParticles;
using Microsoft.WindowsAPICodePack.Dialogs;
using System.IO;
using System.Linq;
using Avatar.Plugs;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using System.Numerics;
using System.Globalization;
using System.Windows.Forms;
using Octokit;

namespace Avatar.Tools
{
    /// <summary>
    /// Interaction logic for MapParticleDat.xaml
    /// </summary>
    public partial class MapParticleDat : MaterialWindow
    {
        public MapParticleDat()
        {
            InitializeComponent();
        }

        string P_name = new string("");
        Vector3 P_position = new Vector3();
        int P_quality = new int();
        Vector3 P_rotation = new Vector3();
        string P_eyecandy = new string("");
        
        

        private void ParticleLoad_Click(object sender, RoutedEventArgs e)
        {
            using CommonOpenFileDialog dialog2 = new CommonOpenFileDialog();
            dialog2.Multiselect = false;
            dialog2.Filters.Add(new CommonFileDialogFilter("Map Particle File", "*.dat"));

            if (dialog2.ShowDialog() == CommonFileDialogResult.Ok)
            {
                var fullpath = dialog2.FileName;
                var namefile = System.IO.Path.GetFileNameWithoutExtension(fullpath);
                if (Root.Items.Count > 0)
                {
                    Root.Items.Clear();
                }
                if (File.Exists("Tools/Templates/particleoutput.py"))
                {
                    File.Delete("Tools/Templates/particleoutput.py");
                }

                try
                {
                    //Creates a new List for Particle Names
                    List<string> Names = new List<string>();
                    List<string> Names2 = new List<string>();
                    List<string> Positions = new List<string>();
                    List<string> Qualitys = new List<string>();
                    List<string> Rotations = new List<string>();
                    List<string> Tags = new List<string>();
                    List<string> jsons = new List<string>();

                    using (StreamReader r = new StreamReader(fullpath))
                    {
                        string line;
                        
                        //Names
                        while ((line = r.ReadLine()) != null)
                        {
                            //Filter out Particle Names
                            string Namelines = line.Split(' ')[0];
                            string Namelines2 = line.Split(' ')[0].Replace(".troy", "");
                            //Filter out Particle Positions
                            string XPoslines = line.Split(' ')[1];
                            string YPoslines = line.Split(' ')[2];
                            string ZPoslines = line.Split(' ')[3];
                            string XYZPoslines = $"{XPoslines}, {YPoslines}, {ZPoslines}";
                            //Filter out Particle Qualitys
                            string Qualitylines = line.Split(' ')[4];
                            //Filter out Particle Rotations
                            string XRotlines = line.Split(' ')[5];
                            string YRotlines = line.Split(' ')[6];
                            string ZRotlines = line.Split(' ')[7];
                            string XYZRotlines = $"{XRotlines}, {YRotlines}, {ZRotlines}";
                            //Filter out Particle Tags

                            string TagMissing = "";
                            if (line.Contains("EyeCandy"))
                            {
                                TagMissing = "EyeCandy";
                            }


                            Names.Add(Namelines);
                            Names2.Add(Namelines2); //Without .troy / For full name
                            Positions.Add(XYZPoslines);
                            Qualitys.Add(Qualitylines);
                            Rotations.Add(XYZRotlines);
                            Tags.Add(TagMissing);

                        }

                    }



                    for (int n = 0; n <int.MaxValue ; n++)
                    {
                        string PName = Names[n];
                        string PPos = Positions[n];
                        string PQuality = Qualitys[n];
                        string PRot = Rotations[n];
                        string PTag = Tags[n];


                        //Parent
                        Root.Header = namefile + ".dat";
                        
                        //Particle File Root
                        TreeViewItem Child2Item = new TreeViewItem();
                        Child2Item.Header = PName;
                        Root.Items.Add(Child2Item);

                        //Particle Name
                        TreeViewItem SubChild1Item = new TreeViewItem();
                        SubChild1Item.Header = $"Name: {PName.Replace(".troy", "")}";
                        Child2Item.Items.Add(SubChild1Item);

                        //Particle Positions
                        TreeViewItem SubChild2Item = new TreeViewItem();
                        SubChild2Item.Header = $"Position: {PPos}";
                        Child2Item.Items.Add(SubChild2Item);

                        //Particle Quality
                        TreeViewItem SubChild3Item = new TreeViewItem();
                        SubChild3Item.Header = $"Quality: {PQuality}";
                        Child2Item.Items.Add(SubChild3Item);
                        
                        //Particle Rotations
                        TreeViewItem SubChild4Item = new TreeViewItem();
                        SubChild4Item.Header = $"Rotation: {PRot}";
                        Child2Item.Items.Add(SubChild4Item);
                        
                        //Particle Tags
                        TreeViewItem SubChild5Item = new TreeViewItem();
                        SubChild5Item.Header = $"Tags: {PTag}";
                        Child2Item.Items.Add(SubChild5Item);

                        //Convert to JSON format
                        string pathtemp = "Tools/Templates/placeparticle.py";
                        
                        jsons = File.ReadAllLines(pathtemp).ToList();
                        string ParticleName = PName.Replace(".troy", "");

                        string TagsTrue = "false";

                        if (PTag.Contains("EyeCandy"))
                        {
                            TagsTrue = "true";
                        }

                        //Replace all settings in list
                        var newList = jsons.Select(s => s.Replace("ParticleNameHere", ParticleName)).ToList();
                        var newList2 = newList.Select(s => s.Replace("PosXYZ", PPos)).ToList();
                        var newList3 = newList2.Select(s => s.Replace("MapParticleName", $"{ParticleName}_{n}")).ToList();
                        var newList4 = newList3.Select(s => s.Replace("Eyecandytrue", TagsTrue)).ToList();
                        
                        
                        //Write output
                        File.AppendAllLines("Tools/Templates/particleoutput.py", newList4);

                        

                    }

                    
                        

                }
                catch (Exception)
                {

                }

                //Load json format to textbox
                    
                ShowJSON.Text = File.ReadAllText("Tools/Templates/particleoutput.py");
            }
            ParticleSave.IsEnabled = true;
        }

        private void ParticleSave_Click(object sender, RoutedEventArgs e)
        {
            //Save to Project
            if (ShowJSON.Text != null)
            {
                File.WriteAllText("material_output/particles.py", ShowJSON.Text);
                System.Windows.Forms.MessageBox.Show($"Map Particles will be added to your Map! \nMake sure your linked particle exist in materials.bin or as .troy in the path!" , "Done!", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

        }
    }
}
