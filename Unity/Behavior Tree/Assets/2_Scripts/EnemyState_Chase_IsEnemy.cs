using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using myBehaviourTree;

public class EnemyState_Chase_IsEnemy : btCondition // 무엇을 상속받는지 꼭 확인하고 기억할것!
{
    private GameObject _myOwner;

    public EnemyState_Chase_IsEnemy(GameObject myOwner)
    {
        _myOwner = myOwner;
    }

    public override enStatus Update()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player)
        {
            float fDistance = Vector3.Distance(player.transform.position, _myOwner.transform.position);
            if (fDistance < 10.0f)
            {
                return enStatus.Success;
            }
        }
        return enStatus.Failure;
    }
}