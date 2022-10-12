using System.Collections.Generic;

namespace MailMerge.OfficeInterop
{
    internal interface IMergeFieldDictionary
    {
        int Count { get; }
        IEnumerable<string> Headers { get; }
        IEnumerable<Dictionary<string, string>> RowList { get; }
    }
}