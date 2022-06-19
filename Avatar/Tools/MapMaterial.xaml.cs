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
using LeagueToolkit.IO.PropertyBin;
using System.Drawing;
using LeagueToolkit.Meta;
using LeagueToolkit.Meta.Classes;
using LeagueToolkit.IO.MapGeometry;

namespace Avatar.Tools
{
    /// <summary>
    /// Interaction logic for MapParticleDat.xaml
    /// </summary>
    public partial class MapMaterial : MaterialWindow
    {
        public MapMaterial()
        {
            InitializeComponent();
        }
       
        //LightDatLight datLight = new LightDatLight();

        

        private void LightLoad_Click(object sender, RoutedEventArgs e)
        {
            using CommonOpenFileDialog dialog2 = new CommonOpenFileDialog();
            dialog2.Multiselect = false;
            dialog2.Filters.Add(new CommonFileDialogFilter("Mapgeo", "*.mapgeo"));

            if (dialog2.ShowDialog() == CommonFileDialogResult.Ok)
            {
                var fullpath = dialog2.FileName;
                var namefile = System.IO.Path.GetFileNameWithoutExtension(fullpath);
                if (Root.Items.Count > 0)
                {
                    Root.Items.Clear();
                }

                MapGeometry map = new MapGeometry(fullpath);
                map.Write(fullpath.Replace(".mapgeo", "_updated.mapgeo"), 11);
                
            }
        }
    }
}
