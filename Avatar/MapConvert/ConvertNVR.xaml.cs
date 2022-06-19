using MaterialDesignExtensions.Controls;
using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using LeagueToolkit.Converters;
using LeagueToolkit.IO.NVR;
using LeagueToolkit.IO.WorldGeometry;
using LeagueToolkit.IO.OBJ;
using Microsoft.WindowsAPICodePack.Dialogs;
using System.Windows.Forms;
using System.IO;
using LeagueToolkit.Helpers.Structures.BucketGrid;
using System.Linq;
using System.Numerics;

namespace Avatar.MapConvert
{
    /// <summary>
    /// Interaktionslogik für ConvertNVR.xaml
    /// </summary>
    public partial class ConvertNVR : MaterialWindow
    {
        public ConvertNVR()
        {
            InitializeComponent();
        }

        public NVRFile nvrpath;
        private object test;

        private void Button_Click(object sender, RoutedEventArgs e)
        {

            AssetBox_Map.Items.Clear();

            TreeViewItem RoomFile = new TreeViewItem();
            RoomFile.Header = "Map Files";
            AssetBox_Map.Items.Add(RoomFile);


            using CommonOpenFileDialog dialog2 = new CommonOpenFileDialog();
            dialog2.Multiselect = false;
            dialog2.Filters.Add(new CommonFileDialogFilter("NVR File", "*.nvr"));

            if (dialog2.ShowDialog() == CommonFileDialogResult.Ok)
            {
                var fullpath = dialog2.FileName;
                var namefile = System.IO.Path.GetFileNameWithoutExtension(fullpath);
                var nvr = new NVRFile(fullpath);
                nvrpath = nvr;
                var getmat = nvr.Meshes;
                List<NVRMesh> mesh = nvr.Meshes;
                //------------------------//
                
                
                RoomFile.ItemsSource = mesh;
                
                
                
            }
        }

        private void Save_Click(object sender, RoutedEventArgs e)
        {
            using FolderBrowserDialog dialog3 = new FolderBrowserDialog();
            if (File.Exists("MapConvert/roomnvr.wgeo"))
            {
                File.Delete("MapConvert/roomnvr.wgeo");
            }
            

            if (dialog3.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                var savepath = dialog3.SelectedPath;
                WGEOConverter.ConvertNVR(nvrpath, new WorldGeometry("MapConvert/room.wgeo").BucketGrid).Write("MapConvert/roomnvr.wgeo");
                
                WorldGeometry wgeo = new WorldGeometry("MapConvert/roomnvr.wgeo");
            

            for (int i = 0; i < 128; i++)
            {
                for (int j = 0; j < 128; j++)
                {
                    BucketGridBucket bucket = wgeo.BucketGrid.Buckets[i, j];

                    List<uint> indices = wgeo.BucketGrid.Indices
                        .GetRange((int)bucket.StartIndex, (bucket.InsideFaceCount + bucket.StickingOutFaceCount) * 3)
                        .Select(x => (uint)x)
                        .ToList();

                    if (indices.Count != 0)
                    {
                        int startVertex = (int)indices.Min();
                        int vertexCount = (int)indices.Max() - startVertex;
                        List<Vector3> vertices = wgeo.BucketGrid.Vertices.GetRange(startVertex + (int)bucket.BaseVertex, vertexCount);

                        new OBJFile(vertices, indices).Write(string.Format(savepath + "//room{0}_{1}.obj", i, j));
                            
                    }
                }
            }
                wgeo.Write(savepath + "//roomwgeo.wgeo");
            }
        }
    }
}
