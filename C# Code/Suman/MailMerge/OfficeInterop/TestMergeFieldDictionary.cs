using System.Collections.Generic;

namespace MailMerge1.OfficeInterop
{
    internal class TestMergeFieldDictionary : IMergeFieldDictionary
    {
        private List<string> mHeaders;

        public int Count
        {
            get { return 2; }
        }

        public IEnumerable<string> Headers
        {
            get { return new List<string> {"FullName", "Aarskort"}; }
        }

        public IEnumerable<Dictionary<string, string>> RowList
        {
            get
            {
                return new List<Dictionary<string, string>>
                {
                    new Dictionary<string, string> {{"Aarskort", "200"}, {"FullName", "Foo Bargensen"}}
                };
            }
        }
    }
}