using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using FSM.Base;
using UnityEngine;

public class Chase : BState
{
    /// <summary>
    /// 상태에 전이되어 진입할 때 1번 실행되는 함수
    /// </summary>
    public override void Enter()
    {
        Debug.Log("Chase State Enter");

    }

    /// <summary>
    /// 상태에 있는 동안 설정한 주기마다 실행되는 Update함수
    /// </summary>
    public override void Execute()
    {
        //대상이 없으면 다시 Wander로 보내주기
        if (!Owner.IsFindTarget)
            SuperFSM.ChangeState<Wander>();
        
        //Chase 대상을 쫓는 기능 - StoppingDistance 안쓰고 바로 상태전이 해도 됨.
        float stoppingDistance = 0.5f;
        Transform targetTransform = Owner.NearFindPlayer.player.transform;
        Vector3 dir = (targetTransform.position - Owner.transform.position).normalized;
        Vector3 destPos = targetTransform.position - dir * stoppingDistance;

        float distance = Vector3.Distance(targetTransform.position, Owner.transform.position);
        Debug.Log(distance);
        Owner._navMeshAgent.destination = destPos;

        //Owner._navMeshAgent.destination = Owner.NearFindPlayer.player.transform.position;
        
        //Chase 거리에 따라 Attack으로 상태 전이
        if (Owner._navMeshAgent.remainingDistance <= stoppingDistance)
            SuperFSM.ChangeState<Attack>();
    }

    /// <summary>
    /// 다른 상태로 전이될 때 1번 실행되는 함수
    /// </summary>
    public override void Exit()
    {
        Owner._navMeshAgent.ResetPath();
        Debug.Log("Chase State Exit");
    }

    private AIFSM SuperFSM => (AIFSM) SuperMachine;
    private AIController Owner => SuperFSM.owner;
}
