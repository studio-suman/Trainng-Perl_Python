using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using MailMerge.OfficeInterop;
using Novacode;

namespace MailMerge
{
    /// <summary>
    ///     Interaction logic for DoTemplateWindow.xaml
    /// </summary>
    public partial class DoTemplateWindow
    {
        private readonly DocX mDoc;
        private readonly string mDocPath;
        private readonly WordMergeFieldDictionary mWordMergeFieldDictionary;

        public DoTemplateWindow(string pPath)
        {
            mDoc = DocX.Load(pPath);
            mDocPath = pPath;
            mWordMergeFieldDictionary = new WordMergeFieldDictionary(mDoc, 1);
            InitializeComponent();
            GenerateHeaders();
            AddRow();
            MergeFieldDataGrid.ItemsSource = mWordMergeFieldDictionary.RowList;
        }

        public ObservableCollection<Dictionary<string, string>> mMergeFields
        {
            get { return mWordMergeFieldDictionary.RowList as ObservableCollection<Dictionary<string, string>>; }
        }

        private void AddRow()
        {
            mWordMergeFieldDictionary.AddRow();
        }

        public void GenerateHeaders()
        {
            MergeFieldDataGrid.Columns.Clear();
            Binding emailBinding = new Binding("[Email]");
            MergeFieldDataGrid.Columns.Add(new DataGridTextColumn()
            {
                Header = "Email",
                Binding = emailBinding
            });

            foreach (string header in mWordMergeFieldDictionary.Headers)
            {
                Binding b = new Binding($"[{header}]");
                MergeFieldDataGrid.Columns.Add(new DataGridTextColumn
                {
                    Header = header,
                    Binding = b
                });
            }
        }

        private void MergeButton_Click(object sender, RoutedEventArgs e)
        {
            int i = 0;
            foreach (Dictionary<string, string> dictionary in mWordMergeFieldDictionary.RowList)
            {
                if (dictionary.Count < mWordMergeFieldDictionary.Count)
                    continue;
                i++;
                DocX doc = DocX.Load(mDocPath);
                foreach (string header in mWordMergeFieldDictionary.Headers)
                {
                    if(header.Equals("Email"))
                        continue;
                    doc.ReplaceText($"%{header}%", dictionary[header]);
                }
                MailUtility.SendMail(doc, new []{dictionary["Email"]}, SubjectTextBox.Text);
            }
        }

        private void AddRowButton_Click(object sender, RoutedEventArgs e)
        {
            AddRow();
        }
    }
}