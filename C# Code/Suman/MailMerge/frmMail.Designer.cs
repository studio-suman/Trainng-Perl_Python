
namespace MailMerge1
{
    partial class MailMerge
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MailMerge));
            this.btnUplDot = new System.Windows.Forms.Button();
            this.btnUplCsv = new System.Windows.Forms.Button();
            this.txtBoxXl = new System.Windows.Forms.TextBox();
            this.txtboxDotx = new System.Windows.Forms.TextBox();
            this.btnCancel = new System.Windows.Forms.Button();
            this.btnSend = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btnUplDot
            // 
            this.btnUplDot.Location = new System.Drawing.Point(413, 26);
            this.btnUplDot.Name = "btnUplDot";
            this.btnUplDot.Size = new System.Drawing.Size(109, 23);
            this.btnUplDot.TabIndex = 0;
            this.btnUplDot.Text = "Upload Dotx";
            this.btnUplDot.UseVisualStyleBackColor = true;
            this.btnUplDot.Click += new System.EventHandler(this.btnUplDot_Click);
            // 
            // btnUplCsv
            // 
            this.btnUplCsv.Location = new System.Drawing.Point(413, 65);
            this.btnUplCsv.Name = "btnUplCsv";
            this.btnUplCsv.Size = new System.Drawing.Size(109, 23);
            this.btnUplCsv.TabIndex = 0;
            this.btnUplCsv.Text = "Upload (.Csv/Xlsx)";
            this.btnUplCsv.UseVisualStyleBackColor = true;
            this.btnUplCsv.Click += new System.EventHandler(this.btnUplCsv_Click);
            // 
            // txtBoxXl
            // 
            this.txtBoxXl.ForeColor = System.Drawing.SystemColors.InactiveCaption;
            this.txtBoxXl.Location = new System.Drawing.Point(24, 65);
            this.txtBoxXl.Name = "txtBoxXl";
            this.txtBoxXl.Size = new System.Drawing.Size(351, 20);
            this.txtBoxXl.TabIndex = 1;
            this.txtBoxXl.Text = "Path to Directory";
            // 
            // txtboxDotx
            // 
            this.txtboxDotx.ForeColor = System.Drawing.SystemColors.InactiveCaption;
            this.txtboxDotx.Location = new System.Drawing.Point(24, 26);
            this.txtboxDotx.Name = "txtboxDotx";
            this.txtboxDotx.Size = new System.Drawing.Size(351, 20);
            this.txtboxDotx.TabIndex = 1;
            this.txtboxDotx.Text = "Path to Directory";
            // 
            // btnCancel
            // 
            this.btnCancel.Location = new System.Drawing.Point(413, 278);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(109, 23);
            this.btnCancel.TabIndex = 0;
            this.btnCancel.Text = "Cancel";
            this.btnCancel.UseVisualStyleBackColor = true;
            // 
            // btnSend
            // 
            this.btnSend.Location = new System.Drawing.Point(285, 278);
            this.btnSend.Name = "btnSend";
            this.btnSend.Size = new System.Drawing.Size(109, 23);
            this.btnSend.TabIndex = 0;
            this.btnSend.Text = "Send Email";
            this.btnSend.UseVisualStyleBackColor = true;
            // 
            // textBox1
            // 
            this.textBox1.ForeColor = System.Drawing.SystemColors.GrayText;
            this.textBox1.Location = new System.Drawing.Point(24, 103);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.textBox1.Size = new System.Drawing.Size(498, 158);
            this.textBox1.TabIndex = 2;
            this.textBox1.Text = "Enter Mail Subject Here";
            // 
            // MailMerge
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Black;
            this.ClientSize = new System.Drawing.Size(534, 327);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.txtboxDotx);
            this.Controls.Add(this.txtBoxXl);
            this.Controls.Add(this.btnSend);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnUplCsv);
            this.Controls.Add(this.btnUplDot);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "MailMerge";
            this.Text = "Mail Merge";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnUplDot;
        private System.Windows.Forms.Button btnUplCsv;
        private System.Windows.Forms.TextBox txtBoxXl;
        private System.Windows.Forms.TextBox txtboxDotx;
        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.Button btnSend;
        private System.Windows.Forms.TextBox textBox1;
    }
}

