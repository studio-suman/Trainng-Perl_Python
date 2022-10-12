using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
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

    public enum SkinMode : int
    {
        Dark = 0,
        Light = 1,
        Hippy = 2
    }

    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window, INotifyPropertyChanged
    {
        private double _height;
        private HardwareInfo hardwareInfo;
        private pgJunkCleaner JunkCleaner;
        private pgDiscAnalizer DiscAnalizer;
        public event PropertyChangedEventHandler PropertyChanged;
        private List<SkinElement> skins = new List<SkinElement>();

        public MainWindow()
        {
            InitializeComponent();
            hardwareInfo = new HardwareInfo(txtSystemInfo);
            btnDarkSkin.IsChecked = true;
            btnJunkCleaner.IsChecked = true;
            SkinsInit();
            Globals.ChangeSkinMode(skins[(int)SkinMode.Dark]);
            JunkCleaner = new pgJunkCleaner();
            DiscAnalizer = new pgDiscAnalizer();
            frmNavigate.Navigate(JunkCleaner);
            ChangeSkin(SkinMode.Dark);
        }

        private void SkinsInit()
        {
            try
            {
                //Dark Skin
                skins.Add(new SkinElement(new SolidColorBrush { Color = Color.FromRgb(11, 22, 29), Opacity = 1 },
                                          Brushes.White,
                                          new SolidColorBrush { Color = Color.FromRgb(21, 132, 224), Opacity = 1 },
                                          new SolidColorBrush { Color = Color.FromRgb(214, 58, 97), Opacity = 1 },
                                          new SolidColorBrush { Color = Color.FromRgb(85, 228, 57), Opacity = 1 }));
                //Light skin
                skins.Add(new SkinElement(Brushes.Gainsboro,
                                          Brushes.Black,
                                          Brushes.SteelBlue,
                                          Brushes.Tomato,
                                          Brushes.LimeGreen));
                //Hippy skin
                skins.Add(new SkinElement(Brushes.DarkSlateGray,
                                          Brushes.White,
                                          Brushes.SteelBlue,
                                          Brushes.Tomato,
                                          Brushes.LimeGreen));
            }
            catch (Exception){throw;}
        }

        public double CustomHeight
        {
            get { return _height; }
            set
            {
                if (value != _height)
                {
                    _height = value;
                    if (PropertyChanged != null)
                        PropertyChanged(this, new PropertyChangedEventArgs("CustomHeight"));
                }
            }
        }

        private void ChangeSkin(SkinMode skin)
        {
            try
            {
                Globals.ChangeSkinMode(skins[(int)skin]);
                this.Background = Globals.BackgroundColor;
                gbxSystem.Foreground = Globals.LabelColor;
                hardwareInfo.changeSkinMode();
                JunkCleaner.changeSkinMode();
            }
            catch (Exception){throw;}
        }

        private void btnMenu_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                MenuItem menu = sender as MenuItem;
                switch (menu.Name)
                {
                    case "btnJunkCleaner":
                        btnDiskAnalyzer.IsChecked = false;
                        frmNavigate.Navigate(JunkCleaner);
                        break;
                    case "btnDiskAnalyzer":
                        btnJunkCleaner.IsChecked = false;
                        frmNavigate.Navigate(DiscAnalizer);
                        break;
                    case "btnDarkSkin":
                        btnLightSkin.IsChecked = false;
                        btnHippySkin.IsChecked = false;
                        ChangeSkin(SkinMode.Dark);
                        break;
                    case "btnLightSkin":
                        btnDarkSkin.IsChecked = false;
                        btnHippySkin.IsChecked = false;
                        ChangeSkin(SkinMode.Light);
                        break;
                    case "btnHippySkin":
                        btnDarkSkin.IsChecked = false;
                        btnLightSkin.IsChecked = false;
                        ChangeSkin(SkinMode.Hippy);
                        break;
                    case "btnSourceCodeLink":
                        Process.Start("https://github.com/Obrelix/Junk-Cleaner-.NET-WPF");
                        break;
                    case "btnIssuesLink":
                        Process.Start("https://github.com/Obrelix/Junk-Cleaner-.NET-WPF/issues");
                        break;
                    case "btnAbout":
                        Process.Start("https://github.com/Obrelix");
                        break;
                    case "btnLoad":
                        break;
                    case "btnSave":
                        break;
                    case "btnExit":
                        base.OnClosed(e);
                        Application.Current.Shutdown();
                        break;
                    default:
                        break;
                }
            }
            catch (Exception)
            {

                throw;
            }
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
        }

        private void FrmNavigate_SizeChanged(object sender, SizeChangedEventArgs e)
        {
            Application.Current.MainWindow = this;
            Frame frame = sender as Frame;
            Application.Current.MainWindow.Height = frame.ActualHeight + gbxSystem.ActualHeight + 90;
            Application.Current.MainWindow.Width = frame.ActualWidth +  70;
        }
    }
}
