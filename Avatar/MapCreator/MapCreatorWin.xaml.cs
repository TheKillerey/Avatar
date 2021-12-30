using MaterialDesignExtensions.Controls;
using MaterialDesignThemes.Wpf;
using Microsoft.WindowsAPICodePack.Dialogs;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace Avatar.MapCreator
{
    /// <summary>
    /// Interaktionslogik für MapCreatorWin.xaml
    /// </summary>
    public partial class MapCreatorWin : MaterialWindow
    {
        public string lolpath = "";
        public MapCreatorWin()
        {
            InitializeComponent();
            string settings = File.ReadAllText("MapCreator/settings.cfg");
            if (File.Exists("MapCreator/temp/settings.cfg"))
            {
                OpenPath.IsEnabled = false;
            }
            else
            {
                Directory.CreateDirectory("MapCreator/temp");
                File.WriteAllText("MapCreator/temp/settings.cfg", settings);
            }
            
            string temp = File.ReadAllText("MapCreator/temp/settings.cfg");
            
            if (temp.Contains("NoPath"))
            {
                OpenPath.ShowDialog(true);
            }
            
            else
            {
                OpenPath.ShowDialog(false);
            }
            
        }


        private void ChoosePath(object sender, RoutedEventArgs e)
        {
            using CommonOpenFileDialog dialog = new CommonOpenFileDialog();
            dialog.Multiselect = false;
            dialog.Filters.Add(new CommonFileDialogFilter("League of Legends.exe", "*.exe"));


            if (dialog.ShowDialog() == CommonFileDialogResult.Ok)
            {
                string fullpath = dialog.FileName.Replace("League of Legends.exe", "");
                string tempsettings = File.ReadAllText("MapCreator/temp/settings.cfg");
                var update = tempsettings.Replace("NoPath", fullpath);
                File.WriteAllText("MapCreator/temp/settings.cfg", update);
            }
        }
    }
}
