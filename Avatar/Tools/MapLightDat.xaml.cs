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
using LeagueToolkit.IO.LightDat;
using System.Drawing.Imaging;
using SharpGLTF.Memory;
using LeagueToolkit.Helpers.Structures;
using System.Drawing;

namespace Avatar.Tools
{
    /// <summary>
    /// Interaction logic for MapParticleDat.xaml
    /// </summary>
    public partial class MapLightDat : MaterialWindow
    {
        public MapLightDat()
        {
            InitializeComponent();
        }
       
        //LightDatLight datLight = new LightDatLight();

        

        private void LightLoad_Click(object sender, RoutedEventArgs e)
        {
            using CommonOpenFileDialog dialog2 = new CommonOpenFileDialog();
            dialog2.Multiselect = false;
            dialog2.Filters.Add(new CommonFileDialogFilter("Map Light File", "*.dat"));

            if (dialog2.ShowDialog() == CommonFileDialogResult.Ok)
            {
                var fullpath = dialog2.FileName;
                var namefile = System.IO.Path.GetFileNameWithoutExtension(fullpath);
                if (Root.Items.Count > 0)
                {
                    Root.Items.Clear();
                }
                List<string> wrongfiles = new List<string>();
                wrongfiles.Add("_env");
                wrongfiles.Add("_Env");
                wrongfiles.Add("Particles");
                wrongfiles.Add("particles");
                int i = 0;

                if (!namefile.Contains(wrongfiles[i++]))
                {

                    try
                {
                    //Creates a new List for Light Names
                    List<string> Names = new List<string>();
                    List<string> Positions = new List<string>();
                    List<string> Color = new List<string>();
                    List<string> Radius = new List<string>();


                    using (StreamReader r = new StreamReader(fullpath))
                    {
                        string line;
                        
                        //Names
                        while ((line = r.ReadLine()) != null)
                        {
                            //Filter out Particle Names
                            string Namelines = "MapLight";
                            //Filter out Particle Positions
                            string XPoslines = line.Split(' ')[0];
                            string YPoslines = line.Split(' ')[1];
                            string ZPoslines = line.Split(' ')[2];
                            string XYZPoslines = $"X={XPoslines} | Y={YPoslines} | Z={ZPoslines}";
                            //Filter out Particle Radius
                            string Radiuslines = line.Split(' ')[6];
                            //Filter out Particle Color
                            string XCollines = line.Split(' ')[3];
                            string YCollines = line.Split(' ')[4];
                            string ZCollines = line.Split(' ')[5];
                            string XYZCollines = $"R={XCollines} | G={YCollines} | B={ZCollines}";

                            Names.Add(Namelines);
                            Positions.Add(XYZPoslines);
                            Color.Add(XYZCollines);
                            Radius.Add(Radiuslines);
                            

                        }

                    }



                    for (int n = 0; n <int.MaxValue ; n++)
                    {
                        string PName = Names[n];
                        string PPos = Positions[n];
                        string PColor = Color[n];
                        string PRad = Radius[n];


                        //Parent
                        Root.Header = namefile + ".dat";
                        
                        //Particle File Root
                        TreeViewItem Child2Item = new TreeViewItem();
                        Child2Item.Header = PName + "_" + n;
                        Root.Items.Add(Child2Item);

                        //Particle Positions
                        TreeViewItem SubChild2Item = new TreeViewItem();
                        SubChild2Item.Header = $"Position: {PPos}";
                        Child2Item.Items.Add(SubChild2Item);

                        //Particle Color
                        TreeViewItem SubChild3Item = new TreeViewItem();
                        SubChild3Item.Header = $"Color: {PColor}";
                        Child2Item.Items.Add(SubChild3Item);
                        
                        //Particle Radius
                        TreeViewItem SubChild4Item = new TreeViewItem();
                        SubChild4Item.Header = $"Radius: {PRad}";
                        Child2Item.Items.Add(SubChild4Item);
                        
                    }

                    
                        
                        
                        





                }
                catch (Exception)
                {

                }

                }
                else
                {
                    System.Windows.MessageBox.Show("Your file is not a valid Light.dat file!", "Error!", MessageBoxButton.OK, MessageBoxImage.Information);
                }


            }
        }
    }
}
