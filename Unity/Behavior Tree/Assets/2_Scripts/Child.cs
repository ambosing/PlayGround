using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Child : Parent
{
    protected override void Awake()
    {
        base.Awake();
        print(aa);
        aa = 9999;
        print(aa);
    }

    public override void Action()
    {
        base.Action();
        Debug.Log("자식이 실행됨");
    }
}
