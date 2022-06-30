using System.Collections.Generic;
using System.Collections.ObjectModel;
using Xceed.Words.NET;

namespace MailMerge1.OfficeInterop
{
    internal class WordMergeFieldDictionary : IMergeFieldDictionary
    {
        private readonly ObservableCollection<string> mHeaders;
        private readonly ObservableCollection<Dictionary<string, string>> mRows;

        public WordMergeFieldDictionary(DocX doc, int numOfRows)
        {
            mHeaders = new ObservableCollection<string>(WordUtility.GetMergeFields(doc));
            mRows = new ObservableCollection<Dictionary<string, string>>();
            for (int i = 0; i < numOfRows; i++)
            {
                Dictionary<string, string> dictionary = new Dictionary<string, string>();
                foreach (string header in mHeaders)
                {
                    dictionary[header] = "";
                }
                mRows.Add(dictionary);
            }
        }

        public int Count
        {
            get { return mRows.Count; }
        }

        public IEnumerable<string> Headers
        {
            get { return mHeaders; }
        }

        public IEnumerable<Dictionary<string, string>> RowList
        {
            get { return mRows; }
        }

        public void AddValueForHeader(int pRow, string pHeader, string pValue)
        {
            mRows[pRow][pHeader] = pValue;
        }

        public void AddRow()
        {
            mRows.Add(new Dictionary<string, string>());
        }
    }
}