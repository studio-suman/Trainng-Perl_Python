using System.Collections.Generic;
using System.Reflection;
using System.Text.RegularExpressions;
using Microsoft.Office.Interop.Word;
using Xceed.Words.NET;

namespace MailMerge1.OfficeInterop
{
    public static class WordUtility
    {
        public static Regex MergeFieldRegex = new Regex("%(.+)%", RegexOptions.IgnoreCase);

        public static List<string> GetMergeFields(DocX doc)
        {
            List<string> retList = new List<string>();
            MatchCollection matches = MergeFieldRegex.Matches(doc.Text);
            if (matches.Count > 0)
            {
                foreach (Match match in matches)
                    retList.Add(match.Groups[1].Value);
            }

            return retList;
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