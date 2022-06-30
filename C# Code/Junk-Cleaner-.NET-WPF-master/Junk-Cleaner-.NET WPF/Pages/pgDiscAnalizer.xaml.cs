using System;
using System.Collections.Generic;
using System.IO;
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

namespace Junk_Cleaner_.NET_WPF
{
    /// <summary>
    /// Interaction logic for pgDiscAnalizer.xaml
    /// </summary>
    public partial class pgDiscAnalizer : Page
    {
        private List<ElementControler> gbx = new List<ElementControler>(); 
        public pgDiscAnalizer()
        {
            InitializeComponent();
            initializeDrives();
        }
        private void initializeDrives()
        {
            DriveInfo[] drives = DriveInfo.GetDrives();
            List<ErazedElements> lst = new List<ErazedElements>();
            foreach (DriveInfo drive in drives)
            {
                //We only want drives with folders, "Fixed" is hard drives
                if (drive.DriveType == DriveType.Fixed)
                {
                    
                    ErazedElements ele = new ErazedElements(drive.Name,new List<string>(){ drive.Name });
                    lst.Add(ele);
                }
            }
            gbx.Add(new ElementControler(grdWinElements, "Local Drives", lst));
        }
        private void BtnAnalyze_Click(object sender, RoutedEventArgs e)
        {

        }
    }
}
