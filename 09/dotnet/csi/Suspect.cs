using System;

namespace csi
{
    public class Suspect
    {
        public string name { get; set; }
        public string hairColor { get; set; }
        public string faceShape { get; set; }
        public string eyeColor { get; set; }
        public string gender { get; set; }
        public string race { get; set; }

        public Suspect(string _name, 
                        string _hairColor, 
                        string _faceShape, 
                        string _eyeColor,
                        string _gender,
                        string _race)
        {
            name = _name;
            hairColor = _hairColor;
            faceShape = _faceShape;
            eyeColor = _eyeColor;
            gender = _gender;
            race = _race;
        }
    }
}