using Junk_Cleaner_.NET_WPF;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;

namespace Junk_Cleaner_.NET_WPF
{
    public class PathController
    {
        private delegate void displayProgress();
        private Grid parentGrid;
        private bool isEnded;
        public long totalFiles;
        public long totalFolders;
        public long totalSize;
        public long totlaTime;
        private TextBlock txtTotalStatus;
        private TextBlock txtProcessStatus;
        private ProgressBar progressBar;
        private Thread trdUpdateUI;
        private List<PathElementUI> lstChilds;
        private List<ElementControler> lstElements;

        /// <summary>
        /// Main Constructor
        /// </summary>
        /// <param name="path">Search for files inside this path</param>
        /// <param name="files">List of files to be manipulated</param>
        /// <param name="progressBar">The ProgressBar to be updated</param>
        /// <param name="grdDisplay">The DataGrid to be updated</param>
        public PathController(List<ElementControler> lstElements,ProgressBar progressBar, Grid grdDisplay, TextBlock txtTotalStatus, TextBlock txtProcessStatus)
        {
            isEnded = false;
            totalFiles = 0;
            totalFolders = 0;
            totalSize = 0;
            totlaTime = 0;
            parentGrid = grdDisplay;
            lstChilds = new List<PathElementUI>();
            this.txtTotalStatus = txtTotalStatus;
            this.txtProcessStatus = txtProcessStatus;
            this.progressBar = progressBar;
            this.lstElements = lstElements;
            grdDisplay.Children.Clear();
            SearchForFiles();
        }

        public void changeSkinMode()
        {
            try
            {
                txtTotalStatus.Dispatcher.Invoke(new displayProgress(updateTolaStatus));
                foreach (PathElementUI child in lstChilds) child.changeSkinMode();
            }
            catch (Exception){throw;}
        }

        public void SearchForFiles()
        {
            try
            {
                parentGrid.Children.Clear();
                foreach (ElementControler ec in lstElements)
                {
                    GroupBox grb = GroupBoxInit(ec.strName);
                    foreach (ErazedElements element in ec.lstChilds)
                        if (element.IsActive)
                        {
                            
                            foreach (string path in element.lstPaths)
                                if (new DirectoryInfo(path).Exists)
                                    lstChilds.Add(new PathElementUI(path, progressBar, grb, element));

                        }
                }
                trdUpdateUI = new Thread(new ThreadStart(UpdateUIRunner));
                trdUpdateUI.IsBackground = true;
                trdUpdateUI.Start();
            }
            catch (Exception)
            {
                throw;
            }
        }

        private GroupBox GroupBoxInit(string name)
        {
            try
            {
                parentGrid.RowDefinitions.Add(new RowDefinition { Height = new GridLength(100, GridUnitType.Auto) });
                GroupBox gbxElement = new GroupBox()
                {
                    Foreground = Brushes.RosyBrown,
                    Background = new SolidColorBrush { Color = Color.FromRgb(70, 130, 180), Opacity = 0.1 },
                    FontFamily = new FontFamily("Consolas"),
                    FontSize = 12,
                    Header = name,
                    Margin = new Thickness(5,0,5,5),
                    BorderThickness = new Thickness(0.25),
                    //BorderBrush = Brushes.White,
                    HorizontalAlignment = HorizontalAlignment.Stretch
                };
                Grid grid = new Grid();
                gbxElement.Content = grid;
                gbxElement.SetValue(Grid.RowProperty, parentGrid.RowDefinitions.Count - 1);
                gbxElement.MouseEnter += brdMouseEnter;
                gbxElement.MouseLeave += brdMouseLeave;
                parentGrid.Children.Add(gbxElement);
                return gbxElement;
            }
            catch (Exception)
            {

                throw;
            }
        }

        private void brdMouseEnter(object sender, MouseEventArgs e)
        {
            //((GroupBox)sender).BorderBrush = Brushes.SteelBlue;
            //((GroupBox)sender).BorderThickness = new Thickness(2);
            //((GroupBox)sender).Margin = new Thickness(0);
        }

        private void brdMouseLeave(object sender, MouseEventArgs e)
        {
            //((GroupBox)sender).BorderBrush = Brushes.White;
        }

        private void UpdateUIRunner()
        {
            try
            {
                System.Diagnostics.Stopwatch watch = System.Diagnostics.Stopwatch.StartNew();
                int intEndedCount = 0;
                while (!isEnded)
                {
                    intEndedCount = lstChilds.Where(child => child.blnIsEnded == true).Count();
                    isEnded = (intEndedCount == lstChilds.Count);
                    txtTotalStatus.Dispatcher.Invoke(new displayProgress(updateTolaStatus));
                    parentGrid.Dispatcher.Invoke(new displayProgress(HideGroupBoxes));
                    Thread.Sleep(30);
                }
                watch.Stop();
                totlaTime = watch.ElapsedMilliseconds;
                txtTotalStatus.Dispatcher.Invoke(new displayProgress(updateTolaStatus));
            }
            catch (Exception)
            {

                throw;
            }
        }

        private void HideGroupBoxes()
        {
            try
            {
                foreach(UIElement child in parentGrid.Children)
                {
                    GroupBox groupBox = child as GroupBox;
                    Grid grid = groupBox.Content as Grid;
                    groupBox.Visibility = Visibility.Collapsed;
                    foreach (UIElement grdChild in grid.Children)
                    {
                        Border brd = grdChild as Border;
                        if (brd.Visibility == Visibility.Visible)
                            groupBox.Visibility = Visibility.Visible;
                    }
                }
            }
            catch (Exception) { throw;}
        }

        private void updateTolaStatus()
        {
            try
            {
                totalSize = 0;
                totalFolders = 0;
                totalFiles = 0;
                foreach (PathElementUI child in lstChilds)
                {
                    totalSize += child.totalSize;
                    totalFiles += child.totalFiles;
                    totalFolders += child.totalFolders;
                }
                string strOutput = string.Empty;
                string strTotalSize = "(" + String.Format("{0:#,0}", totalSize) + " bytes)";
                double time = totlaTime / 1000;
                string strTotalTime = String.Format("{0:0.000}", time) + " secs";
                txtTotalStatus.Inlines.Clear();
                if (isEnded)
                {
                    txtTotalStatus.Inlines.Add(Globals.coloredRun("Analysis Complete 🗸 ", Brushes.LimeGreen));
                    txtTotalStatus.Inlines.Add(Globals.coloredRun("( ", Globals.LabelColor));
                    txtTotalStatus.Inlines.Add(Globals.coloredRun(strTotalTime, Globals.ValueColor));
                    txtTotalStatus.Inlines.Add(Globals.coloredRun(" )", Globals.LabelColor));
                    txtTotalStatus.Inlines.Add(new Run(Environment.NewLine));
                }

                txtTotalStatus.Inlines.Add(Globals.coloredRun("[ ", Globals.LabelColor));
                txtTotalStatus.Inlines.Add(Globals.coloredRun(Globals.sizeFix(totalSize, 2), Brushes.Tomato, strTotalSize));
                txtTotalStatus.Inlines.Add(Globals.coloredRun(" ]  ", Globals.LabelColor));
                txtTotalStatus.Inlines.Add(Globals.coloredRun(String.Format("{0:#}", totalFiles), Globals.ValueColor));
                txtTotalStatus.Inlines.Add(Globals.coloredRun(" Files ", Globals.LabelColor)); 
                txtTotalStatus.Inlines.Add(Globals.coloredRun(String.Format("{0:#}",totalFolders), Globals.ValueColor));
                txtTotalStatus.Inlines.Add(Globals.coloredRun(" Folders", Globals.LabelColor));

            }
            catch (Exception) { throw; }
        }
    }

    public class PathElementUI
    {
        private delegate void displayProgress();
        private delegate void displayFiles();
        private delegate void displayDir();
        private TextBlock txtElementInfo;
        private ProgressBar progressBar;
        private Border brd;
        private GroupBox parentPanel;
        private Thread trdUpdateUI;
        private Thread trdExecuteJob;
        private Thread trdInitialSearch;
        private int intStatusPrc;
        public long totalFiles;
        public long totalFolders;
        public long totalSize;
        public long currentFile;
        public bool blnSizeSearchIsEnded;
        public bool blnTotalFilesCountIsEnded;
        public bool blnIsEnded;
        private string path;
        private ErazedElements parent;
        private List<Files> files = new List<Files>();

        /// <summary>
        /// Main Constructor
        /// </summary>
        /// <param name="path">Search for files inside this path</param>
        /// <param name="files">List of files to be manipulated</param>
        /// <param name="progressBar">The ProgressBar to be updated</param>
        /// <param name="grdDisplay">The DataGrid to be updated</param>
        public PathElementUI(string path, ProgressBar progressBar, GroupBox parentPanel, ErazedElements parent)
        {
            this.parent = parent;
            blnSizeSearchIsEnded = false;
            blnTotalFilesCountIsEnded = false;
            blnIsEnded = false;
            this.path = path;
            intStatusPrc = 0;
            totalFiles = 0;
            totalFolders = 0;
            currentFile = 0;
            totalSize = 0;
            this.parentPanel = parentPanel;
            this.progressBar = progressBar;
            ControlsInit();
            SearchForFiles();
        }

        public void changeSkinMode()
        {
            try
            {
                txtElementInfo.Dispatcher.Invoke(new displayDir(updateTextBlock));
            }
            catch (Exception) { throw; }
        }

        private void ControlsInit()
        {
            try
            {
                Grid parentGrid = ((Grid)(parentPanel.Content));
                parentGrid.RowDefinitions.Add(new RowDefinition { Height = new GridLength(100, GridUnitType.Auto) });

                txtElementInfo = new TextBlock()
                {

                    Foreground = Brushes.White,
                    FontFamily = new FontFamily("Consolas"),
                    FontSize = 11
                };
                txtElementInfo.MouseDown += txtMouseClick;
                MenuItem mnuCopy = new MenuItem() { Header = "Copy", Name = "mnuCopy" };
                MenuItem mnuOpen = new MenuItem() { Header = "Open", Name = "mnuOpen" };
                mnuOpen.Click += mnuClick;
                mnuCopy.Click += mnuClick;
                ContextMenu menu = new ContextMenu()
                {
                    Items = { mnuCopy, mnuOpen }
                };
                txtElementInfo.ContextMenu = menu;

                brd = new Border
                {
                    Background = Brushes.Transparent,
                    BorderBrush = new SolidColorBrush { Color = Color.FromRgb(255, 255, 255), Opacity = 0.5 },
                    BorderThickness = new Thickness(1),
                    Margin = new Thickness(2),
                    Opacity = 0.9
                };
                brd.SetValue(Grid.RowProperty, parentGrid.RowDefinitions.Count - 1);
                brd.Child = txtElementInfo;
                brd.MouseEnter += brdMouseEnter;
                brd.MouseLeave += brdMouseLeave;
                parentGrid.Children.Add(brd);
            }
            catch (Exception)
            {

                throw;
            }
        }

        private void txtMouseClick(object sender, MouseEventArgs e)
        {
            //if (e. == 2)
        }

        private void mnuClick(object sender, EventArgs e)
        {
            MenuItem item = sender as MenuItem;

            switch (item.Name)
            {
                case "mnuOpen":
                    RunProcessAsync(path);
                    break;
                case "mnuCopy":
                    Clipboard.SetText(path);
                    break;
                default:
                    break;
            }
        }

        private static Task<int> RunProcessAsync(string fileName)
        {
            try
            {
                var tcs = new TaskCompletionSource<int>();

                DirectoryInfo dir = new DirectoryInfo(fileName);
                if (!dir.Exists) return null;
                var process = new Process
                {
                    StartInfo = { FileName = @fileName },
                    EnableRaisingEvents = true
                };

                process.Exited += (sender, args) =>
                {
                    tcs.SetResult(process.ExitCode);
                    process.Dispose();
                };

                process.Start();

                return tcs.Task;
            }
            catch (Exception){throw;}
        }

        private void brdMouseEnter(object sender, MouseEventArgs e)
        {
            ((Border)sender).BorderBrush = new SolidColorBrush { Color = Color.FromRgb(70, 130, 180), Opacity = 0.5 };
            ((Border)sender).BorderThickness = new Thickness(2);
            ((Border)sender).Margin = new Thickness(1);
        }

        private void brdMouseLeave(object sender, MouseEventArgs e)
        {
            ((Border)sender).BorderBrush = new SolidColorBrush { Color = Color.FromRgb(255, 255, 255), Opacity = 0.5 };
            ((Border)sender).BorderThickness = new Thickness(1);
            ((Border)sender).Margin = new Thickness(2);
        }

        public void SearchForFiles()
        {
            try
            {
                files.Clear();
                trdInitialSearch = new Thread(new ThreadStart(UpdateTotalFilesFolders));
                trdInitialSearch.IsBackground = true;
                trdInitialSearch.Start();
                trdExecuteJob = new Thread(new ThreadStart(SearchRunner));
                trdExecuteJob.IsBackground = true;
                trdExecuteJob.Start();
                trdUpdateUI = new Thread(new ThreadStart(UpdateUIRunner));
                trdUpdateUI.IsBackground = true;
                trdUpdateUI.Start();
            }
            catch (Exception)
            {
                throw;
            }
        }

        private void updateProgressStatus()
        {
            try
            {
                if (totalFiles != 0)
                {
                    intStatusPrc = (int)((currentFile * 100) / totalFiles);
                    progressBar.Value = intStatusPrc;
                }
                else progressBar.Value = 0;
            }
            catch (Exception)
            {
                throw;
            }
        }

        private void updateTextBlock()
        {
            try
            {
                
                string strTotalSize = "(" + String.Format("{0:#,##0}", totalSize) + " bytes)";

                txtElementInfo.Inlines.Clear();
                txtElementInfo.Inlines.Add(Globals.coloredRun("Location : ", Globals.LabelColor));
                txtElementInfo.Inlines.Add(Globals.coloredRun(path, Globals.ValueColor));
                txtElementInfo.Inlines.Add(new Run(Environment.NewLine));
                txtElementInfo.Inlines.Add(Globals.coloredRun("Size     : ", Globals.LabelColor));
                txtElementInfo.Inlines.Add(Globals.coloredRun(Globals.sizeFix(totalSize, 2), Brushes.Tomato, strTotalSize));
                txtElementInfo.Inlines.Add(Globals.coloredRun(" ( ", Globals.LabelColor));
                txtElementInfo.Inlines.Add(Globals.coloredRun(totalFolders.ToString() , Globals.ValueColor));
                txtElementInfo.Inlines.Add(Globals.coloredRun(" Folders ", Globals.LabelColor));
                txtElementInfo.Inlines.Add(Globals.coloredRun(totalFiles.ToString(), Globals.ValueColor));
                txtElementInfo.Inlines.Add(Globals.coloredRun(" Files ) ", Globals.LabelColor));
                //txtElementInfo.Text = string.Format(strOutput, path, totalFiles, totalFolders, Globals.sizeFix(totalSize, 2), strTotalSize);
            }
            catch (Exception){throw;}
        }

        private void HideElement()
        {
            try
            {
                if (totalFiles == 0 && totalFolders == 0 && totalSize == 0)
                {
                    brd.Visibility = Visibility.Collapsed;
                    return;
                }
            }
            catch (Exception){ throw; }
        }

        private void UpdateUIRunner()
        {
            try
            {
                while (!blnSizeSearchIsEnded || !blnTotalFilesCountIsEnded)
                {
                    progressBar.Dispatcher.Invoke(new displayProgress(updateProgressStatus));
                    txtElementInfo.Dispatcher.Invoke(new displayDir(updateTextBlock));
                    brd.Dispatcher.Invoke(new displayDir(HideElement));
                    Thread.Sleep(10);
                }
                progressBar.Dispatcher.Invoke(new displayProgress(updateProgressStatus));
                txtElementInfo.Dispatcher.Invoke(new displayDir(updateTextBlock));
                blnIsEnded = true;
            }
            catch (Exception){ throw; }
        }

        private void SearchRunner()
        {
            try
            {
                FillListFiles(path);
                blnSizeSearchIsEnded = true;
            }
            catch (Exception e){throw;}
        }

        private void UpdateTotalFilesFolders()
        {
            try
            {
                FindTotalFiles(path);
                blnTotalFilesCountIsEnded = true;
            }
            catch (Exception){throw;}
        }

        private void FindTotalFiles(string path)
        {
            try
            {
                if (path.Length > 248)
                    return;
                DirectoryInfo dir = new DirectoryInfo(path);
                if (!dir.Exists)
                    return;
                int intFilesTotal = dir.GetFiles().Length;
                totalFiles += intFilesTotal;
                //parent.totalFiles += intFilesTotal;
                DirectoryInfo[] dirs = dir.GetDirectories();
                int intFoldersTotal = dirs.Length;
                totalFolders += intFoldersTotal;
                //parent.totalFolders += intFoldersTotal;
                foreach (DirectoryInfo subdir in dirs)
                    try { FindTotalFiles(subdir.FullName); }
                    catch (UnauthorizedAccessException) { continue; }
            }
            catch (UnauthorizedAccessException) { return; }
            catch (Exception){throw;}
        }

        public void FillListFiles(string path)
        {
            try
            {
                if (path.Length > 248) return;
                DirectoryInfo dir = new DirectoryInfo(path);
                if (!dir.Exists) return;

                FileInfo[] filesIO = dir.GetFiles();
                foreach (FileInfo file in filesIO)
                    try
                    {
                        Files f = new Files(file.Name, Path.Combine(path, file.Name), file.Length);
                        files.Add(f);
                        long size = file.Length;
                        totalSize += size;
                        //parent.totalSize += size;
                        currentFile++;
                    }
                    catch (UnauthorizedAccessException){ continue; }

                DirectoryInfo[] dirs = dir.GetDirectories();
                foreach (DirectoryInfo subdir in dirs)
                    try { FillListFiles(subdir.FullName); }
                    catch (UnauthorizedAccessException) { continue; }

            }
            catch (UnauthorizedAccessException) { return; }
            catch (Exception exc)
            {
                System.Diagnostics.Debug.WriteLine(exc.Message + " Directory upload Error");
                throw;
            }
        }

    }
}

//FileIOPermission permis = new FileIOPermission(FileIOPermissionAccess.AllAccess, file.DirectoryName);
//bool all = true;
//try
//{
//    permis.Demand();
//    permis.PermitOnly();

//}
//catch (System.Security.SecurityException ex)
//{
//    all = false;
//}
//if (all)