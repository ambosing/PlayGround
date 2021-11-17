using UnityEngine;
using System.Collections;

///
/// !!! Machine generated code !!!
/// !!! DO NOT CHANGE Tabs to Spaces !!!
///
///

public enum CharType
{
  Monster,
  Character,
  Giant
}

[System.Serializable]
public class Sheet1Data
{
  [SerializeField]
  int id;
  public int Id { get {return id; } set { this.id = value;} }
  
  [SerializeField]
  CharType chartype;
  public CharType CHARTYPE { get {return chartype; } set { this.chartype = value;} }
  
  [SerializeField]
  int grade;
  public int Grade { get {return grade; } set { this.grade = value;} }
  
  [SerializeField]
  string namekr;
  public string Namekr { get {return namekr; } set { this.namekr = value;} }
  
  [SerializeField]
  string nameen;
  public string Nameen { get {return nameen; } set { this.nameen = value;} }
  
  [SerializeField]
  float maxhp;
  public float Maxhp { get {return maxhp; } set { this.maxhp = value;} }
  
  [SerializeField]
  float str;
  public float Str { get {return str; } set { this.str = value;} }
  
  [SerializeField]
  float dex;
  public float Dex { get {return dex; } set { this.dex = value;} }
  
  [SerializeField]
  float wis;
  public float Wis { get {return wis; } set { this.wis = value;} }
  
  [SerializeField]
  float main;
  public float Main { get {return main; } set { this.main = value;} }
  
  [SerializeField]
  int sub;
  public int Sub { get {return sub; } set { this.sub = value;} }
  
  [SerializeField]
  int armor;
  public int Armor { get {return armor; } set { this.armor = value;} }
  
}