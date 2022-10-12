using System;
using System.Collections.Generic;
using System.Linq;
using System.Management;
using System.Text;
using System.Threading;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Media;
using Microsoft.VisualBasic.Devices;

namespace Junk_Cleaner_.NET_WPF
{
    public class HardwareInfo
    {
        private delegate void displayInfo();
        private Thread trdOSInfo;
        private Thread trdCPUInfo;
        private Thread trdGPUInfo;
        private TextBlock textBlock;
        private List<string> strGPUOutput;
        private string strCPUOutput;
        private string strOSFullName;
        private string strServicePack;
        private string strOSBits;
        private string strProcessorBits;
        private string strVersionString;
        private string strRamInfo;
        private List<string> strGPURamInfo;

        public HardwareInfo(TextBlock textBlock)
        {
            strGPUOutput = new List<string>();
            strCPUOutput = string.Empty;
            strOSFullName = string.Empty;
            strServicePack = string.Empty;
            strOSBits = string.Empty;
            strVersionString = string.Empty;
            strProcessorBits = string.Empty;
            strRamInfo = string.Empty;
            strGPURamInfo = new List<string>();
            this.textBlock = textBlock;
            SetOutputString();
            run();
        }


        public void changeSkinMode()
        {
            textBlock.Dispatcher.Invoke(new displayInfo(SetOutputString));
        }

        private void run()
        {
            try
            {
                trdOSInfo = new Thread(new ThreadStart(OSRunner));
                trdOSInfo.IsBackground = true;
                trdOSInfo.Start();
                trdCPUInfo = new Thread(new ThreadStart(CPURunner));
                trdCPUInfo.IsBackground = true;
                trdCPUInfo.Start();
                trdGPUInfo = new Thread(new ThreadStart(GPURunner));
                trdGPUInfo.IsBackground = true;
                trdGPUInfo.Start();
            }
            catch (Exception){throw;}
        }

        private void OSRunner()
        {
            try
            {
                ComputerInfo ci = new ComputerInfo();
                strOSFullName = ci.OSFullName;
                strServicePack = OSVersionInfo.ServicePack;
                strOSBits = OSVersionInfo.OSBits.ToString();
                strVersionString = OSVersionInfo.VersionString;
                strProcessorBits = OSVersionInfo.ProcessorBits.ToString();
                strRamInfo = Globals.sizeFix((long)ci.TotalPhysicalMemory, 0);
                textBlock.Dispatcher.Invoke(new displayInfo(SetOutputString));
            }
            catch (Exception) { throw; }
        }

        private void CPURunner()
        {
            try
            {
                GetGPUInfo(); 
                textBlock.Dispatcher.Invoke(new displayInfo(SetOutputString));
            }
            catch (Exception){throw;}
        }

        private void GPURunner()
        {
            try
            {
                strCPUOutput = GetProcessorID();
                textBlock.Dispatcher.Invoke(new displayInfo(SetOutputString));
            }
            catch (Exception) { throw; }
        }

        private string GetProcessorID()
        {
            try
            {
                ManagementClass mgt = new ManagementClass("Win32_Processor");
                ManagementObjectCollection procs = mgt.GetInstances();
                foreach (ManagementObject item in procs)
                {
                    //List<string> ls = new List<string>();
                    //foreach (PropertyData prop in item.Properties)
                    //    if (prop.Value != null)
                    //        ls.Add(prop.Name + " : " + prop.Value.ToString());
                    return item.Properties["Name"].Value.ToString().Trim();
                }

                return "Unknown";
            }
            catch (Exception) { return "Unknown"; }
        }

        private void SetOutputString()
        {
            try
            {
                textBlock.Inlines.Clear();
                textBlock.Inlines.Add(Globals.coloredRun("OS  : ", Globals.LabelColor));
                textBlock.Inlines.Add(Globals.coloredRun(strOSFullName + " " , Globals.ValueColor));
                if(!string.IsNullOrEmpty(strServicePack.Trim()))
                    textBlock.Inlines.Add(Globals.coloredRun(strServicePack + " ", Globals.ValueColor));
                if (!string.IsNullOrEmpty(strOSBits.Trim()))
                    textBlock.Inlines.Add(Globals.coloredRun(strOSBits + " ", Globals.ValueColor));
                if (!string.IsNullOrEmpty(strVersionString.Trim()))
                {
                    textBlock.Inlines.Add(Globals.coloredRun("[ Version : ", Globals.LabelColor));
                    textBlock.Inlines.Add(Globals.coloredRun(strVersionString, Globals.ValueColor));
                    textBlock.Inlines.Add(Globals.coloredRun(" ]", Globals.LabelColor));
                }
                textBlock.Inlines.Add(new Run(Environment.NewLine));
                textBlock.Inlines.Add(Globals.coloredRun("CPU : ", Globals.LabelColor));
                textBlock.Inlines.Add(Globals.coloredRun(strCPUOutput + " ", Globals.ValueColor));
                textBlock.Inlines.Add(Globals.coloredRun(strProcessorBits + " ", Globals.ValueColor));
                textBlock.Inlines.Add(new Run(Environment.NewLine));
                textBlock.Inlines.Add(Globals.coloredRun("RAM : ", Globals.LabelColor));
                textBlock.Inlines.Add(Globals.coloredRun(strRamInfo + " ", Globals.ValueColor));
                textBlock.Inlines.Add(new Run(Environment.NewLine));
                for (int i = 0; i < strGPUOutput.Count; i++)
                {
                    string vga = strGPUOutput[i];
                    string ram = string.Empty;
                    if (strGPURamInfo.Count > i) ram = strGPURamInfo[i];
                    textBlock.Inlines.Add(Globals.coloredRun("VGA : ", Globals.LabelColor));
                    textBlock.Inlines.Add(Globals.coloredRun(vga + " ", Globals.ValueColor));
                    textBlock.Inlines.Add(Globals.coloredRun("[ Ram : ", Globals.LabelColor));
                    textBlock.Inlines.Add(Globals.coloredRun(ram + " ", Globals.ValueColor));
                    textBlock.Inlines.Add(Globals.coloredRun(" ]", Globals.LabelColor));
                }
                //StringBuilder sb = new StringBuilder(String.Empty);
                //sb.AppendLine(String.Format("OS  : {0} {1} {2} [ {3} ]", strOSFullName, strServicePack, strOSBits, strVersionString));
                //sb.AppendLine(String.Format("CPU : {0} {1}", strCPUOutput, strProcessorBits));
                //sb.AppendLine(String.Format("RAM : {0}", strRamInfo));
                //sb.AppendLine(String.Format("VGA : {0} {1}", strGPUOutput, strGPURamInfo));
                //textBlock.Text = sb.ToString();
            }
            catch (Exception) { throw; }
        }

        private void GetGPUInfo()
        {
            try
            {
                ManagementObjectSearcher objvide = new ManagementObjectSearcher("select * from Win32_VideoController");

                foreach (ManagementObject obj in objvide.Get())
                {
                    strGPUOutput.Add(obj["Name"].ToString());
                    long VGARam = 0;
                    //List<string> ls = new List<string>();
                    //foreach (PropertyData prop in obj.Properties)
                    //    if(prop.Value != null)
                    //        ls.Add(prop.Name +" : " + prop.Value.ToString());
                    long.TryParse(obj["AdapterRAM"].ToString(), out VGARam);
                    strGPURamInfo.Add(Globals.sizeFix(VGARam, 0));
                }
            }
            catch (Exception)
            {

                throw;
            }
        }
    }
}
