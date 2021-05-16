using LeagueToolkit.Meta.Classes;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Numerics;
using System.Text;

namespace Avatar.Plugs
{

    public class MParticle
    {
        public string name;
        public Vector3 position;
        public int quality;
        public Vector3 rotation;
        public string eyecandy;

        public MParticle(string Name, Vector3 Position, int Quality, Vector3 Rotation, string Eyecandy, StreamReader sr)
        {
            string[] input =  sr.ReadLine().Split(new char[] {' '}, StringSplitOptions.RemoveEmptyEntries);
            this.name = input[0];

            this.position = new Vector3(float.Parse(input[1], CultureInfo.InvariantCulture),
                float.Parse(input[2], CultureInfo.InvariantCulture),
                float.Parse(input[3], CultureInfo.InvariantCulture));

            this.quality = int.Parse(input[4]);

            this.rotation = new Vector3(float.Parse(input[5], CultureInfo.InvariantCulture),
                float.Parse(input[6], CultureInfo.InvariantCulture),
                float.Parse(input[7], CultureInfo.InvariantCulture));

            if(this.eyecandy.Contains("EyeCandy"))
            {
                this.eyecandy = "EyeCandy";
            }
            else
            {
                this.eyecandy = "";
            }
            
            name = Name;
            position = Position;
            quality = Quality;
            rotation = Rotation;
            eyecandy = Eyecandy;


        }




    }
}
