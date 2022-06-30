using System.Collections.Generic;

namespace MailMerge1.OfficeInterop
{
    internal interface IMergeFieldDictionary
    {
        int Count { get; }
        IEnumerable<string> Headers { get; }
        IEnumerable<Dictionary<string, string>> RowList { get; }
    }
}