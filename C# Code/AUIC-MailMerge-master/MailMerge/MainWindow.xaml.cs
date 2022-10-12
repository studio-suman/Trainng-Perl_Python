using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using MailMerge.OfficeInterop;
using Microsoft.Office.Interop.Word;
using NetOffice.OutlookApi;
using NetOffice.OutlookApi.Enums;
using Novacode;
using Application = NetOffice.OutlookApi.Application;
using _Application = Microsoft.Office.Interop.Word._Application;

namespace MailMerge
{
    /// <summary>
    ///     Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow
    {
        private readonly string mTemplateFolder = "Templates";

        public MainWindow()
        {
            InitializeComponent();

            string[] files = Directory.GetFiles(mTemplateFolder);

            foreach (string file in files)
            {
                Button fileButton = new Button();
                fileButton.Content = Path.GetFileNameWithoutExtension(file);
                TemplateStack.Children.Add(fileButton);
                fileButton.Click += fileButton_Click;
            }

            return;
            DocX doc = DocX.Load("Test.docx");

            IMergeFieldDictionary mergeFieldDictionary = new TestMergeFieldDictionary();
            foreach (Dictionary<string, string> dictionary in mergeFieldDictionary.RowList)
            {
                foreach (string header in mergeFieldDictionary.Headers)
                {
                    doc.ReplaceText(string.Format("%{0}%", header), dictionary[header]);
                }
            }

            StreamWriter SW = new StreamWriter("test.txt");
            SW.Write(doc.Text);
            SW.Close();

            doc.SaveAs("Test_Out.docx");

            Convert(Path.GetFullPath("Test_Out.docx"), Path.GetFullPath("Test_Out.html"),
                WdSaveFormat.wdFormatFilteredHTML);

            bool isLocked = true;
            StreamReader SR = null;
            while (isLocked)
            {
                try
                {
                    SR = new StreamReader("Test_Out.html", Encoding.GetEncoding(1252));
                    isLocked = false;
                }
                catch
                {
                }
            }

            string content = SR.ReadToEnd();
            SR.Close();

            // start outlook 
            Application outlookApplication = new Application();

            // create a new MailItem.
            MailItem mailItem =
                outlookApplication.CreateItem(OlItemType.olMailItem) as MailItem;

            // prepare item and send
            mailItem.Recipients.Add("luk__5@hotmail.com");
            mailItem.Subject = "hello Helene";
            mailItem.HTMLBody = content;
            mailItem.BodyFormat = OlBodyFormat.olFormatHTML;
            mailItem.Send();

            // close outlook and dispose
            outlookApplication.Quit();
            outlookApplication.Dispose();
        }

        private void fileButton_Click(object sender, RoutedEventArgs e)
        {
            string path = string.Format("{0}/{1}.docx",
                mTemplateFolder,
                (sender as Button).Content);
            DoTemplateWindow DOT = new DoTemplateWindow(path);
            Hide();
            DOT.ShowDialog();
            Show();
        }

        public static void Convert(string input, string output, WdSaveFormat format)
        {
            // Create an instance of Word.exe
            _Application oWord = new Microsoft.Office.Interop.Word.Application();

            // Make this instance of word invisible (Can still see it in the taskmgr).
            oWord.Visible = false;

            // Interop requires objects.
            object oMissing = Missing.Value;
            object isVisible = true;
            object readOnly = false;
            object oInput = input;
            object oOutput = output;
            object oFormat = format;

            // Load a document into our instance of word.exe
            _Document oDoc = oWord.Documents.Open(ref oInput, ref oMissing, ref readOnly, ref oMissing, ref oMissing,
                ref oMissing, ref oMissing, ref oMissing, ref oMissing, ref oMissing, ref oMissing, ref isVisible,
                ref oMissing, ref oMissing, ref oMissing, ref oMissing);

            // Make this document the active document.
            oDoc.Activate();

            // Save this document in Word 2003 format.
            oDoc.SaveAs(ref oOutput, ref oFormat, ref oMissing, ref oMissing, ref oMissing, ref oMissing, ref oMissing,
                ref oMissing, ref oMissing, ref oMissing, ref oMissing, ref oMissing, ref oMissing, ref oMissing,
                ref oMissing, ref oMissing);

            // Always close Word.exe.
            oWord.Quit(ref oMissing, ref oMissing, ref oMissing);
        }
    }
}