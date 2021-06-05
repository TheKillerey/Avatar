using System;
using System.Collections.Generic;
using System.Reflection;
using System.Text;
using System.Threading;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace Avatar.Tools
{
    /// <summary>
    /// Interaktionslogik für Splashscreen.xaml
    /// </summary>
    public partial class Splashwindow : Window
    {
        
        public Splashwindow()
        {
            InitializeComponent();

            DispatcherTimer disTimer = new DispatcherTimer();
            disTimer.Tick += new EventHandler(timer1_Tick);
            disTimer.Interval = new TimeSpan(0, 0, 0, 0 ,20); 
            disTimer.Start();

            System.Reflection.Assembly assembly = System.Reflection.Assembly.GetExecutingAssembly();
            Version version = assembly.GetName().Version;
            versiontext.Content = version;
        }

        MainWindow mainwin = new MainWindow();

        

        private void timer1_Tick(object sender, EventArgs e)
        {
            
            Loadingbar.Value++;

            if (Loadingbar.Value == 100)
            {

                mainwin.Show();
                Close();
            }

            else
            {
                return;
            }
        }
    }
}
