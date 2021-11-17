using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Parent : MonoBehaviour
{
    
    private Collider _collider;
    protected int aa = 1000;

    
    protected virtual void Awake()
    {
        _collider = GetComponent<Collider>();
    }

    public virtual void Action()
    {
        Debug.Log("부모가 실행됨");
    }
}
