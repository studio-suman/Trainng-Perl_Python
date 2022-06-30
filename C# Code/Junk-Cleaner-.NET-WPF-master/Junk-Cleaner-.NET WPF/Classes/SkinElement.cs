using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Media;

namespace Junk_Cleaner_.NET_WPF
{
    public class SkinElement
    {
        public  Brush Background { get; set; }
        public  Brush Values { get; set; }
        public  Brush Labels { get; set; }
        public  Brush Size { get; set; }
        public  Brush Finished { get; set; }

        public SkinElement(Brush Background, Brush Values, Brush Labels, Brush Size, Brush Finished)
        {
            this.Background = Background;
            this.Values = Values;
            this.Labels = Labels;
            this.Size = Size;
            this.Finished = Finished;
        }
    }
}
