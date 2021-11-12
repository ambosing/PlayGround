using System.Collections;
using System.Collections.Generic;
using FSM.Base;
using UnityEngine;

public class Wander : BState
{
    
    /// <summary>
    /// 상태에 전이되어 진입할 때 1번 실행되는 함수
    /// </summary>
    public override void Enter()
    {
        Debug.Log("Wander State Enter");
        Owner._navMeshAgent.destination = Owner.CurrentWanderPoint;
    }

    /// <summary>
    /// 상태에 있는 동안 설정한 주기마다 실행되는 Update함수
    /// </summary>
    public override void Execute()
    {
        if (Owner._navMeshAgent.remainingDistance <= 0.5f)
        {
            Owner.curWanderIndex =
                (int) Mathf.Repeat(SuperFSM.owner.curWanderIndex + 1,
                    SuperFSM.owner.wanderPoints.Length);
            Owner._navMeshAgent.destination = Owner.CurrentWanderPoint;
        }
        
        //ChangeChaseState
        if (Owner.IsFindTarget)
        {
            SuperFSM.ChangeState<Chase>();
        }
    }

    /// <summary>
    /// 다른 상태로 전이될 때 1번 실행되는 함수
    /// </summary>
    public override void Exit()
    {
        Debug.Log("Wander State Exit");
        Owner._navMeshAgent.ResetPath();
    }

    private AIFSM SuperFSM => (AIFSM) SuperMachine;
    private AIController Owner => SuperFSM.owner;
}
