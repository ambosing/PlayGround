using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AttackStateBehaviour : StateMachineBehaviour
{
    public override void OnStateEnter(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)
    {
        animator.GetComponent<PlayerAnimator>().AttackComboIndexIncrease();

    }

    //public override void OnStateExit(Animator animator, AnimatorStateInfo stateInfo, int layerIndex)
    //{
    //    animator.GetComponent<PlayerAnimator>().ClearAttackComboIndex();
    //}

    public override void OnStateMachineExit(Animator animator, int stateMachinePathHash)
    {
        animator.GetComponent<PlayerAnimator>().ClearAttackComboIndex();
    }

    
}
