using System.IO;
using System.Text;
using Microsoft.Office.Interop.Word;
using NetOffice.OutlookApi;
using NetOffice.OutlookApi.Enums;
using Novacode;
using Application = NetOffice.OutlookApi.Application;

namespace MailMerge.OfficeInterop
{
    internal class MailUtility
    {
        public static void SendMail(DocX docX, string[] recipients, string subject)
        {
            string tmpFile = Path.GetRandomFileName();
            string tmpHTML = Path.GetRandomFileName();
            docX.SaveAs(tmpFile);
            WordUtility.Convert(Path.GetFullPath(tmpFile), Path.GetFullPath(tmpHTML),
                WdSaveFormat.wdFormatFilteredHTML);

            bool isLocked = true;
            StreamReader SR = null;
            while (isLocked)
            {
                try
                {
                    SR = new StreamReader(tmpHTML, Encoding.GetEncoding(1252));
                    isLocked = false;
                }
                catch
                {
                }
            }
            string content = SR.ReadToEnd();
            SR.Close();

            File.Delete(tmpFile);
            File.Delete(tmpHTML);

            // start outlook 
            Application outlookApplication = new Application();

            // create a new MailItem.
            MailItem mailItem =
                outlookApplication.CreateItem(OlItemType.olMailItem) as MailItem;

            // prepare item and send
            foreach (string recipient in recipients)
            {
                mailItem.Recipients.Add(recipient);
            }
            mailItem.Subject = subject;
            mailItem.HTMLBody = content;
            mailItem.BodyFormat = OlBodyFormat.olFormatHTML;
            mailItem.Send();

            // close outlook and dispose
            outlookApplication.Quit();
            outlookApplication.Dispose();
        }
    }
}