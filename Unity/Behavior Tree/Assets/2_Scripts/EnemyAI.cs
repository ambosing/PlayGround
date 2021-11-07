using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using myBehaviourTree;

public class EnemyAI : MonoBehaviour
{
    private btRoot _btAIState;

    // Start is called before the first frame update
    void Start()
    {
        CreateBehaviorTreeAIState();
    }

    // Update is called once per frame
    void Update()
    {
        // 자식노드들이 체크하면서 돌아감
        _btAIState.Tick();
    }


    void CreateBehaviorTreeAIState()
    {
        _btAIState = new btRoot();

        btSeletor btMainSelector = new btSeletor();

        //chase
        btSequence btChase = new btSequence();
        EnemyState_Chase_IsEnemy stateChase_IsEnemy = new EnemyState_Chase_IsEnemy(gameObject);
        btChase.AddChild(stateChase_IsEnemy);
        EnemyState_Chase_LookAt stateChase_LookAt = new EnemyState_Chase_LookAt(gameObject);
        btChase.AddChild(stateChase_LookAt);

        //patrol
        btSequence btPatrol = new btSequence();
        EnemyState_Patrol_Rotation statePatrol_Rotation = new EnemyState_Patrol_Rotation(gameObject);
        btPatrol.AddChild(statePatrol_Rotation);
        EnemyState_Patrol_WayPoint statePatrol_WayPoint = new EnemyState_Patrol_WayPoint(gameObject);
        btPatrol.AddChild(statePatrol_WayPoint);

        //main selector
        btMainSelector.AddChild(btChase);
        btMainSelector.AddChild(btPatrol);

        // 최종 root에 attach
        _btAIState.AddChild(btMainSelector);
    }
}