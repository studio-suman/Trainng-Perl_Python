﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows.Forms;


namespace MailMerge1.OfficeInterop

{
    public class FileHandle
    {
        List<float> t = new List<float>();
        List<float> SensorI = new List<float>();
        List<float> SensorII = new List<float>();
        List<float> SensorIII = new List<float>();

        public string FileOpen(string path)

        {

            using (OpenFileDialog dialog = new OpenFileDialog())
            {
                string sSelectedFile = String.Empty;
                string sSelectedFilePath = String.Empty;

                try
                {

                    dialog.Filter = "csv files (*.csv)|*.csv";
                    dialog.Multiselect = false;
                    dialog.InitialDirectory = ".";
                    dialog.Title = "Select file (only in csv format)";
                    if (dialog.ShowDialog() == DialogResult.OK)
                    {
                        sSelectedFilePath = dialog.FileName;
                        var fs = File.ReadAllLines(dialog.FileName).Select(a => a.Split(';'));
                        int counter = 0;
                        foreach (var line in fs)
                        {
                            counter++;
                            if (counter > 2)    // Skip first two headder lines
                            {
                                this.t.Add(float.Parse(line[0]));
                                this.SensorI.Add(float.Parse(line[1]));
                                this.SensorII.Add(float.Parse(line[2]));
                                this.SensorIII.Add(float.Parse(line[3]));
                            }
                        }
                    }
                }
                catch (Exception exc)
                {
                    MessageBox.Show(
                        "Error while opening the file.\n" + exc.Message,this.ToString(),
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error
                    );
                }
             path = sSelectedFilePath;
                return path;
            } 
        }
    }
}