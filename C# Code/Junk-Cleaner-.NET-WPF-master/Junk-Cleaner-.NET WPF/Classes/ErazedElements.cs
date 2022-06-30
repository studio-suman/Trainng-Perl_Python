using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;

namespace Junk_Cleaner_.NET_WPF
{
    public class ElementControler
    {
        private Grid parentGrid;
        private GroupBox gbx;
        public Grid childGrid;
        public string strName;
        public List<ErazedElements> lstChilds;

        public ElementControler(Grid parentGrid, string strName, List<ErazedElements> lstChilds)
        {
            this.parentGrid = parentGrid;
            this.strName = strName;
            this.lstChilds = lstChilds;
            ControlsInit();
        }

        private void ControlsInit()
        {
            try
            {
                parentGrid.RowDefinitions.Add(new RowDefinition { Height = new GridLength(100, GridUnitType.Auto) });
                gbx = new GroupBox()
                {
                    Foreground = Brushes.RosyBrown,
                    FontFamily = new FontFamily("Consolas"),
                    FontSize = 11,
                    Header = strName,
                    BorderThickness = new Thickness(0.3)
                };
                childGrid = new Grid { Background = Brushes.Transparent };
                gbx.Content = childGrid;
                foreach (ErazedElements child in lstChilds)
                    child.setParentGrid(childGrid);
                gbx.SetValue(Grid.RowProperty, parentGrid.RowDefinitions.Count - 1);
                parentGrid.Children.Add(gbx);
            }
            catch (Exception) { throw; }
        }

        public static explicit operator ElementControler(DependencyObject v)
        {
            throw new NotImplementedException();
        }

    }

    public class ErazedElements
    {
        private Grid parentGrid;
        private CheckBox chkIsActive;

        public string strName;
        public bool IsActive;
        public List<string> lstPaths;

        public ErazedElements(string strName, List<string> lstPaths)
        {
            IsActive = true;
            this.lstPaths = lstPaths;
            this.strName = strName;
        }

        public ErazedElements(string strName, List<string> lstPaths, Grid parentGrid)
        {
            IsActive = true;
            this.lstPaths = lstPaths;
            this.strName = strName;
            this.parentGrid = parentGrid;
            ControlsInit();
        }

        public void setParentGrid(Grid parentGrid)
        {
            try
            {
                this.parentGrid = parentGrid;
                ControlsInit();
            }
            catch (Exception){throw;}
        }

        public void changeSkinMode()
        {
            chkIsActive.Foreground = Globals.ValueColor;
            chkIsActive.UpdateLayout();
        }

        private void ControlsInit()
        {
            try
            {
                parentGrid.RowDefinitions.Add(new RowDefinition { Height = new GridLength(100, GridUnitType.Auto) });
                chkIsActive = new CheckBox()
                {
                    Foreground = Globals.ValueColor,
                    FontFamily = new FontFamily("Consolas"),
                    FontSize = 10,
                    IsChecked = true,
                    Content = strName,
                };
                chkIsActive.Checked += CheckBox_Checked;
                chkIsActive.Unchecked += CheckBox_Checked;
                Border brd = new Border
                {
                    Background = Brushes.Transparent,
                    VerticalAlignment = VerticalAlignment.Center,
                    BorderBrush = new SolidColorBrush { Color = Color.FromRgb(102, 255, 179), Opacity = 0.1 },
                    BorderThickness = new Thickness(1),
                    Margin = new Thickness(2),
                    Opacity = 0.9
                };

                brd.Child = chkIsActive;
                brd.SetValue(Grid.RowProperty, parentGrid.RowDefinitions.Count - 1);
                brd.MouseEnter += brdMouseEnter;
                brd.MouseLeave += brdMouseLeave;
                parentGrid.Children.Add(brd);
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
            ((Border)sender).BorderBrush = new SolidColorBrush { Color = Color.FromRgb(102, 255, 179), Opacity = 0.1 };
            ((Border)sender).BorderThickness = new Thickness(1);
            ((Border)sender).Margin = new Thickness(2);
        }
        private void CheckBox_Checked(object sender, RoutedEventArgs e)
        {
            IsActive = (bool)chkIsActive.IsChecked;
        }

    }
    
}
