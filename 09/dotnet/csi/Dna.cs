using System;
using System.Collections.Generic;

namespace csi
{
    public static class Dna
    {
        public static Dictionary<string, string> hairColor = new Dictionary<string, string>()
        {
            {"Black", "CCAGCAATCGC"},
            {"Brown", "GCCAGTGCCG"},
            {"Blonde", "TTAGCTATCGC"}
        };
        public static Dictionary<string, string> faceShape = new Dictionary<string, string>()
        {
            {"Square", "GCCACGG"},
            {"Round", "ACCACAA"},
            {"Oval", "AGGCCTCA"}
        };
        public static Dictionary<string, string> eyeColor = new Dictionary<string, string>()
        {
            {"Blue", "TTGTGGTGGC"},
            {"Green", "GGGAGGTGGC"},
            {"Brown", "AAGTAGTGAC"}
        };
        public static Dictionary<string, string> gender = new Dictionary<string, string>()
        {
            {"Female", "TGAAGGACCTTC"},
            {"Male", "TGCAGGAACTTC"}
        };
        public static Dictionary<string, string> race = new Dictionary<string, string>()
        {
            {"White", "AAAACCTCA"},
            {"Black", "CGACTACAG"},
            {"Asian", "CGCGGGCCG"}
        };

        public static Dictionary<string, string> getSuspectDNA(Suspect suspect)
        {
            Dictionary<string, string> dnaResults = new Dictionary<string, string>();
            dnaResults.Add("name", suspect.name);
            dnaResults.Add("hairColor", Dna.hairColor[suspect.hairColor]);
            dnaResults.Add("faceShape", Dna.faceShape[suspect.faceShape]);
            dnaResults.Add("eyeColor", Dna.eyeColor[suspect.eyeColor]);
            dnaResults.Add("gender", Dna.gender[suspect.gender]);
            dnaResults.Add("race", Dna.race[suspect.race]);
            return dnaResults;
        }
    }
} 