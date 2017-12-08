using System;
using System.Collections.Generic;
using System.Text;

namespace menu.table
{
    class Table
    {
        public string Rendered { get; set; }
        private List<string> header = new List<string>();
        private List<List<string>> data = new List<List<string>>();
        private List<Int32> lengths = new List<Int32>();

        public Table(List<List<string>> items, List<string> headerRow = null)
        {
            // TODO: check if all the rows have the same length
            data = items;
            
            if (headerRow != null && headerRow.Count > 0)
            {
                header = headerRow;
            }
            else
            {
                header = data[0];
                // TODO: pop data[0] and set data to the new, sliced list
            }
        }
        private void setTableParams()
        {
            if (header.Count > 0)
            {
                data.Insert(0, header);
            }
            for (int i = 0; i < header.Count; i++)
            {
                var maxLength = int.MinValue;
                foreach (var element in data)
                {
                    var elementLength = element[i].Length;
                    if (elementLength > maxLength) {
                        maxLength = elementLength;
                    }
                }
                lengths.Add(maxLength);
            }
        }
        private string drawRow(List<string> rowData, int index)
        {
            var row = "";
            // Draw the border
            var border = "+";

            foreach (int len in lengths)
            {
                border += "-";
                var lines = new StringBuilder().Insert(0, "-", len).ToString();
                border += lines;
                border += "-+";
            }
            border += Environment.NewLine;
            
            if (index == 0)
            {
                row += border;
            }
            
            var rowDataToString = "|";

            for (int i = 0; i < rowData.Count; i++)
            {
                // rowDataToString += rowData[i].PadRight(lengths[i]) + " |";
               rowDataToString += " ";
               rowDataToString += rowData[i].PadRight(lengths[i]) + " |";
            }
            rowDataToString += Environment.NewLine;
            
            row += rowDataToString;
            row += border;
            
            return row;;
        }

        public void drawTable()
        {
            // Prepare the data
            setTableParams();
            for (int i = 0; i < data.Count; i++)
            {
                Rendered += drawRow(data[i], i);
            }
            Console.WriteLine(Rendered);
        }
    }
}