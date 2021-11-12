using System.Collections;
using System.Collections.Generic;
using FSM.Base;
using UnityEngine;

public class Attack : BState
{
    /// <summary>
    /// 상태에 전이되어 진입할 때 1번 실행되는 함수
    /// </summary>
    public override void Enter()
    {
        
    }

    /// <summary>
    /// 상태에 있는 동안 설정한 주기마다 실행되는 Update함수
    /// </summary>
    public override void Execute()
    {
        base.Execute();
    }

    /// <summary>
    /// 다른 상태로 전이될 때 1번 실행되는 함수
    /// </summary>
    public override void Exit()
    {
        base.Exit();
    }
}
