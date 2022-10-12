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
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Windows.Forms;
using Binding = System.Windows.Data.Binding;
using Path = System.IO.Path;
using CheckBox = System.Windows.Controls.CheckBox;

namespace Junk_Cleaner_.NET_WPF
{
    /// <summary>
    /// Interaction logic for pgJunkCleaner.xaml
    /// </summary>
    public partial class pgJunkCleaner : Page
    {
        private List<string> lstPaths = new List<string>();
        private List<ElementControler> lstElements;
        private PathController fileController;
        public pgJunkCleaner()
        {
            InitializeComponent();
            string strAppDataPath = Directory.GetParent(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData)).FullName;
            string strProgramFilesPath = Environment.GetFolderPath(Environment.SpecialFolder.ProgramFilesX86);

            lstElements = new List<ElementControler>()
            {
                new ElementControler(grdWinElements,"Internet Explorer",new List<ErazedElements>()
                {
                    new ErazedElements("Cache", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Local\Microsoft\Intern~1")
                    }),
                    new ErazedElements("History", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Local\Microsoft\Windows\History")
                    }),
                    new ErazedElements("Cookies",new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Roaming\Microsoft\Windows\Cookies")
                    }),
                    new ErazedElements("Temp Files", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Local\Microsoft\Windows\Tempor~1"),
                        Path.Combine(strAppDataPath, @"Local\Microsoft\Windows\INetCache")
                    })
                }),
                new ElementControler(grdWinElements,"Windows Explorer",new List<ErazedElements>()
                {
                    new ErazedElements("Recent Documents", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Roaming\Microsoft\Windows\Recent")
                    }),
                    new ErazedElements("Thumbnail Cache", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Local\Microsoft\Windows\Explorer")
                    }),
                }),
                new ElementControler(grdWinElements,"System",
                new List<ErazedElements>()
                {
                    new ErazedElements("Recycle Bin", new List<string>()
                    {
                        @"C:\$Recycle.bin",
                        //Path.Combine(strAppDataPath, @"Local\Temp")
                    }),
                    new ErazedElements("Temporary Files", new List<string>()
                    {
                        @"C:\Windows\Temp",
                        Path.Combine(strAppDataPath, @"Local\Temp")
                    }),
                    new ErazedElements("Old Prefetch data", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"C:\Windows\Prefetch")
                    })
                }),
                new ElementControler(grdAppElements,"Google Chrome",
                new List<ErazedElements>()
                {
                    new ErazedElements("Profiles",new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Local\Google\Chrome\User Data")
                    })
                }),
                new ElementControler(grdAppElements,"Mozilla Firefox",
                new List<ErazedElements>()
                {
                    new ErazedElements("Profiles", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Local\Mozilla\Firefox\Profiles"),
                        Path.Combine(strAppDataPath, @"Roaming\Mozilla\Firefox\Profiles")
                    })
                }),
                new ElementControler(grdAppElements,"Opera",
                new List<ErazedElements>()
                {
                    new ErazedElements("Profiles", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Local\Opera\Opera"),
                        Path.Combine(strAppDataPath, @"Roaming\Opera\Opera")
                    })
                }),
                new ElementControler(grdAppElements,"Multimedia",
                new List<ErazedElements>()
                {
                    new ErazedElements("Flash Player", new List<string>()
                    {
                        Path.Combine(strAppDataPath, @"Roaming\Macromedia\Flashp~1")
                    }),
                    new ErazedElements("Steam", new List<string>()
                    {
                        Path.Combine(strProgramFilesPath, @"Steam\dumps"),
                        Path.Combine(strProgramFilesPath, @"Steam\logs")
                    })
                }),

            };
        }


        public void changeSkinMode()
        {
            try
            {
                gbxAnalysisInfo.Foreground = Globals.LabelColor;
                expJunkFiles.Foreground = Globals.LabelColor;
                tbApplications.Foreground = Globals.LabelColor;
                tbWindows.Foreground = Globals.LabelColor;
                foreach (ElementControler ec in lstElements)
                    foreach(ErazedElements element in ec.lstChilds)
                        element.changeSkinMode();
                if (!(fileController is null)) fileController.changeSkinMode();
            }
            catch (Exception){throw;}
        }

        private void BtnAnalyze_Click(object sender, RoutedEventArgs e)
        {
            //using (var dialog = new FolderBrowserDialog())
            //{
            //    DialogResult result = dialog.ShowDialog();
            //    if (result == DialogResult.OK)
            //    {
            //    }
            //}
            fileController = new PathController(lstElements, pgbFilesStatus, grdFileInfo, txtTotalStatus, txtProcessStatus);
        }

        private void CheckBox_Checked(object sender, RoutedEventArgs e)
        {

        }
    }
}
