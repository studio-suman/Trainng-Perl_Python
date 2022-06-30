using System;
using System.Windows.Forms;

namespace MailMerge1
{


    public partial class MailMerge : Form
    {



        public MailMerge()
        {
            InitializeComponent();
        }

        private void btnUplDot_Click(object sender, System.EventArgs e)
        {
            string path1 = null;
            OfficeInterop.FileHandle h2 = new OfficeInterop.FileHandle();
            //string sSelectedFilePath = null;
            txtboxDotx.Text = h2.FileOpen(path1).ToString();

        }

        private void btnUplCsv_Click(object sender, EventArgs e)
        {
            string path = null;
            OfficeInterop.FileHandle h1 = new OfficeInterop.FileHandle();
            //string sSelectedFilePath = null;
            txtBoxXl.Text = h1.FileOpen(path).ToString();

        }
    }
}
