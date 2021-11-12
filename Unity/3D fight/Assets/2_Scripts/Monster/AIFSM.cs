using System;
using System.Collections;
using System.Collections.Generic;
using FSM.Mono;
using UnityEngine;

public class AIFSM : MonoFSM
{
    public AIController owner;

    private void Awake()
    {
        owner = GetComponent<AIController>();
    }

    public override void AddStates()
    {
        SetUpdateFrequency(0.1f);
        
        AddState<Chase>();
        AddState<Wander>();
        AddState<Attack>();
        
        SetInitialState<Wander>();
    }
}
