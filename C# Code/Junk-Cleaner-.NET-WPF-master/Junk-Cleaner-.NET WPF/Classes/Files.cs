using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Junk_Cleaner_.NET_WPF
{
    public class Files
    {
        public string name { get; set; }
        public string size { get; private set; }
        public string path { get; set; }
        public long length { get; set; }
        public Files(string name, string path, long length)
        {
            this.name = name;
            this.path = path;
            this.length = length;
            size = Globals.sizeFix(length, 2);
        }
        
    }
}
