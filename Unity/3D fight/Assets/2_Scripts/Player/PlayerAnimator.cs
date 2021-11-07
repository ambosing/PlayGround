using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerAnimator : MonoBehaviour
{
    [HideInInspector] public Player player;
    private Animator _animator;
    private int attackComboIndex;
    private Coroutine checkComboCoroutine;

    private void Awake()
    {

        player = GetComponent<Player>();
        _animator = GetComponent<Animator>();
        attackComboIndex = 0;
    }

    public void AttackComboIndexIncrease()
    {
        attackComboIndex = attackComboIndex > 5 ? 0 : attackComboIndex + 1;
    }

    public void ClearAttackComboIndex()
    {
        attackComboIndex = 0;
        _animator.SetInteger("AttackIndex", attackComboIndex);
    }


    public IEnumerator CheckComboLimit()
    {
        yield return new WaitForSeconds(player._combat.attackComboLimitTime);
        attackComboIndex = 0;
    }

    public void Attack()
    {
        //if (checkComboCoroutine != null)
        //{
        //    StopCoroutine(checkComboCoroutine);
        //}

        //checkComboCoroutine = StartCoroutine(CheckComboLimit());

        SetAttackTrigger(attackComboIndex);
        //Debug.Log(attackComboIndex);
    }

    private void SetAttackTrigger(int index)
    {
        _animator.SetTrigger("Attack");
        _animator.SetInteger("AttackIndex", index);
    }

}
