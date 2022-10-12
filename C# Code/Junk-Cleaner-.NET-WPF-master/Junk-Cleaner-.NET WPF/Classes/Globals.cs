using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Documents;
using System.Windows.Media;

namespace Junk_Cleaner_.NET_WPF
{

    public static class Globals
    {
        private static readonly string strAppDataPath = Directory.GetParent(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData)).FullName;
        public static Brush BackgroundColor { get; set; }
        public static Brush ValueColor { get; set; }
        public static Brush LabelColor { get; set; }
        public static Brush SizeColor { get; set; }
        public static Brush FinishedColor { get; set; }

        private static readonly string[] SizeSuffixes =
                  { "bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB" };

        public static void ChangeSkinMode(SkinElement skin)
        {
            BackgroundColor = skin.Background;
            ValueColor = skin.Values;
            LabelColor = skin.Labels;
            SizeColor = skin.Size;
            FinishedColor = skin.Finished;
        }

        public static string sizeFix(long length, int decimalPlaces)
        {
            try
            {
                if (length < 0) { return "-" + sizeFix((-length), decimalPlaces); }
                int i = 0;
                decimal dValue = (decimal)length;
                while (Math.Round(dValue, decimalPlaces) >= 1000) { dValue /= 1024; i++; }
                return string.Format("{0:n" + decimalPlaces + "} {1}", dValue, SizeSuffixes[i]);
            }
            catch (Exception)
            {
                throw;
            }
        }

        /// <summary>
        /// Returns a new coloured Run with text
        /// </summary>
        /// <param name="txt">Text to include the Run</param>
        /// <param name="brush">Colour of Text</param>
        /// <returns>A new coloured Run with text</returns>
        public static Run coloredRun(string txt, Brush brush, string txtToolTip = "")
        {
            try
            {
                if (String.IsNullOrEmpty(txtToolTip))
                    return new Run { Text = txt, Foreground = brush };
                else
                    return new Run { Text = txt, Foreground = brush, ToolTip = txtToolTip };
            }
            catch (Exception)
            {

                throw;
            }
        }
    }
}
