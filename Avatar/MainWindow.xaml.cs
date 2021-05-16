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

        private void OnOBJFileOpen_Click(object sender, RoutedEventArgs e)
        {
            using CommonOpenFileDialog dialog = new CommonOpenFileDialog();
            dialog.Multiselect = true;
            dialog.Filters.Add(new CommonFileDialogFilter("OBJ Files", "*.obj"));

            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {
                AssetBox_Map.Items.Clear();

                foreach (string FileName in dialog.FileNames)
                {
                    AssetBox_Map.Items.Add(System.IO.Path.GetFileNameWithoutExtension(FileName));
                }

                if (AssetBox_Map.Items.Count == 1)
                {


                    System.Windows.MessageBox.Show(AssetBox_Map.Items.Count.ToString() + " file is loaded!", "Done!", MessageBoxButton.OK, MessageBoxImage.Information);
                }

                if (AssetBox_Map.Items.Count > 1)
                {
                    System.Windows.MessageBox.Show(AssetBox_Map.Items.Count.ToString() + " files are loaded!", "Done!", MessageBoxButton.OK, MessageBoxImage.Information);
                }
            }
        }

        private void OnMapgeoFileSave_Click(object sender, RoutedEventArgs e)
        {


        }

        private void DATParticleButton_Click(object sender, RoutedEventArgs e)
        {
            
            MapParticleDat mapParticleDat = new MapParticleDat();
            mapParticleDat.Show();
        }

        private void DATLightButton_Click(object sender, RoutedEventArgs e)
        {
            MapLightDat mapLightDat = new MapLightDat();
            mapLightDat.Show();
        }
    }
}
