using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class DataLoadManager : MonoBehaviour
{
    public static DataLoadManager Instance;
    public List<Sheet1Data> sheet1Datas = new List<Sheet1Data>();
    public Sheet1 sheet1DataObject;

    private void Awake()
    {
        Instance = this;
        sheet1Datas = Resources.Load<Sheet1>("Sheet1").dataArray.ToList();

        //이렇게 하면 공유 데이터 활용 
        sheet1DataObject = Resources.Load<Sheet1>("Sheet1");
    }
}
