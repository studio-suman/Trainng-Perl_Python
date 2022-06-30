using System;
using System.Collections.Generic;

namespace MailMerge1.OfficeInterop
{
    internal class ExcelMergeFieldDictionary : IMergeFieldDictionary
    {
        private List<string> mHeaders;

        public ExcelMergeFieldDictionary(string path)
        {
        }

        public int Count
        {
            get { throw new NotImplementedException(); }
        }

        public IEnumerable<string> Headers
        {
            get { throw new NotImplementedException(); }
        }

        public IEnumerable<Dictionary<string, string>> RowList
        {
            get { throw new NotImplementedException(); }
        }
    }
}